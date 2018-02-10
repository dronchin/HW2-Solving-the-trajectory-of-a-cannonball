import numpy as np
import matplotlib.pyplot as plt
#Euler method function
def Euler(x, dx, dt):
    return x + dt*dx
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
    #saves coordinates for graphing
    xes = [0]
    yes = [0]
    while y >= 0:
        steps += 1 #saves number of steps
        #updates position
        x = Euler(x, vx, dt)
        y = Euler(y, vy, dt)
        #updates velocity
        vx = Euler(vx, ax, dt)
        vy = Euler(vy, ay, dt)
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
