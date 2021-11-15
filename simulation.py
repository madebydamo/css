import math
import simple
import creature

# socialForce and objectForce are lambdas with distance as an input
def simulate(socialForce, objectForce, timestep, duration):
    # simulated field is 800x800"""
    creatures = []
    # initialization creatures
    creatures.append(creature.Creature(400, 0, 400, 800))
    creatures.append(creature.Creature(0, 400, 800, 400))
    """for x in range (300, 500, 30):
        for y in range (0, 200, 30):
            creatures.append(Creature(x, y, 0, 1.3888))
    for y in range (300, 500, 30):
        for x in range (0, 200, 30):
            creatures.append(Creature(x, y, 1.3888, 0))
            """
    # finish initialization

    for i in range(0, duration / timestep):
        
        # TODO do the actual simulation with social both functions

    for c in creatures:
        distance += c.distance()
    return distance


