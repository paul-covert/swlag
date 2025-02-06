import pandas as pd


def read_tob(
    filepath_or_buffer, date_col=0, time_col=1, temp_inlet_col=2, temp_lab_col=3
):

    with open(filepath_or_buffer) as f:
        skiprows = 0

        # scan file to end of header
        for line in f:
            if line.rstrip() == "*END OF HEADER":
                break

        # use pandas to read the remaining file
        df = pd.read_csv(
            f,
            sep="\s+",
            usecols=[date_col, time_col, temp_inlet_col, temp_lab_col],
            names=["date", "time", "temp_inlet", "temp_lab"],
        )
        df["datetime"] = pd.to_datetime(df["date"] + " " + df["time"])
        df.drop(columns=["date", "time"], inplace=True)
        df.set_index("datetime", inplace=True)
    return df
