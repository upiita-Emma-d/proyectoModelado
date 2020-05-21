import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt 
import numpy as np
from matplotlib import animation
from scipy.integrate import odeint
import matplotlib.pyplot as plt

def pend(y, t, g, L):
    theta, omega = y
    dydt = [omega,- g/L*np.sin(theta)]
    return dydt


g = 9.81
L = 1



y0 = [np.pi - 0.1, 0.0]



t = np.linspace(0, 10, 501)



sol = odeint(pend, y0, t, args=(g, L))



Xm=L*np.sin(sol[:,0])
Ym=-L*np.cos(sol[:,0])
def init():
    line.set_data([], [])
    return line,


"""
fig=plt.figure(figsize=(15,15))
fig.tight_layout()

ax1=fig.add_subplot(1,2,1)
ax2=fig.add_subplot(1,2,2)

ax1.plot(t, sol[:, 0], label='$theta$')
ax1.plot(t, sol [:, 1], '--k', label='$\dot{tetha}$')


ax1.legend()
ax2.plot(Xm,Ym)

ax1.set_xlabel('x')
ax1.set_ylabel('y')

ax2.set_xlabel('x')
ax2.set_ylabel('y')

ax1.set_title('Tiempo contra Angulo de tetha y $\dot{tetha}$')
ax2.set_title('Grafica2')
escala =10
"""
# First set up the figure, the axis, and the plot element we want to animate
#fig = plt.figure()
#ax2 = plt.axes(xlim=(0, 2), ylim=(-2, 2))
fig = plt.figure()
ax = plt.axes(xlim=(0, 2), ylim=(-2, 2))
line, = ax.plot([], [], lw=2)

# initialization function: plot the background of each frame
def init():
    line.set_data([], [])
    return line,

# animation function.  This is called sequentially
def animate(i):
    x = np.linspace(0, 2, 1000)
    y = np.sin(2 * np.pi * (x - 0.01 * i))
    line.set_data(x, y)
    return line,

# call the animator.  blit=True means only re-draw the parts that have changed.
anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=200, interval=20, blit=True)

# save the animation as an mp4.  This requires ffmpeg or mencoder to be
# installed.  The extra_args ensure that the x264 codec is used, so that
# the video can be embedded in html5.  You may need to adjust this for
# your system: for more information, see
# http://matplotlib.sourceforge.net/api/animation_api.html
anim.save('basic_animation.mp4', fps=30, extra_args=['-vcodec', 'libx264'])

plt.show()