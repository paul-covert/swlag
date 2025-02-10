# swlag: Lag and averaging time constant calculation in Python.
# Copyright (C) 2025  Paul A. Covert (GNU GPLv3)
"""Read IOS Shell files and write calculation results"""


def read_tob(
    filepath_or_buffer,
    date_col=0,
    time_col=1,
    temp_inlet_col=2,
    temp_lab_col=3,
    flow_tsg_col=9,
):
    """
    Loads the time and temperature columns from IOS Shell *.tob files.

    Parameters
    ----------
    filepath_or_buffer : string, path object or file-like object
        IOS Shell file containing the surface underway temperature
        data.
    date_col : integer (optional)
        Column (0-indexed) containing date values.
        Default is 0.
    time_col : integer (optional)
        Column (0-indexed) containing time values.
        Default is 1.
    temp_inlet_col : integer (optional)
        Column (0-indexed) containing inlet temperature values.
        Default is 2.
    temp_lab_col : integer (optional)
        Column (0-indexed) containing lab temperature values.
        Default is 3.
    flow_tsg_col : integer (optional)
        Column (0-indexed) containing TSG flow rate values.
        Default is 9.

    Returns
    -------
    df : Pandas dataframe
        Time and temperature data from input file.

    """
    import pandas as pd

    with open(filepath_or_buffer) as f:

        # scan file to end of header
        for line in f:
            if line.strip() == "*END OF HEADER":
                break

        # use pandas to read the remaining file
        df = pd.read_csv( # change to read_fwf to better handle file format
            f,
            sep="\s+",
            usecols=[date_col, time_col, temp_inlet_col, temp_lab_col, flow_tsg_col],
            names=["date", "time", "temp_inlet", "temp_lab", "flow_tsg"],
            na_values=["-99", "-99.0000"]
        )

        # convert date and time columns and set as index
        df["datetime"] = pd.to_datetime(df["date"] + " " + df["time"])
        df.drop(columns=["date", "time"], inplace=True)
        df.set_index("datetime", inplace=True)

    return df
