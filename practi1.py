import numpy as np 
import matplotlib.pyplot as plt 
from scipy.integrate import odeint
from matplotlib import animation 
idm=0
fdm=100
dt=.1
t=np.arange(idm,fdm,dt)

def oscilador(y,t,m,k):
    x, v = y
    dydt = [v,- (k*x/m)]
    return dydt
m=1
k=1/2
x0=[1,0]
sol = odeint(oscilador, x0, t, args=(m, k))
x=sol[:,0]
Xm=x
Ym=0
#fig = plt.figure()
#ax = plt
#ax.plot([t], [Xm],'o',markersize=1)






fig = plt.figure()
ax = plt.axes(xlim=(-4, 4), ylim=(-5,5))
line, = ax.plot([], [],'r-o',markersize=15)
ax=plt.style.use(['dark_background'])

def init():
    line.set_data([], [])
    return line,


def animate(i):
    x = Xm[i]
    y =0
    line.set_data(x, y)
    return line,


anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=1000, interval=14, blit=True,repeat=True)


plt.show()
