import numpy as np
from numpy.linalg import norm
from models.shared import agentDistanceForceAB, agentObjectForce, accelerationForce

"""
    Implements the different forces
    Additionally there is also implementations of the forces dependent on a field of view of a creature
"""
paramnr = 5

def socialForce(creatureA,creatures, objects, dt):
    return (accelerationForce(creatureA)
            + agentDistanceForce(creatureA, creatures, dt)
            + agentObjectForce(creatureA, objects, dt))


def socialForceWithParams(creatureA, creatures, objects, dt, params):
    return (accelerationForce(creatureA, tau=params[2])
            + agentDistanceForce(creatureA, creatures, dt, A=params[0], B=params[1])
            + agentObjectForce(creatureA, objects, dt, A=params[3], B=params[4]))


# f_{alpha beta}, the force between two agents
def agentDistanceForce(creatureA, creatures, dt, A=2.1 ,B=0.3):
    forceA = np.zeros(2)
    for creatureI in creatures:
        if creatureI is not creatureA:
            forceA += agentDistanceForceAB(creatureA, creatureI, dt, A, B)
    return forceA
