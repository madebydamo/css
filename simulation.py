import math

class Creature:
    def __init__(self, x, y, dx, dy):
        self.x = x
        self.y = y
        self.dx = dx #distance he wants to travel each step
        self.dy = dy
        self.ox = x
        self.oy = y

    def dinstance(self):
        return math.sqrt(abs(self.x - self.ox)**2 + abs(self.y - self.oy)**2)

# socialForce and objectForce are lambdas with distance as an input
def simulate(socialForce, objectForce):
    """simulated field is 800x800"""
    creatures = []
    for x in range (300, 500, 30):
        for y in range (0, 200, 30):
            creatures.append(Creature(x, y, 0, 1.3888))
    for y in range (300, 500, 30):
        for x in range (0, 200, 30):
            creatures.append(Creature(x, y, 1.3888, 0))
    # for i in range(0, 600):
        # TODO do the actual simulation with social both functions
    distance = 0.0
    for c in creatures:
        distance += c.distance()
    return distance
