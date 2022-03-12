import pygame
from button import Button
from math import *


# Clock
clock = pygame.time.Clock()
fps = 250

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
dir = "pyton\projects\images\\"
run = True

# Images
pro_img = pygame.image.load(dir + "coin.png")
trace_img = pygame.image.load(dir + "play_sh\icons\\bullet.png")
button_img = pygame.image.load(dir + "menu.png")
ruller = pygame.image.load(dir + "ruller.png")
ruller1 = pygame.transform.rotate(ruller, 180)
ruller2 = pygame.transform.rotate(ruller, 90)

class Projectile(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.power = 7
        self.image = pro_img
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def update(self):
        global run
        #move proj -------------------------------------------------------------------

        self.rect.x += 1 #self.power*t
        
        self.rect.y = (((self.rect.x/10 - (9.8/2 + 20))**2) + (-self.power +6)*self.rect.x) # change equation

        if self.rect.y == screen_height:
            print(f"---------  {self.rect.x} is the max distance  -------") #at {-(self.rect.center[1]) + screen_height}")


        # stop running -------------------------------------------------------------------------
        # if some int stop
        if self.rect.y in range(int(screen_height+5), int(screen_height + 10)):
            run = False

        return run
        
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

projectile = Projectile(0, 0)
#button = Button(370, 600, button_img, 0.5)

# Groups
trace_group = pygame.sprite.Group()


running = True
while running:
    clock.tick(fps)
    screen.fill(BG)

    screen.blit(ruller2, (-40, 147))
    screen.blit(ruller2, (-40, 0))
    screen.blit(ruller1, (-1, screen_height - 15))
    screen.blit(ruller1, (325, screen_height - 15))

    trace_group.draw(screen)
    projectile.draw()
    if run:
        #print(projectile.rect.y)
        print(str(float(projectile.rect.center[0])) + ", " + str(-(projectile.rect.center[1]) + screen_height))
        projectile.update()
        trace = Trace(projectile.rect.center[0], projectile.rect.center[1])
        trace_group.add(trace)
        #print("hello")

    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    pygame.display.update()
pygame.quit()