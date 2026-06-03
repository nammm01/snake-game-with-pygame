from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

loc_p1 = 1
loc_p2 = 1
current_player = 1
loc_max = 100

def draw_player(grid_x, grid_y, color, scale):
    glPushMatrix()
    glColor3f(color[0], color[1], color[2])
    glTranslate(grid_x, grid_y, 0)
    glScale(scale, scale, 0)
    glBegin(GL_QUADS)
    glVertex2d(0, 0)
    glVertex2d(1, 0)
    glVertex2d(1, 1)
    glVertex2d(0, 1)
    glEnd()
    glPopMatrix()

def draw_cube(x, y):
    glBegin(GL_POINTS)
    glVertex3f(x, y, 0.0)
    glVertex3f(x + 1, y, 0.0)
    glVertex3f(x + 1, y + 1, 0.0)
    glVertex3f(x, y + 1, 0.0)
    glEnd()


def draw_grid():
    glPushMatrix()
    glScale(1.7, 1.7, 0)
    glTranslate(-8, -5, 0)
    number = 1
    row = 0

    for i in range(10):
        if row % 2 == 0:
            for j in range(10):
                draw_cube(j, i)
                if number == loc_p1 and number == loc_p2:
                    draw_player(j + 0.10, i + 0.10, color=(1, 0, 0), scale = 0.35)
                    draw_player(j + 0.55, i + 0.55, color=(0, 1, 0), scale = 0.35)
                elif number == loc_p1:
                    draw_player(j + 0.25, i + 0.25, color=(1, 0, 0), scale = 0.5)
                elif number == loc_p2:
                    draw_player(j + 0.25, i + 0.25, color=(0, 1, 0), scale = 0.5)
                number += 1
        else:
            for j in range(9, -1, -1):
                draw_cube(j, i)
                if number == loc_p1 and number == loc_p2:
                    draw_player(j + 0.10, i + 0.10, color=(1, 0, 0), scale = 0.35)
                    draw_player(j + 0.55, i + 0.55, color=(0, 1, 0), scale = 0.35)
                elif number == loc_p1:
                    draw_player(j + 0.25, i + 0.25, color=(1, 0, 0), scale = 0.5)
                elif number == loc_p2:
                    draw_player(j + 0.25, i + 0.25, color=(0, 1, 0), scale = 0.5)
                number += 1
        row += 1

    glPopMatrix()

def draw_current_player():
    font = GLUT_BITMAP_TIMES_ROMAN_24

    glPushMatrix()
    glTranslatef(10, 4, 0.0)
    glColor3f(1, 1, 1)
    glRasterPos2f(0.0, 0.0)
    for char in "Player 1":
        glutBitmapCharacter(font, ord(char))
    glPopMatrix()

    glPushMatrix()
    glTranslatef(10, -7, 0.0)
    glColor3f(1, 1, 1)
    glRasterPos2f(0.0, 0.0)
    for char in "Player 2":
        glutBitmapCharacter(font, ord(char))
    glPopMatrix()

    draw_player(10.2, 5, color=(0.3,0,0), scale = 1.5)
    draw_player(10.2, -6, color=(0,0.3,0), scale = 1.5)
    if current_player == 1:
        draw_player(10.2, 5, color=(1,0,0), scale = 1.5)
    elif current_player == 2:
        draw_player(10.2, -6, color=(0,1,0), scale = 1.5)





