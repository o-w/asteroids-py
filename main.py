import pygame
from pygame.locals import *

from asteroidfield import AsteroidField
from constants import *
from circleshape import *
from asteroid import *
from player import *

def main():

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock_fps = pygame.time.Clock()

    my_group_updateable = pygame.sprite.Group()
    my_group_drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    Player.containers = (my_group_updateable, my_group_drawable)
    Asteroid.containers = (my_group_updateable, my_group_drawable, asteroids)
    AsteroidField.containers = (my_group_updateable)
    AsteroidField()

    player = Player(SCREEN_WIDTH/2 , SCREEN_HEIGHT/2)

    #ast1 = Asteroid(SCREEN_WIDTH/2 , SCREEN_HEIGHT/2, )

    dt = 0

    #my_group_updateable.add(player)
    #my_group_drawable.add(player)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True

        for hitsmack in asteroids:
            if Asteroid.collides_with(hitsmack, player):
                print("Collision!")
                exit()

        my_group_updateable.update(dt)

        screen.fill(0)

        for each in my_group_drawable:
            each.draw(screen)
        pygame.display.flip()
        dt = (clock_fps.tick(60) / 1000)


if __name__ == "__main__":
    main()
