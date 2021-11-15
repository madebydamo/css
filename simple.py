import simulation

def evalData(individual):
    params = individual
    socialForce = lambda distance: params[0] * distance + params[1]
    objectForce = lambda distance: params[2] * distance + params[3]
    return simulation.simulate(socialForce, objectForce)

