import matplotlib.pyplot as plt
import numpy as np

from models import simple


def plotCreatures(creatures, objects, numberOfTimesteps, dt):
    fig, ax = plt.subplots(ncols=2)
    locations, velocities = collectData(creatures, objects, numberOfTimesteps, dt)
    plotLocations(ax, creatures, objects, locations)
    plotVelocities(ax, creatures, velocities, numberOfTimesteps, dt)
    plt.show()


def collectData(creatures, objects, numberOfTimesteps, dt):
    numberOfCreatures = len(creatures)
    locations = np.zeros((numberOfTimesteps, numberOfCreatures, 2))
    velocities = np.zeros((numberOfTimesteps, numberOfCreatures))

    for timestep in range(numberOfTimesteps):
        for i, creatureI in enumerate(creatures):
            creatureI.update(simple.socialForce, creatures, objects, dt)
            locations[timestep, i, :] = creatureI.location
            velocities[timestep, i] = np.linalg.norm(creatureI.velocity)

        for _, creatureI in enumerate(creatures):
            creatureI.updateLocation()

    return locations, velocities


def plotLocations(ax, creatures, objects, locations):
    numberOfCreatures = len(creatures)

    for object in objects:
        x = np.array([object.start[0], object.end[0]])
        y = np.array([object.start[1], object.end[1]])
        ax[0].plot(x, y, color='black', lw=5)

    for i in range(numberOfCreatures):
        ax[0].plot(locations[..., i, 0], locations[..., i, 1], label='Pedestrian #{}'.format(i))

    ax[0].legend(loc='best')
    ax[0].set_xlabel(r'x-axis $[m]$')
    ax[0].set_ylabel(r'y-axis $[m]$')
    return


def plotVelocities(ax, creatures, velocities, numberOfTimesteps, dt):
    numberOfCreatures = len(creatures)
    t = np.linspace(0, dt * numberOfTimesteps, numberOfTimesteps)
    for i in range(numberOfCreatures):
        ax[1].plot(t, velocities[..., i], label='Pedestrian #{}'.format(i))

    ax[1].legend(loc='best')
    ax[1].set_xlabel(r'time $[ s ]$')
    ax[1].set_ylabel(r'velocity $[m/s]$')
    return
