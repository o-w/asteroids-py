import pygame
from pygame.locals import *

import asteroidfield
from asteroidfield import AsteroidField
from constants import *
from circleshape import *
from asteroid import *
from player import *
from shot import *

def main():

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock_fps = pygame.time.Clock()

    my_group_updateable = pygame.sprite.Group()
    my_group_drawable = pygame.sprite.Group()
    my_group_shots = pygame.sprite.Group()
    my_group_asteroids = pygame.sprite.Group()

    Player.containers = (my_group_updateable, my_group_drawable)
    Asteroid.containers = (my_group_updateable, my_group_drawable, my_group_asteroids)
    Shot.containers = (my_group_updateable, my_group_drawable, my_group_shots)

    AsteroidField.containers = (my_group_updateable,)
    AsteroidField()

    player = Player(SCREEN_WIDTH/2 , SCREEN_HEIGHT/2)

    dt = 0

    #my_group_updateable.add(player)
    #my_group_drawable.add(player)

    while True:
        my_group_updateable.update(dt)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True

        for asteroid_smacked in my_group_asteroids:
            if Asteroid.collides_with(asteroid_smacked, player):
                print("Player collision!")
                exit()

            for shot_smacked in my_group_shots:
                 if asteroid_smacked.collides_with(shot_smacked):
                    shot_smacked.kill()
                    asteroid_smacked.split()



        player.cooldown_timer -= dt
        screen.fill(0)

        for each in my_group_drawable:
            each.draw(screen)
        pygame.display.flip()
        dt = (clock_fps.tick(60) / 1000)

if __name__ == "__main__":
    main()
