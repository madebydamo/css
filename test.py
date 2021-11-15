import simple
import creature
a = creature.Creature(0, 1, 5, 1)
b = creature.Creature(1, 0, 1, 5)
print(simple.socialForce(a, b, 1/30))

a = creature.Creature(0, 2, 5, 1)
b = creature.Creature(2, 0, 1, 5)
print(simple.socialForce(a, b, 1/30))

print(simple.accelerationForce(a))
