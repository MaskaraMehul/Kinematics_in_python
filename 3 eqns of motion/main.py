import tkinter
import numpy as np
import matplotlib.pyplot as plt 
import math

required = input("What do you want to Calculate: Acceleration(a), Final Velocity(v), Initial Velocity(u), Distance(s) or Time(t)?: ")

time_units = ['Time', 'time', 't', 'T']
hour_units = ["Hours, Hour, hours, hour, H, h"]
minute_units = ["Minutes", "Minute", "minutes", 'minute', 'm', 'M']
second_units = ["Seconds", "Second", "seconds", "seconds", "s", "S"]
acc_units = ["Acceleration", 'acceleration', 'a', 'A']
vfinal_units = ['v', "V"]
vinitial_units = ['u', 'U']
distance_units = ["Distance", 'distance', 's', 'S']

unit = input("Which unit of time are you using, (Hours, Minutes or Seconds)?: ")
def unit_sec(t):
        if unit in hour_units:
            return float(t)*3600
        elif unit in minute_units:
            return float(t)*60
        elif unit in second_units:
            return float(t)

fig = plt.figure()
ax1 = fig.add_subplot(3,1,1)
ax2 = fig.add_subplot(3,1,2)
ax3 = fig.add_subplot(3,1,3)

if required in acc_units:
    formula = input("Which formula do you want to use?(1 or 3)?: ")
    
    if formula == '1':
        u = input("Enter Initial Velocity: ")
        v = input("Enter Final Velocity: ")
        t = input("Enter time: ")
    
        a = (float(v) - float(u))/float(unit_sec(t))
        print(f"Acceleration is: {a}m/s^2")
        s = float(u)*float(unit_sec(t)) + 0.5*float(a)*float(unit_sec(t))**2
        print(f"Distance covered is: {s}m")

        t_range = np.arange(0,unit_sec(t) + 0.1, 0.1)
        acc = [a]*len(t_range)
        v = [(float(u) + float(a)*float(unit_sec(t))) for t in t_range]
        s = [(float(u)*float(unit_sec(t)) + 0.5*float(a)*float(unit_sec(t))**2) for t in t_range]
        
        ax1.plot(t_range,acc, label = "Acceleration")
        ax2.plot(t_range,v, 'orange', label = "Velocity")
        ax3.plot(t_range,s, 'green', label = "Distance")

        ax1.set_title('Acceleration(m\s^2) v/s Time(s)')
        ax1.set_xlabel('Time(s)')
        ax1.set_ylabel('Acceleration(m/s^2)')


        ax2.set_title('Velocity(m/s) v/s Time(s)')
        ax2.set_xlabel('Time(s)')
        ax2.set_ylabel('Velocity(m/s)')

        ax3.set_title('Distance(m) v/s Time(s)')
        ax3.set_xlabel('Time(s)')
        ax3.set_ylabel('Distance(m)')

        ax1.grid()
        ax2.grid()
        ax3.grid()

        ax1.legend(loc = 'upper left')
        ax2.legend(loc = 'upper left')
        ax3.legend(loc = 'upper left')

        plt.subplots_adjust(hspace=0.6)
        fig.suptitle("Graphs of the Given Motion")
        plt.show()
    
    elif formula == '3':
        u = input("Enter Initial Velocity: ")
        v = input("Enter Final Velocity: ")
        s = input("Enter Distance: ")
    
        a  = (float(v)**2 - float(u)**2)/(2*float(s))
        print(f"Acceleration is: {a}m/s^2")
        t = (float(v) - float(u))/float(a)
        print(f"Time taken is: {t}s")

        t_range = np.arange(0,unit_sec(t) + 0.1, 0.1)
        acc = [a]*len(t_range)
        v = [(float(u) + float(a)*float(unit_sec(t))) for t in t_range]
        s = [(float(u)*float(unit_sec(t)) + 0.5*float(a)*float(unit_sec(t))**2) for t in t_range]
        
        ax1.plot(t_range,acc, label = "Acceleration")
        ax2.plot(t_range,v, 'orange', label = "Velocity")
        ax3.plot(t_range,s, 'green', label = "Distance")

        ax1.set_title('Acceleration(m\s^2) v/s Time(s)')
        ax1.set_xlabel('Time(s)')
        ax1.set_ylabel('Acceleration(m/s^2)')


        ax2.set_title('Velocity(m/s) v/s Time(s)')
        ax2.set_xlabel('Time(s)')
        ax2.set_ylabel('Velocity(m/s)')

        ax3.set_title('Distance(m) v/s Time(s)')
        ax3.set_xlabel('Time(s)')
        ax3.set_ylabel('Distance(m)')

        ax1.grid()
        ax2.grid()
        ax3.grid()

        ax1.legend(loc = 'upper left')
        ax2.legend(loc = 'upper left')
        ax3.legend(loc = 'upper left')

        plt.subplots_adjust(hspace=0.6)
        fig.suptitle("Graphs of the Given Motion")
        plt.show()

    
