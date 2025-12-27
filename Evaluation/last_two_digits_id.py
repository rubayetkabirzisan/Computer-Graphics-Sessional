from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def draw_five():
    # Draws a '5' roughly centered at (0,0) with height 2 and width 1
    glBegin(GL_LINES)
    # Top horizontal bar
    glVertex2f(0.0, 2.0)
    glVertex2f(1.0, 2.0)
    
    # Upper vertical (left)
    glVertex2f(0.0, 2.0)
    glVertex2f(0.0, 1.0)
    
    # Middle horizontal
    glVertex2f(0.0, 1.0)
    glVertex2f(1.0, 1.0)
    
    # Lower vertical (right)
    glVertex2f(1.0, 1.0)
    glVertex2f(1.0, 0.0)
    
    # Bottom horizontal
    glVertex2f(1.0, 0.0)
    glVertex2f(0.0, 0.0)
    glEnd()

def draw_four():
    # Draws a '4'
    glBegin(GL_LINES)
    # Upper left vertical
    glVertex2f(0.0, 2.0)
    glVertex2f(0.0, 1.0)
    
    # Middle horizontal
    glVertex2f(0.0, 1.0)
    glVertex2f(1.0, 1.0)
    
    # Long right vertical
    glVertex2f(1.0, 2.0)
    glVertex2f(1.0, 0.0)
    glEnd()

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0, 1.0, 1.0) # White color
    
    # --- DRAW THE '5' ---
    glPushMatrix()
    # Move slightly left to position the first digit
    glTranslatef(-1.5, -1.0, 0.0) 
    draw_five()
    glPopMatrix()
    
    # --- DRAW THE '4' ---
    glPushMatrix()
    # Move slightly right to position the second digit
    glTranslatef(0.5, -1.0, 0.0)
    draw_four()
    glPopMatrix()
    
    glFlush()

def main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(500, 500)
    glutCreateWindow(b"Manual Drawing of 54")
    
    # Set up a 2D coordinate system from -5 to 5
    gluOrtho2D(-5, 5, -5, 5)
    
    glutDisplayFunc(display)
    glClearColor(0.0, 0.0, 0.0, 1.0)
    glutMainLoop()

if __name__ == "__main__":
    main()