from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import player

class Snake:
    def __init__(self, head_position, tail_position):
        self.head = head_position
        self.tail = tail_position

def snake_system(snake):
    if player.loc_p1 == snake.head:
        player.loc_p1 -= (snake.head - snake.tail)
    elif player.loc_p2 == snake.head:
        player.loc_p2 -= (snake.head - snake.tail)
    return player.loc_p1, player.loc_p2

snakes = [
    Snake(23, 14),
    Snake(99, 77),
    Snake(65, 32),
    Snake(13, 9),
    Snake(85, 63),
    Snake(41, 20),
    Snake(30, 8),
    Snake(74, 59),
    ]

def snakes_init():
    global snakes
    for snake in snakes:
        snake_system(snake)