import simple
import creature
import numpy as np
import matplotlib.pyplot as plt
from plots import plotCreatures

locations = np.random.random((20,2))*10
goals = np.random.random((20,1,2))*10
#locations = np.array([[1,1],[9,9],[1,9]])
#goals = np.array([[9,9],[1,1],[9,1]])

creatures = []

for i in range(locations.shape[0]):
    creatures.append(creature.Creature(locations[i],goals[i]))

plotCreatures(creatures,1500,0.01)
