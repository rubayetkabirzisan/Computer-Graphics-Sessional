from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def draw_A():
    # Draws an 'A' roughly centered at (0,0) with height 2 and width 1
    glBegin(GL_LINES)
    
    # Left Diagonal Leg (from bottom-left to top-center)
    glVertex2f(0.0, 0.0)
    glVertex2f(0.5, 2.0)
    
    # Right Diagonal Leg (from top-center to bottom-right)
    glVertex2f(0.5, 2.0)
    glVertex2f(1.0, 0.0)
    
    # Middle Horizontal Bar
    # Roughly halfway up the legs
    glVertex2f(0.25, 1.0)
    glVertex2f(0.75, 1.0)
    
    glEnd()

def draw_N():
    # Draws an 'N' roughly centered at (0,0) with height 2 and width 1
    glBegin(GL_LINES)
    
    # Left Vertical Line
    glVertex2f(0.0, 0.0)
    glVertex2f(0.0, 2.0)
    
    # Diagonal Line (Top-left to Bottom-right)
    glVertex2f(0.0, 2.0)
    glVertex2f(1.0, 0.0)
    
    # Right Vertical Line
    glVertex2f(1.0, 0.0)
    glVertex2f(1.0, 2.0)
    
    glEnd()

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0, 1.0, 1.0) # White color
    
    # --- DRAW THE 'A' ---
    glPushMatrix()
    # Move left to position the first letter
    glTranslatef(-1.5, -1.0, 0.0) 
    draw_A()
    glPopMatrix()
    
    # --- DRAW THE 'N' ---
    glPushMatrix()
    # Move right to position the second letter
    glTranslatef(0.5, -1.0, 0.0)
    draw_N()
    glPopMatrix()
    
    glFlush()

def main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(500, 500)
    glutCreateWindow(b"Manual Drawing of AN")
    
    # Set up a 2D coordinate system from -5 to 5
    gluOrtho2D(-5, 5, -5, 5)
    
    glutDisplayFunc(display)
    # Set clear color to black
    glClearColor(0.0, 0.0, 0.0, 1.0)
    glutMainLoop()

if __name__ == "__main__":
    main()