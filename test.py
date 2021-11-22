import simple
import creature
import numpy as np
import matplotlib.pyplot as plt

#locations = np.array([[6,6],[5,5]])  #agentDistanceForce > accelerationForce
#locations = np.array([[3.8,5.0],[6.2,5.0]])
#locations = np.array([[1,9],[9,1]])
locations = np.array([[1,1],[9,9],[1,9]])
goals = np.array([[9,9],[1,1],[9,1]])

# creatureA = creature.Creature(locations[0],goals[0])
# creatureB = creature.Creature(locations[1],goals[1])

creatures = []
for i in range(3):
    creatures.append(creature.Creature(locations[i],goals[i]))


def quiver(a,b,color):
    fa = simple.socialForce(a, b, 0.2)
    fab = simple.agentDistanceForce(a,b,0.2)
    acc = simple.accelerationForce(a)

    ax[1].quiver(a.location[0],a.location[1],fab[0],fab[1],color='darkviolet',alpha=0.5,label=(r'$f_{\alpha \beta} = $' +str(round(np.linalg.norm(fab),3))),scale=1)
    ax[1].quiver(a.location[0],a.location[1],acc[0],acc[1],color='orange',alpha=0.5,label=r'$a_\alpha = $' +str(round(np.linalg.norm(acc),3)),scale=1)
    ax[1].legend(loc='best')
    ax[0].quiver(a.location[0],a.location[1],fa[0],fa[1],color=color,alpha=0.5,scale=1)
    ax[0].plot(a.location[0],a.location[1],marker='.',color=color)
    ax[0].plot(a.goal[0],a.goal[1],color=color,marker='X')
    return

def plotVectors(a,b):
    fig, ax = plt.subplots(ncols=2,sharex=True, sharey=True)
    quiver(a,b,'blue')
    quiver(b,a,'red')
    plt.show()

def plotTrajectories(creatures,dt=0.01,n=20):
    locations = np.zeros((len(creatures),n,2))
    olocations = np.zeros((2,n,2))

    for i in range(n):
        for j,creature in enumerate(creatures):
            creature.update(simple.socialForce, creatures, dt)
            locations[j,i] = creature.location

        for creature in creatures:
            creature.updateLocation()

        # creatureA.update(simple.osocialForce, creatureB, dt)
        # creatureB.update(simple.osocialForce, creatureA, dt)
        #
        # olocations[0,i] = creatureA.nextLocation
        # olocations[1,i] = creatureB.nextLocation
        #
        # creatureA.updateLocation()
        # creatureB.updateLocation()



    plt.figure()
    for i in range(len(creatures)):
        plt.plot(locations[i,:,0],locations[i,:,1],label='Pedestrian #{}'.format(i))
    # plt.plot(olocations[0,:,0],olocations[0,:,1],'r:',label='A')
    # plt.plot(olocations[1,:,0],olocations[1,:,1],'b:',label='B')
    plt.legend()
    plt.show()

plotTrajectories(creatures,n=1000)
