import creature
import math
import numpy as np
from numpy.linalg import norm

paramnr = 3
"""
    Implements the different forces
    Additionally there is also implementations of the forces dependent on a field of view of a creature
"""

def socialForce(creatureA,creatures, objects, dt):
    return accelerationForce(creatureA) + agentDistanceForce(creatureA,creatures,dt) + agentObjectForce(creatureA, objects,dt)

#todo
def socialForceWithParams(creatureA,creatures, dt, params):
    return accelerationForce(creatureA, tau=params[2]) + agentDistanceForce(creatureA,creatures,dt, A=params[0], B=params[1])

def agentDistanceForceAB(creatureA, creatureB, dt, A, B):
    velocity = creatureB.velocity - creatureA.velocity
    distance = creatureA.location - creatureB.location
    distanceByVelocity = velocity * dt  # yab
    b = np.sqrt(norm(distance) + norm(distance - distanceByVelocity) ** 2 - norm(distanceByVelocity) ** 2) / 2
    return A * np.exp(-b / B) * (norm(distance) + norm(distance - distanceByVelocity)) / (2 * b) * 0.5 * (
                distance / norm(distance) + (distance - distanceByVelocity) / norm(distance - distanceByVelocity))

# f_{alpha beta}, the force between two agents
def agentDistanceForce(creatureA, creatures, dt, A=2.1 ,B=0.3):
    forceA = np.zeros(2)
    velocityA = creatureA.velocity
    for creatureI in creatures:
        if creatureI is not creatureA:
            forceA += agentDistanceForceAB(creatureA, creatureI, dt, A, B)
    return forceA
    """
    va,vb = creatureA.velocity, creatureB.velocity
    distance = creatureA.location - creatureB.location
    distanceByVelocity = (vb - va)*dt
    b = np.sqrt(norm(distance) + norm(distance - (vb-va)*dt)**2 - norm((vb-va)*dt)**2)/2
    return A * np.exp(-b/B) * (norm(distance)+norm(distance-distanceByVelocity))/(2*b) * 0.5*(distance/norm(distance) + (distance-distanceByVelocity)/norm(distance-distanceByVelocity))
    """

def projectedVectorBa(vectorA, vectorB):
    Ba = (vectorA[0]*vectorB[0] + vectorA[1]*vectorB[1])/(vectorA[0]**2+vectorA[1]**2) * vectorA
    return Ba

def agentObjectForceAB(creatureA, objectI, dt, A,B):
    nearestPoint = objectI.nearestPoint(creatureA.location)
    distanceVector = creatureA.location - nearestPoint
    velocity = -creatureA.velocity
    distanceByVelocity = velocity*dt
    distance = distanceVector
#    b = np.sqrt(norm(distance) + norm(distance - distanceByVelocity) ** 2 - norm(distanceByVelocity) ** 2) / 2
    return A * np.exp(-norm(distance) / B) * (norm(distance) + norm(distance - distanceByVelocity)) / (2 * norm(distance)) * 0.5 * (
                distance / norm(distance) + (distance - distanceByVelocity) / norm(distance - distanceByVelocity))

def agentObjectForce(creatureA, objects, dt, A=10, B=0.2):
    forceA = np.zeros(2)
    for index,objectI in enumerate(objects):
        forceAI = agentObjectForceAB(creatureA,objectI,dt,A,B)
        forceA += forceAI
        #print('Wall Nr° {}, Start{},{} & End {},{} , Force = {}'.format(index,objectI.start[0],objectI.start[1], objectI.end[0], objectI.end[1], np.mean(forceAI)))
    return forceA

# def osocialForce(creatureA,creatures, dt):
#     return accelerationForce(creatureA) + oagentDistanceForce(creatureA,creatures,dt)
#
# # f_{alpha beta}, the force between two agents
# def oagentDistanceForce(creatureA, creatureB, dt, A=2.1 ,B=0.3):
#
#     va,vb = creatureA.velocity, creatureB.velocity
#     distance = creatureA.location - creatureB.location
#     distanceByVelocity = (vb - va)*dt
#     b = np.sqrt(norm(distance) + norm(distance - (vb-va)*dt)**2 - norm((vb-va)*dt)**2)/2
#     return A * np.exp(-b/B) * (norm(distance)+norm(distance-distanceByVelocity))/(2*b) * 0.5*(distance/norm(distance) + (distance-distanceByVelocity)/norm(distance-distanceByVelocity))

# acceleration to desired velocity
def accelerationForce(creature, tau=0.5, desiredVelocity=1.333):
    desiredDirection = creature.desiredDirection()
    desiredVelocity = desiredVelocity * desiredDirection
    return 1/tau * (desiredVelocity - creature.velocity)
