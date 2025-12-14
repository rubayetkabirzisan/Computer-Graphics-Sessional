import glfw
from OpenGL.GL import *

if not glfw.init():
    raise Exception("GLFW cannot be initialized")

window = glfw.create_window(800, 600, "OpenGL Triangle", None, None)

if not window:
    glfw.terminate()
    raise Exception("Window cannot be created")

glfw.make_context_current(window)
glViewport(0, 0, 800, 600)
glClearColor(0.0, 0.0, 0.0, 1.0)

while not glfw.window_should_close(window):
    glClear(GL_COLOR_BUFFER_BIT)

    glBegin(GL_TRIANGLES)
    glColor3f(1.0, 0.0, 0.0)
    glVertex2f(0.0, 0.5)      # Top
    glVertex2f(-0.5, -0.5)   # Bottom left
    glVertex2f(0.5, -0.5)    # Bottom right
    glEnd()

    glfw.swap_buffers(window)
    glfw.poll_events()

glfw.terminate()