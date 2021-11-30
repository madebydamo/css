import numpy as np
import math

class Wall:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.vector = self.end - self.start

    def projectedVector(self,b):
        a = self.vector
        ba = (a[0]*b[0] + a[1]*b[1])/(a[0]**2+a[1]**2) * a
        return ba

    def projectedPoint(self, vector):
        proPoint = self.projectedVector(vector)+self.start
        print('Projected Point: ',proPoint)
        return proPoint

    def nearestPoint(self,creatureLocation):
        creatureVector = creatureLocation - self.start
        projectedPoint = self.projectedPoint(creatureVector)

        # collision checks
        xCheck = projectedPoint[0] < min(self.start[0], self.end[0]) or projectedPoint[0] > max(self.start[0], self.end[0])
        yCheck = projectedPoint[1] < min(self.start[1], self.end[1]) or projectedPoint[1] > max(self.start[1], self.end[1])
        if xCheck or yCheck:
            startDistance = creatureLocation - self.start
            endDistance = creatureLocation - self.end

            if (np.linalg.norm(startDistance) < np.linalg.norm(endDistance)):
                return self.start
            else:
                return self.end
        else:
            return projectedPoint

    def distance(self, location):
        length_squared = (self.start[0] - self.end[0]) ** 2 + (self.start[1] - self.end[1]) ** 2
        if(length_squared <= 0e-6):
            return math.sqrt((self.start[0] - location[0]) ** 2 + (self.start[1] - location[1]) ** 2)
        t = max(0.0, min(1.0, np.dot(location - self.start, self.end - self.start) / length_squared))
        projection = self.start + t * (self.end - self.start)
        return math.sqrt((projection[0] - location[0]) ** 2 + (projection[1] - location[1]) ** 2)

    def asarray(self):
        return [[self.start[0], self.start[1]], [self.end[0], self.end[1]]]
