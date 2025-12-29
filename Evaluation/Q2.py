# you are asked to create a simple 2d linedisplay using opengl and glut in python. the program must drw
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

# --- Configuration ---
WINDOW_WIDTH = 500
WINDOW_HEIGHT = 500
GRID_SIZE = 50 # Size of each square cell in pixels

def init():
    # Set background color to BLACK (R, G, B, Alpha)
    glClearColor(0.0, 0.0, 0.0, 1.0)
    
    # Set up the projection (Coordinate system 0 to Width/Height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0, WINDOW_WIDTH, 0, WINDOW_HEIGHT)

def draw_grid():
    glLineWidth(1.0) # Set line thickness
    glColor3f(1.0, 1.0, 1.0) # Set line color to WHITE
    
    glBegin(GL_LINES)
    
    # 1. Draw Vertical Lines
    # Iterate across the X axis from 0 to Width
    for x in range(0, WINDOW_WIDTH + 1, GRID_SIZE):
        glVertex2f(x, 0)             # Bottom point
        glVertex2f(x, WINDOW_HEIGHT) # Top point

    # 2. Draw Horizontal Lines
    # Iterate across the Y axis from 0 to Height
    for y in range(0, WINDOW_HEIGHT + 1, GRID_SIZE):
        glVertex2f(0, y)            # Left point
        glVertex2f(WINDOW_WIDTH, y) # Right point
        
    glEnd()

def display():
    glClear(GL_COLOR_BUFFER_BIT) # Clear screen with the black background set in init()
    
    draw_grid()
    
    glutSwapBuffers()

def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(WINDOW_WIDTH, WINDOW_HEIGHT)
    glutInitWindowPosition(100, 100)
    glutCreateWindow(b"OpenGL Square Grid")
    
    init() # Call our initialization settings
    
    glutDisplayFunc(display)
    glutMainLoop()

if __name__ == "__main__":
    main()