import numpy as np
import matplotlib.pyplot as plt

#Euler method function
def Euler(x, dx, dt):
    return x + dt*dx

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

dt = 0.5
x = 0
y = 0
v = 100
th = 40/180*np.pi
vx = v*np.cos(th)
vy = v*np.sin(th)
ax = Fair(vx)/Mass
ay = (Fair(vy) - 9.81)/Mass
steps1 = 0
#saves coordinates for graphing
xes1 = [0]
yes1 = [0]
while y >= 0:
    steps1 += 1 #saves number of steps
    #updates velocity
    vx = Euler(vx, ax, dt)
    vy = Euler(vy, ay, dt)

    #updates position
    x = Euler(x, vx, dt)
    y = Euler(y, vy, dt)

    #updates forces and acceleration
    Fx = Fair(vx)
    Fy = Fair(vy) - 9.81
    ax = Fx/Mass
    ay = Fy/Mass

    xes1.append(x)
    yes1.append(y)

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

dt = 0.5
x = 0
y = 0
v = 100
th = 40/180*np.pi
vx = v*np.cos(th)
vy = v*np.sin(th)
ax = Fair(vx)/Mass
ay = (Fair(vy) - 9.81)/Mass
steps2 = 0
t = 0
#saves coordinates for graphing
xes2 = [0]
yes2 = [0]
while y >= 0:
    steps2 += 1 #saves number of steps
    vx = midpoint2(accelxf, vx, t, dt)
    x = midpoint(velocityxf, x, t, dt, vx)
    vy = midpoint2(accelyf, vy, t, dt)
    y = midpoint(velocityyf, y, t, dt, vy)

    t += dt

    xes2.append(x)
    yes2.append(y)

plt.plot(xes1,yes1, label="Euler")
plt.plot(xes2,yes2, label="Midpoint")
plt.legend()
plt.show()
