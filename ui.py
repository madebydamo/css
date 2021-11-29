from raylib import *
import numpy as np

import creature
import wall
import simulation

"""
    Class used to show a simulation on a window:
        - additional functions to convert between window and world space
"""

class UI:
    def __init__(self, windowWidth, windowHeight, worldWidth, worldHeight):
        InitWindow(windowWidth, windowHeight, b"Social Forces Model")
        SetTargetFPS(60)

        self.windowWidth = windowWidth
        self.windowHeight = windowHeight

        self.worldWidth = worldWidth
        self.worldHeight = worldHeight
        self.creatureRadius = (windowWidth / worldWidth) / 4

    def worldToWindow(self, x, y): # inverted coordinate y space
        # print(f"x: {x}, y: {y}")
        return int(x * self.windowWidth / self.worldWidth), int(self.windowHeight - y * self.windowHeight / self.worldHeight)

    def windowToWorld(self, x, y):
        return float(x * self.worldWidth / self.windowWidth), float((self.windowHeight - y) * self.worldHeight / self.windowHeight)

    # use WindowShouldClose() to decide how long to run
    def drawWindowFromArray(self, creatureArray, objectArray):
        BeginDrawing()
        ClearBackground(RAYWHITE)
        for objectEl in objectArray:
            (pos1X, pos1Y) = self.worldToWindow(objectEl[0][0], objectEl[0][1])
            (pos2X, pos2Y) = self.worldToWindow(objectEl[1][0], objectEl[1][1])
            DrawLine(pos1X, pos1Y, pos2X, pos2Y, BLACK)
        for creature in creatureArray:
            print(creature)
            (posX, posY) = self.worldToWindow(creature[0], creature[1])
            DrawCircle(posX, posY, self.creatureRadius, BLACK) # position

            # normalizedVel = (creature.velocity / creature.maxVelocity) * 1.25
            # (lineX, lineY) = self.worldToWindow(creature[0] + normalizedVel[0],
            #                                     creature[1] + normalizedVel[1])
            # DrawLine(posX, posY, lineX, lineY, BLACK)

        # output current mouse position
        (mouseX, mouseY) = self.windowToWorld(GetMouseX(), GetMouseY())

        DrawText(bytes(str(mouseX)+","+str(mouseY), 'utf-8'), 10, 10, 12, GRAY)

        EndDrawing()

    def drawWindow(self, creatures, walls = [], timePassed = 0):
        BeginDrawing()
        ClearBackground(RAYWHITE)

<<<<<<< HEAD
        for creature in creatures:
            #print(creature)
=======
        for creature in creatures: # draws all the creatures
>>>>>>> 5f11b128c62adb2a1c583aa8981ae2d53b7c7264
            if np.isnan(creature.location[0]) or np.isnan(creature.location[1]):
                continue
            (posX, posY) = self.worldToWindow(creature.location[0], creature.location[1])
            DrawCircle(posX, posY, 5, BLACK)

            # draw line showing current velocity
            normalizedVel = (creature.velocity / creature.maxVelocity) * 1.25
            (lineX, lineY) = self.worldToWindow(creature.location[0] + normalizedVel[0],
                                                creature.location[1] + normalizedVel[1])
            DrawLine(posX, posY, lineX, lineY, GRAY)

        for wall in walls: # draws walls
            (startX, startY) = self.worldToWindow(wall.start[0], wall.start[1])
            (endX, endY) = self.worldToWindow(wall.end[0], wall.end[1])

            DrawLine(startX, startY, endX, endY, BLACK)

        # output current mouse position
        (mouseX, mouseY) = self.windowToWorld(GetMouseX(), GetMouseY())
        DrawText(bytes(str(mouseX)+","+str(mouseY), 'utf-8'), 10, 10, 12, GRAY)

        # output current troughput
        DrawText(bytes("Troughput: " + str(simulation.calculateTroughput(creatures, timePassed)), 'utf-8'), 10, self.windowHeight-20, 12, GRAY)

        EndDrawing()

    def closeWindow(self):
        CloseWindow()


