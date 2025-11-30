# DDA Line Drawing Algorithm

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math

def ddaLine(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1

    steps = max(abs(dx), abs(dy))

    xInc = dx / float(steps)
    yInc = dy / float(steps)

    x = x1
    y = y1

    glBegin(GL_POINTS)
    for i in range(steps + 1):
        glVertex2i(int(round(x)), int(round(y)))
        x += xInc
        y += yInc
    glEnd()


def display():
    glClear(GL_COLOR_BUFFER_BIT)

    glColor3f(1, 1, 1)
    ddaLine(50, 50, 400, 300)

    glFlush()


def init():
    glClearColor(0, 0, 0, 1)
    glColor3f(1, 1, 1)

    # Set the coordinate system
    gluOrtho2D(0, 500, 0, 500)


def main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(500, 500)
    glutCreateWindow(b"DDA Line Drawing in Python")   # <-- FIXED

    init()
    glutDisplayFunc(display)
    glutMainLoop()



if __name__ == "__main__":
    main()
