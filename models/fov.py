import creature
import math
import numpy as np
from numpy.linalg import norm

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
    return (accelerationForce(creatureA)
            + agentDistanceForceWithFOV(creatureA,creatures,dt)
            + agentObjectForce(creatureA, objects,dt))

def socialForceWithParams(creatureA,creatures, objects, dt, params):
    return (accelerationForce(creatureA, tau=params[2])
            + agentDistanceForceWithFOV(creatureA,creatures,dt, A=params[0], B=params[1], phi=params[3], w=params[4])
            + agentObjectForce(creatureA, objects,dt))

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
    velocityA = creatureA.velocity
    for creatureI in creatures:
        if creatureI is not creatureA:
            forceAI = agentDistanceForceAB(creatureA, creatureI, dt, A, B)
            forceA += limitForce(creatureA, forceAI, phi, w)
    return forceA

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

