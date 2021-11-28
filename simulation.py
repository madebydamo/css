import math
import simple
import creature
import numpy as np
import time

# socialForce and objectForce are lambdas with distance as an input
def simulate(socialForce, objectForce, timestep, duration):
    # simulated field is 800x800"""
    savearray = []
    creatures = []
    # initialization creatures
    # creatures.append(creature.Creature(400, 0, 400, 800))
    # creatures.append(creature.Creature(0, 400, 800, 400))
    for x in range (15, 25, 2):
        for y in range (0, 10, 2):
            creatures.append(creature.Creature(np.array([x, y]), np.array([20, 40])))
    for y in range (15, 25, 2):
        for x in range (0, 10, 2):
            creatures.append(creature.Creature(np.array([x, y]), np.array([40, 20])))
    # finish initialization

    for i in range(0, round(duration / timestep)):
        creaturecopy = creatures.copy()
        savearray.append(list(map(creature.Creature.asarray, creaturecopy)))
        for c in creatures:
            for other in creaturecopy:
                if(c.seed != other.seed):
                    c.update(socialForce, other, timestep)
        print(f"Frame {i} rendered")
    np.save(f'./tmp/{time.time()}.npy', np.array(savearray))
    # np.array(savearray).tofile(f'/tmp/${time.time()}', "", '%s')
    return 0


def calculateTroughput(creatures, timePassed):
    sum = 0
    for creature in creatures:
        sum += creature.numberOfRounds
    if timePassed < 0.0000001:
        return sum
    return sum / timePassed