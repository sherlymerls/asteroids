import pygame
from circleshape import *
from constants import *
from shot import *

class Player(CircleShape):
    def __init__(self, x, y):
        
        self.pos_x = x
        self.pos_y = y
        super().__init__(self.pos_x, self.pos_y, PLAYER_RADIUS)
        self.rotation = 0
        self.fire_cooldown_timer = 0

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)

    def rotate(self, dt):
        self.rotation += dt * PLAYER_TURN_SPEED

    def update(self, dt):
        self.fire_cooldown_timer -= dt
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(dt * -1)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(dt * -1)
        if keys[pygame.K_SPACE]:
            self.shoot()

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self):
        if self.fire_cooldown_timer <= 0: 
            new_shot = Shot(self.position[0], self.position[1], self.rotation)
            self.fire_cooldown_timer = 0.3
        else:
            pass
        


#print(PLAYER_RADIUS)