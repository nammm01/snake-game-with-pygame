from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

class Ladder:
    def __init__(self, rotation_angle=0, scale_factor=(1, 1), translation=(0, 0)):
        self.rotation_angle = rotation_angle
        self.scale_factor = scale_factor
        self.translation = translation

    def draw_ladder(self):
        glPushMatrix()
        glTranslatef(self.translation[0], self.translation[1], 0)
        glRotatef(self.rotation_angle, 0, 0, 1)
        glScalef(self.scale_factor[0], self.scale_factor[1], 0)

        for i in range(2):
            glBegin(GL_QUADS)
            glColor3f(78/255, 30/255, 133/255)
            glVertex2f(-0.4 + i*0.8,3)
            glVertex2f(-0.6 + i*1.2,3)
            glVertex2f(-0.6 + i*1.2,-3)
            glVertex2f(-0.4 + i*0.8,-3)
            glEnd()

        for i in range(9):
            glBegin(GL_QUADS)
            glColor3f(78/255, 30/255, 133/255)
            glVertex2f(-0.4,2.6 - i*0.6)
            glVertex2f(0.4,2.6 - i*0.6)
            glVertex2f(0.4,2.4 - i*0.6)
            glVertex2f(-0.4,2.4 - i*0.6)
            glEnd()
        glPopMatrix()

def draw_ladders(): #panggil kedalam main.py
    global ladder_configurations
    for ladder_config in ladder_configurations:
        ladder = Ladder(**ladder_config)
        ladder.draw_ladder()

# list tangga -> rotasi, ukuran, dan translasi
ladder_configurations = [
    {"rotation_angle": 20, "scale_factor": (0.6, 0.6), "translation": (1.7, -6)},
    {"rotation_angle": 0, "scale_factor": (0.5, 0.5), "translation": (-4, -6)},
    {"rotation_angle": -14, "scale_factor": (0.8, 0.8), "translation": (-6.8, -3.5)},
    {"rotation_angle": 0, "scale_factor": (0.5, 0.5), "translation": (-1.3, 0.8)},
    {"rotation_angle": 70, "scale_factor": (0.5, 0.5), "translation": (-0.8, 5)},
    {"rotation_angle": 20, "scale_factor": (0.5, 0.5), "translation": (-10.3, 2.5)},
    {"rotation_angle": -15, "scale_factor": (0.55, 0.55), "translation": (-12, 4.2)},
]
