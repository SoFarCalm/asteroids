from circleshape import *
from constants import *
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, 'purple', self.position, self.radius, 2)
    
    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            random_angle = random.uniform(0, 100)
            new_velocity_1 = self.velocity.rotate(random_angle)
            new_velocity_2 = self.velocity.rotate(-random_angle)
            old_radius = self.radius
            new_radius = old_radius - ASTEROID_MIN_RADIUS

            #Create first split asteroid
            asteroid_1 = Asteroid(self.position[0], self.position[1], new_radius)
            asteroid_1.velocity = new_velocity_1 * 1.2

            #Create second split asteroid 
            asteroid_2 = Asteroid(self.position[0], self.position[1], new_radius)
            asteroid_1.velocity = new_velocity_2 * 1.2
        
        