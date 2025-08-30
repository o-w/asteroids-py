# this allows us to use code from
# the open-source pygame library
# throughout this file

import pygame
from pygame.locals import *
from constants import *

def main():

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()

    if pygame.get_init:
        print("Game on. Pygame initialized.")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    screen.fill(0)
    pygame.display.flip()
    clock_fps = pygame.time.Clock()
    dt = 0

    while True:
        for event in pygame.event.get():         #check if window is closed, stop if it is
            if event.type == pygame.QUIT:
                dt = (clock_fps.tick(60) / 1000)        # screen refresh to 60hz
                return



if __name__ == "__main__":
    main()
