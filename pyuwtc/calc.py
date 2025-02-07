def _check_timeseries_spacing(df):
    """Ensure monotonically increasing time"""
    import numpy as np
    
    diff = np.diff(df.index.to_numpy())
    return np.all(diff==diff[0])


def transform_inlet_temp(T, dt, dT, tau):
    T_prime = T.shift(int(dt / 5))
    T_prime = T_prime.rolling(int(tau / 5), center=False).mean()
    T_prime = T_prime + dT
    return T_prime


def errfunc(Tinlet, Tlab):
    Tinlet_prime = transform_inlet_temp(T, dt, dT, tau)
    return ((Tlab - Tinlet) ** 2).sum()


def calc_time_consts(Tinlet, Tlab, dt0, dT0, tau0):
    
