import pygame
from circleshape import *
from constants import ASTEROID_MIN_RADIUS
import random


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            new_asteroid_launch_angle = random.uniform(20, 50)
            new_asteroid_radius = self.radius / 2
            new_asteroid_velocity = self.velocity.rotate(new_asteroid_launch_angle)
            new_asteroid_velocity2 = new_asteroid_velocity.rotate(-new_asteroid_launch_angle)

            new_asteroid1 = Asteroid(
                self.position.x, self.position.y, new_asteroid_radius
            )

            new_asteroid2 = Asteroid(
                self.position.x, self.position.y, new_asteroid_radius
            )

            new_asteroid1.velocity = new_asteroid_velocity
            new_asteroid2.velocity = new_asteroid_velocity2

