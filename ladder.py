from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import player

class Ladder:
    def __init__(self, head_position, tail_position):
        self.head = head_position
        self.tail = tail_position

def snake_system(ladder):
    if player.loc_p1 == ladder.head:
        player.loc_p1 -= (ladder.head - ladder.tail)
    elif player.loc_p2 == ladder.head:
        player.loc_p2 -= (ladder.head - ladder.tail)
    return player.loc_p1, player.loc_p2

Ladders = [
    Ladder(6,26),
    Ladder(10,29),
    Ladder(17,45),
    Ladder(48,68),
    Ladder(58,79),
    Ladder(61,82),
    Ladder(72,87),
    ]

def ladder_init():
    global Ladders
    for Ladder in Ladders:
        snake_system(Ladder)