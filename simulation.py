import numpy as np
import time
import os

import creature
from scene import wall
from scene import evacuate as scene #selected scene. Can be {evacuate, crossing, lane, bottlekneck}


# socialForce and objectForce are lambdas with distance as an input
def simulate(socialForce, objectForce, timestep, duration, dosave=False, filename=f'./tmp/{time.time()}.npy'):
    savearray = []
    # initialization creatures
    creatures = scene.creatures()
    objects = scene.objects()
    savearray.append(list(map(wall.Wall.asArray, objects)))
    # finish initialization

    destinationRating=0.0
    collisionRating=0.0
    for i in range(0, round(duration / timestep)):
        creatureCopy = creatures.copy()
        a = []
        savearray.append(list(map(creature.Creature.asArray, creatureCopy)))
        for c in creatures:
            if c.finished:
                destinationRating+=1 + 1/i
                creatures.remove(c)
                creatureCopy.remove(c)
            c.update(socialForce, creatureCopy, objects, timestep)

        for c in creatures:
            c.updateLocation()

        # Collision detection and punishment assuming creatures have r=0.25
        for c in creatures:
            for c2 in creatures:
                if np.linalg.norm(c.location - c2.location) < 0.5:
                    collisionRating += 1
            for o in objects:
                if o.distance(c.location) < 0.25:
                    collisionRating +=1
    # calculate distance it already walked and add fitness accordingly
    for c in creatures:
        destinationRating += 1 - np.linalg.norm(c.finalDest - c.location) / np.linalg.norm(c.startingLocation - c.finalDest)

    # saves simulation as file to rewatch it visually
    if dosave:
        if not os.path.exists(os.path.dirname(filename)):
            os.makedirs(os.path.dirname(filename))
        np.warnings.filterwarnings('ignore', category=np.VisibleDeprecationWarning)                 
        np.save(filename, np.array(savearray))

    return [destinationRating, collisionRating]


# runs a simulation with the desired params set for the creature
def simulateWithParams(socialForceWithParams, objectForce, timestep, duration, params, filename):
    def socialForce(creatureA, creatures, objects, dt):
        return socialForceWithParams(creatureA, creatures, objects, dt, params)
    return simulate(socialForce, objectForce, timestep, duration, True, filename)
