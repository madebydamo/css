import matplotlib.pyplot as plt
import numpy as np
import os

from models import simple

"""
    This file is used to run a simulation with default parameters and then show those in plots containing
        * positions
        * velocites over time
        * walls
    
    It can also show the different creatures each in their own file which is then saved into tmp
"""

# simulates and plots all the creatures, objects and velocities
def plotCreatures(creatures, objects, numberOfTimesteps, dt):
    fig, ax = plt.subplots(ncols=2)
    locations, velocities = collectData(creatures, objects, numberOfTimesteps, dt)

    plotObjects(ax, objects)
    plotLocations(ax, creatures, locations)
    plotVelocities(ax, creatures, velocities, numberOfTimesteps, dt)

    plt.show()

# plots a single creature and saves it into dir
def plotCreature(idx, objects, locations, velocities, numberOfTimesteps, dt, dirName):
    fig, ax = plt.subplots(ncols=2)

    plotObjects(ax, objects)
    plotLocation(ax, idx, locations)
    plotVelocity(ax, idx, velocities, numberOfTimesteps, dt)

    filename = f'{dirName}/creature{idx}.png'
    if not os.path.exists(os.path.dirname(filename)):
        os.makedirs(os.path.dirname(filename))

    plt.savefig(filename)


# does the simulation
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


# plots all the objects (walls)
def plotObjects(ax, objects):
    for object in objects:
        x = np.array([object.start[0], object.end[0]])
        y = np.array([object.start[1], object.end[1]])
        ax[0].plot(x, y, color='black', lw=5)


# plot location of a single creature (at index idx)
def plotLocation(ax, idx, locations):
    ax[0].plot(locations[..., idx, 0], locations[..., idx, 1], label='Pedestrian #{}'.format(idx))

    ax[0].legend(loc='best')
    ax[0].set_xlabel(r'x-axis $[m]$')
    ax[0].set_ylabel(r'y-axis $[m]$')


# plot all locations of all creatures
def plotLocations(ax, creatures, locations):
    numberOfCreatures = len(creatures)

    for i in range(numberOfCreatures):
        ax[0].plot(locations[..., i, 0], locations[..., i, 1], label='Pedestrian #{}'.format(i))

    ax[0].legend(loc='best')
    ax[0].set_xlabel(r'x-axis $[m]$')
    ax[0].set_ylabel(r'y-axis $[m]$')
    return


# plot velocity of a single creature (at index idx)
def plotVelocity(ax, idx, velocities, numberOfTimesteps, dt):
    t = np.linspace(0, dt * numberOfTimesteps, numberOfTimesteps)

    ax[1].plot(t, velocities[..., idx], label='Pedestrian #{}'.format(idx))

    ax[1].legend(loc='best')
    ax[1].set_xlabel(r'time $[ s ]$')
    ax[1].set_ylabel(r'velocity $[m/s]$')


# plot all velocities of all creatures
def plotVelocities(ax, creatures, velocities, numberOfTimesteps, dt):
    numberOfCreatures = len(creatures)
    t = np.linspace(0, dt * numberOfTimesteps, numberOfTimesteps)
    for i in range(numberOfCreatures):
        ax[1].plot(t, velocities[..., i], label='Pedestrian #{}'.format(i))

    ax[1].legend(loc='best')
    ax[1].set_xlabel(r'time $[ s ]$')
    ax[1].set_ylabel(r'velocity $[m/s]$')
    return
