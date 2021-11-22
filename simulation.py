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
    for x in range (300, 500, 30):
        for y in range (0, 200, 30):
            creatures.append(creature.Creature(np.array([x, y]), np.array([400, 800])))
    for y in range (300, 500, 30):
        for x in range (0, 200, 30):
            creatures.append(creature.Creature(np.array([x, y]), np.array([800, 400])))
    # finish initialization

    for i in range(0, round(duration / timestep)):
        for c in creatures:
            for other in creatures:
                if(c != other):
                    c.update(socialForce, other, timestep)
        savearray.append(creatures.copy())
        print(f"Frame {i} rendered")
    np.save(f'/tmp/${time.time()}', np.array(savearray))
    # np.array(savearray).tofile(f'/tmp/${time.time()}', "", '%s')
    return 0


