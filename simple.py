#import simulation
import creature
import math

v0 = 2.1
sigma = 0.3


def evalData(individual):
    params = individual
    socialForce = lambda distance: params[0] * distance + params[1]
    objectForce = lambda distance: params[2] * distance + params[3]
    #return simulation.simulate(socialForce, objectForce, 1/30, 20)
    return 0

def socialForce(creatureA, creatureB, dTime):
    distanceX = (creatureA.x - creatureB.x)
    distanceY = (creatureA.y - creatureB.y)
    distanceBetween = math.sqrt(distanceX**2 + distanceY**2)
    gradX = distanceBetween / distanceX
    gradY = distanceBetween / distanceY
    veldifx = (creatureA.velX - creatureB.velX) * dTime
    veldify = (creatureA.velY - creatureB.velY) * dTime
    b = 0.5 * math.sqrt(distanceBetween + creature.norm(distanceX - veldifx, distanceY - veldify) - creature.norm(veldifx, veldify))
    v = v0 * math.exp(-b / sigma)
    return (-gradX * v, -gradY * v)

def accelerationForce(creature):
    (dirX, dirY) = creature.desiredDirection()
    desVelX = dirX * creature.desiredSpeed
    desVelY = dirY * creature.desiredSpeed
    difVelX = (desVelX - creature.velX) / creature.tau
    difVelY = (desVelY - creature.velY) / creature.tau
    return (difVelX, difVelY)
