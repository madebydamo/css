import math
import simple
import creature
import numpy as np
import time
import crossing as scene
import wall 

# socialForce and objectForce are lambdas with distance as an input
def simulate(socialForce, objectForce, timestep, duration):
    # simulated field is 800x800"""
    savearray = []
    # initialization creatures
    creatures = scene.creatures()
    objects = scene.objects()
    savearray.append(list(map(wall.Wall.asarray, objects)))
    # finish initialization

    for i in range(0, round(duration / timestep)):
        creaturecopy = creatures.copy()
        a = []
        savearray.append(list(map(creature.Creature.asarray, creaturecopy)))
        for c in creatures:
            if(c.finished):
                creatures.remove(c)
                creaturecopy.remove(c)
            c.update(socialForce, creaturecopy, timestep)
        for c in creatures:
            c.updateLocation()
        print(f"Frame {i} rendered")
    np.save(f'./tmp/{time.time()}.npy', np.array(savearray))
    # np.array(savearray).tofile(f'/tmp/${time.time()}', "", '%s')
    return 0


