import csv
from math import floor, log10
import numpy as np
import pandas as pd
import argparse
import re

from cal_qc import cal_qc_excel
from btwn_rns import between_runs
from concentrations import concentrations


# Mock pharmacokinetics data is from https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9372427/ Table S1


def main():
    # Get command-line arguments
    args = command_args()

    # Get Excel sheet names
    sheets = get_sheets(args.input)

    # Initiate the writer object
    writer = pd.ExcelWriter(args.output, engine="xlsxwriter")

    # Get the basic information of the raw data
    basic_data = get_data(args.data)

    # Declare variables
    row = 5
    frames = []
    pk_data = []

    for sheet in sheets:
        # Read one sheet at the time into DataFrames which is divided below
        df = pd.read_excel(args.input, sheet_name=sheet)

        # Study samples are saved into a separate DataFrame
        pk_conc = df.loc[
            (df["Sample Type"] == "Unknown")
            & (~df["Sample Name"].str.contains(r"Blank"))
        ]

        # Rename, add helper columns
        df = add_columns(df)

        # Additional sub-DataFrames for calibrators, QCs and dilution QCs
        cals = df.loc[df["Sample Type"] == "Standard"]
        qcs = df.loc[
            (df["Sample Type"] == "Quality Control")
            & (df["Sample Name"].str.contains(r"^QC[LMH]{1}"))
        ]
        dqcs = df.loc[
            (df["Sample Type"] == "Quality Control")
            & (df["Sample Name"].str.contains(r"^dil-QCH"))
        ]

        # Calls a function to write to the Excel
        cal_qc_excel(cals, qcs, dqcs, writer, sheet, args.testitem, row)
        # Row variable is increased so the next RUN's cals and QCs are below
        row += len(cals) + len(qcs) + len(dqcs) + 24
        # The QCs across all RUNs are collected for between run analytics
        frames.append(qcs)
        if dqcs.empty != True:
            frames.append(dqcs)
        pk_data.append(pk_conc)

    # The collected (dil)QCs are analysed
    between_runs(writer, pd.concat(frames), args.testitem,)

    # The collected PK/TK study samples are analysed
    concentrations(writer, basic_data, pd.concat(pk_data))

    writer.close()


def command_args():
    """
    Parse command-line arguments
    """
    parser = argparse.ArgumentParser(description="Takes a raw data excel and a text file of basic informations and processes it")
    # Input
    parser.add_argument("-i", "--input",    help="Excel of raw data", required=True)
    # Helper data
    parser.add_argument("-d", "--data",     help="Text or csv of the data condtaining animal numbers and groups, time points etc.", required=True,)
    # Test item name for table headers
    parser.add_argument("-t", "--testitem", help="Name of the test item", required=True)
    # If a particular output name is required
    parser.add_argument("-o", "--output",   help="File name of output", default="BA.xlsx")

    arguments = parser.parse_args()

    return arguments


def get_sheets(excel_name):
    """
    Get the sheets that contain Raw Data
    """
    shs = pd.ExcelFile(excel_name).sheet_names
    sheets = [sh for sh in shs if re.match(r"^RD R[0-9]{2}(?:[a-zA-Z])*", sh)]
    return sheets


def get_data(data_name):
    """
    Read the provided data into a dict
    """
    dict_data = {}
    data_values = []
    with open(data_name) as file:
        reader = csv.reader(file, delimiter=":")
        for data_type, data_value in reader:
            data_value = data_value.split(", ")
            for data in data_value:
                data_values.append(data)
            dict_data[data_type] = data_values
            data_values = []
    return dict_data


def add_columns(dataframe):
    """
    Rename columns, add helper columns
    """
    # ID of sample column to identify calibrator an QC samples
    dataframe["ID of sample"] = dataframe["Sample Name"].str.extract(
        r"((?:C[1-9]{1}0?)|(?:(?:dil-)?QC[LMH]{1}(?:LOQ|-[0-9]+x)?))"
    )
    # Nominal conc. [ng/mL] is the required name for the column
    dataframe.rename(
        columns={"Analyte Concentration (ng/mL)": "Nominal conc. [ng/mL]"},
        inplace=True,
    )
    # Accuracy is the deviation from the nominal concentration,
    # and is rounded to 3 significant digits
    dataframe["Accuracy [%]"] = (
        (dataframe["Calculated Concentration (ng/mL)"] - dataframe["Nominal conc. [ng/mL]"])
        / dataframe["Nominal conc. [ng/mL]"]
        * 100
    )
    dataframe["Accuracy [%]"] = dataframe["Accuracy [%]"].apply(lambda x: sign_round(x) if not pd.isnull(x) else x)
    # Measured conc. [ng/mL] is the required name for the column
    dataframe.rename(
        columns={"Calculated Concentration (ng/mL)": "Measured conc. [ng/mL]"},
        inplace=True,
    )
    return dataframe


def sign_round(n):
    """
    Rounds to 3 significant digist
    """
    # as n == 0 might occur frequently, I believe that an if/else is more efficent than a try/except(ValueError)
    # https://stackoverflow.com/questions/1835756/using-try-vs-if-in-python
    if n == 0:
        signif = 0
    else:
        signif = 3 - (1 + int(floor(log10(abs(n)))))
    return round(n, signif)


if __name__ == "__main__":
    main()
