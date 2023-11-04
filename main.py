import pygame
import random

pygame.init()

W = 400 # 800
H = 500 # 1000

screen = pygame.display.set_mode([W, H])
pygame.display.set_caption('2048')
timer = pygame.time.Clock()
fps = 60

font = pygame.font.Font('freesansbold.ttf', 24)

bg ={
    0:(204,192,179),
    2:(238,228,218),
    4:(237,224,200),
    8:(242,177,121),
    16:(245,149,99),
    32:(246,124,95),
    64:(246,94,59),
    128:(237,207,114),
    256:(237,204,97),
    512:(237,200,80),
    1024:(237,197,63),
    2048:(237,194,46),
    'light':(249,246,242),
    'dark':(119,110,101),
    'other':(204,192,179),
    'bg':(187,173,160),
    'back':(220,150,90)
}

def draw_board():
    """
    Draw the board on the screen using pygame.draw.rect() method
    """
    pygame.draw.rect(screen,bg['back'],[0,0,W,W],0,10)
    pass

def draw_pieces():
    pass




run=True

while run:
    timer.tick(fps)
    screen.fill('gray')
    draw_board()
    draw_pieces()


    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            run = False
    
    pygame.display.flip()

pygame.quit()