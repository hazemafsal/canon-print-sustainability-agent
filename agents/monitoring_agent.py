def monitoring_agent(df):

    if df.empty:

        return {
            "status": "NO DATA",
            "message": "No monitoring data available."
        }

    sorted_df = df.sort_values("date")

    first_period = sorted_df.iloc[0]
    last_period = sorted_df.iloc[-1]

    first_reprints = first_period["reprints"]
    last_reprints = last_period["reprints"]

    if first_reprints == 0:

        change = 0

    else:

        change = (
            (last_reprints - first_reprints)
            / first_reprints
        ) * 100

    if change < 0:

        interpretation = (
            "Reprint volume decreased compared with "
            "the earliest recorded period."
        )

    elif change > 0:

        interpretation = (
            "Reprint volume increased compared with "
            "the earliest recorded period."
        )

    else:

        interpretation = (
            "Reprint volume remained unchanged."
        )

    return {
        "status": "MONITORED",
        "first_reprint_volume": first_reprints,
        "latest_reprint_volume": last_reprints,
        "percentage_change": round(change, 2),
        "message": interpretation,
    }