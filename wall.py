import numpy as np
import math

class Wall:
    def __init__(self, start, end):
        self.start = np.array(start)
        self.end = np.array(end)

    def distance(self, location):
        length_squared = (self.start[0] - self.end[0]) ** 2 + (self.start[1] - self.end[1]) ** 2
        if(length_squared <= 0e-6):
            return math.sqrt((self.start[0] - location[0]) ** 2 + (self.start[1] - location[1]) ** 2)
        t = max(0.0, min(1.0, np.dot(location - self.start, self.end - self.start) / length_squared))
        projection = self.start + t * (self.end - self.start)
        return math.sqrt((projection[0] - location[0]) ** 2 + (projection[1] - location[1]) ** 2)

    def asarray(self):
        return [[self.start[0], self.start[1]], [self.end[0], self.end[1]]]
