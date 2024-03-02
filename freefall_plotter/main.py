import matplotlib.pyplot as plt  
import numpy as np 
import math
import scienceplots

user_height = float(input("Enter height(in m) from which ball is dropped: "))
user_mass = float(input("Enter mass(in kg) of ball dropped: "))

t = np.linspace(0,10,1000)
s = user_height - (0.5*9.8*t**2)
v = 9.8*t
k = 0.5*(user_mass)*(v**2)
p = (user_mass)*9.8*s

s1 = []

for num in s:
    if num >= 0:
        s1.append(num)

t1 = (t[:len(s1)])
v1 = (v[:len(s1)])
k1 = (k[:len(s1)])
p1 = (p[:len(s1)])

plt.style.use(['science','no-latex'])
plt.rcParams.update({"font.family": "garamond", "font.serif": ["Garamond"], "font.size":14})

fig = plt.figure()

ax1 = fig.add_subplot(1,2,1)
ax2 = fig.add_subplot(2,2,2)
ax3 = fig.add_subplot(2,2,4)

ax1.plot(t1,v1, label = "Velocity(m/s)", linewidth = 1, color = 'red')
ax1.plot(t1,s1, label = 'Height(m)', linewidth = 1, color = 'blue')
ax1.set_xlabel("Time(s)")
ax1.set_ylabel("Velocity(m/s), Height(m)")
ax1.set_title("Velocity/Height v/s Time")
ax1.legend()
ax1.grid()

ax2.plot(t1,s1, label = 'Height(m)', color  = 'blue', linewidth = 1)
ax2.plot(t1,p1, label = "Potential Energy(J)",color = 'green', linewidth = 1)
ax2.set_xlabel("Time(s)")
ax2.set_ylabel("Height(m), Potential Energy(J)")
ax2.set_title("Height, Potential Energy v/s Time")
ax2.legend()
ax2.grid()

ax3.plot(t1,v1, label = "Velocity(m/s)", color = 'red', linewidth = 1)
ax3.plot(t1,k1, label = "Kinetic Energy(J)",color = 'green', linewidth = 1)
ax3.set_xlabel("Time(s)")
ax3.set_ylabel("Velocity(m/s), Kinetic Energy(J)")
ax3.set_title("Velocity, Kinetic Energy v/s Time")
ax3.legend()
ax3.grid()

plt.subplots_adjust(hspace=0.35)

plt.suptitle("Height,Velocity, KE and PE of an object dropped from a height")
plt.show()
