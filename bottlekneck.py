import wall
import creature
import numpy as np

def objects():
    objects = []
    objects.append(wall.Wall(np.asarray([5.0, 0.0]), np.asarray([5.0, 4.5])))
    objects.append(wall.Wall(np.asarray([5.0, 5.5]), np.asarray([5.0, 10])))

    return objects

def creatures():
    creatures = []

    middle1 = np.asarray([5+0.2, 5])
    middle2 = np.asarray([5-0.2, 5])

    for i in range(0, 10):
        location = np.random.random((2)) * np.asarray([4, 10])
        goal = np.random.random((2)) * np.asarray([4, 10]) + np.asarray([6, 0])
        creatures.append(creature.Creature(location, np.asarray([middle1, goal])))

    for i in range(0, 10):
        goal = np.random.random((2)) * np.asarray([4, 10])
        location = np.random.random((2)) * np.asarray([4, 10]) + np.asarray([6, 0])
        creatures.append(creature.Creature(location, np.asarray([middle2, goal])))

    return creatures
