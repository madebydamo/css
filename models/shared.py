import numpy as np
from numpy.linalg import norm

"""
    Implements the different forces
    Additionally there is also implementations of the forces dependent on a field of view of a creature
"""
def agentDistanceForceAB(creatureA, creatureB, dt, A, B):
    velocity = creatureB.velocity - creatureA.velocity
    distance = creatureA.location - creatureB.location
    distanceByVelocity = velocity * dt  # yab
    b = np.sqrt(norm(distance) + norm(distance - distanceByVelocity) ** 2 - norm(distanceByVelocity) ** 2) / 2
    if B == 0:
        return np.zeros(2)
    return A * np.exp(-b / B) * (norm(distance) + norm(distance - distanceByVelocity)) / (2 * b) * 0.5 * (
                distance / norm(distance) + (distance - distanceByVelocity) / norm(distance - distanceByVelocity))

def agentObjectForceAB(creatureA, objectI, dt, A, B):
    nearestPoint = objectI.nearestPoint(creatureA.location)
    distanceVector = creatureA.location - nearestPoint
    velocity = -creatureA.velocity
    distanceByVelocity = velocity*dt

    if B == 0:
        return np.zeros(2)

    """if B == 0 or norm(distanceVector) == 0 or norm(distanceVector - distanceByVelocity) == 0:
        print("B: "+str(B))
        print("norm(distVec)"+str(norm(distanceVector)))
        print("norm(distVec-distByVel)"+str(norm(distanceVector - distanceByVelocity)))"""

    return A * np.exp(-norm(distanceVector) / B) * (norm(distanceVector) + norm(distanceVector - distanceByVelocity)) / (2 * norm(distanceVector)) * 0.5 * (
            distanceVector / norm(distanceVector) + (distanceVector - distanceByVelocity) / norm(distanceVector - distanceByVelocity))


def agentObjectForce(creatureA, objects, dt, A=10, B=0.2):
    forceA = np.zeros(2)
    for objectI in objects:
        forceA += agentObjectForceAB(creatureA,objectI,dt,A,B)
    return forceA


# acceleration to desired velocity
def accelerationForce(creature, tau=0.5, desiredVelocity=1.333):
    if tau <= 0:
        tau = 0.01
    desiredDirection = creature.desiredDirection()
    desiredVelocity = desiredVelocity * desiredDirection
    return 1/tau * (desiredVelocity - creature.velocity)
