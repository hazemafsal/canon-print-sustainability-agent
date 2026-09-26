import pandas as pd


REQUIRED_COLUMNS = [
    "date",
    "department",
    "printer_id",
    "pages_printed",
    "color_pages",
    "black_white_pages",
    "reprints",
    "failed_prints",
    "paper_sheets",
    "energy_kwh",
]


def load_printer_data(file=None):

    if file is not None:
        df = pd.read_csv(file)
    else:
        df = pd.read_csv("data/printer_data.csv")

    df["date"] = pd.to_datetime(df["date"], errors="coerce")

    numeric_columns = [
        "pages_printed",
        "color_pages",
        "black_white_pages",
        "reprints",
        "failed_prints",
        "paper_sheets",
        "energy_kwh",
    ]

    for column in numeric_columns:
        df[column] = pd.to_numeric(df[column], errors="coerce")

    return df


def validate_columns(df):

    missing = [
        column
        for column in REQUIRED_COLUMNS
        if column not in df.columns
    ]

    return missing