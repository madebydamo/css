import numpy as np
from numpy.linalg import norm

from models.shared import agentDistanceForceAB, agentObjectForce, accelerationForce

"""
    Implements function for calculating forces
"""
paramnr = 5

# computes all the different forces for a single creature with default parameters
def socialForce(creatureA,creatures, objects, dt):
    return (accelerationForce(creatureA)
            + agentDistanceForce(creatureA, creatures, dt)
            + agentObjectForce(creatureA, objects, dt))


# computes all the different forces for a single creature with certain parameters
def socialForceWithParams(creatureA, creatures, objects, dt, params):
    return (accelerationForce(creatureA, tau=params[2])
            + agentDistanceForce(creatureA, creatures, dt, A=params[0], B=params[1])
            + agentObjectForce(creatureA, objects, dt, C=params[3], D=params[4]))


# calculate forces between one creature and all other creatures
def agentDistanceForce(creatureA, creatures, dt, A=2.1 ,B=0.3):
    forceA = np.zeros(2)
    for creatureI in creatures:
        if creatureI is not creatureA:
            forceA += agentDistanceForceAB(creatureA, creatureI, dt, A, B)
    return forceA
