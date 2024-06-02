from project import command_args, get_sheets, get_data, add_columns, sign_round
import sys
import pandas as pd
from pandas.testing import assert_frame_equal
import numpy as np

from pathlib import Path
import unittest
from unittest.mock import patch


root_dir = Path(__file__).resolve().parent


def test_command_args():
    testargs = [
        "project.py",
        "-i",
        "RAW_DATA.xlsx",
        "-t",
        "ibuprofen",
        "-d",
        "data.txt",
        "-c",
        "columns.txt",
    ]
    with patch.object(sys, "argv", testargs):
        args = command_args()
        assert args.input == "RAW_DATA.xlsx"
        assert args.data == "data.txt"
        assert args.testitem == "ibuprofen"
        assert args.output == "data/BA.xlsx"
        assert args.column == "columns.txt"

    testargs_again = [
        "project.py",
        "-t",
        "Midazolam",
        "-d",
        "data.txt",
        "-i",
        "RAW DATA02.xlsx",
        "-o",
        "Bioanalytical_results.xlsx",
        "--column",
        "cols.txt",
    ]
    with patch.object(sys, "argv", testargs_again):
        args_again = command_args()
        assert args_again.input == "RAW DATA02.xlsx"
        assert args_again.data == "data.txt"
        assert args_again.testitem == "Midazolam"
        assert args_again.output == "Bioanalytical_results.xlsx"
        assert args_again.column == "cols.txt"


def test_get_sheets():
    assert get_sheets(root_dir / "test" / "TEST_DATA01.xlsx") == [
        "RD R01",
        "RD R02",
        "RD R03",
        "RD R04",
    ]
    assert get_sheets(root_dir / "test" / "TEST_DATA02.xlsx") == [
        "RD R01",
        "RD R02",
        "RD R03",
        "RD R04",
        "RD R05",
        "RD R06",
        "RD R07",
        "RD R08",
        "RD R09",
        "RD R10",
        "RD R11",
    ]


def test_get_data():
    # Vulnerable to end-of-line commas
    assert get_data(root_dir / "test" / "test_data.txt")["day"] == [
        "Day 1",
        "Day 2",
        "Day 3",
        "Day 100",
        "Day 25800",
        "Day 4",
    ]
    assert get_data(root_dir / "test" / "test_data.txt")["group"] == [
        "Group 1 male",
        "G 1 F",
        "GROUPE2 male",
        "Group2F",
        "Gp3M",
        "g3f",
    ]
    assert get_data(root_dir / "test" / "test_data.txt")["time"] == [
        "0h",
        "0.5h",
        "1h",
        "2h",
        "4h",
        "6h",
        "8h",
        "12h",
        "24h",
        "36h",
        "48h",
        "51h",
    ]
    assert get_data(root_dir / "test" / "test_data.txt")["additional_data"] == [
        "data01",
        "2nd_data",
        "data_the_3rd",
    ]


def test_add_columns():
    columns = {
        "id": ["ID of sample"],
        "name": ["Sample Name"],
        "type": ["Sample Type"],
        "nominal": ["Analyte Concentration (ng/mL)"],
        "measured": ["Calculated Concentration (ng/mL)"],
    }
    d1 = {
        "Sample Name": [
            "Blank",
            "IS Blank",
            "C1 - 1 ng/mL",
            "C2 - 2 ng/mL",
            "C3 - 5 ng/mL",
            "C4 - 10 ng/mL",
            "C5 - 20 ng/mL",
            "C6 - 50 ng/mL",
            "C7 - 100 ng/mL",
            "C8 - 200 ng/mL",
            "C9 - 500 ng/mL",
            "C10 - 1000 ng/mL",
            "QCH - 800 ng/mL",
            "QCM - 300 ng/mL",
            "QCL - 3 ng/mL",
            "dil-QCH-15x 12000 ng/mL",
            "dil-QCH-15x 12000 ng/mL",
        ],
        "Calculated Concentration (ng/mL)": [
            "#DIV/0!",
            "No Peak",
            0.955,
            2.04,
            5.62,
            9.4,
            17.9,
            50.1,
            91.4,
            188,
            414,
            920,
            858,
            277,
            2.72,
            10800,
            12700,
        ],
        "Analyte Concentration (ng/mL)": [
            np.NaN,
            np.NaN,
            1.0,
            2.0,
            5.0,
            10.0,
            20.0,
            50.0,
            100.0,
            200.0,
            500.0,
            1000.0,
            800.0,
            300.0,
            3.0,
            12000.0,
            12000.0,
        ],
    }
    d2 = {
        "Sample Name": [
            "Blank",
            "IS Blank",
            "C1 - 1 ng/mL",
            "C2 - 2 ng/mL",
            "C3 - 5 ng/mL",
            "C4 - 10 ng/mL",
            "C5 - 20 ng/mL",
            "C6 - 50 ng/mL",
            "C7 - 100 ng/mL",
            "C8 - 200 ng/mL",
            "C9 - 500 ng/mL",
            "C10 - 1000 ng/mL",
            "QCH - 800 ng/mL",
            "QCM - 300 ng/mL",
            "QCL - 3 ng/mL",
            "dil-QCH-15x 12000 ng/mL",
            "dil-QCH-15x 12000 ng/mL",
        ],
        "Measured conc. [ng/mL]": [
            "#DIV/0!",
            "No Peak",
            0.955,
            2.04,
            5.62,
            9.4,
            17.9,
            50.1,
            91.4,
            188,
            414,
            920,
            858,
            277,
            2.72,
            10800,
            12700,
        ],
        "Nominal conc. [ng/mL]": [
            np.NaN,
            np.NaN,
            1.0,
            2.0,
            5.0,
            10.0,
            20.0,
            50.0,
            100.0,
            200.0,
            500.0,
            1000.0,
            800.0,
            300.0,
            3.0,
            12000.0,
            12000.0,
        ],
        "ID of sample": [
            np.NaN,
            np.NaN,
            "C1",
            "C2",
            "C3",
            "C4",
            "C5",
            "C6",
            "C7",
            "C8",
            "C9",
            "C10",
            "QCH",
            "QCM",
            "QCL",
            "dil-QCH-15x",
            "dil-QCH-15x",
        ],
        "Accuracy [%]": [
            np.NaN,
            np.NaN,
            (-4.5),
            2.0,
            12.4,
            (-6.0),
            (-10.5),
            0.2,
            (-8.6),
            (-6.0),
            (-17.2),
            (-8.0),
            7.25,
            (-7.67),
            (-9.33),
            (-10.0),
            5.83,
        ],
    }
    df1 = pd.DataFrame(data=d1)
    df2 = pd.DataFrame(data=d2)
    df1 = add_columns(df1, columns)
    assert_frame_equal(df1, df2)


def test_sign_round():
    assert sign_round(0) == 0
    assert sign_round(1) == 1
    assert sign_round(-0.9876) == -0.988
    assert sign_round(12.369) == 12.4
    assert sign_round(-105) == -105
    assert sign_round(1111) == 1110
