import pygame
import sys

pygame.init()
clock = pygame.time.Clock()
fps = 6

# screen
BG = (0, 0, 89)
screen_width = 800
screen_height = screen_width * 0.8

screen = pygame.display.set_mode((screen_width, screen_height), pygame.RESIZABLE)
pygame.display.set_caption('Graph')

pro_img = pygame.image.load("pyton/projects/images/coin.png")
button_img = pygame.image.load("pyton/projects/images/menu.png")


# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 150)
GREY = (128, 128, 128)
color = GREY

# global variables
i = 0
speed = 0
x = []
y = []
font = pygame.font.Font(None, 25)
font2 = pygame.font.Font(None, 30)
text_rect = pygame.Rect(75, 550, 140, 25)
text = ""
active_color = False
speed_txt = font2.render("speed: ", True, WHITE)

for t in range(0, 500):
    x.append(speed*t + speed*2)
    y.append(screen_height - (speed*t - (9.8/2)*t**2 + 500))



while True:
    clock.tick(fps)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if text_rect.collidepoint(event.pos):
                active_color = True
            else:
                active_color = False
        if event.type == pygame.KEYDOWN:
            if active_color == True:
                if event.key == pygame.K_BACKSPACE:
                    text = text[:-1]
                elif event.key == pygame.K_p:
                    print(text)
                else:
                    text += event.unicode
    # screen
    screen.fill(BLACK)

    # color
    if active_color:
        color = WHITE
    else:
        color = GREY

    # plot
    tuplo = [x[i], y[i]]
    screen.blit(pro_img, tuplo)
    if i != len(x) - 1:
        i += 1
    else:
        i = len(x) - 1
    """for i in range(len(x)):
        tuplo = [x[i], y[i]]
        screen.blit(pro_img, tuplo)"""
    
    # blue rectagle
    pygame.draw.rect(screen, BLUE, pygame.Rect(0, (screen_height - 120), screen_width, screen_height))

    # text input
    screen.blit(speed_txt, (10, 555))
    pygame.draw.rect(screen, color, text_rect, 2)
    text_surface = font.render(text, True, WHITE)
    screen.blit(text_surface, (text_rect.x + 5, text_rect.y + 5))
    text_rect.w = max(50, text_surface.get_width() + 10)

    pygame.display.update()