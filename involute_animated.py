"""
animation of a circle involute
by Gerrit Nowald
"""

import numpy as np
from math import pi as π

import matplotlib.pyplot as plt
plt.style.use('dark_background')
from matplotlib import animation


def plot_circ(*plt_args, radius = 1, center = (0,0), Npoints = 50, ax = None, **plt_kwargs ):
        """circle in x,y plane"""
        if ax is None:
            ax = plt.gca()
        # calculate circle coordinates
        angle = np.linspace(0, 2*np.pi, Npoints+1)
        x = center[0] + radius*np.cos(angle)
        y = center[1] + radius*np.sin(angle)
        # plot circle
        ax.plot( x, y, *plt_args, **plt_kwargs )
        ax.axis('equal')
        return ax

# --------------------------------------------------------------------------
# input

rb = 1      # radius of base circle
N  = 200    # number of points of involute

# --------------------------------------------------------------------------
# calculation

α = np.linspace(0, π, N+1)

r = rb * np.sqrt(1 + α**2)
φ = α - np.arctan(α)

xi = r*np.cos(φ)
yi = r*np.sin(φ)

xt = rb*np.cos(α)
yt = rb*np.sin(α)

# --------------------------------------------------------------------------
# initialise plot

fig, ax = plt.subplots()
fig.tight_layout()
fig.patch.set_alpha(0.0)

plot_circ('w', radius = rb, ax = ax, linewidth=1)

ax.axis('equal')
ax.set_xlim(-3,3)
ax.set_ylim(-2,4)
ax.set_axis_off()

involute, = ax.plot( xi[0],yi[0], c='gold')
tangent,  = ax.plot([xt[0],xi[0]], [yt[0],yi[0]],'w', linewidth=1)
# radius,   = ax.plot([0,xt[0]],[0,yt[0]],         'w', linewidth=0.5)

# --------------------------------------------------------------------------
# animation

def animate(i):
    # update the data
    involute.set_ydata(yi[:i+1])
    involute.set_xdata(xi[:i+1])
    tangent.set_xdata([xt[i],xi[i]])
    tangent.set_ydata([yt[i],yi[i]])
    # radius.set_xdata([0,xt[i]])
    # radius.set_ydata([0,yt[i]])
    return involute,tangent,

ani = animation.FuncAnimation(
    fig, animate, interval=10, blit=True, save_count=N)

# --------------------------------------------------------------------------
# save

ani.save(
    "involute.gif",
    codec="png",
    dpi=300,
    fps=30,
    bitrate=-1,
    savefig_kwargs={"transparent": True, "facecolor": "none"},
)

plt.show()