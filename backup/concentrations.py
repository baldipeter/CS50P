import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import formatting
from io import BytesIO


def concentrations(writer, basic_data, pk_concs):
    """
    Prints PK/TK results to Excel sheets, and plots the TK curve
    """
    # Helper columns (time points are not in order), and rearrange
    pk_concs = add_cols(pk_concs, basic_data)
    pk_concs = pk_concs.groupby("Group")

    # Declare basic variables
    start_row = 2
    row = 2
    length = 0

    # Print male and female animals side by side
    for i in range(int(len(basic_data["group"]) / 2)):
        # Create a gouped DataFrame of male and female animals
        grpd1 = pk_concs.get_group(basic_data["group"][i * 2])
        grpd2 = pk_concs.get_group(basic_data["group"][i * 2 + 1])
        grouped = pd.concat([grpd1, grpd2])

        # Create Pivot
        # TODO: Be able to handle if there were remeasurements and two values are present for a point
        animal_conc = grouped.pivot(
            index=["Day", "sortby", "Time"],
            columns=["Group", "Animal"],
            values="Calculated Concentration (ng/mL)",
        )
        # Calculate mean in a new DataFrame
        animal_mean = animal_conc.mean(axis=1, skipna=False)
        # Calculate CV% in a new DataFrame
        animal_cv = animal_conc.apply(lambda x: np.std(x, ddof=1) / np.mean(x) * 100 if np.mean(x) != 0 else "0", axis=1, raw=True,)

        # To to_excel object with all three DataFrames
        animal_conc.reset_index(level=1, inplace=True, drop=True)
        animal_conc.to_excel(
            excel_writer=writer,
            sheet_name="App_conc",
            index=True,
            header=True,
            float_format="%.3g",
            startrow=start_row,
            startcol=1,
        )
        animal_mean.to_excel(
            excel_writer=writer,
            sheet_name="App_conc",
            index=False,
            header=False,
            float_format="%.3g",
            startrow=start_row + 3,
            startcol=3 + len(list(animal_conc.columns)),
        )
        animal_cv.to_excel(
            excel_writer=writer,
            sheet_name="App_conc",
            index=False,
            header=False,
            float_format="%.3g",
            startrow=start_row + 3,
            startcol=3 + len(list(animal_conc.columns)) + 1,
        )

        workbook = writer.book

        # Plot the data, based on basic_data slices
        for group in basic_data["group"][i * 2 : i * 2 + 2]:
            # New worksheet for every group
            worksheet = workbook.add_worksheet(f"App_figure_{group}")
            for_animal = grouped.loc[grouped["Group"] == group]
            animals = for_animal["Animal"].drop_duplicates()
            # Draw plot for every animal
            for animal in animals:
                # Draw plot for every animal every day
                for day in basic_data["day"]:
                    for_plot = for_animal.loc[
                        (for_animal["Animal"] == animal) & (for_animal["Day"] == day)
                    ]
                    X = for_plot["Time"]
                    X = for_plot["Time"].replace({"h": ""}, regex=True)
                    X = X.astype(float)
                    Y = for_plot["Calculated Concentration (ng/mL)"]
                    plt.plot(X, Y, label=f"{animal} - {day}", marker=".")

                # Plotting details
                plt.legend()
                plt.title(f'Group {group} - Animal "{animal}" PK curve')
                plt.xlabel("Time [h]")
                plt.xlim(0, 24)
                plt.xticks(np.arange(0, 25, step=2))
                plt.ylabel("Conc. [ng/mL]")
                # Save to the Excel as a picture
                imgdata = BytesIO()
                plt.savefig(imgdata, format="png")
                worksheet.insert_image(row, 1, "", {"image_data": imgdata})
                row += 25
                plt.close()
            row = 2

        # Worksheet formatting
        worksheet = writer.sheets["App_conc"]

        column_format = formatting.column_format(workbook, 10)
        cell_format = formatting.cell_format(workbook)

        if (3 + len(list(animal_conc.columns)) + 1) > length:
            length = 3 + len(list(animal_conc.columns)) + 1
            worksheet.set_column(1, length, 8, column_format,)
            worksheet.set_column("A:A", 1,column_format,)
            worksheet.set_column(length + 1, length + 1, 1, column_format,)

        worksheet.merge_range(start_row + 2,    3,                                      start_row + 2, 3 + len(list(animal_conc.columns)) - 1, "Concentration [ng/mL]", cell_format,)
        worksheet.merge_range(start_row,        3 + len(list(animal_conc.columns)),     start_row + 2, 3 + len(list(animal_conc.columns)),      "Mean",                 cell_format,)
        worksheet.merge_range(start_row,        3 + len(list(animal_conc.columns)) + 1, start_row + 2, 3 + len(list(animal_conc.columns)) + 1, "CV%",                   cell_format,)
        worksheet.conditional_format(start_row + 3, 3, start_row + len(basic_data["time"]) * 2 + 2, 3 + len(list(animal_conc.columns)) + 1,
            {"type": "cell", "criteria": ">=", "value": 0, "format": cell_format},
        )

        start_row += len(basic_data["time"]) + 15


def add_cols(df, data):
    """
    Adds a helper column, sorted, as the timepoints are stored as stirngs
    Also changes the Calculated Concentration column to be able to plot it
    """
    for key in iter(data):
        df[key.title()] = np.nan
        for item in data[key]:
            df[key.title()] = np.where(df["Sample Name"].str.contains(item), item, df[key.title()])

    # based on: https://stackoverflow.com/questions/30574740/pandas-multiindex-custom-sort-levels-by-categorical-order-not-alphabetically
    mappings = {}
    for sort, time in enumerate(data["time"]):
        mappings[time] = sort
    df["sortby"] = df["Time"].map(lambda x: mappings[x])
    df["Calculated Concentration (ng/mL)"] = (df["Calculated Concentration (ng/mL)"].replace({"No Peak": "0"}).astype("float64"))
    return df
