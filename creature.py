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
    force = np.zeros(2)
    velocity = np.zeros(2)
    nextLocation = np.zeros(2)

    finished = False
    numberOfRounds = 0

    #PRE: location = np.array([x,y]), goal = np.array([goalX,goalY])
    def __init__(self, location, path, desiredVelocity = 1.333, tau = 0.5, repeating = False):
        self.location = location
        self.startingLocation = location

        self.currentDest = path[0]
        self.finalDest = path[-1]
        self.path = path
        self.pathIdx = 0
        self.finished = False

        self.repeating = repeating
        self.seed = random.randbytes(4)

        # params // shouldn't be needed here
        self.desiredVelocity = desiredVelocity
        self.tau = tau
    def __eq__(self, other):
        return self.seed == other.seed

    def update(self,socialForce, creatureB, objects, dt):
        if self.finished: # could also be reset after finishing path
            return

        self.updateForce(socialForce,creatureB,objects,dt)
        self.updateVelocity(dt)
        self.calculateLocation(dt)

        self.updateDestination()

    def updateForce(self,socialForce, creatureB, objects,dt):
        self.force = socialForce(self,creatureB,objects,dt)

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
                # finished round
                self.numberOfRounds += 1
                if self.repeating:
                    self.location = self.startingLocation
                    self.nextLocation = self.location

                    self.force = np.zeros(2)
                    self.velocity = np.zeros(2)
                else:
                    self.finished = True


    def __str__(self):
        return f"loc:{self.location}, force:{self.force}"

    def asarray(self):
        return [self.location[0], self.location[1], self.force[0], self.force[1]]




def normalize(v):
    norm = np.linalg.norm(v)
    return v/norm
