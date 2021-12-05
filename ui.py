from raylib import *
import numpy as np
import creature
import simulation
from scene import wall

"""
    Class used to show a simulation on a window.
    The simulation is either done at the same time (with possible slow down to rendering) or can be done in advanced 
    and then be visualized using the method.
    
    The world is assumed to always be starting at (0,0) and only expand in the positive x and y direction. Creatures and objects may be placed outside those bounds
    and still work as expected but won't be shown on screen.
"""
class UI:
    # initilazes the window and sets the size of both the window and the simualted world
    def __init__(self, windowWidth, windowHeight, worldWidth, worldHeight):
        InitWindow(windowWidth, windowHeight, b"Social Forces Model")
        SetTargetFPS(60)

        # important: creatures may appear to be walking much faster into 1 axis than in the other one.
        # This may happen if the ration of world and screen don't match up
        self.windowWidth = windowWidth
        self.windowHeight = windowHeight

        self.worldWidth = worldWidth
        self.worldHeight = worldHeight
        # sets creature radius to 0.25m
        self.creatureRadius = (windowWidth / worldWidth) / 4

    # converts from world to window space
    def worldToWindow(self, x, y): # inverted coordinate y space
        return int(x * self.windowWidth / self.worldWidth), int(self.windowHeight - y * self.windowHeight / self.worldHeight)

    # converts from window to world space (useful for finding out where cursor is in the world)
    def windowToWorld(self, x, y):
        return float(x * self.worldWidth / self.windowWidth), float((self.windowHeight - y) * self.worldHeight / self.windowHeight)

    # draws creatures and objects for one frame
    def drawWindowFromArrays(self, creatureArray, objectArray):
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

    # draws the world with all the creatures and walls. The creature also show their current velocity vector
    def drawWindow(self, creatures, walls=[], timePassed=0):
        BeginDrawing()
        ClearBackground(RAYWHITE)

        for creature in creatures: # draws all the creatures
            if np.isnan(creature.location[0]) or np.isnan(creature.location[1]):
                continue

            (posX, posY) = self.worldToWindow(creature.location[0], creature.location[1])
            DrawCircle(posX, posY, self.creatureRadius, BLACK)

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


# gets filepath to generated simulation file and visualises content
def showSimulation(filepath):
    creatures = np.load(filepath, allow_pickle=True)
    ui = UI(800, 800, 10, 10)
    objects = creatures[0]

    i = 1
    # print(creatures)
    # print("devider----------------------")
    # print(creatures[i])
    while creatures.size > i and not WindowShouldClose():
        ui.drawWindowFromArrays(creatures[i], objects)

        i += 1
    ui.closeWindow()


# example scene that will be played when running ui.py without any additional parameters
def testUI():
    import lane, bottleneck, evacuate, crossing

    creatures = bottleneck.creatures()# or bottleneck, evacuate, crossing
    walls = bottleneck.objects()

    ui = UI(800, 800, 10, 10)

    timePassed = 0

    # update loop (simulates at most 60 seconds)
    while not WindowShouldClose() and timePassed < 60:
        ui.drawWindow(creatures, walls, timePassed)

        dt = 0.01

        for robot in creatures:
            robot.update(simple.socialForce, creatures, walls, dt)

        for robot in creatures:
            robot.updateLocation()

        timePassed += dt

    ui.closeWindow()
    print(simulation.calculateTroughput(creatures, timePassed))


if __name__ == "__main__":
    from models import simple
    import sys
    if len(sys.argv) == 2:
        showSimulation(sys.argv[1])
    else:
        testUI()
