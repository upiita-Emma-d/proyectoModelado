import numpy as np 
import matplotlib.pyplot as plt 
from scipy.integrate import odeint 
import matplotlib.animation as animation

#creamos primero el tiempo de muestreo 
idm=0 #inicio de tiempo
fdm=3 #fin de tiempo 
dt=0.05 # diferencial de tiempo 
t=np.arange(idm,fdm+dt,dt)


#creamos nuestra funcion 
def fdtetha(y,t,g,L):
    teta,W=y
    dwdt=[W,- g/L*np.sin(teta)]
    return dwdt


g = 9.81
L = 1

y0=[(np.pi)/4,0.0]
sol = odeint(fdtetha, y0, t, args=(g, L))
print(len(sol))
#print(sol)
teta=sol[:,0]
Xm=L*np.sin(teta)
print(len(Xm))
Ym=-L*np.cos(teta)
print(len(Ym))


fig = plt.figure()
ax = plt.axes(xlim=(-4, 4), ylim=(-5,5))
pt, = ax.plot([], [],'o',markersize=15)



def init():
    pt.set_data([], [])
    
    return pt,


def dibujador(i):
    x = Xm[i]
    y = Ym[i]
    pt.set_data(x, y)
    
    return pt,


f=len(t)
anim = animation.FuncAnimation(fig, dibujador, init_func=init,frames=43, interval=60, blit=True,repeat=True)


plt.show()
