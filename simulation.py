import math
import simple
import creature
import NumPy as np
import time

# socialForce and objectForce are lambdas with distance as an input
def simulate(socialForce, objectForce, timestep, duration):
    # simulated field is 800x800"""
    savearray = []
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
        for c in creatures:
            for other in creatures:
                if(c != other):
                    c.update(socialForce, other, timestep)
        savearray[i] = creatures.copy()
    byteoutput = np.array(savearray).tobytes()
    with open(f'/tmp/${time.time()}') as f:
        f.write(byteoutput)
        # TODO do the actual simulation with social both functions

    return 0


