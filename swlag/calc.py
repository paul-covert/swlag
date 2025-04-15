# swlag: Lag and averaging time constant calculation in Python.
# Copyright (C) 2025  Paul A. Covert (GNU GPLv3)
"""Calculate transformed inlet temperatures and error functions"""


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


def _transform_inlet_temp(T, dt, dT, tau):
    """
    Apply time offset, temperature offset, and windowing transform
    to a temperature record.
    
    Parameters
    ----------
    T : 1-d numpy array or Pandas Series
        Temperature series to be transformed.
    dt : float
        Constant representing the timelag of the loop system.
    dT : float
        Constant representing the change in water temperature
        between the inlet and lab.
    tau : integer
        width of the averaging window in seconds.
        
    Returns
    -------
    T_prime : 1-d numpy array or Pandas Series
        Transformed temperature series.
        
    """
    
    T_prime = T.shift(int(dt / 5))
    T_prime = T_prime.rolling(int(tau / 5), center=False).mean()
    T_prime = T_prime + dT
    
    return T_prime


def _errfunc(Tinlet, Tlab, dt, dT, tau):
    """
    Error function used in minimization function.
    
    Parameters
    ----------
    Tinlet : 1-d array
        Inlet temperature series.
    Tlab : 1-d array
        Lab temperature series.
    dt : float
        Time offset in seconds.
    dT : float
        Temperature offset in seconds.
    tau : int
        Window width in seconds.
    
    Returns
    -------
    sumsq : float
        Sum of squares of residuals
    
    """
    
    Tinlet_prime = _transform_inlet_temp(Tinlet, dt, dT, tau)
    sumsq = ((Tlab - Tinlet) ** 2).sum()
    
    return sumsq