elif required in distance_units:
    formula = input("Which formula do you want to use?(2 or 3)?: ")
    
    if formula == "2":
        u = input("Enter Initial Velocity: ")
        a = input("Enter Acceleration(m/s^2): ")
        t = input("Enter time: ")

        s = float(u)*float(unit_sec(t)) + 0.5*float(a)*float(unit_sec(t))**2
        print(f"Distance covered is: {s}m")
        v = float(u) + float(a)*float(unit_sec(t))
        print(f"Final Velocity is: {v}m/s")
        
        t_range = np.arange(0,unit_sec(t) + 0.1, 0.1)
        acc = [a]*len(t_range)
        v = [(float(u) + float(a)*float(unit_sec(t))) for t in t_range]
        s = [(float(u)*float(unit_sec(t)) + 0.5*float(a)*float(unit_sec(t))**2) for t in t_range]
        
        ax1.plot(t_range,acc, label = "Acceleration")
        ax2.plot(t_range,v, 'orange', label = "Velocity")
        ax3.plot(t_range,s, 'green', label = "Distance")

        ax1.set_title('Acceleration(m\s^2) v/s Time(s)')
        ax1.set_xlabel('Time(s)')
        ax1.set_ylabel('Acceleration(m/s^2)')


        ax2.set_title('Velocity(m/s) v/s Time(s)')
        ax2.set_xlabel('Time(s)')
        ax2.set_ylabel('Velocity(m/s)')

        ax3.set_title('Distance(m) v/s Time(s)')
        ax3.set_xlabel('Time(s)')
        ax3.set_ylabel('Distance(m)')

        ax1.grid()
        ax2.grid()
        ax3.grid()

        ax1.legend(loc = 'upper left')
        ax2.legend(loc = 'upper left')
        ax3.legend(loc = 'upper left')

        plt.subplots_adjust(hspace=0.6)
        fig.suptitle("Graphs of the Given Motion")
        plt.show()
    
    elif formula == '3':
        u = input("Enter Initial Velocity: ")
        v = input("Enter Final Velocity: ): ")
        a = input("Enter Acceleration(m/s^2): ")

        s = (float(v)**2 - float(u)**2)/2*float(a)
        print(f"Distance covered is: {s}m")
        t = (float(v) - float(u))/float(a)
        print(f"Time taken is: {t}s")

        t_range = np.arange(0,unit_sec(t) + 0.1, 0.1)
        acc = [a]*len(t_range)
        v = [(float(u) + float(a)*float(unit_sec(t))) for t in t_range]
        s = [(float(u)*float(unit_sec(t)) + 0.5*float(a)*float(unit_sec(t))**2) for t in t_range]
        
        ax1.plot(t_range,acc, label = "Acceleration")
        ax2.plot(t_range,v, 'orange', label = "Velocity")
        ax3.plot(t_range,s, 'green', label = "Distance")

        ax1.set_title('Acceleration(m\s^2) v/s Time(s)')
        ax1.set_xlabel('Time(s)')
        ax1.set_ylabel('Acceleration(m/s^2)')


        ax2.set_title('Velocity(m/s) v/s Time(s)')
        ax2.set_xlabel('Time(s)')
        ax2.set_ylabel('Velocity(m/s)')

        ax3.set_title('Distance(m) v/s Time(s)')
        ax3.set_xlabel('Time(s)')
        ax3.set_ylabel('Distance(m)')

        ax1.grid()
        ax2.grid()
        ax3.grid()

        ax1.legend(loc = 'upper left')
        ax2.legend(loc = 'upper left')
        ax3.legend(loc = 'upper left')

        plt.subplots_adjust(hspace=0.6)
        fig.suptitle("Graphs of the Given Motion")
        plt.show()

    
