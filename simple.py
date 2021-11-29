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

# limits the influence of a force depending if its viewable
def limitForce(creatureA, force):
    w = creatureA.c
    e = creatureA.desiredDirection()
    if np.dot(e, -force) > norm(-force) * math.cos(creatureA.phi):
        w = 1
    return w * force

def socialForce(creatureA,creatures, objects, dt):
    return accelerationForce(creatureA) + agentDistanceForceWithFOV(creatureA,creatures,dt) + agentObjectForce(creatureA, objects,dt)

def agentDistanceForceAB(creatureA, creatureB, dt, A=2.1, B=0.3):
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

def agentDistanceForceWithFOV(creatureA, creatures, dt, A=2.1 ,B=0.3):
    forceA = np.zeros(2)
    velocityA = creatureA.velocity
    for creatureI in creatures:
        if creatureI is not creatureA:
            forceAI = agentDistanceForceAB(creatureA, creatureI, dt, A, B)
            forceA += limitForce(creatureA, forceAI)
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
def accelerationForce(creature):
    desiredDirection = creature.desiredDirection()
    desiredVelocity = creature.desiredVelocity * desiredDirection
    return 1/creature.tau * (desiredVelocity - creature.velocity)
