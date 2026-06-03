from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

win = False
text = None

def btn():
    global text
    if not win:
        glPushMatrix()
        glScalef(2, 2, 0)
        glTranslatef(5.1, -0.7, 0)
        
        # Draw the button
        glBegin(GL_QUADS)
        glColor3f(1, 1, 1)
        glVertex2f(0, 0)
        glVertex2f(0.8, 0)
        glVertex2f(0.8, 0.4)
        glVertex2f(0, 0.4)
        glEnd()

        # Draw the text
        glColor3f(0, 0, 0)  # Set text color to black
        glRasterPos2f(0.15, 0.1)  # Set text position
        btn1 = "Roll"
        for char in btn1:
            glutBitmapCharacter(GLUT_BITMAP_TIMES_ROMAN_24, ord(char))
        glPopMatrix()
    
    elif win:
        glPushMatrix()
        glScalef(2, 2, 0)
        glTranslatef(-3, -0.7, 0)
        # Draw the button
        glBegin(GL_QUADS)
        glColor3f(1, 1, 1)
        glVertex2f(0, 0)
        glVertex2f(6, 0)
        glVertex2f(6, 3)
        glVertex2f(0, 3)
        glEnd()
        glPopMatrix()

        glPushMatrix()
        glScalef(2, 2, 0)
        glTranslatef(-2.95, -0.65, 0)
        # Draw the button
        glBegin(GL_QUADS)
        glColor3f(0, 0, 0)
        glVertex2f(0, 0)
        glVertex2f(5.9, 0)
        glVertex2f(5.9, 2.9)
        glVertex2f(0, 2.9)
        glEnd()
        glPopMatrix()

        glPushMatrix()
        glScalef(2, 2, 0)
        glTranslatef(-2.90, -0.60, 0)
        # Draw the button
        glBegin(GL_QUADS)
        glColor3f(1, 1, 1)
        glVertex2f(0, 0)
        glVertex2f(5.8, 0)
        glVertex2f(5.8, 2.8)
        glVertex2f(0, 2.8)
        glEnd()

        glColor3f(0, 0, 0)
        glRasterPos2f(1.8, 2)
        for char in text:
            glutBitmapCharacter(GLUT_BITMAP_TIMES_ROMAN_24, ord(char))
        glPopMatrix()

        glPushMatrix()
        glScalef(2, 2, 0)
        glTranslatef(-0.5, -0.2, 0)
        glBegin(GL_QUADS)
        glColor3f(0, 0, 0)
        glVertex2f(0, 0)
        glVertex2f(1, 0)
        glVertex2f(1, 0.4)
        glVertex2f(0, 0.4)
        glEnd()

        glColor3f(1, 1, 1)
        glRasterPos2f(0.1, 0.1)
        btn2 = "Reset"
        for char in btn2:
            glutBitmapCharacter(GLUT_BITMAP_TIMES_ROMAN_24, ord(char))
        glPopMatrix()

    
