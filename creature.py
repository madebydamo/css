import math
import numpy as np

# run with python3 -m pipenv run python3 ui.py

class Creature:
    maxVelocity = 1.388888
    force = np.zeros(2)
    velocity = np.zeros(2)
    nextLocation = np.zeros(2)

    #PRE: location = np.array([x,y]), goal = np.array([goalX,goalY])
    def __init__(self, location, goal, desiredVelocity = 1.333, tau = 0.5):
        self.location = location
        self.goal = goal
        self.desiredVelocity = desiredVelocity
        self.tau = tau

    def desiredDirection(self):
        return normalize(self.goal-self.location)

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

    def update(self,socialForce,creatureB,dt):
        self.updateForce(socialForce,creatureB,dt)
        self.updateVelocity(dt)
        self.calculateLocation(dt)
    def __str__(self):
        return f"loc:{self.location}, force:{self.force}"


def normalize(v):
    norm = np.linalg.norm(v)
    return v/norm
