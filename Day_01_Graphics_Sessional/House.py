import numpy as np
import pygame as pg
from OpenGL.GL import *
from OpenGL.GL.shaders import compileProgram, compileShader
import ctypes

# ============================================================
#                 SHADERS (Same Style as Yours)
# ============================================================
VERTEX_SHADER = """
#version 330 core
layout(location = 0) in vec3 aPos;
layout(location = 1) in vec3 aColor;

out vec3 vertexColor;

void main()
{
    gl_Position = vec4(aPos, 1.0);
    vertexColor = aColor;
}
"""

FRAGMENT_SHADER = """
#version 330 core
in vec3 vertexColor;
out vec4 FragColor;

void main()
{
    FragColor = vec4(vertexColor, 1.0);
}
"""
# ============================================================


class App:
    def __init__(self):
        # Initialize window
        pg.init()
        pg.display.set_mode((800, 600), pg.OPENGL | pg.DOUBLEBUF)
        pg.display.set_caption("OpenGL House")
        self.running = True

        # Compile shader program
        self.shader = compileProgram(
            compileShader(VERTEX_SHADER, GL_VERTEX_SHADER),
            compileShader(FRAGMENT_SHADER, GL_FRAGMENT_SHADER)
        )
        glUseProgram(self.shader)

        # ---------------------------------------------------------
        # House geometry (positions + colors)
        # ---------------------------------------------------------

        # Roof (triangle) – red
        self.roof_vertices = np.array([
            -0.6,  0.0, 0.0,   1, 0, 0,
             0.6,  0.0, 0.0,   1, 0, 0,
             0.0,  0.6, 0.0,   1, 0, 0
        ], dtype=np.float32)

        # Walls (quad) – blue
        self.walls_vertices = np.array([
            -0.5, -0.6, 0.0,   0, 0, 1,
             0.5, -0.6, 0.0,   0, 0, 1,
             0.5,  0.0, 0.0,   0, 0, 1,
            -0.5,  0.0, 0.0,   0, 0, 1
        ], dtype=np.float32)

        # Door (quad) – brown
        self.door_vertices = np.array([
            -0.15, -0.6, 0.0,   0.5, 0.25, 0.0,
             0.15, -0.6, 0.0,   0.5, 0.25, 0.0,
             0.15, -0.2, 0.0,   0.5, 0.25, 0.0,
            -0.15, -0.2, 0.0,   0.5, 0.25, 0.0
        ], dtype=np.float32)

        # Create VAOs + VBOs
        self.roof = self._setup_buffer_objects(self.roof_vertices)
        self.walls = self._setup_buffer_objects(self.walls_vertices)
        self.door = self._setup_buffer_objects(self.door_vertices)

        # Enter main loop
        self.main_loop()

    # ============================================================
    #           VAO / VBO SETUP (Reused for each shape)
    # ============================================================
    def _setup_buffer_objects(self, vertex_data):
        vao = glGenVertexArrays(1)
        glBindVertexArray(vao)

        vbo = glGenBuffers(1)
        glBindBuffer(GL_ARRAY_BUFFER, vbo)
        glBufferData(GL_ARRAY_BUFFER, vertex_data.nbytes, vertex_data, GL_STATIC_DRAW)

        # Position attribute (location 0)
        glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 6 * 4, ctypes.c_void_p(0))
        glEnableVertexAttribArray(0)

        # Color attribute (location 1)
        glVertexAttribPointer(1, 3, GL_FLOAT, GL_FALSE, 6 * 4, ctypes.c_void_p(12))
        glEnableVertexAttribArray(1)

        glBindBuffer(GL_ARRAY_BUFFER, 0)
        glBindVertexArray(0)

        return vao, vbo, len(vertex_data) // 6

    # ============================================================
    #                          RENDER
    # ============================================================
    def render(self):
        glClear(GL_COLOR_BUFFER_BIT)
        glClearColor(0.8, 0.9, 1.0, 1.0)  # Sky blue background

        glUseProgram(self.shader)

        # Draw roof
        glBindVertexArray(self.roof[0])
        glDrawArrays(GL_TRIANGLES, 0, self.roof[2])

        # Draw walls (quad)
        glBindVertexArray(self.walls[0])
        glDrawArrays(GL_TRIANGLE_FAN, 0, self.walls[2])

        # Draw door (quad)
        glBindVertexArray(self.door[0])
        glDrawArrays(GL_TRIANGLE_FAN, 0, self.door[2])

        pg.display.flip()

    # ============================================================
    #                       MAIN LOOP
    # ============================================================
    def main_loop(self):
        while self.running:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.running = False

            self.render()

        self.destroy()
        self.quit()

    def quit(self):
        pg.quit()

    # ============================================================
    #                        CLEANUP
    # ============================================================
    def destroy(self):
        for vao, vbo, count in (self.roof, self.walls, self.door):
            glDeleteVertexArrays(1, (vao,))
            glDeleteBuffers(1, (vbo,))


# ============================================================
#                      ENTRY POINT
# ============================================================
if __name__ == "__main__":
    App()
