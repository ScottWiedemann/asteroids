import pygame
import random
from circleshape import CircleShape
from constants import (
    ASTEROID_EXPLOSION_LARGE,
    ASTEROID_EXPLOSION_MEDIUM,
    ASTEROID_EXPLOSION_SMALL,
    ASTEROID_MAX_RADIUS,
    ASTEROID_MIN_RADIUS,
)


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

        self.explosion_large = pygame.mixer.Sound(ASTEROID_EXPLOSION_LARGE)
        self.explosion_medium = pygame.mixer.Sound(ASTEROID_EXPLOSION_MEDIUM)
        self.explosion_small = pygame.mixer.Sound(ASTEROID_EXPLOSION_SMALL)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.play_sound()
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        random_angle = random.uniform(20, 50)
        new_velocity_1 = self.velocity.rotate(random_angle)
        new_velocity_2 = self.velocity.rotate(-random_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        asteroid_1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid_2 = Asteroid(self.position.x, self.position.y, new_radius)

        asteroid_1.velocity = new_velocity_1 * 1.2
        asteroid_2.velocity = new_velocity_2 * 1.2

    def play_sound(self):
        if self.radius == ASTEROID_MAX_RADIUS:
            self.explosion_large.play()

        elif self.radius == ASTEROID_MIN_RADIUS:
            self.explosion_small.play()

        else:
            self.explosion_medium.play()