elif required in vfinal_units:
    formula = input("Which formula do you want to use?(1 or 3)?: ")
    
    if formula == "1":
        u = input("Enter Initial Velocity: ")
        t = input("Enter Time: ")
        a = input("Enter Acceleration: ")
        
        v = float(u) + float(a)*float(unit_sec(t))
        print(f"Final Velocity is: {v}m/s")
        s = float(u)*float(unit_sec(t)) + 0.5*float(a)*float(unit_sec(t)**2)
        print(f"Distance covered is: {s}m")

        t_range = np.arange(0,unit_sec(t) + 0.1, 0.1)
        acc = [a]*len(t_range)
        v = [(float(u) + float(a)*float(unit_sec(t))) for t in t_range]
        s = [(float(u)*float(unit_sec(t)) + 0.5*float(a)*float(unit_sec(t))**2) for t in t_range]
        
        ax1.plot(t_range,acc, label = "Acceleration")
        ax2.plot(t_range,v, 'orange', label = "Velocity")
        ax3.plot(t_range,s, 'green', label = "Distance")

        ax1.set_title('Acceleration(m\s^2) v/s Time(s)')
        ax1.set_xlabel('Time(s)')
        ax1.set_ylabel('Acceleration(m/s^2)')


        ax2.set_title('Velocity(m/s) v/s Time(s)')
        ax2.set_xlabel('Time(s)')
        ax2.set_ylabel('Velocity(m/s)')

        ax3.set_title('Distance(m) v/s Time(s)')
        ax3.set_xlabel('Time(s)')
        ax3.set_ylabel('Distance(m)')

        ax1.grid()
        ax2.grid()
        ax3.grid()

        ax1.legend(loc = 'upper left')
        ax2.legend(loc = 'upper left')
        ax3.legend(loc = 'upper left')

        plt.subplots_adjust(hspace=0.6)
        fig.suptitle("Graphs of the Given Motion")
        plt.show()

    elif formula == "3":
        u = input("Enter Initial Velocity: ")
        a = input("Enter Acceleration: ")
        s = input("Enter Distance: ")

        v = math.sqrt(float(u)**2 + 2*float(a)*float(s))
        print(f"Final Velocity is: {v}m/s")
        t = (float(v) - float(u))/float(a)
        print(f"Time is {s}s")

        t_range = np.arange(0,unit_sec(t) + 0.1, 0.1)
        acc = [a]*len(t_range)
        v = [(float(u) + float(a)*float(unit_sec(t))) for t in t_range]
        s = [(float(u)*float(unit_sec(t)) + 0.5*float(a)*float(unit_sec(t))**2) for t in t_range]
        
        ax1.plot(t_range,acc, label = "Acceleration")
        ax2.plot(t_range,v, 'orange', label = "Velocity")
        ax3.plot(t_range,s, 'green', label = "Distance")

        ax1.set_title('Acceleration(m\s^2) v/s Time(s)')
        ax1.set_xlabel('Time(s)')
        ax1.set_ylabel('Acceleration(m/s^2)')


        ax2.set_title('Velocity(m/s) v/s Time(s)')
        ax2.set_xlabel('Time(s)')
        ax2.set_ylabel('Velocity(m/s)')

        ax3.set_title('Distance(m) v/s Time(s)')
        ax3.set_xlabel('Time(s)')
        ax3.set_ylabel('Distance(m)')

        ax1.grid()
        ax2.grid()
        ax3.grid()

        ax1.legend(loc = 'upper left')
        ax2.legend(loc = 'upper left')
        ax3.legend(loc = 'upper left')

        plt.subplots_adjust(hspace=0.6)
        fig.suptitle("Graphs of the Given Motion")
        plt.show()

