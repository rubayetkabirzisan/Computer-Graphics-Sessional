import glfw
from OpenGL.GL import *

if not glfw.init():
    raise Exception("GLFW cannot be initialized")

window = glfw.create_window(800, 600, "OpenGL Window", None, None)

if not window:
    glfw.terminate()
    raise Exception("Window cannot be created")

glfw.make_context_current(window)

while not glfw.window_should_close(window):
    glClear(GL_COLOR_BUFFER_BIT)

    # --- Rectangle drawing using GL_QUADS (The simple, but deprecated way) ---
    glBegin(GL_QUADS)
    glColor3f(1.0, 0.0, 0.0)
    glVertex2f(-0.5, 0.5)   # Top-Left
    glVertex2f(-0.5, -0.5)  # Bottom-Left
    glVertex2f(0.5, -0.5)   # Bottom-Right
    glVertex2f(0.5, 0.5)    # Top-Right
    glEnd()
    # --------------------------------------------------------------------------

    glfw.swap_buffers(window)
    glfw.poll_events()

glfw.terminate()