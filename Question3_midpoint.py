import numpy as np
import matplotlib.pyplot as plt

RAD_cm = 10
RAD_m = 0.1
DENS_ball = 11.34 #g/cm^3
C = 0.47
DENS_air = 1.2 #kg/m^3

Mass = (3./4.)*np.pi*RAD_cm**2*DENS_ball*0.001 #mass in kg
Area = np.pi*RAD_m**2 #cross sectional area of the ball in m^2

def Fair(velocity, C=C, DENS_air=DENS_air, Area=Area):
    if velocity > 0:
        return -0.5*C*DENS_air*Area*velocity**2
    if velocity < 0:
        return 0.5*C*DENS_air*Area*velocity**2

def accelxf(t,v):
    return (Fair(v))/Mass
def accelyf(t,v):
    return (Fair(v)-9.81)/Mass

def velocityxf(t,x,curvx):
    v = midpoint2(accelxf, curvx, t,dt)
    return v
def velocityyf(t,x,curvy):
    v = midpoint2(accelyf, curvy, t,dt)
    return v

def midpoint(f, x, t, dt,curv):
    k1 = dt*f(t,x,curv)
    k2 = dt*f(t+dt/2, x+k1/2, curv)
    return x+k2
def midpoint2(f, x, t, dt):
    k1 = dt*f(t,x)
    k2 = dt*f(t+dt/2, x+k1/2)
    return x+k2


#starting dt
dt_change = 0.001
dt = 0.01 + dt_change
old_dist = 1000000
percentError = 10
while percentError > 1: #loop until wanted %error
    #reset all intial variables
    dt -= dt_change #shanges dt
    x = 0
    y = 0
    v = 100
    th = 40/180*np.pi
    vx = v*np.cos(th)
    vy = v*np.sin(th)
    ax = Fair(vx)/Mass
    ay = (Fair(vy) - 9.81)/Mass
    steps = 0
    t = 0
    #saves coordinates for graphing
    xes = [0]
    yes = [0]
    while y >= 0:
        steps += 1 #saves number of steps
        vx = midpoint2(accelxf, vx, t, dt)
        x = midpoint(velocityxf, x, t, dt, vx)
        vy = midpoint2(accelyf, vy, t, dt)
        y = midpoint(velocityyf, y, t, dt, vy)

        t += dt

        xes.append(x)
        yes.append(y)

    #distance calculated using pythagorean theorem
    dist = np.sqrt((x)**2+(y)**2)
    percentError = (abs(dist-old_dist)/old_dist)*100
    print(percentError)
    old_dist = dist


print("Numerical distance: ", dist)
print("step size: ", dt)
print("number of steps: ", steps)
print("percent error of distance: ", percentError)
plt.plot(xes,yes)
plt.show()
