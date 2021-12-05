from models import simple as simulationcase
import simulation


def socialForce(creatureA, creatures,objects, dt):
    return simulationcase.socialForceWithParams(creatureA, creatures, objects, dt, [9.469819000928979, 8.944300800008584, 5.236841352031811, 1, 1])


simulation.simulate(socialForce, 1.0/30, 10, True)
