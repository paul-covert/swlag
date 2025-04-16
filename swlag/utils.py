# swlag: Lag and averaging time constant calculation in Python.
# Copyright (C) 2025  Paul A. Covert (GNU GPLv3)
"""Convenience routines for calculation of time constants"""

def _check_timeseries_spacing(df):
    """
    Ensure uniformly, monotonically increasing time
    
    Parameters
    ----------
    df : Pandas dataframe indexed by datetime64
        Contains the time (index), inlet temperature, and
        lab temperature series.
    
    Returns
    -------
    monotonic : boolean
        True of index of df is monotonically increasing.
    
    """
    import numpy as np
    
    diff = np.diff(df.index.to_numpy())
    monotonic = np.all(diff==diff[0])
    
    return monotonic