elif required in vinitial_units:
    formula = input("Which formula do you want to use?(1,2 or 3)?: ")
    
    if formula == "1":
        v = input("Enter Final Velocity: ")
        a = input("Enter Acceleration: ")
        t = input("Enter Time: ")

        u = float(v) - float(a)*float(unit_sec(t))
        print(f"Initial Velocity is {u}m/s")
        s = float(u)*float(unit_sec(t)) + 0.5*float(a)*float(unit_sec(t))**2
        print(f"Distance covered is: {s}m")

        t_range = np.arange(0,unit_sec(t) + 0.1, 0.1)
        acc = [a]*len(t_range)
        v = [(float(u) + float(a)*float(unit_sec(t))) for t in t_range]
        s = [(float(u)*float(unit_sec(t)) + 0.5*float(a)*float(unit_sec(t))**2) for t in t_range]
        
        ax1.plot(t_range,acc, label = "Acceleration")
        ax2.plot(t_range,v, 'orange', label = "Velocity")
        ax3.plot(t_range,s, 'green', label = "Distance")

        ax1.set_title('Acceleration(m\s^2) v/s Time(s)')
        ax1.set_xlabel('Time(s)')
        ax1.set_ylabel('Acceleration(m/s^2)')


        ax2.set_title('Velocity(m/s) v/s Time(s)')
        ax2.set_xlabel('Time(s)')
        ax2.set_ylabel('Velocity(m/s)')

        ax3.set_title('Distance(m) v/s Time(s)')
        ax3.set_xlabel('Time(s)')
        ax3.set_ylabel('Distance(m)')

        ax1.grid()
        ax2.grid()
        ax3.grid()

        ax1.legend(loc = 'upper left')
        ax2.legend(loc = 'upper left')
        ax3.legend(loc = 'upper left')

        plt.subplots_adjust(hspace=0.6)
        fig.suptitle("Graphs of the Given Motion")
        plt.show()

    elif formula == "2":
        s = input("Enter Distance: ")
        a = input("Enter Acceleration: ")
        t = input("Enter Time: ")

        u = (float(s) - 0.5*float(a)*float(unit_sec(t))**2)/float(unit_sec(t))
        print(f"Initial Velocity is: {u}m/s")
        v = float(u) + float(a)*float(unit_sec(t))
        print(f"Final Velocity is: {v}m/s")

        t_range = np.arange(0,unit_sec(t) + 0.1, 0.1)
        acc = [a]*len(t_range)
        v = [(float(u) + float(a)*float(unit_sec(t))) for t in t_range]
        s = [(float(u)*float(unit_sec(t)) + 0.5*float(a)*float(unit_sec(t))**2) for t in t_range]
        
        ax1.plot(t_range,acc, label = "Acceleration")
        ax2.plot(t_range,v, 'orange', label = "Velocity")
        ax3.plot(t_range,s, 'green', label = "Distance")

        ax1.set_title('Acceleration(m\s^2) v/s Time(s)')
        ax1.set_xlabel('Time(s)')
        ax1.set_ylabel('Acceleration(m/s^2)')


        ax2.set_title('Velocity(m/s) v/s Time(s)')
        ax2.set_xlabel('Time(s)')
        ax2.set_ylabel('Velocity(m/s)')

        ax3.set_title('Distance(m) v/s Time(s)')
        ax3.set_xlabel('Time(s)')
        ax3.set_ylabel('Distance(m)')

        ax1.grid()
        ax2.grid()
        ax3.grid()

        ax1.legend(loc = 'upper left')
        ax2.legend(loc = 'upper left')
        ax3.legend(loc = 'upper left')

        plt.subplots_adjust(hspace=0.6)
        fig.suptitle("Graphs of the Given Motion")
        plt.show()

    elif formula == "3":
        s = input("Enter Distance: ")
        a = input("Enter Acceleration: ")
        v = input("Enter Final Velocity: ")

        u = math.sqrt(float(v)**2 - 2*float(a)*float(s))
        print(f"Initial Velocity is: {u}m/s")
        t = (float(v) - float(u))/float(a)
        print(f"Time taken is: {t}s")

        t_range = np.arange(0,unit_sec(t) + 0.1, 0.1)
        acc = [a]*len(t_range)
        v = [(float(u) + float(a)*float(unit_sec(t))) for t in t_range]
        s = [(float(u)*float(unit_sec(t)) + 0.5*float(a)*float(unit_sec(t))**2) for t in t_range]
        
        ax1.plot(t_range,acc, label = "Acceleration")
        ax2.plot(t_range,v, 'orange', label = "Velocity")
        ax3.plot(t_range,s, 'green', label = "Distance")

        ax1.set_title('Acceleration(m\s^2) v/s Time(s)')
        ax1.set_xlabel('Time(s)')
        ax1.set_ylabel('Acceleration(m/s^2)')


        ax2.set_title('Velocity(m/s) v/s Time(s)')
        ax2.set_xlabel('Time(s)')
        ax2.set_ylabel('Velocity(m/s)')

        ax3.set_title('Distance(m) v/s Time(s)')
        ax3.set_xlabel('Time(s)')
        ax3.set_ylabel('Distance(m)')

        ax1.grid()
        ax2.grid()
        ax3.grid()

        ax1.legend(loc = 'upper left')
        ax2.legend(loc = 'upper left')
        ax3.legend(loc = 'upper left')

        plt.subplots_adjust(hspace=0.6)
        fig.suptitle("Graphs of the Given Motion")
        plt.show()

