import pygame

Game_resolution = (600, 460)
use_gamepad = True

pygame.init()
pygame.display.set_caption("Psychic Fighters")

pygame.font.init()

if (use_gamepad):
    pygame.joystick.init()

    if (pygame.joystick.get_count() == 0):
        use_gamepad = False
    else:
        current_joystick = pygame.joystick.Joystick(0)
        current_joystick.init()

#use_gamepad = False
screen = pygame.display.set_mode(Game_resolution)

font = pygame.font.Font(None, 20)
background = pygame.image.load("stage/arena.png").convert()

NUMBERS_OF_ROUNDS = 4
ROUND_TIME = 15
