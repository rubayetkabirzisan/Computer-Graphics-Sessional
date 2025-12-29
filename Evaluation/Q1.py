# YOU ARE TASKED WITh CREATING A 2D ANIMATED roadside scene using opengl and glut. the scene represents a roadside environment containng a moving windmil and moving clouds. the windmill moves continuously, while the chouds cycle through automatically. you are required to implement this scsne using pyton opengl(py opengl) with the following:
# use 2d orthographic projection :glu ortho2d(0,100,0,100)
# draw the windmil , road, clouds using glbegin and glend only.
#use double nufferin gto avoid flickering (glut_double)
# the animation loop must be implemented using glutidlefunc
# the window size is 500x500 pixels

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math

# ==========================================
# Global Variables for Animation
# ==========================================
WINDOW_WIDTH = 500
WINDOW_HEIGHT = 500

# Animation states
windmill_angle = 0.0
cloud_x = 0.0
car_x = 100.0  # Car starts at the right side

# ==========================================
# Helper Functions (Makes drawing easier)
# ==========================================
def draw_circle(x, y, radius, red, green, blue):
    """ draws a filled circle using math.cos and math.sin """
    glColor3f(red, green, blue)
    glBegin(GL_POLYGON)
    for i in range(360):
        theta = i * 3.14159 / 180
        cx = x + radius * math.cos(theta)
        cy = y + radius * math.sin(theta)
        glVertex2f(cx, cy)
    glEnd()

def draw_rect(x, y, width, height, r, g, b):
    """ draws a simple rectangle """
    glColor3f(r, g, b)
    glBegin(GL_QUADS)
    glVertex2f(x, y)
    glVertex2f(x + width, y)
    glVertex2f(x + width, y + height)
    glVertex2f(x, y + height)
    glEnd()

# ==========================================
# Scene Drawing Functions
# ==========================================
def draw_background():
    # 1. Sky (Clear Blue) - Handled by glClearColor in init()
    
    # 2. Sun (Top Right)
    draw_circle(85, 85, 8, 1.0, 0.9, 0.0) # Yellow Sun

    # 3. Green Grass (Bottom half)
    draw_rect(0, 0, 100, 35, 0.1, 0.8, 0.1) # Bright Green

    # 4. Road (Gray strip)
    draw_rect(0, 10, 100, 15, 0.3, 0.3, 0.3) # Dark Gray Road

    # 5. Road Stripes (White dashes)
    glColor3f(1.0, 1.0, 1.0)
    glLineWidth(3)
    glBegin(GL_LINES)
    for i in range(0, 110, 15):
        glVertex2f(i, 17.5)
        glVertex2f(i + 8, 17.5)
    glEnd()

def draw_windmill():
    global windmill_angle
    
    # Base of the Windmill (Brown Triangle)
    glColor3f(0.5, 0.35, 0.05)
    glBegin(GL_TRIANGLES)
    glVertex2f(70, 35)  # Bottom Left
    glVertex2f(80, 35)  # Bottom Right
    glVertex2f(75, 65)  # Top Tip
    glEnd()

    # The Blades (Rotating)
    glPushMatrix()
    glTranslatef(75, 65, 0)      # Move to the top of the tower
    glRotatef(windmill_angle, 0, 0, 1) # Rotate
    
    glColor3f(0.9, 0.9, 0.9)     # White Blades
    
    glBegin(GL_TRIANGLES)
    # Top Blade
    glVertex2f(0, 0); glVertex2f(-3, 25); glVertex2f(3, 25)
    # Bottom Blade
    glVertex2f(0, 0); glVertex2f(-3, -25); glVertex2f(3, -25)
    # Left Blade
    glVertex2f(0, 0); glVertex2f(-25, -3); glVertex2f(-25, 3)
    # Right Blade
    glVertex2f(0, 0); glVertex2f(25, -3); glVertex2f(25, 3)
    glEnd()
    
    # Center dot of the fan
    draw_circle(0, 0, 2, 0.2, 0.2, 0.2)
    
    glPopMatrix()

def draw_clouds():
    global cloud_x
    glPushMatrix()
    glTranslatef(cloud_x, 0, 0) # Move clouds based on variable
    
    # Cloud 1 (Three overlapping white circles)
    draw_circle(10, 80, 5, 1, 1, 1)
    draw_circle(18, 80, 6, 1, 1, 1)
    draw_circle(25, 80, 5, 1, 1, 1)

    # Cloud 2 (Another cluster)
    draw_circle(40, 70, 5, 1, 1, 1)
    draw_circle(48, 75, 7, 1, 1, 1)
    draw_circle(56, 70, 5, 1, 1, 1)
    
    glPopMatrix()

def draw_car():
    global car_x
    glPushMatrix()
    glTranslatef(car_x, 0, 0) # Move car based on variable
    
    # Car Body (Red Rectangle)
    draw_rect(0, 12, 12, 6, 1.0, 0.0, 0.0) 
    # Car Roof (Blue Rectangle)
    draw_rect(2, 18, 8, 4, 0.0, 0.0, 1.0)
    
    # Wheels (Black Circles)
    draw_circle(2, 12, 2.5, 0, 0, 0)
    draw_circle(10, 12, 2.5, 0, 0, 0)
    
    glPopMatrix()

# ==========================================
# Core OpenGL Functions
# ==========================================
def display():
    glClear(GL_COLOR_BUFFER_BIT)
    
    draw_background()
    draw_windmill()
    draw_clouds()
    draw_car()
    
    glutSwapBuffers()

def animate():
    global windmill_angle, cloud_x, car_x
    
    # 1. Spin Windmill
    windmill_angle += 2.0
    if windmill_angle >= 360:
        windmill_angle = 0
        
    # 2. Move Clouds (Left to Right)
    cloud_x += 0.05
    if cloud_x > 100:
        cloud_x = -60
        
    # 3. Move Car (Right to Left)
    car_x -= 0.15
    if car_x < -20:
        car_x = 110
        
    glutPostRedisplay()

def init():
    glClearColor(0.53, 0.81, 0.92, 1.0) # Sky Blue Background
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0, 100, 0, 100) # Simple 0-100 coordinate system

def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(WINDOW_WIDTH, WINDOW_HEIGHT)
    glutCreateWindow(b"Animated Roadside Scene")
    
    init()
    
    glutDisplayFunc(display)
    glutIdleFunc(animate)
    
    glutMainLoop()

if __name__ == "__main__":
    main()