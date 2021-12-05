from models import simple as simulationcase
import simulation


def socialForce(creatureA, creatures,objects, dt):
    return simulationcase.socialForceWithParams(creatureA, creatures, objects, dt, [0.        , 0.        , 1.        , 3.50992592, 0.        ])


print(simulation.simulate(socialForce, 1.0/30, 10, True))
