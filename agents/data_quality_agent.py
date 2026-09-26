def data_quality_agent(df):

    issues = []

    if df.empty:
        issues.append("Dataset is empty.")

    missing_values = df.isnull().sum()

    for column, count in missing_values.items():

        if count > 0:
            issues.append(
                f"{column} contains {count} missing values."
            )

    if "pages_printed" in df.columns:

        if (df["pages_printed"] < 0).any():
            issues.append(
                "Negative page counts detected."
            )

    if "reprints" in df.columns:

        if (df["reprints"] < 0).any():
            issues.append(
                "Negative reprint values detected."
            )

    if "energy_kwh" in df.columns:

        if (df["energy_kwh"] < 0).any():
            issues.append(
                "Negative energy values detected."
            )

    if not issues:

        status = "PASS"
        message = "Data quality checks passed."

    else:

        status = "WARNING"
        message = "Data quality issues detected."

    return {
        "status": status,
        "message": message,
        "issues": issues,
    }