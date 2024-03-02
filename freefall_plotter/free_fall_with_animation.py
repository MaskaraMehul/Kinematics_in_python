import matplotlib.pyplot as plt  
import numpy as np 
import math
from matplotlib.animation import FuncAnimation
import scienceplots

#plt.style.use(['science','no-latex'])
#plt.rcParams.update({"font.family": "garamond", "font.serif": ["Garamond"], "font.size":14})

user_height = float(input("Enter height(in m) from which ball is dropped: "))
user_mass = float(input("Enter mass(in kg) of ball dropped: "))

g = 9.81
t = np.linspace(0,10,1000)
s = user_height - (0.5*g*t**2)
v = g*t
k = 0.5*(user_mass)*(v**2)
p = (user_mass)*g*s

s1 = [num for num in s if num >= 0 ]

t1 = (t[:len(s1)])
v1 = (v[:len(s1)])
k1 = (k[:len(s1)])
p1 = (p[:len(s1)])

fig = plt.figure(figsize = (8,5))

ax1 = fig.add_subplot(1,2,1)
ax2 = fig.add_subplot(2,2,2)
ax3 = fig.add_subplot(2,2,4)

ax1.set_xlim([min(t1), max(t1)])
if max(v1) > max(s1):
    ax1.set_ylim([0,max(v1)])
elif max(s1) > max(v1):
    ax1.set_ylim([0, max(s1)])

animated_plot1, = ax1.plot([], [], color = 'red',linewidth = 1)
animated_plot2, = ax1.plot([], [], color = 'blue', linewidth = 1)
animated_plot3, = ax2.plot([], [], color = 'blue', linewidth = 1)
animated_plot4, = ax2.plot([], [], color = 'green', linewidth = 1)
animated_plot5, = ax3.plot([], [], color = 'red', linewidth = 1)
animated_plot6, = ax3.plot([], [], color = 'green', linewidth = 1)

def update_data(frame):
    animated_plot1.set_data(t1[:frame], v1[:frame])
    animated_plot2.set_data(t1[:frame], s1[:frame])
    animated_plot3.set_data(t1[:frame], s1[:frame])
    animated_plot4.set_data(t1[:frame], p1[:frame])
    animated_plot5.set_data(t1[:frame], v1[:frame])
    animated_plot6.set_data(t1[:frame], k1[:frame])
    return animated_plot1,
    return animated_plot2,
    return animated_plot3,
    return animated_plot4,
    return animated_plot5,
    return animated_plot6,

animation = FuncAnimation(fig = fig, func = update_data, frames = len(t1), interval = 1)

ax1.set_xlabel("Time(s)")
ax1.set_ylabel("Velocity(m/s), Height(m)")
ax1.set_title("Velocity/Height v/s Time")
ax1.legend(['Velocity(m/s)', 'Height(m)'])
ax1.grid()

ax2.set_xlim([min(t1), max(t1)])
if max(p1) > max(s1):
    ax2.set_ylim([0, max(p1)])
elif max(s1) > max(p1):
    ax2.set_ylim([0, max(s1)])

ax2.set_xlabel("Time(s)")
ax2.set_ylabel("Height(m), Potential Energy(J)")
ax2.set_title("Height, Potential Energy v/s Time")
ax2.legend(['Height(m)','Potential Energy(J)'])
ax2.grid()

ax3.set_xlim([min(t1), max(t1)])
if max(v1) > max(k1):
    ax3.set_ylim([0, max(v1)])
elif max(k1) > max(v1):
    ax3.set_ylim([0, max(k1)])

ax3.set_xlabel("Time(s)")
ax3.set_ylabel("Velocity(m/s), Kinetic Energy(J)")
ax3.set_title("Velocity, Kinetic Energy v/s Time")
ax3.legend(['Velocity(m/s)', 'Kinetic Energy(J)'])
ax3.grid()

plt.subplots_adjust(hspace=0.35)
animation.save('[InsertName].gif')
plt.suptitle("Height,Velocity, KE and PE of an object dropped from a height")
plt.show()
