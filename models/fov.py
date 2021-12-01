import math
import numpy as np
from numpy.linalg import norm

import simple

"""
    Implements the different forces
    Additionally there is also implementations of the forces dependent on a field of view of a creature
"""

# limits the influence of a force depending if its viewable
def limitForce(creatureA, force, phi, w):
    e = creatureA.desiredDirection()
    if np.dot(e, -force) > norm(-force) * math.cos(phi):
        w = 1
    return w * force


def socialForce(creatureA,creatures, objects, dt):
    return (simple.accelerationForce(creatureA)
            + agentDistanceForceWithFOV(creatureA,creatures,dt)
            + simple.agentObjectForce(creatureA, objects,dt))


def socialForceWithParams(creatureA,creatures, objects, dt, params):
    return (simple.accelerationForce(creatureA, tau=params[2])
            + agentDistanceForceWithFOV(creatureA,creatures,dt, A=params[0], B=params[1], phi=params[3], w=params[4])
            + simple.agentObjectForce(creatureA, objects,dt))


def agentDistanceForceAB(creatureA, creatureB, dt, A, B):
    velocity = creatureB.velocity - creatureA.velocity
    distance = creatureA.location - creatureB.location
    distanceByVelocity = velocity * dt  # yab
    b = np.sqrt(norm(distance) + norm(distance - distanceByVelocity) ** 2 - norm(distanceByVelocity) ** 2) / 2
    return A * np.exp(-b / B) * (norm(distance) + norm(distance - distanceByVelocity)) / (2 * b) * 0.5 * (
                distance / norm(distance) + (distance - distanceByVelocity) / norm(distance - distanceByVelocity))


# f_{alpha beta}, the force between two agents
def agentDistanceForceWithFOV(creatureA, creatures, dt, A=2.1 ,B=0.3, phi=math.pi/2, w=0.1):
    forceA = np.zeros(2)
    for creatureI in creatures:
        if creatureI is not creatureA:
            forceAI = agentDistanceForceAB(creatureA, creatureI, dt, A, B)
            forceA += limitForce(creatureA, forceAI, phi, w)
    return forceA
