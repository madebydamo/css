import wall
import creature
import numpy as np

def objects():
    objects = []
    objects.append(wall.Wall([0.5, 0.5], [0.5, 5.5]))
    objects.append(wall.Wall([0.5, 0.5], [5.5, 0.5]))
    objects.append(wall.Wall([5.5, 0.5], [5.5, 2.6]))
    objects.append(wall.Wall([5.5, 3.4], [5.5, 5.5]))
    objects.append(wall.Wall([0.5, 5.5], [5.5, 5.5]))
    return objects

def creatures():
    creatures = []
    creatures.append(creature.Creature(np.asarray([1.4, 1.2]), np.asarray([[5.5, 3.0], [8.0, 3.0]]), 1.333, 1))
    creatures.append(creature.Creature(np.asarray([1.1, 4.7]), np.asarray([[5.5, 3.0], [8.0, 3.0]]), 1.333, 1))
    creatures.append(creature.Creature(np.asarray([2.2, 3.7]), np.asarray([[5.5, 3.0], [8.0, 3.0]]), 1.333, 1))
    creatures.append(creature.Creature(np.asarray([3.3, 1.1]), np.asarray([[5.5, 3.0], [8.0, 3.0]]), 1.333, 1))
    creatures.append(creature.Creature(np.asarray([2.8, 4.6]), np.asarray([[5.5, 3.0], [8.0, 3.0]]), 1.333, 1))
    creatures.append(creature.Creature(np.asarray([4.2, 2.2]), np.asarray([[5.5, 3.0], [8.0, 3.0]]), 1.333, 1))
    creatures.append(creature.Creature(np.asarray([3.9, 4.2]), np.asarray([[5.5, 3.0], [8.0, 3.0]]), 1.333, 1))
    creatures.append(creature.Creature(np.asarray([4.8, 3.2]), np.asarray([[5.5, 3.0], [8.0, 3.0]]), 1.333, 1))
    creatures.append(creature.Creature(np.asarray([5.0, 4.7]), np.asarray([[5.5, 3.0], [8.0, 3.0]]), 1.333, 1))
    return creatures
