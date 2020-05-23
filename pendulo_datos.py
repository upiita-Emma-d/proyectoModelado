import numpy as np
from scipy.integrate import odeint
def pendulosimple():
    def pend(y, t, g, L):
        theta, omega = y
        dydt = [omega,- g/L*np.sin(theta)]
        return dydt
    y0 = [np.pi - 0.1, 0.0]
    dt=0.040
    g=9.81
    L=1
    t = np.arange(0,15,dt)
    sol = odeint(pend, y0, t, args=(g, L))
    angulo=sol[:,0]
    velocidad=sol[:,1]
    Xm=L*100*np.sin(angulo)
    Ym=L*100*np.cos(angulo)
    anguloGra=np.degrees(angulo)
    anguloGra=np.around(anguloGra,decimals=1)
    velocidad=np.around(velocidad,decimals=1)
    return anguloGra,velocidad,Xm,Ym,t 