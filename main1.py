import pygame
from pygame.locals import *

success, fails = pygame.init()
print(f"success: {success}, fails: {fails}")

# define fps and clock
clock = pygame.time.Clock()
fps = 60

# define colors
red = (255, 0, 0)
green = (0, 255, 0)

# SCREEN 
screen_width = 600
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))

# set title for the game
pygame.display.set_caption("Space Invaders || Yossef")

# load images
bg = pygame.image.load("img/bg.png")

class Spaceship(pygame.sprite.Sprite):
    def __init__(self, x, y, health):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("img/spaceship.png")
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        self.health_start = health
        self.health_remaining = health


    def update(self):
        speed = 8
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= speed
        if keys[pygame.K_RIGHT] and self.rect.right < screen_width:
            self.rect.x += speed

        # draw health bar 
        pygame.draw.rect(screen, red, (self.rect.x, (self.rect.bottom + 10), self.rect.width, 15))
        if self.health_remaining > 0:
            pygame.draw.rect(screen, green, (self.rect.x, (self.rect.bottom + 10), int(self.rect.width * (self.health_remaining / self.health_start)), 15))


# make group for all spaceships
spaceship_group = pygame.sprite.Group()

# create player 
spaceship = Spaceship(int(screen_width / 2), (screen_height - 100), 3)
spaceship_group.add(spaceship)

def draw_bg():
    screen.blit(bg, (0, 0))

run = True
while run:
    # for the frame in second for the game
    clock.tick(fps)
    
    draw_bg()
    # event handlers
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    spaceship.update()
    # draw spaceship
    spaceship_group.draw(screen)
    
    pygame.display.update()

pygame.quit()
