import numpy as np
import matplotlib.pyplot as plt
#Midpoint method function
def vfunc(v0, a, t):
    return v0 + a*t

def dismidpoint(x, t, dt, v0 ,a):
    k1 = dt*vfunc(v0,a,t)
    k2 = dt*vfunc(v0, a, t+dt/2)
    return x+k2


percentError = 10

#starting dt
dt_change = 0.01
dt = 5 + dt_change
while percentError > 1: #loop until wanted %error
    #reset all intial variables
    dt -= dt_change #shanges dt
    x = 0
    y = 0
    v = 100
    ax = 0
    ay = -9.8
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
        xold = x
        yold = y
        x = dismidpoint(x, t, dt, vx ,ax)
        y = dismidpoint(y, t, dt, vy ,ay)
        time += dt
        xes.append(x)
        yes.append(y)

    #distance calculated using pythagorean theorem
    dist = np.sqrt((x)**2+(y)**2)
    percentError = (abs(dist-endx)/endx)*100


print("Numerical distance: ", dist)
print("Analytical distance: ", endx)
print("step size: ", dt)
print("number of steps: ", steps)
print("percent error of distance: ", percentError)
plt.plot(xes,yes)
plt.show()
