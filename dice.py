from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import math, player, random, button

number_dice = 1
kali = 0

def quads():
    glBegin(GL_QUADS)
    glColor3f(1, 1, 1)
    glVertex2f(0.0, 0.0)  
    glVertex2f(1.0, 0.0)  
    glVertex2f(1.0, 1.0)  
    glVertex2f(0.0, 1.0)  
    glEnd()

def circle(x, y, sides, radius):
    glBegin(GL_TRIANGLE_FAN)
    glColor3f(0, 0, 0)
    for i in range(sides + 1):
        angle = (i / sides) * 2 * math.pi
        glVertex2f(x + radius * math.cos(angle), y + radius * math.sin(angle))
    glEnd()


def dice_draw():
    glPushMatrix()
    glScalef(2, 2, 0)
    glTranslatef(5, 0, 0)

    if number_dice == 1:
        quads()  
        circle(0.5, 0.5, 100, 0.2) 
        
    elif number_dice == 2:
        quads()
        circle(0.3, 0.3, 100, 0.1)
        circle(0.7, 0.7, 100, 0.1)

    elif number_dice == 3:
        quads()
        circle(0.5, 0.5, 100, 0.1)
        circle(0.75, 0.25, 100, 0.1)
        circle(0.25, 0.75, 100, 0.1)
    
    elif number_dice == 4:
        quads()
        circle(0.25, 0.25, 100, 0.1)
        circle(0.75, 0.25, 100, 0.1)
        circle(0.25, 0.75, 100, 0.1)
        circle(0.75, 0.75, 100, 0.1)

    elif number_dice == 5:
        quads()
        circle(0.25, 0.25, 100, 0.1)
        circle(0.75, 0.25, 100, 0.1)
        circle(0.25, 0.75, 100, 0.1)
        circle(0.75, 0.75, 100, 0.1)
        circle(0.5, 0.5, 100, 0.1)

    elif number_dice == 6:
        quads()
        circle(0.25, 0.25, 100, 0.1)
        circle(0.75, 0.25, 100, 0.1)
        circle(0.25, 0.75, 100, 0.1)
        circle(0.75, 0.75, 100, 0.1)
        circle(0.25, 0.5, 100, 0.1)
        circle(0.75, 0.5, 100, 0.1)

    glPopMatrix()

def roll_dice():
    global number_dice, kali
    number_dice = random.randint(1, 6)
    print(number_dice)
    if player.current_player == 1:
        player.loc_p1 += number_dice
        if player.loc_p1 > player.loc_max:
            player.loc_p1 -= number_dice
        elif player.loc_p1 == player.loc_max:
            button.win = True
            button.text = "Player 1 Menang"
            print("player 1 win")
        
        elif kali == 2:
            player.current_player = 3 - player.current_player 
            player.loc_p1 -= number_dice
            kali = 0

        if number_dice == 6:
            kali += 1
        else:
            player.current_player = 3 - player.current_player
            kali = 0

            
    elif player.current_player == 2:
        player.loc_p2 += number_dice
        if player.loc_p2 > player.loc_max:
            player.loc_p2 -= number_dice
        elif player.loc_p2 == player.loc_max:
            button.win = True
            button.text = "Player 2 Menang"
            print("player 2 win")

        elif kali == 2:
            player.current_player = 3 - player.current_player 
            player.loc_p2 -= number_dice
            kali = 0

        if number_dice == 6:
            kali += 1
        else:
            player.current_player = 3 - player.current_player
            kali = 0

def update_scene():
    roll_dice()
    glutTimerFunc(100, update_scene, 0)