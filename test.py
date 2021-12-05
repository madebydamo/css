from models import simple
import creature
from scene import wall
import numpy as np
import matplotlib.pyplot as plt
import time
from plot.plots import plotCreatures, collectData, plotCreature




"""locations = np.array([[1.1,1]])
goals = np.array([[9,9]])

creatures = []

for i in range(locations.shape[0]):
    creatures.append(creature.Creature(locations[i],goals[i]))

wallStart = np.array([[0,0],[4,0],[4,4],[0,4],[1.5,1.5],[2.5,1.5],[2.5,2.5],[1.5,2.5]])
wallEnd = np.array([[4,0],[4,4],[0,4],[0,0],[2.5,1.5],[2.5,2.5],[1.5,2.5],[1.5,1.5]])


walls = []

for i in range(wallStart.shape[0]):
    walls.append(wall.Wall(wallStart[i], wallEnd[i]))"""

from scene import lane, bottlekneck, evacuate

simulationDuration = 30
dt = 0.01
numberOfTimesteps = int(simulationDuration / dt)

creatures = bottlekneck.creatures()
walls = bottlekneck.objects()

#plotCreatures(creatures, walls, numberOfTimesteps, dt)


locations, velocities = collectData(creatures, walls, numberOfTimesteps, dt)

dirName = f'./tmp/eval{time.time()}'
for i, creature in enumerate(creatures):
    plotCreature(i, walls, locations, velocities, numberOfTimesteps, dt, dirName)
