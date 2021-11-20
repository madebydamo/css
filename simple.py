#import simulation
import creature
import math
import numpy as np
from numpy.linalg import norm


def evalData(individual):
    params = individual
    socialForce = lambda distance: params[0] * distance + params[1]
    objectForce = lambda distance: params[2] * distance + params[3]
    #return simulation.simulate(socialForce, objectForce, 1/30, 20)
    return 0

def socialForce(creatureA,creatureB, dt):
    return accelerationForce(creatureA) + agentDistanceForce(creatureA,creatureB,dt)    

# f_{alpha beta}, the force between two agents
def agentDistanceForce(creatureA, creatureB, dt, A=1 ,B=1): 
    va,vb = creatureA.velocity, creatureB.velocity
    distance = creatureA.location - creatureB.location
    distanceByVelocity = (vb - va)*dt 
    b = np.sqrt(norm(distance) + norm(distance - (vb-va)*dt)**2 - norm((vb-va)*dt)**2)/2
    return A * np.exp(-b/B) * (norm(distance)+norm(distance-distanceByVelocity))/(2*b) * 0.5*(distance/norm(distance) + (distance-distanceByVelocity)/norm(distance-distanceByVelocity))

# acceleration to desired velocity
def accelerationForce(creature):
    desiredDirection = creature.desiredDirection()
    desiredVelocity = creature.desiredVelocity * desiredDirection
    return 1/creature.tau * (desiredVelocity - creature.velocity)