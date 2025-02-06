def errfunc(T_lab, T_inlet_prime):
    return ((T_lab - T_inlet_prime)**2).sum()
    
def transform_inlet_temp(T, dt, dT, tau):
    
    