# swlag: Lag and averaging time constant calculation in Python.
# Copyright (C) 2025  Paul A. Covert (GNU GPLv3)
"""Calculate transformed inlet temperatures and error functions"""


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


def _errfunc(tracer_inlet, tracer_lab, dt, dy, tau):
    """
    Error function used in minimization function.
    
    Parameters
    ----------
    tracer_inlet : 1-d array
        Inlet tracer series
    tracer_lab : 1-d array
        Lab tracer series
    dt : float
        Time offset in seconds
    dy : float
        Tracer offset
    tau : int
        Window width in seconds
    
    Returns
    -------
    sumsq : float
        Sum of squares of residuals
    
    """
    
    tracer_inlet_prime = _transform_inlet_temp(tracer_inlet, dt, dy, tau)
    sumsq = ((tracer_lab - tracer_inlet_prime) ** 2).sum()
    
    return sumsq


def estimate_time_consts(tracer_inlet, tracer_lab, freq=1.0):
    """
    Calculate, by minimization of error function, the best
    fit time constants to transform a tracer signal (e.g. 
    temperature, salinity, dye, etc.) measured at the inlet
    to the tracer signal measured in the lab.
    
    
    Parameters
    ----------
    tracer_inlet : 1-d array
        Inlet tracer series.
    tracer_lab : 1-d array
        Lab tracer series.
    freq : float
        Sampling frequency (Hz)
        Default is 1.0.
        
    Returns
    -------
    dt : float
        Time offset in seconds.
    dy : float
        Tracer offset.
    tau : int
        Window width in seconds.

    """
    
    return dt, dy, tau