elif required in time_units:
    
    u = input("Enter Initial Velocity: ")
    a = input("Enter Acceleration: ")
    v = input("Enter Final Velocity: ")

    t = (float(v) - float(u))/float(a)
    print(f"Time is {t}s")
    s = s = float(u)*float(unit_sec(t)) + 0.5*float(a)*float(unit_sec(t))**2
    print(f"Distance covered is: {s}m")

    t_range = np.arange(0,unit_sec(t) + 0.1, 0.1)
    acc = [a]*len(t_range)
    v = [(float(u) + float(a)*float(unit_sec(t))) for t in t_range]
    s = [(float(u)*float(unit_sec(t)) + 0.5*float(a)*float(unit_sec(t))**2) for t in t_range]
    
    ax1.plot(t_range,acc, label = "Acceleration")
    ax2.plot(t_range,v, 'orange', label = "Velocity")
    ax3.plot(t_range,s, 'green', label = "Distance")
        
    ax1.set_title('Acceleration(m\s^2) v/s Time(s)')
    ax1.set_xlabel('Time(s)')
    ax1.set_ylabel('Acceleration(m/s^2)')  
        
    ax2.set_title('Velocity(m/s) v/s Time(s)')
    ax2.set_xlabel('Time(s)')
    ax2.set_ylabel('Velocity(m/s)')
        
    ax3.set_title('Distance(m) v/s Time(s)')
    ax3.set_xlabel('Time(s)')
    ax3.set_ylabel('Distance(m)') 
        
    ax1.grid()
    ax2.grid()
    ax3.grid()  
        
    ax1.legend(loc = 'upper left')
    ax2.legend(loc = 'upper left')
    ax3.legend(loc = 'upper left')  
        
    plt.subplots_adjust(hspace=0.6)
    fig.suptitle("Graphs of the Given Motion")
    plt.show()  

