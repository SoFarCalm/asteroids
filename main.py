import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
import sys

def main():
    pygame.init()

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    updateable = pygame.sprite.Group() 
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updateable, drawable)
    Shot.containers = (shots, drawable, updateable)
    Asteroid.containers = (updateable, drawable, asteroids)
    AsteroidField.containers = (updateable)
    player = Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()
    clock = pygame.time.Clock()
    dt = 0

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        updateable.update(dt)

        for asteroid in asteroids:
            if asteroid.check_collision(player):
                print("Game Over!!!")
                sys.exit()
        
        for asteroid in asteroids:
            for shot in shots:
                if asteroid.check_collision(shot):
                    asteroid.split()
                    shot.kill()

        screen.fill('black')

        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()

        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()