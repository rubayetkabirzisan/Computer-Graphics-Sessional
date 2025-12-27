from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math
import random

# Window dimensions
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

# Global list to store snowflake data: [x, y, speed, size]
snowflakes = []

def init_snowflakes():
    """Generates random starting positions for snowflakes."""
    global snowflakes
    num_flakes = 100  # Total number of snowflakes
    for _ in range(num_flakes):
        x = random.randint(-400, 400)
        y = random.randint(-300, 300)
        speed = random.uniform(1.0, 3.0) # Random falling speed
        size = random.uniform(5, 15)     # Random size
        snowflakes.append([x, y, speed, size])

def draw_house():
    """Draws a simple house."""
    # --- House Body (Light Gray) ---
    glColor3f(0.8, 0.8, 0.8)
    glBegin(GL_QUADS)
    glVertex2f(-200, -200)
    glVertex2f(0, -200)
    glVertex2f(0, 0)
    glVertex2f(-200, 0)
    glEnd()

    # --- Roof (Brown) ---
    glColor3f(0.6, 0.3, 0.1)
    glBegin(GL_TRIANGLES)
    glVertex2f(-220, 0)
    glVertex2f(20, 0)
    glVertex2f(-100, 120)
    glEnd()

    # --- Door (Dark Brown) ---
    glColor3f(0.4, 0.2, 0.1)
    glBegin(GL_QUADS)
    glVertex2f(-130, -200)
    glVertex2f(-70, -200)
    glVertex2f(-70, -80)
    glVertex2f(-130, -80)
    glEnd()
    
    # --- Window (Light Blue) ---
    glColor3f(0.6, 0.8, 1.0)
    glBegin(GL_QUADS)
    glVertex2f(-170, -60)
    glVertex2f(-140, -60)
    glVertex2f(-140, -30)
    glVertex2f(-170, -30)
    glEnd()

def draw_rainbow():
    """Draws a rainbow using concentric arcs."""
    radius = 300
    center_x = 0
    center_y = -100
    thickness = 20
    
    colors = [
        (1.0, 0.0, 0.0), # Red
        (1.0, 0.5, 0.0), # Orange
        (1.0, 1.0, 0.0), # Yellow
        (0.0, 1.0, 0.0), # Green
        (0.0, 0.0, 1.0), # Blue
        (0.3, 0.0, 0.5)  # Indigo
    ]

    for i, color in enumerate(colors):
        glColor3f(*color)
        current_radius = radius - (i * thickness)
        
        glBegin(GL_POINTS)
        for angle in range(0, 181):
            rad = math.radians(angle)
            x = center_x + current_radius * math.cos(rad)
            y = center_y + current_radius * math.sin(rad)
            glVertex2f(x, y)
        glEnd()

def draw_single_snowflake(size):
    """Helper to draw the geometry of one snowflake."""
    glBegin(GL_LINES)
    glColor3f(1.0, 1.0, 1.0) # White
    for _ in range(6):
        glVertex2f(0, 0)
        glVertex2f(0, size)
        glVertex2f(0, size * 0.6)
        glVertex2f(size * 0.2, size * 0.8)
        glVertex2f(0, size * 0.6)
        glVertex2f(-size * 0.2, size * 0.8)
        
        # Manually rotate the coordinates for the next branch could be complex,
        # but here we rely on glRotate in the display loop, 
        # OR we just draw 6 static lines rotated:
    glEnd()

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    
    draw_rainbow()
    draw_house()
    
    # Draw all snowflakes based on their current positions
    for flake in snowflakes:
        x, y, speed, size = flake
        glPushMatrix()
        glTranslatef(x, y, 0)
        
        # Draw the star shape of the flake
        for _ in range(6):
            draw_single_snowflake(size)
            glRotatef(60, 0, 0, 1)
            
        glPopMatrix()

    glutSwapBuffers() # Swaps the double buffer to show the frame

def animate(value):
    """Updates the position of snow."""
    global snowflakes
    
    for flake in snowflakes:
        # Decrease Y coordinate (fall down)
        flake[1] -= flake[2] 
        
        # If snowflake hits the bottom (-300), reset to top (300)
        if flake[1] < -300:
            flake[1] = 300
            # Randomize X again so it doesn't look like a repeating loop
            flake[0] = random.randint(-400, 400)
    
    glutPostRedisplay() # Trigger the display function again
    glutTimerFunc(16, animate, 0) # Call this function again in ~16ms (60 FPS)

def init():
    glClearColor(0.53, 0.81, 0.92, 1.0) # Sky blue
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(-400, 400, -300, 300)
    glPointSize(3.0)

def main():
    glutInit()
    # Changed to GLUT_DOUBLE for smoother animation
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB) 
    glutInitWindowSize(WINDOW_WIDTH, WINDOW_HEIGHT)
    glutCreateWindow(b"Falling Snow Animation")
    
    init()
    init_snowflakes() # Initialize the snow data
    
    glutDisplayFunc(display)
    glutTimerFunc(0, animate, 0) # Start the timer
    
    glutMainLoop()

if __name__ == "__main__":
    main()