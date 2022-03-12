import pygame
from button import Button
from math import *


# Clock
clock = pygame.time.Clock()
fps = 10

# screen variables
BG = (0, 0, 89)
screen_width = 800
screen_height = screen_width * 0.8

screen = pygame.display.set_mode((screen_width, screen_height), pygame.RESIZABLE)
pygame.display.set_caption('Bred Fixe Platformer')

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Global Variables
t = -5

# Images
pro_img = pygame.image.load("projects/images/coin.png")
trace_img = pygame.image.load("projects/images/play_sh/icons/bullet.png")
button_img = pygame.image.load("projects/images/menu.png")

class Projectile(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.speed = 60
        self.z = 5
        self.image = pro_img
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def update(self):
        global t
        #move bullet

        self.rect.x = self.speed*t + 100 #self.speed*t
        
        self.rect.y = screen_height - (self.speed*t - (9.8/2)*t**2 + 100)

        t += 0.5

        #check if bullet has gone off screen
        if self.rect.right < 0 or self.rect.left > screen_width:
            self.z = 0
        # if some int stop
        if self.rect.y == 500:
            self.z = 0
        return t
        
    def draw(self):
        screen.blit(self.image, self.rect)
        #pygame.draw.rect(screen, (255, 255, 255), self.rect, 1)

class Trace(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = trace_img
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def draw(self):
        screen.blit(self.image, self.rect)

projectile = Projectile(0, screen_width)
button = Button(370, 600, button_img, 0.5)

# Groups
trace_group = pygame.sprite.Group()


running = True
while running:
    clock.tick(fps)
    screen.fill(BG)

    print(str(projectile.rect.x) + ", " + str(-(projectile.rect.y) + screen_height))

    trace_group.draw(screen)
    projectile.draw()
    
    #if button.draw(screen):
    projectile.update()
    trace = Trace(projectile.rect.x, projectile.rect.y)
    trace_group.add(trace)
    #print("hello")
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    pygame.display.update()
pygame.quit()