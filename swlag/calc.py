# swlag: Lag and averaging time constant calculation in Python.
# Copyright (C) 2025  Paul A. Covert (GNU GPLv3)
"""Calculate transformed inlet temperatures and error functions"""


def _transform_inlet_tracer(y, dt, dy, tau):
    """
    Apply time offset, temperature offset, and windowing transform
    to a temperature record.
    
    Parameters
    ----------
    y : Pandas Series
        Tracer series to be transformed.
    dt : float
        Constant representing the timelag of the loop system.
    dy : float
        Constant representing a net addition or subtraction of
        tracer intensity between the inlet and lab.  This, most
        likely, only applies to temperature (warming or cooling).
    tau : integer
        width of the averaging window in seconds.
        
    Returns
    -------
    y_prime : 1-d numpy array or Pandas Series
        Transformed tracer series.
        
    """
    
    y_prime = y.shift(int(dt / 5))
    y_prime = y_prime.rolling(int(tau / 5), center=False).mean()
    y_prime = y_prime + dy
    
    return y_prime


def _errfunc(y, y_prime, dt, dy, tau):
    """
    Error function used in minimization function.
    
    Parameters
    ----------
    y : Pandas Series
        Input tracer series
    y_prime : Pandas Series
        Transformed tracer series
    dt : float
        Constant representing the timelag of the loop system.
    dy : float
        Constant representing an integrated addition or subtraction 
        of tracer intensity.
    tau : integer
        width of the averaging window in seconds.
    
    Returns
    -------
    sumsq : float
        Sum of squares of residuals
    
    """
    
    y_prime = _transform_inlet_temp(y, dt, dy, tau)
    sumsq = ((y - y_prime) ** 2).sum()
    
    return sumsq


def estimate_time_consts(
    y_inlet, 
    y_lab, 
    freq=1.0, 
    dt0=None,
    dy0=None,
    tau0=None
):
    """
    Calculate, by minimization of error function, the best
    fit time constants to transform a tracer signal (e.g. 
    temperature, salinity, dye, etc.) measured at the inlet
    to the tracer signal measured in the lab.
    
    Parameters
    ----------
    y_inlet : Pandas Series
        Inlet tracer series.
    y_lab : Pandas Series
        Lab tracer series.
    freq : float (optional)
        Sampling frequency (Hz)
        Default is 1.0.
    dt0 : float (optional)
        Initial guess for dt.
        Default is None.
    dy0 : float (optional)
        Initial guess for dy.
        Default is None.
    tau0 : float (optional)
        Initial guess for tau.
        Default is None.
        
    Returns
    -------
    dt : float
        Constant representing the timelag of the loop system.
    dy : float
        Constant representing a net addition or subtraction of
        tracer intensity between the inlet and lab.  This, most
        likely, only applies to temperature (warming or cooling).
    tau : integer
        width of the averaging window in seconds.

    """
    
    return dt, dy, tau
