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




"""
        ifloat minimum_distance(vec2 v, vec2 w, vec2 p) {
  // Return minimum distance between line segment vw and point p
  const float l2 = length_squared(v, w);  // i.e. |w-v|^2 -  avoid a sqrt
  if (l2 == 0.0) return distance(p, v);   // v == w case
  // Consider the line extending the segment, parameterized as v + t (w - v).
  // We find projection of point p onto the line. 
  // It falls where t = [(p-v) . (w-v)] / |w-v|^2
  // We clamp t from [0,1] to handle points outside the segment vw.
  const float t = max(0, min(1, dot(p - v, w - v) / l2));
  const vec2 projection = v + t * (w - v);  // Projection falls on the segment
  return distance(p, projection);
}
"""
