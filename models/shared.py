import numpy as np
from numpy.linalg import norm

"""
    Implements function for forces used by both the simple and fov model
"""

# repulsive force between two creatures (creatureA and creatureB)
def agentDistanceForceAB(creatureA, creatureB, dt, A, B):
    velocity = creatureB.velocity - creatureA.velocity
    distance = creatureA.location - creatureB.location
    distanceByVelocity = velocity * dt  # yab
    b = np.sqrt(norm(distance) + norm(distance - distanceByVelocity) ** 2 - norm(distanceByVelocity) ** 2) / 2
    if B == 0:
        return np.zeros(2)
    return A * np.exp(-b / B) * (norm(distance) + norm(distance - distanceByVelocity)) / (2 * b) * 0.5 * (
                distance / norm(distance) + (distance - distanceByVelocity) / norm(distance - distanceByVelocity))

# repulsive force between one creature (creatureA) and one object/wall (objectI)
def agentObjectForceAB(creatureA, objectI, dt, C, D):
    nearestPoint = objectI.nearestPoint(creatureA.location)
    distanceVector = creatureA.location - nearestPoint
    velocity = -creatureA.velocity
    distanceByVelocity = velocity*dt

    if D == 0:
        return np.zeros(2)

    """if B == 0 or norm(distanceVector) == 0 or norm(distanceVector - distanceByVelocity) == 0:
        print("B: "+str(B))
        print("norm(distVec)"+str(norm(distanceVector)))
        print("norm(distVec-distByVel)"+str(norm(distanceVector - distanceByVelocity)))"""

    return C * np.exp(-norm(distanceVector) / D) * (norm(distanceVector) + norm(distanceVector - distanceByVelocity)) / (2 * norm(distanceVector)) * 0.5 * (
            distanceVector / norm(distanceVector) + (distanceVector - distanceByVelocity) / norm(distanceVector - distanceByVelocity))


# calculate forces between one creature and all objects
def agentObjectForce(creatureA, objects, dt, C=10, D=0.2):
    forceA = np.zeros(2)
    for objectI in objects:
        forceA += agentObjectForceAB(creatureA, objectI, dt, C, D)
    return forceA


# acceleration to desired velocity
def accelerationForce(creature, tau=0.5, desiredVelocity=1.333):
    if tau <= 0:
        tau = 0.01
    desiredDirection = creature.desiredDirection()
    desiredVelocity = desiredVelocity * desiredDirection
    return 1/tau * (desiredVelocity - creature.velocity)
