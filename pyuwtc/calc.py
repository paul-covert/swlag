def errfunc(T_lab, T_inlet_prime):
    return ((T_lab - T_inlet_prime)**2).sum()
    
def transform_inlet_temp(T, dt, dT, tau):
    T_prime = T.shift(int(dt / 5))
    T_prime = T_prime.rolling(int(tau / 5), center=False).mean()
    T_prime = T_prime + dT
