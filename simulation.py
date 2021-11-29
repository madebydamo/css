import math
import creature
import numpy as np
import time
import evacuate as scene
import wall 

# socialForce and objectForce are lambdas with distance as an input
def simulate(socialForce, objectForce, timestep, duration, dosave=False):
    # simulated field is 800x800"""
    savearray = []
    # initialization creatures
    creatures = scene.creatures()
    objects = scene.objects()
    savearray.append(list(map(wall.Wall.asarray, objects)))
    # finish initialization

    rating=0.0
    for i in range(0, round(duration / timestep)):
        creaturecopy = creatures.copy()
        a = []
        savearray.append(list(map(creature.Creature.asarray, creaturecopy)))
        for c in creatures:
            if(c.finished):
                rating+=1 + 1/i
                creatures.remove(c)
                creaturecopy.remove(c)
            c.update(socialForce, creaturecopy, objects, timestep)
        for c in creatures:
            c.updateLocation()
        for c in creatures:
            for c2 in creatures:
                if np.linalg.norm(c.location - c2.location) < 0.5:
                    rating -= 1
            for o in objects:
                if o.distance(c.location) < 0.25:
                    rating -=1
        # print(f"Frame {i} rendered")
    for c in creatures:
        rating += np.linalg.norm(c.startingLocation - c.location) / np.linalg.norm(c.startingLocation - c.finalDest)
    if(dosave):
        np.save(f'./tmp/{time.time()}.npy', np.array(savearray))
    return rating


def calculateTroughput(creatures, timePassed):
    sum = 0
    for creature in creatures:
        sum += creature.numberOfRounds
    if timePassed < 0.0000001:
        return sum
    return sum / timePassed
