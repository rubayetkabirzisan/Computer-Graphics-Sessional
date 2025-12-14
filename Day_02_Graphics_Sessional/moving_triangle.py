import glfw
from OpenGL.GL import *
import time

def draw_triangle(x):
    glBegin(GL_TRIANGLES)
    glColor3f(1.0, 0.0, 0.0)

    glVertex2f(x, 0.5)          # Top
    glVertex2f(x - 0.3, -0.5)   # Bottom left
    glVertex2f(x + 0.3, -0.5)   # Bottom right

    glEnd()

if not glfw.init():
    raise Exception("GLFW cannot be initialized")

window = glfw.create_window(800, 600, "Moving Triangle", None, None)

if not window:
    glfw.terminate()
    raise Exception("Window cannot be created")

glfw.make_context_current(window)

glViewport(0, 0, 800, 600)
glClearColor(0.0, 0.0, 0.0, 1.0)

x_position = -1.0

while not glfw.window_should_close(window):
    glClear(GL_COLOR_BUFFER_BIT)

    draw_triangle(x_position)
    x_position += 0.01

    if x_position > 1.2:
        x_position = -1.2

    glfw.swap_buffers(window)
    glfw.poll_events()
    time.sleep(0.01)

glfw.terminate()

# py "e:\Graphics_Sessional\Day_02_Graphics_Sessional\moving_triangle.py"