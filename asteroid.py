import pygame
import random
from circleshape import CircleShape
from logger import log_event
from constants import ASTEROID_MIN_RADIUS, LINE_WIDTH

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def update(self, dt):
        self.position += self.velocity * dt

    def draw(self, screen):
        pygame.draw.circle(screen, "white", (self.position), self.radius, LINE_WIDTH)

    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        log_event("asteroid_split")
        angle = random.uniform(20, 50)
        velocity1 = self.velocity.rotate(angle)
        velocity2 = self.velocity.rotate(-angle)
        radius = self.radius - ASTEROID_MIN_RADIUS

        asteroid1 = Asteroid(self.position.x, self.position.y, radius)
        asteroid2 = Asteroid(self.position.x, self.position.y, radius)

        asteroid1.velocity = velocity1 * 1.2
        asteroid2.velocity = velocity2 * 1.2

