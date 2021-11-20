import simple
import creature
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

#locations = np.array([[5,5],[5.5,5.5]])  #agentDistanceForce > accelerationForce
locations = np.array([[3.8,3.8],[6.2,6.2]])
#locations = np.array([[1,9],[9,1]])
goals = np.array([[9,9],[1,1]])

a = creature.Creature(locations[0],goals[0])
b = creature.Creature(locations[1],goals[1])


print(simple.accelerationForce(a))

def quiver(a,b,color):
    fa = simple.socialForce(a, b, 1/30)
    fab = simple.agentDistanceForce(a,b,1/30)
    acc = simple.accelerationForce(a)
    
    ax[1].quiver(a.location[0],a.location[1],fab[0],fab[1],color='darkviolet',alpha=0.5,label=(r'$f_{\alpha \beta} = $' +str(round(np.linalg.norm(fab),3))),scale=10)
    ax[1].quiver(a.location[0],a.location[1],acc[0],acc[1],color='orange',alpha=0.5,label=r'$a_\alpha = $' +str(round(np.linalg.norm(acc),3)),scale=10)
    ax[1].legend(loc='best')
    ax[0].quiver(a.location[0],a.location[1],fa[0],fa[1],color=color,alpha=0.5,scale=10)
    ax[0].plot(a.location[0],a.location[1],marker='.',color=color)
    ax[0].plot(a.goal[0],a.goal[1],color=color,marker='X')
    return

fig, ax = plt.subplots(ncols=2,sharex=True, sharey=True)
quiver(a,b,'blue')
quiver(b,a,'red')
plt.show()