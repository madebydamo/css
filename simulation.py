import numpy as np
import time
import os

import creature
import wall
import evacuate as scene


# socialForce and objectForce are lambdas with distance as an input
def simulate(socialForce, objectForce, timestep, duration, dosave=False, filename=f'./tmp/{time.time()}.npy'):
    # simulated field is 800x800"""
    savearray = []
    # initialization creatures
    creatures = scene.creatures()
    objects = scene.objects()
    savearray.append(list(map(wall.Wall.asArray, objects)))
    # finish initialization

    rating=0.0
    for i in range(0, round(duration / timestep)):
        creatureCopy = creatures.copy()
        a = []
        savearray.append(list(map(creature.Creature.asArray, creatureCopy)))
        for c in creatures:
            if c.finished:
                rating+=1 + 1/i
                creatures.remove(c)
                creatureCopy.remove(c)
            c.update(socialForce, creatureCopy, objects, timestep)

        for c in creatures:
            c.updateLocation()

        # Collision detection and punishment assuming creatures have r=0.25
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
        if not os.path.exists(os.path.dirname(filename)):
            os.makedirs(os.path.dirname(filename))
        np.warnings.filterwarnings('ignore', category=np.VisibleDeprecationWarning)                 
        np.save(filename, np.array(savearray))

    return rating


def simulateWithParams(socialForceWithParams, objectForce, timestep, duration, params, filename):
    def socialForce(creatureA, creatures, objects, dt):
        return socialForceWithParams(creatureA, creatures, objects, dt, params)
    return simulate(socialForce, objectForce, timestep, duration, True, filename)


def calculateTroughput(creatures, timePassed):
    sum = 0
    for creature in creatures:
        sum += creature.numberOfRounds
    if timePassed < 0.0000001:
        return sum
    return sum / timePassed
