import random
from deap import creator, base, tools, algorithms
from models import simple as simulationcase
import simulation
import time

def evalData(params):
    def socialForce(creatureA,creatures,objects,dt):
        return simulationcase.socialForceWithParams(creatureA, creatures,objects, dt, params)
    return [simulation.simulate(socialForce, None, 1.0/30, 10, False)]

creator.create("FitnessMax", base.Fitness, weights=(1.0,))
creator.create("Individual", list, fitness=creator.FitnessMax)

toolbox = base.Toolbox()

toolbox.register("attr_param", random.uniform, 0.01, 2.)
toolbox.register("individual", tools.initRepeat, creator.Individual, toolbox.attr_param, n=simulationcase.paramnr)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)

toolbox.register("evaluate", evalData)
toolbox.register("mate", tools.cxTwoPoint)
toolbox.register("mutate", tools.mutFlipBit, indpb=0.05)
toolbox.register("select", tools.selTournament, tournsize=3)

population = toolbox.population(n=100)

NGEN=100
print("start training")
dirname = f'./tmp/evol{time.time()}'
for gen in range(NGEN):
    offspring = algorithms.varAnd(population, toolbox, cxpb=0.5, mutpb=0.1)
    fits = toolbox.map(toolbox.evaluate, offspring)
    for fit, ind in zip(fits, offspring):
        ind.fitness.values = fit
    print(f"gen {gen} trained")
    population = toolbox.select(offspring, k=len(population))
    print(tools.selBest(population, k=1))
    print(simulation.simulateWithParams(
        simulationcase.socialForceWithParams,
        None,
        1.0/30,
        10,
        tools.selBest(population, k=1)[0],
        f'{dirname}/gen{gen}.npy'))
