import glfw
from OpenGL.GL import *
import math

if not glfw.init():
    raise Exception("GLFW cannot be initialized")

window = glfw.create_window(800, 600, "OpenGL Window (Circle)", None, None)

if not window:
    glfw.terminate()
    raise Exception("Window cannot be created")

glfw.make_context_current(window)
RADIUS = 0.5
NUM_SEGMENTS = 6  # 6 sides for a hexagon

while not glfw.window_should_close(window):
    glClear(GL_COLOR_BUFFER_BIT)
    
    # --- Draw the Hexagon ---
    glBegin(GL_TRIANGLE_FAN)
    glColor3f(1.0,0.0,0.0)
    glVertex2f(0.0, 0.0)  # Center
    
    for i in range(NUM_SEGMENTS + 1):
        angle = 2.0 * math.pi * i / NUM_SEGMENTS
        x = RADIUS * math.cos(angle)
        y = RADIUS * math.sin(angle)
        glVertex2f(x, y)
        
    glEnd()
    # ------------------------
    
    glfw.swap_buffers(window)
    glfw.poll_events()

# ... (terminate code is the same) ...