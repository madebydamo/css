import numpy as np
import matplotlib.pyplot as plt
import wall

locationPedestrian = np.array([3,2])

mauer = wall.Wall(np.array([2,2]),np.array([3,3]))

nearestPoint = mauer.nearestPoint(locationPedestrian)


plt.figure()
plt.plot(np.array([mauer.start[0],mauer.end[0]]),np.array([mauer.start[1],mauer.end[1]]))
#plt.quiver(mauer.start[0],mauer.start[1],mauer.end[0],mauer.end[1],units='xy',scale=1)
plt.scatter(nearestPoint[0],nearestPoint[1])
plt.scatter(locationPedestrian[0],locationPedestrian[1])
plt.show()
