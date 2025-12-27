from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math
import random

# Window dimensions
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

# Global list to store rain data: [x, y, speed, length]
raindrops = []

def init_rain():
    """Generates random starting positions for rain."""
    global raindrops
    num_drops = 300  # More drops than snowflakes for a "heavy rain" look
    for _ in range(num_drops):
        x = random.randint(-400, 400)
        y = random.randint(-300, 300)
        speed = random.uniform(8.0, 15.0) # Much faster than snow
        length = random.uniform(10, 20)   # Length of the drop
        raindrops.append([x, y, speed, length])

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

def draw_rain():
    """Draws all raindrops."""
    glBegin(GL_LINES)
    glColor3f(0.7, 0.7, 0.9)  # Light Blueish-Gray color for rain
    
    for drop in raindrops:
        x, y, speed, length = drop
        # Draw a vertical line for the drop
        glVertex2f(x, y)
        glVertex2f(x, y + length) 
        
        # Optional: For slanted rain (wind), change x in the second vertex:
        # glVertex2f(x + 5, y + length) 
        
    glEnd()

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    
    draw_rainbow()
    draw_house()
    draw_rain() # Draw the rain over the scene

    glutSwapBuffers()

def animate(value):
    """Updates the position of rain."""
    global raindrops
    
    for drop in raindrops:
        # Decrease Y coordinate (fall down)
        drop[1] -= drop[2] 
        
        # If drop hits the bottom (-300), reset to top (300)
        if drop[1] < -300:
            drop[1] = 300
            # Randomize X again
            drop[0] = random.randint(-400, 400)
    
    glutPostRedisplay()
    glutTimerFunc(16, animate, 0) 

def init():
    # Slightly darker sky for a rainy day effect
    glClearColor(0.4, 0.4, 0.6, 1.0) 
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(-400, 400, -300, 300)
    glLineWidth(1.0) # Thinner lines for rain
    glPointSize(3.0) # For the rainbow

def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(WINDOW_WIDTH, WINDOW_HEIGHT)
    glutCreateWindow(b"House with Heavy Rain")
    
    init()
    init_rain() # Initialize the rain data
    
    glutDisplayFunc(display)
    glutTimerFunc(0, animate, 0) 
    
    glutMainLoop()

if __name__ == "__main__":
    main()