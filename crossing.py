import wall
import creature
import numpy as np

def objects():
    objects = []
    objects.append(wall.Wall(np.asarray([0.0, 3.0]), np.asarray([3.0, 3.0])))
    objects.append(wall.Wall(np.asarray([5.0, 3.0]), np.asarray([8.0, 3.0])))
    objects.append(wall.Wall(np.asarray([0.0, 5.0]), np.asarray([3.0, 5.0])))
    objects.append(wall.Wall(np.asarray([5.0, 5.0]), np.asarray([8.0, 5.0])))

    objects.append(wall.Wall(np.asarray([3.0, 0.0]), np.asarray([3.0, 3.0])))
    objects.append(wall.Wall(np.asarray([3.0, 5.0]), np.asarray([3.0, 8.0])))
    objects.append(wall.Wall(np.asarray([5.0, 0.0]), np.asarray([5.0, 3.0])))
    objects.append(wall.Wall(np.asarray([5.0, 5.0]), np.asarray([5.0, 8.0])))

    objects.append(wall.Wall(np.asarray([0.0, 3.0]), np.asarray([0.0, 5.0])))
    objects.append(wall.Wall(np.asarray([3.0, 0.0]), np.asarray([5.0, 0.0])))
    objects.append(wall.Wall(np.asarray([8.0, 3.0]), np.asarray([8.0, 5.0])))
    objects.append(wall.Wall(np.asarray([3.0, 8.0]), np.asarray([5.0, 8.0])))
    return objects

def creatures():
    creatures = []
    creatures.append(creature.Creature(np.asarray([0.6, 3.6]), np.asarray([[7.7, 4.0]]), 1.333))
    creatures.append(creature.Creature(np.asarray([0.5, 4.4]), np.asarray([[7.7, 4.0]]), 1.333))
    creatures.append(creature.Creature(np.asarray([1.1, 4.0]), np.asarray([[7.7, 4.0]]), 1.333))
    creatures.append(creature.Creature(np.asarray([1.3, 3.6]), np.asarray([[7.7, 4.0]]), 1.333))
    creatures.append(creature.Creature(np.asarray([1.4, 4.4]), np.asarray([[7.7, 4.0]]), 1.333))
    creatures.append(creature.Creature(np.asarray([1.6, 4.0]), np.asarray([[7.7, 4.0]]), 1.333))

    creatures.append(creature.Creature(np.asarray([3.6, 0.5]), np.asarray([[4.0, 7.7]]), 1.333))
    creatures.append(creature.Creature(np.asarray([4.4, 0.6]), np.asarray([[4.0, 7.7]]), 1.333))
    creatures.append(creature.Creature(np.asarray([4.0, 1.0]), np.asarray([[4.0, 7.7]]), 1.333))
    creatures.append(creature.Creature(np.asarray([3.6, 1.4]), np.asarray([[4.0, 7.7]]), 1.333))
    creatures.append(creature.Creature(np.asarray([4.4, 1.3]), np.asarray([[4.0, 7.7]]), 1.333))
    creatures.append(creature.Creature(np.asarray([4.0, 1.7]), np.asarray([[4.0, 7.7]]), 1.333))
    return creatures