def showSimulation(filepath):
    creatures = np.load(filepath, allow_pickle=True)
    ui = UI(800, 800, 10, 10)
    objects = creatures[0]

    i = 1
    # print(creatures)
    # print("devider----------------------")
    # print(creatures[i])
    while creatures.size > i and not WindowShouldClose():
        ui.drawWindowFromArray(creatures[i], objects)

        i += 1
    ui.closeWindow()

def testUI():
<<<<<<< HEAD
        # #locations = np.array([[1,1],[1,1.1],[3,1]])
        # #goals = np.array([[1,9],[1,9.1],[3,9]])
        # locations = np.array([[2.2,1],[2,9]])
        # goals = np.array([[[2.2,11],[3,11]],[[2,1],[2,9],[2,1]]])
        # wall_positions = np.array([[2.5,0.5],[2.5,10]])
        #
        # """a = creature.Creature(locations[0],goals[0])
        # b = creature.Creature(locations[1],goals[1])
        # creatures = [a, b]"""
        #
        # creatures = []
        # for i in range(locations.ndim):
        #     creatures.append(creature.Creature(locations[i],goals[i]))
        #
        # walls = []
        # for i in range(0, wall_positions.ndim, 2):
        #     walls.append(wall.Wall(wall_positions[i], wall_positions[i+1]))
=======
    locations = np.array([[1.1,1],[0.9,1.5],[1.2,2],[5,1.2],[5,1.51],[5,1.8]])
    goals = np.array([[[4.5,1]],[[4.5,1.5]],[[4.5,2]],[[1.5,1]],[[1.5,1.5]],[[1.5,2]]])
    #locations = np.array([[2.2,1],[2,9]])
    #goals = np.array([[[2.2,11],[3,11]],[[2,1],[2,9],[2,1]]])
    wall_positions = np.array([])
>>>>>>> 5f11b128c62adb2a1c583aa8981ae2d53b7c7264

    locations = np.array([[0.2,1.2]])
    goals = np.array([[[3.8,3.8]]])
    #locations = np.array([[1,1],[9,9],[1,9]])
    #goals = np.array([[9,9],[1,1],[9,1]])

    print("#Creatures: "+str(len(locations)))
    print("#Walls: "+str(len(wall_positions)/2))

    creatures = []
<<<<<<< HEAD

    for i in range(locations.shape[0]):
        creatures.append(creature.Creature(locations[i],goals[i]))

    #wallStart = np.array([[0,0],[4,0],[4,4],[0,4],[1.5,1.5],[2.5,1.5],[2.5,2.5],[1.5,2.5]])
    #wallEnd = np.array([[4,0],[4,4],[0,4],[0,0],[2.5,1.5],[2.5,2.5],[1.5,2.5],[1.5,1.5]])
    wallStart = np.array([[4,1]])
    wallEnd = np.array([[1,3]])

    walls = []

    for i in range(wallStart.shape[0]):
        walls.append(wall.Wall(wallStart[i],wallEnd[i]))



    ui = UI(800, 800, 5, 5)
=======
    for i in range(len(locations)):
        creatures.append(creature.Creature(locations[i],goals[i], 1.3333, 0.4, True))

    walls = []
    for i in range(0, len(wall_positions), 2):
        walls.append(wall.Wall(wall_positions[i], wall_positions[i+1]))

    ui = UI(500, 500, 5, 5)
>>>>>>> 5f11b128c62adb2a1c583aa8981ae2d53b7c7264

    timePassed = 0

    while not WindowShouldClose() and timePassed < 20:
        ui.drawWindow(creatures, walls, timePassed)

        dt = 0.01 # GetFrameTime()

        for j,robot in enumerate(creatures):
            robot.update(simple.socialForce, creatures, walls, dt)

        for robot in creatures:
            robot.updateLocation()

        timePassed += dt

    ui.closeWindow()
    print(simulation.calculateTroughput(creatures, timePassed))

if __name__ == "__main__":
    from models import simple
    import sys
    if(len(sys.argv) == 2):
        showSimulation(sys.argv[1])
    else:
        testUI()
