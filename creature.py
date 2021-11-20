import math
import numpy as np


class Creature:
    maxVelocity = 1.388888
    force = np.array([0,0])
    velocity = np.array([1,1])

    #PRE: location = np.array([x,y]), goal = np.array([goalX,goalY])
    def __init__(self, location, goal, desiredVelocity = 1.333, tau = 5):
        self.location = location
        self.goal = goal
        self.desiredVelocity = desiredVelocity
        self.tau = tau

    def desiredDirection(self):
        return normalize(self.goal-self.location)


    def update(self, timestep):
        self.velocity = self.velocity + self.force * timestep
        if np.linalg.norm(self.velocity) > self.maxVelocity:
            unitVec = normalize(self.velocity)
            self.velocity = unitVec * self.maxVelocity
        self.location = self.location + self.velocity * timestep

def normalize(v):
    norm = np.linalg.norm(v)
    return v/norm
