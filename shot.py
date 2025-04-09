import pygame
from circleshape import *
from constants import *

class Shot(CircleShape):
    def __init__(self, x, y, player_rotation):
        super().__init__(x, y, SHOT_RADIUS)
        self.rotation = player_rotation
        self.velocity = pygame.Vector2(0, 1)

        
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.move(dt)
        
    def move(self, dt):
        #print("xx")
        orig_state = self.velocity.rotate(self.rotation)
        self.position += orig_state * PLAYER_SHOOT_SPEED * dt

    