import pygame
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, radius=self.radius, width=2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius < ASTEROID_MIN_RADIUS:
            return
        else:
            shear_angle = random.uniform(20, 50)
            first_child = self.velocity.rotate(shear_angle)
            second_child = self.velocity.rotate(-shear_angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            first_asteroid = Asteroid(self.position[0], self.position[1], new_radius)
            second_asteroid = Asteroid(self.position[0], self.position[1], new_radius)
            first_asteroid.velocity = first_child * 1.2
            second_asteroid.velocity = second_child * 1.2
