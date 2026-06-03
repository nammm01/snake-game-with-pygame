from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

vertices = [
    (0.313, 3.202),
    (-0.087, 3.202),
    (0.513, 2.802),
    (-0.287, 2.802),
    (0.323, 2.252),
    (-0.127, 2.252),
    (0.113, 1.402),
    (-0.287, 1.402),
    (0.313, 0.602),
    (-0.087, 0.602),
    (0.113, -0.198),
    (-0.287, -0.198),
    (0.283, -0.948),
    (-0.087, -0.998),
    (0.113, -1.798),
    (-0.287, -1.798),
    (0.12, -2.44),
    (-0.094, -2.44),
    (-0.05, -3.24)
]

eye1_vertices = [
    (-0.054, 3),
    (0.046, 2.8),
    (-0.154, 2.8)
]

eye2_vertices = [
    (0.2, 2.8),
    (0.4, 2.8),
    (0.3, 3)
]
mouth_vertex = [
    (0.313, 3.202),
    (-0.087, 3.202),
    (0.1, 3.0)
]

class Snake:
    def __init__(self, rotation_angle=0, scale_factor=(1, 1), translation=(0, 0)):
        self.rotation_angle = rotation_angle
        self.scale_factor = scale_factor
        self.translation = translation

    def draw_snake(self):
        glPushMatrix()
        glTranslatef(self.translation[0], self.translation[1], 0)
        glRotatef(self.rotation_angle, 0, 0, 1)
        glScalef(self.scale_factor[0], self.scale_factor[1], 0)
        glBegin(GL_TRIANGLE_STRIP)
        glColor3f(150/255, 63/255, 20/255)
        for vertex in vertices:
            glVertex2fv(vertex)
        glEnd()

        glBegin(GL_TRIANGLES)
        glColor3f(255/255, 255/255, 255/255)
        for vertex in eye1_vertices:
            glVertex2fv(vertex)
        glEnd()

        glBegin(GL_TRIANGLES)
        glColor3f(255/255, 255/255, 255/255)
        for vertex in eye2_vertices:
            glVertex2fv(vertex)
        glEnd()

        glBegin(GL_TRIANGLES)
        glColor3f(97/255, 30/255, 8/255)
        for vertex in mouth_vertex:
            glVertex2fv(vertex)
        glEnd()
        glPopMatrix()

def draw_snakes(): #panggil kedalam main.py
    global snake_configurations
    for snake_config in snake_configurations:
        snake = Snake(**snake_config)
        snake.draw_snake()

# list ular -> rotasi, ukuran, dan translasi
snake_configurations = [
    {"rotation_angle": 45, "scale_factor": (0.3, 0.3), "translation": (0.1, -7)},
    {"rotation_angle": -45, "scale_factor": (0.6, 0.6), "translation": (0.9, -6)},
    {"rotation_angle": 82, "scale_factor": (0.8, 1), "translation": (-5.9, -5.3)},
    {"rotation_angle": 0, "scale_factor": (0.7, 0.7), "translation": (-13.3, -3.5)},
    {"rotation_angle": 56, "scale_factor": (0.9, 1.2), "translation": (-2.4,-0.1)},
    {"rotation_angle": -69, "scale_factor": (0.8, 1.3), "translation": (-7,2.3)},
    {"rotation_angle": -45, "scale_factor": (0.55, 0.55), "translation": (-7.8,4.2)},
    {"rotation_angle": 45, "scale_factor": (0.5, 0.55), "translation": (-9.3,5.9)},
]