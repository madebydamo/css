from raylib import *
import numpy as np

import creature
import wall

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
    def drawWindowFromArray(self, creatureArray):
        BeginDrawing()
        ClearBackground(RAYWHITE)
        for creature in creatureArray:
            print(creature)
            (posX, posY) = self.worldToWindow(creature[0], creature[1])
            DrawCircle(posX, posY, 5, BLACK) # position

            # normalizedVel = (creature.velocity / creature.maxVelocity) * 1.25
            # (lineX, lineY) = self.worldToWindow(creature[0] + normalizedVel[0],
            #                                     creature[1] + normalizedVel[1])
            # DrawLine(posX, posY, lineX, lineY, BLACK)

        # output current mouse position
        (mouseX, mouseY) = self.windowToWorld(GetMouseX(), GetMouseY())

        DrawText(bytes(str(mouseX)+","+str(mouseY), 'utf-8'), 10, 10, 12, GRAY)

        EndDrawing()

    def drawWindow(self, creatures, walls = []):
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
            DrawLine(posX, posY, lineX, lineY, GRAY)

        for wall in walls:
            (startX, startY) = self.worldToWindow(wall.start[0], wall.start[1])
            (endX, endY) = self.worldToWindow(wall.end[0], wall.end[1])

            DrawLine(startX, startY, endX, endY, BLACK)

        # output current mouse position
        (mouseX, mouseY) = self.windowToWorld(GetMouseX(), GetMouseY())

        DrawText(bytes(str(mouseX)+","+str(mouseY), 'utf-8'), 10, 10, 12, GRAY)

        EndDrawing()

    def closeWindow(self):
        CloseWindow()


def showSimulation(filepath):
    creatures = np.load(filepath)
    ui = UI(800, 800, 40, 40)

    i = 0
    # print(creatures)
    # print("devider----------------------")
    # print(creatures[i])
    while not WindowShouldClose():
        ui.drawWindowFromArray(creatures[i])

        i += 1
        # print("A: " + str(np.linalg.norm(a.goal-a.location)))
        # print("B: " + str(np.linalg.norm(b.goal - b.location)))
    ui.closeWindow()

def testUI():
    #locations = np.array([[1,1],[1,1.1],[3,1]])
    #goals = np.array([[1,9],[1,9.1],[3,9]])
    locations = np.array([[2.2,1],[2,9]])
    goals = np.array([[[2.2,11],[3,11]],[[2,1],[2,9],[2,1]]])
    wall_positions = np.array([[2.5,0.5],[2.5,10]])

    """a = creature.Creature(locations[0],goals[0])
    b = creature.Creature(locations[1],goals[1])
    creatures = [a, b]"""

    creatures = []
    for i in range(locations.ndim):
        creatures.append(creature.Creature(locations[i],goals[i]))

    walls = []
    for i in range(0, wall_positions.ndim, 2):
        walls.append(wall.Wall(wall_positions[i], wall_positions[i+1]))

    ui = UI(800, 500, 15, 15)

    while not WindowShouldClose():
        ui.drawWindow(creatures, walls)

        dt = 0.01 # GetFrameTime()

        for j,robot in enumerate(creatures):
            robot.update(simple.socialForce, creatures, dt)

        for robot in creatures:
            robot.updateLocation()

        #print("A: " + str(np.linalg.norm(a.goal-a.location)))
        #print("B: " + str(np.linalg.norm(b.goal - b.location)))

    ui.closeWindow()

if __name__ == "__main__":
    import simple
    import sys
    if(len(sys.argv) == 2):
        showSimulation(sys.argv[1])
    else:
        testUI()
