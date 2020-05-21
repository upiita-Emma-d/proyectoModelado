
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation
from scipy.integrate import odeint


def pend(y, t, g, L):
    theta, omega = y
    dydt = [omega,- g/L*np.sin(theta)]
    return dydt


g = 9.81
L = 1



y0 = [np.pi - 0.1, 0.0]
t = np.linspace(0, 10, 501)
sol = odeint(pend, y0, t, args=(g, L))
teta=sol[:,0]
Xm=L*np.sin(teta)
Ym=-L*np.cos(teta)






fig = plt.figure()
ax = plt.axes(xlim=(-4, 4), ylim=(-5,5))
line, = ax.plot([], [],'o',markersize=15)


def init():
    line.set_data([], [])
    return line,


def animate(i):
    x = Xm[i]
    y = Ym[i]
    line.set_data(x, y)
    return line,


anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=500, interval=10, blit=True)


plt.show()