import numpy as np
import pandas as pd
import formatting


def between_runs(writer, between_run, test_item):
    """
    Analytics of the quality control samples and the dilution quality control between runs, across the whole study
    """
    # Calculate mean concentration, mean accuracy and CV%
    # Coefficient of variation lambda function is from: https://www.statology.org/coefficient-of-variation-in-python/
    between_run = between_run.groupby(["ID of sample", "Nominal conc. [ng/mL]",]).agg({
            "Accuracy [%]": ["mean",],
            "Measured conc. [ng/mL]": ["mean", lambda x: np.std(x, ddof=1) / np.mean(x) * 100,],
        }
    )

    # To to_excel object
    between_run.to_excel(
        excel_writer=writer,
        sheet_name="App VI - Between-run",
        header=False,
        float_format="%.3g",
        startrow=5,
        startcol=1,
    )

    workbook = writer.book
    worksheet = writer.sheets["App VI - Between-run"]

    # The formatting module is used
    title_format = formatting.title_format(workbook)
    header_format = formatting.header_format(workbook)
    column_format = formatting.warp_format(workbook)
    cell_format = formatting.cell_format(workbook)
    string_format = formatting.string_format(workbook)

    # Worksheet formatted
    worksheet.set_column("B:F", 13, column_format,)
    worksheet.set_column("A:A", 1, column_format,)
    worksheet.set_column("G:G", 1, column_format,)
    worksheet.set_row(1, 30)
    worksheet.set_row(5, 80)
    for i in range(len(between_run)):
        worksheet.set_row(i + 6, 25)

    worksheet.conditional_format(6, 1, 6 + len(between_run) - 1, 5,
        {"type": "cell", "criteria": ">=", "value": 0, "format": cell_format},
    )
    worksheet.conditional_format(6, 1, 6 + len(between_run) - 1, 5,
        {"type": "cell", "criteria": "<=", "value": 0, "format": cell_format},
    )

    worksheet.merge_range("B2:F2", "Results of QC samples: Between-run calculated mean concentrations, accuracies and precisions", column_format,)
    worksheet.merge_range("B4:F4", f"{test_item}", title_format,)
    worksheet.merge_range("B5:F5", "Between-run accuracy and precision of quality control samples", title_format,)

    # Format headers
    for col_num, value in enumerate(["Sample name", "Nominal conc. [ng/mL]", "Accuracy %", "Conc. [ng/mL]", "Precision %",]):
        worksheet.write(5, col_num + 1, value, header_format)

    # Write standard text below the table
    worksheet.write(6 + len(between_run) + 1, 1, "Acceptance criteria: The between-run accuracy should be within", string_format,)
    worksheet.write(6 + len(between_run) + 2, 1, "±15 % of the nominal one and the CV% should be ≤15 %.", string_format,)
