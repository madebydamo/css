import math
import numpy as np
import random

# run with python3 -m pipenv run python3 ui.py

"""
    Implementation of a single creature
    
    Differentiate between variables which are manipulated in the simulation (position, velocity, forces, ...)
    and parameters which are to be decided upon by a genetic algorithm which minimizes a certain function and
    values which are the same for every creature in all simulations (maxVelocity)
"""

class Creature:
    maxVelocity = 1.388888
    c = 0.1 # weaker influence for objects outside of view
    phi = math.pi/2 # effictive angle of sight: 2 phi
    force = np.zeros(2)
    velocity = np.zeros(2)
    nextLocation = np.zeros(2)

    finished = False

    #PRE: location = np.array([x,y]), goal = np.array([goalX,goalY])
    def __init__(self, location, path, desiredVelocity = 1.333, tau = 0.5):
        self.location = location

        self.currentDest = path[0]
        self.path = path
        self.pathIdx = 0
        self.finished = False

        self.desiredVelocity = desiredVelocity
        self.tau = tau
        self.seed = random.randbytes(4)
    def __eq__(self, other):
        return self.seed == other.seed

    def update(self,socialForce,creatureB,dt):
        if self.finished: # could also be reset after finishing path
            return

        self.updateForce(socialForce,creatureB,dt)
        self.updateVelocity(dt)
        self.calculateLocation(dt)

        self.updateDestination()

    def updateForce(self,socialForce,creatureB,dt):
        self.force = socialForce(self,creatureB,dt)

    def updateVelocity(self,dt):
        self.velocity = self.velocity + self.force * dt
        if np.linalg.norm(self.velocity) > self.maxVelocity:
            unitVec = normalize(self.velocity)
            self.velocity = unitVec * self.maxVelocity

    def calculateLocation(self,dt):
        self.nextLocation = self.location + self.velocity*dt

    def updateLocation(self):
        self.location = self.nextLocation

    def desiredDirection(self):
        return normalize(self.currentDest-self.location)

    def updateDestination(self):
        if np.linalg.norm(self.currentDest-self.location) < 0.5: # reached current dest
            self.pathIdx += 1
            if self.pathIdx < len(self.path):
                self.currentDest = self.path[self.pathIdx]
            else:
                self.finished = True

    def __str__(self):
        return f"loc:{self.location}, force:{self.force}"

    def asarray(self):
        return [self.location[0], self.location[1], self.force[0], self.force[1]]




def normalize(v):
    norm = np.linalg.norm(v)
    return v/norm
