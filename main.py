import pygame, board, dice, button, snake, ladder, ladder_draw, snake_draw, player
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

# Lebar dan tinggi window
viewport_width = 1280
viewport_height = 720

# Faktor konversi pixel per unit
aspect_ratio = viewport_width / viewport_height
pixel_per_unit = viewport_width / (2 * 10 * aspect_ratio)

def reset_game():
    player.loc_p1 = 1
    player.loc_p2 = 1
    player.current_player = 1
    dice.number_dice = 1
    button.win = False

def main():
    pygame.init()
    display = (1280, 720)
    pygame.display.set_mode(display, pygame.DOUBLEBUF | pygame.OPENGL)

    glViewport(0, 0, 1280, 720)  # Sesuaikan dengan ukuran layar Anda
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    aspect_ratio = 1280 / 720  # Sesuaikan dengan ukuran layar Anda
    glOrtho(-10 * aspect_ratio, 10 * aspect_ratio, -10, 10, -1, 1)
    glMatrixMode(GL_MODELVIEW)

    glutInit()
    # gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
    glTranslatef(0, 0, -1)

    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if not button.win:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        mouse_pos = pygame.mouse.get_pos()
                        print(f"Mouse clicked at position: {mouse_pos}")
                        if 1007 <= event.pos[0] <= 1065 and 381 <= event.pos[1] <= 409:
                            dice.update_scene()
            
            if button.win:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        mouse_pos = pygame.mouse.get_pos()
                        print(f"Mouse clicked at position: {mouse_pos}")
                        if 604 <= event.pos[0] <= 674 and 345 <= event.pos[1] <= 372:
                            reset_game()

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        board.draw_grid()
        player.draw_current_player()
        dice.dice_draw()
        snake.snakes_init()
        snake_draw.draw_snakes()
        ladder.ladder_init()
        ladder_draw.draw_ladders()
        player.draw_grid()
        button.btn()
        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()