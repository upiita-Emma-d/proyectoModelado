import matplotlib.pyplot as plt 
from matplotlib import  animation
import numpy as np 
from scipy.integrate import  odeint

idm=0
fdm=20
dt=0.1
t=np.arange(idm,fdm,dt)

def mmr(y,t,m,k):
    x,v =y
    dxdy=[v ,-k*x/m]
    return dxdy

m=1
k=.1
y0=[1,0]
sol=odeint(mmr,y0,t,args=(m,k))
xp=sol[:,0]



fig = plt.figure()
ax = plt.axes(xlim=(-4, 4), ylim=(-5,5))
line, = ax.plot([], [],'r-o',markersize=15)
ax=plt.style.use(['dark_background'])

def init():
    line.set_data([], [])
    return line,


def animate(i):
    x = xp[i]
    y =0
    line.set_data(x, y)
    return line,


anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=len(t), interval=14, blit=True,repeat=True)


plt.show()

