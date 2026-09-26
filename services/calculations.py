def safe_percentage(numerator, denominator):

    if denominator == 0:
        return 0

    return (numerator / denominator) * 100


def calculate_metrics(df):

    total_pages = df["pages_printed"].sum()
    total_color = df["color_pages"].sum()
    total_reprints = df["reprints"].sum()
    total_failed = df["failed_prints"].sum()
    total_paper = df["paper_sheets"].sum()
    total_energy = df["energy_kwh"].sum()

    reprint_rate = safe_percentage(
        total_reprints,
        total_pages
    )

    failure_rate = safe_percentage(
        total_failed,
        total_pages
    )

    color_rate = safe_percentage(
        total_color,
        total_pages
    )

    return {
        "total_pages": total_pages,
        "total_color_pages": total_color,
        "total_reprints": total_reprints,
        "total_failed_prints": total_failed,
        "total_paper": total_paper,
        "total_energy": total_energy,
        "reprint_rate": reprint_rate,
        "failure_rate": failure_rate,
        "color_rate": color_rate,
    }


def department_metrics(df):

    result = (
        df.groupby("department")
        .agg(
            pages_printed=("pages_printed", "sum"),
            reprints=("reprints", "sum"),
            failed_prints=("failed_prints", "sum"),
            color_pages=("color_pages", "sum"),
            energy_kwh=("energy_kwh", "sum"),
        )
        .reset_index()
    )

    result["reprint_rate"] = (
        result["reprints"]
        / result["pages_printed"]
        * 100
    )

    result["failure_rate"] = (
        result["failed_prints"]
        / result["pages_printed"]
        * 100
    )

    result["color_rate"] = (
        result["color_pages"]
        / result["pages_printed"]
        * 100
    )

    return result