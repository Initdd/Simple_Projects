import pygame
import numpy as np
import math
import button

pygame.init()
clock = pygame.time.Clock()
fps = 20

# screen
BG = (0, 0, 89)
screen_width = 800
screen_height = screen_width * 0.8
screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
pygame.display.set_caption('Graph')

# images
pro_img = pygame.image.load("images/projectile.png")
trace_img = pygame.image.load("images/trace.png")
start = pygame.image.load("images/start.png")


# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 150)
GREY = (128, 128, 128)
color = GREY

# fonts
font1 = pygame.font.Font(None, 30)

# global variables
run = False
layer = 1
i = 0
speed = 100
angle = 45
x = []
y = []

for time in np.arange(0, 500, 0.5):
    xitem = speed*time*math.cos(math.radians(angle))
    yitem = screen_height - (speed*time*math.sin(math.radians(angle)) - (9.8/2)*time**2)
    if yitem < screen_height+0.01:
        x.append(xitem)
        y.append(yitem)


class Trace(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = trace_img
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def draw(self):
        screen.blit(self.image, self.rect)

# Groups
trace_group = pygame.sprite.Group()

# text
textx = -100
speed_render = font1.render(f"Speed: {speed}", 1, WHITE)
angle_render = font1.render(f"Angle: {angle}", 1, WHITE)
max_width = font1.render(f"Max Width: {max(x)}", 1, WHITE)
max_heigth = font1.render(f"Max Height: {min(y)}", 1, WHITE)

# buttons
but1 = button.Button(screen_width//2, screen_height//2, start, 1)

while True:
    clock.tick(fps)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                pygame.quit()
                exit()

    screen.fill(BLACK)

    pygame.draw.line(screen, WHITE, (0, screen_height), (screen_width + 1000, screen_height), 1)
    if layer == 1:
        if but1.draw(screen):
            layer = 2

    if layer == 2:

        trace_group.draw(screen)

        # plot
        tuplo = [x[i], y[i]]
        #print(tuplo)
        screen.blit(pro_img, tuplo)
        trace = Trace(tuplo[0], tuplo[1])
        trace_group.add(trace)
        if i != len(x) - 1:
            i += 1
        else:
            i = len(x) - 1

        # text pos
        current_pos = font1.render(f"Position: {tuplo[0]}, {tuplo[1]}", 1, WHITE)
        
        # text
        screen.blit(speed_render, (screen_width+textx, 50))
        screen.blit(angle_render, (screen_width+textx, 100))
        screen.blit(max_width, (screen_width+textx, 150))
        screen.blit(max_heigth, (screen_width+textx, 200))
        screen.blit(current_pos, (screen_width+textx, 250))
    
    
    pygame.display.update()