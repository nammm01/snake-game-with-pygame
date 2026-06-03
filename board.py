from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

def draw_cube(x, y, color, number_boards):
    glBegin(GL_QUADS)
    glColor3fv(color)
    glVertex3f(x, y, 0.0)
    glVertex3f(x + 1, y, 0.0)
    glVertex3f(x + 1, y + 1, 0.0)
    glVertex3f(x, y + 1, 0.0)
    glEnd()

    # Menambahkan teks/angka di tengah kotak
    font = GLUT_BITMAP_TIMES_ROMAN_24
    x_pos = x + 0.35  # Menyesuaikan posisi teks secara manual
    y_pos = y + 0.35
    glPushMatrix()
    glTranslatef(x_pos, y_pos, 0.0)
    glColor3f(0, 0, 0)  # Mengatur warna teks menjadi hitam
    glRasterPos2f(0.0, 0.0)
    for char in str(number_boards):
        glutBitmapCharacter(font, ord(char))
    glPopMatrix()


def draw_grid():
    glPushMatrix()
    glScale(1.7, 1.7, 0)
    glTranslate(-8, -5, 0)
    colors = [
        (232/255, 228/255, 227/255),
        (63/255, 121/255, 178/255)
    ]

    color_index = 0
    number_boards = 1
    row = 0

    for i in range(10):
        if row % 2 == 0:
            for j in range(10):
                draw_cube(j, i, colors[color_index], number_boards)
                color_index = (color_index + 1) % len(colors)
                number_boards += 1
        else:
            for j in range(9, -1, -1):
                draw_cube(j, i, colors[color_index], number_boards)
                color_index = (color_index + 1) % len(colors)
                number_boards += 1
        row += 1

    glPopMatrix()





