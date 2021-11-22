import math
import numpy as np
import random

# run with python3 -m pipenv run python3 ui.py

class Creature:
    maxVelocity = 1.388888
    force = np.zeros(2)
    velocity = np.zeros(2)

    #PRE: location = np.array([x,y]), goal = np.array([goalX,goalY])
    def __init__(self, location, goal, desiredVelocity = 1.333, tau = 5):
        self.location = location
        self.goal = goal
        self.desiredVelocity = desiredVelocity
        self.tau = tau
        self.seed = random.randbytes(4)

    def desiredDirection(self):
        return normalize(self.goal-self.location)

    def updateForce(self,socialForce,creatureB,dt):
        self.force = socialForce(self,creatureB,dt)

    def updateVelocity(self,dt):
        self.velocity = self.velocity + self.force * dt
        if np.linalg.norm(self.velocity) > self.maxVelocity:
            unitVec = normalize(self.velocity)
            self.velocity = unitVec * self.maxVelocity

    def updateLocation(self,dt):
        self.location = self.location + self.velocity*dt

    def update(self,socialForce,creatureB,dt):
        self.updateForce(socialForce,creatureB,dt)
        self.updateVelocity(dt)
        self.updateLocation(dt)

    def __str__(self):
        return f"loc:{self.location}, force:{self.force}"
    def asarray(self):
        return [self.location[0], self.location[1], self.force[0], self.force[1]]



def normalize(v):
    norm = np.linalg.norm(v)
    return v/norm
