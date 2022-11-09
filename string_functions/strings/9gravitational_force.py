def gravity(g:float, me:float, mm:float, r:float):
    grav_force = (g * me * mm) / r**2
    return f"Gravitational Force = {grav_force}"

print(gravity(6.67*10**-11, 6.0*10**24, 7.34*10**24, 3.84*10**8))