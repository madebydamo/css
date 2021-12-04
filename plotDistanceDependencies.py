import models.simple as simple
import numpy as np
import matplotlib.pyplot as plt
import wall
import creature


walls = wall.Wall(np.array([0,0]),np.array([20,0]))
d = np.linspace(0,1.5,100)

def calculateForce(d):
    destination = np.array([10,-100])
    location = np.array([10,d])
    robot = creature.Creature(location,destination)
    return simple.agentObjectForceAB(robot,walls,0.5,A=10, B=0.2)

f = np.zeros((d.size,2))
for i in range(d.size):
    f[i] = calculateForce(d[i])[1]

plt.figure()
plt.plot(d,f)
plt.grid()
plt.xlabel(r'Distance between Obstacle and Pedestrian $|| r_{\alpha i} ||$ in $[m]$')
plt.ylabel(r'Force between Obstacle and Pedestrian $|| f_{\alpha i} ||$ in $[\frac{kg \ m}{ s^2}]$')
plt.savefig('GraphicsForReport/AgentObjectForce.svg',format='svg')
plt.show()

agentA = creature.Creature(np.array([10,0]),np.array([10,0]))

def calculateForce(d):
    destination = np.array([10,-100])
    location = np.array([10,d])
    robot = creature.Creature(location,destination)
    return simple.agentDistanceForceAB(robot,agentA,0.5,A=2.1, B=0.5)

g = np.zeros((d.size,2))
for i in range(d.size):
    g[i] = calculateForce(d[i])[1]

plt.figure()
plt.plot(d,g)
plt.grid()
plt.xlabel(r'Distance between two Pedestrians $|| r_{\alpha \beta} ||$ in $[m]$')
plt.ylabel(r'Force between two Pedestrians $|| f_{\alpha \beta} ||$ in $[\frac{kg \ m}{ s^2}]$')
plt.savefig('GraphicsForReport/AgentAgentForce.svg',format='svg')
plt.show()
