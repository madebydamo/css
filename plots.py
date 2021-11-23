import matplotlib.pyplot as plt
import numpy as np
import simple

def plotCreatures(creatures,numberOfTimesteps,dt):
    fig,ax = plt.subplots(ncols=2)
    locations,velocities = collectData(creatures,numberOfTimesteps,dt)
    plotLocations(ax,creatures,locations,numberOfTimesteps)
    plotVelocities(ax,creatures,velocities,numberOfTimesteps,dt)
    plt.show()

def collectData(creatures,numberOfTimesteps,dt):
    numberOfCreatures = len(creatures)
    locations = np.zeros((numberOfTimesteps,numberOfCreatures,2))
    velocities = np.zeros((numberOfTimesteps,numberOfCreatures))

    for timestep in range(numberOfTimesteps):
        for i,creatureI in enumerate(creatures):
            creatureI.update(simple.socialForce, creatures, dt)
            locations[timestep,i,:] = creatureI.location
            velocities[timestep,i] = np.linalg.norm(creatureI.velocity)
            
        for _,creatureI in enumerate(creatures):
            creatureI.updateLocation()

    return locations,velocities

def plotLocations(ax,creatures,locations,numberOfTimesteps):
    numberOfCreatures = len(creatures)
    for i in range(numberOfCreatures):
        ax[0].plot(locations[...,i,0],locations[...,i,1],label='Pedestrian #{}'.format(i))

    ax[0].legend(loc='best')
    ax[0].set_xlabel(r'x-axis $[m]$')
    ax[0].set_ylabel(r'y-axis $[m]$')
    return

def plotVelocities(ax,creatures,velocities,numberOfTimesteps,dt):
    numberOfCreatures = len(creatures)
    t = np.linspace(0,dt*numberOfTimesteps,numberOfTimesteps)
    for i in range(numberOfCreatures):
        ax[1].plot(t,velocities[...,i],label='Pedestrian #{}'.format(i))

    ax[1].legend(loc='best')
    ax[1].set_xlabel(r'time $[ s ]$')
    ax[1].set_ylabel(r'velocity $[m/s]$')
    return
