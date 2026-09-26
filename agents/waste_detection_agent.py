from services.calculations import department_metrics


def waste_detection_agent(df):

    metrics = department_metrics(df)

    findings = []

    for _, row in metrics.iterrows():

        department = row["department"]

        reprint_rate = row["reprint_rate"]
        failure_rate = row["failure_rate"]
        color_rate = row["color_rate"]

        if reprint_rate >= 15:

            findings.append({
                "department": department,
                "issue": "High reprint activity",
                "severity": "HIGH",
                "metric": round(reprint_rate, 2),
                "unit": "%",
            })

        elif reprint_rate >= 10:

            findings.append({
                "department": department,
                "issue": "Elevated reprint activity",
                "severity": "MEDIUM",
                "metric": round(reprint_rate, 2),
                "unit": "%",
            })

        if failure_rate >= 4:

            findings.append({
                "department": department,
                "issue": "High failed-print activity",
                "severity": "HIGH",
                "metric": round(failure_rate, 2),
                "unit": "%",
            })

        if color_rate >= 50:

            findings.append({
                "department": department,
                "issue": "High color-print usage",
                "severity": "MEDIUM",
                "metric": round(color_rate, 2),
                "unit": "%",
            })

    return findings