import math
import numpy as np
from numpy.linalg import norm

from models.shared import agentDistanceForceAB, agentObjectForce, accelerationForce

"""
    Implements function for calculating forces depending on field of view
"""
paramnr = 7

# limits the influence of a force depending if its viewable
def limitForce(creatureA, force, phi, w):
    e = creatureA.desiredDirection()
    if np.dot(e, -force) > norm(-force) * math.cos(phi):
        w = 1
    return w * force


# computes all the different forces for a single creature with default parameters
def socialForce(creatureA,creatures, objects, dt):
    return (accelerationForce(creatureA)
            + agentDistanceForceWithFOV(creatureA,creatures,dt)
            + agentObjectForce(creatureA, objects,dt))


# computes all the different forces for a single creature with certain parameters
def socialForceWithParams(creatureA,creatures, objects, dt, params):
    return (accelerationForce(creatureA, tau=params[2])
            + agentDistanceForceWithFOV(creatureA,creatures,dt, A=params[0], B=params[1], phi=params[5], w=params[6])
            + agentObjectForce(creatureA, objects, dt, C=params[3], D=params[4]))


# calculate forces between one creature and all other creatures (depending on field of view)
def agentDistanceForceWithFOV(creatureA, creatures, dt, A=2.1 ,B=0.3, phi=math.pi/2, w=0.1):
    forceA = np.zeros(2)
    for creatureI in creatures:
        if creatureI is not creatureA:
            forceAI = agentDistanceForceAB(creatureA, creatureI, dt, A, B)
            forceA += limitForce(creatureA, forceAI, phi, w)
    return forceA
