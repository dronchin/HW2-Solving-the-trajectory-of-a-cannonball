import numpy as np
import matplotlib.pyplot as plt
#Midpoint method function
def vfunc(v0, a, t):
    return v0 + a*t

def dismidpoint(x, t, dt, v0 ,a):
    k1 = dt*vfunc(v0,a,t)
    k2 = dt*vfunc(v0, a, t+dt/2)
    return x+k2

RAD_cm = 10
DENS_ball = 11.34 #g/cm^3
Mass = (3./4.)*np.pi*RAD_cm**2*DENS_ball*0.001 #mass in kg

percentError = 10

#starting dt
dt_change = 0.1
dt = 2 + dt_change
errors = []
steplist = []
while percentError > 1: #loop until wanted %error
    #reset all intial variables
    dt -= dt_change #shanges dt
    if dt < 0.00000001:
        dt += dt_change
        break
    x = 0
    y = 0
    v = 100
    ax = 0
    ay = -9.8/Mass
    th = 40/180*np.pi
    vx = v*np.cos(th)
    vy = v*np.sin(th)
    endx = v**2*np.sin(2*th)/abs(ay)
    endy = 0
    steps = 0
    t = 0
    #saves coordinates for graphing
    xes = [0]
    yes = [0]
    while y >= 0:
        steps += 1 #saves number of steps
        #updates position
        x = dismidpoint(x, t, dt, vx ,ax)
        y = dismidpoint(y, t, dt, vy ,ay)
        t += dt
        xes.append(x)
        yes.append(y)

    #distance calculated using pythagorean theorem
    dist = np.sqrt((x)**2+(y)**2)
    percentError = (abs(dist-endx)/endx)*100
    steplist.append(steps)
    errors.append(percentError)


print("Numerical distance: ", dist)
print("Analytical distance: ", endx)
print("step size: ", dt)
print("number of steps: ", steps)
print("percent error of distance: ", percentError)
plt.plot(xes, yes)
plt.show()
