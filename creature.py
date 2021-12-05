import numpy as np
import random

"""
    Implementation of a single creature for our simulation
    The creature it self does not implement the different function for
    calculating forces which are given trough models
"""

class Creature:
    maxVelocity = 1.388888

    force = np.zeros(2)
    velocity = np.zeros(2)

    nextLocation = np.zeros(2)
    nextVelocity = np.zeros(2)

    # used if creature should repeat after reaching final destination
    finished = False
    numberOfRounds = 0 # accumulates number of repetitions

    #location: start location of creature
    #path: array of locations, creature tries to reach one after another
    def __init__(self, location, path, repeating=False):
        self.location = location
        self.startingLocation = location
        # variables for path and destination
        self.currentDest = path[0]
        self.finalDest = path[-1]
        self.path = path
        self.pathIdx = 0
        self.finished = False
        # repeats path
        self.repeating = repeating
        #dirty hack for comparing equality
        self.seed = random.randint(0, 1 << 31)

    def __eq__(self, other):
        return self.seed == other.seed

    # calculates the next position, velocity and already updates forces
    # also updates the current destination
    def update(self, socialForce, creatures, objects, dt):
        if self.finished:
            return

        self.updateForce(socialForce, creatures, objects, dt)
        self.updateVelocity(dt)
        self.calculateLocation(dt)

        self.updateDestination()

    def updateForce(self, socialForce, creatures, objects, dt):
        self.force = socialForce(self, creatures, objects, dt)

    def updateVelocity(self, dt):
        self.nextVelocity = self.velocity + self.force * dt
        if np.linalg.norm(self.nextVelocity) > self.maxVelocity:# capped at max velocity
            unitVec = normalize(self.velocity)
            self.nextVelocity = unitVec * self.maxVelocity

    def calculateLocation(self, dt):
        self.nextLocation = self.location + self.nextVelocity*dt

    # actually now updates the location and velocity. This is done so that the
    # ordering in which creatures are updated doesn't play a role. Forces are
    # not accessed outside of the creature they belong to so not necessary to have a nextForce 
    def updateLocation(self):
        self.velocity = self.nextVelocity
        self.location = self.nextLocation

    # calculates a vector pointing into the direction of our next destination (from viewpoint of creature)
    def desiredDirection(self):
        return normalize(self.currentDest-self.location)

    # Updates the destination to the next one on the path if the current destination has been reached
    def updateDestination(self):
        if np.linalg.norm(self.currentDest-self.location) < 0.5: # reached current dest
            self.pathIdx += 1
            if self.pathIdx < len(self.path):
                self.currentDest = self.path[self.pathIdx]
            else:
                # finished round
                self.numberOfRounds += 1

                self.force = np.zeros(2)
                self.velocity = np.zeros(2)
                self.nextVelocity = np.zeros(2)

                if self.repeating:# go back to start and walk the same route again
                    self.location = self.startingLocation
                    self.nextLocation = self.location
                else:
                    self.finished = True

    def __str__(self):
        return f"loc:{self.location}, force:{self.force}"

    # used for serialization
    def asArray(self):
        return [self.location[0], self.location[1], self.force[0], self.force[1]]

# normalizes a vector
def normalize(v):
    norm = np.linalg.norm(v)
    if norm == 0:
        return np.zeros(2)
    return v/norm
