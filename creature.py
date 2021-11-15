import math

class Creature:
    maxVelocity = 1.388888
    forcX = 0
    forcY = 0
    velX = 0
    velY = 0
    def __init__(self, x, y, goalX, goalY, desiredSpeed = 1.333, tau = 5):
        self.x = x
        self.y = y
        self.goalX = goalX
        self.goalY = goalY
        self.desiredSpeed = desiredSpeed
        self.tau = tau

    def desiredDirection(self):
        return normalize(self.goalX - self.x, self.goalY - self.y)


    def update(self, socialForce, objectForce, timestep):
        self.velX = self.velX + self.forcX * timestep
        self.velY = self.velY + self.forcY * timestep
        if norm(self.velx, self.vely) > self.maxVelocity:
            (nx, ny) = normalize(self.velx, self.vely)
            self.velx = nx * self.maxVelocity
            self.vely = ny * self.maxVelocity
        self.y = self.y + self.vely * timestep
        self.x = self.x + self.velx * timestep

def normalize(x, y):
    return (x / norm(x, y), y / norm(x, y))

def norm(x, y):
    return math.sqrt(x**2 + y**2)
