import pygame
from circleshape import *
import random
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        ran_rad = random.uniform(20, 50)
        ran_angle1 = self.velocity.rotate(ran_rad)
        ran_angle2 = self.velocity.rotate(-ran_rad)
        new_rad = self.radius - ASTEROID_MIN_RADIUS
        new_ast1 = Asteroid(self.position.x, self.position.y, new_rad)
        new_ast1.velocity = ran_angle1 * 1.2
        new_ast2 = Asteroid(self.position.x, self.position.y, new_rad)
        new_ast2.velocity = ran_angle2 * 1.2

        