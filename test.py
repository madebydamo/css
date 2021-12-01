from models import simple
import creature
import wall
import numpy as np
import matplotlib.pyplot as plt
from plots import plotCreatures

locations = np.array([[0.2,0.2]])
goals = np.array([[3.8,3.8]])
#locations = np.array([[1,1],[9,9],[1,9]])
#goals = np.array([[9,9],[1,1],[9,1]])

creatures = []

for i in range(locations.shape[0]):
    creatures.append(creature.Creature(locations[i],goals[i]))

#wallStart = np.array([[0,0],[4,0],[4,4],[0,4],[1.5,1.5],[2.5,1.5],[2.5,2.5],[1.5,2.5]])
#wallEnd = np.array([[4,0],[4,4],[0,4],[0,0],[2.5,1.5],[2.5,2.5],[1.5,2.5],[1.5,1.5]])
wallStart = np.array([[0,2]])
wallEnd = np.array([[4,2]])

walls = []

for i in range(wallStart.shape[0]):
    walls.append(wall.Wall(wallStart[i], wallEnd[i]))

plotCreatures(creatures, walls, 3000, 0.01)
