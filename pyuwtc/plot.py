# pyuwtc: Lag and averaging time constant calculation in Python.
# Copyright (C) 2025  Paul A. Covert (GNU GPLv3)
"""Convenience routines for plotting temperature and flow data"""


def plot_tsg_flow(df):
    """
    Plot flow to the SeaBird 45 thermosalinograph

    Parameters
    ----------
    df : Pandas dataframe
        Time, temperature, and flow data.

    Returns
    -------
    fig : matplotlib figure
    ax : matplotlib axes

    """
    import matplotlib.pyplot as plt

    fig, ax = plt.subplots(ncols=1, nrows=1)
    ax.plot(df.index, df["flow_tsg"], "-")
    ax.set_xlabel("Sampling date & time")
    ax.set_ylabel("Flow / L min$^{-1}$")
    
    return fig, ax


def plot_temp(df, inlet=True, lab=True, transformed=True):
    """
    Plot inlet, lab, and transformed (if available) temperatures

    Parameters
    ----------
    df : Pandas dataframe
        Time, temperature, and flow data.
    inlet : boolean
        Plot inlet temperature flag.
        Default is True.
    lab : boolean
        Plot lab temperature flag.
        Default is True.
    transformed : boolean
        Plot transformed temperature flag.
        Default is True.

    Returns
    -------
    fig : matplotlib figure
    ax : matplotlib axes

    """
    import matplotlib.pyplot as plt

    fig, ax = plt.subplots(ncols=1, nrows=1)
    if inlet:
        ln = ax.plot(df.index, df["temp_inlet"], linestyle="-", label="Inlet")
    if lab:
        ax.plot(df.index, df["temp_lab"], linestyle="-", label="Lab")
    if transformed and ("temp_prime" in df.columns):
        ax.plot(
            df.index,
            df["temp_prime"],
            linestyle="--",
            color=ln[0].get_color(),
            label="Transformed",
        )
    ax.legend()
    ax.set_xlabel("Sampling date & time")
    ax.set_ylabel("Temperature / $^\circ$C")

    return fig, ax
