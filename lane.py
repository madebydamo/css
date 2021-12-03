import wall
import creature
import numpy as np

def objects():
    objects = []
    objects.append(wall.Wall(np.asarray([1, 1]), np.asarray([7, 1])))
    objects.append(wall.Wall(np.asarray([1, 3]), np.asarray([7, 3])))

    return objects

def creatures():
    creatures = []

    for i in range(0,5):
        location = np.random.random((2)) + np.asarray([1, 1.5])
        goal = np.random.random((2)) + np.asarray([6, 1.5])
        creatures.append(creature.Creature(location, np.asarray([goal])))

    for i in range(0,5):
        goal = np.random.random((2)) + np.asarray([1, 1.5])
        location = np.random.random((2)) + np.asarray([6, 1.5])
        creatures.append(creature.Creature(location, np.asarray([goal])))

    return creatures
