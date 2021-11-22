from raylib import *
import numpy as np

import creature

class UI:
    def __init__(self, windowWidth, windowHeight, worldWidth, worldHeight):
        InitWindow(windowWidth, windowHeight, b"Social Forces Model")
        SetTargetFPS(60)

        self.windowWidth = windowWidth
        self.windowHeight = windowHeight

        self.worldWidth = worldWidth
        self.worldHeight = worldHeight

    def worldToWindow(self, x, y): # inverted coordinate y space
        print(f"x: {x}, y: {y}")
        return int(x * self.windowWidth / self.worldWidth), int(self.windowHeight - y * self.windowHeight / self.worldHeight)

    def windowToWorld(self, x, y):
        return float(x * self.worldWidth / self.windowWidth), float((self.windowHeight - y) * self.worldHeight / self.windowHeight)

    # use WindowShouldClose() to decide how long to run
    def drawWindow(self, creatures):
        BeginDrawing()
        ClearBackground(RAYWHITE)

        for creature in creatures:
            print(creature)
            if np.isnan(creature.location[0]) or np.isnan(creature.location[1]):
                continue
            (posX, posY) = self.worldToWindow(creature.location[0], creature.location[1])
            DrawCircle(posX, posY, 5, BLACK) # position

            normalizedVel = (creature.velocity / creature.maxVelocity) * 1.25
            (lineX, lineY) = self.worldToWindow(creature.location[0] + normalizedVel[0],
                                                creature.location[1] + normalizedVel[1])
            DrawLine(posX, posY, lineX, lineY, BLACK)

        # output current mouse position
        (mouseX, mouseY) = self.windowToWorld(GetMouseX(), GetMouseY())

        DrawText(bytes(str(mouseX)+","+str(mouseY), 'utf-8'), 10, 10, 12, GRAY)

        EndDrawing()

    def closeWindow(self):
        CloseWindow()


def showSimulation(filepath):
    import numpy
    creatures = numpy.load(filepath, allow_pickle=True)
    ui = UI(800, 800, 1000, 1000)

    i = 0
    # print(creatures)
    # print("devider----------------------")
    # print(creatures[i])
    while not WindowShouldClose():
        ui.drawWindow(creatures[i])

        i += 1
        # print("A: " + str(np.linalg.norm(a.goal-a.location)))
        # print("B: " + str(np.linalg.norm(b.goal - b.location)))
    ui.closeWindow()

def testUI():
    locations = np.array([[5, 5.1], [6, 6]])
    goals = np.array([[9, 9], [1, 1]])

    a = creature.Creature(locations[0],goals[0])
    b = creature.Creature(locations[1],goals[1])
    creatures = [a, b]

    ui = UI(800, 500, 20, 10)

    while not WindowShouldClose():
        ui.drawWindow(creatures)

        dt = GetFrameTime()

        a.update(simple.socialForce, b, 0.2)
        b.update(simple.socialForce, a, 0.2)

        print("A: " + str(np.linalg.norm(a.goal-a.location)))
        print("B: " + str(np.linalg.norm(b.goal - b.location)))

    ui.closeWindow()

if __name__ == "__main__":
    import simple
    import sys
    if(len(sys.argv) == 2):
        showSimulation(sys.argv[1])
    else:
        testUI()
