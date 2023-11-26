import sys, pygame, random

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Race game")
clock = pygame.time.Clock()

Background = pygame.image.load('assets/background/background(800x600).png')
#Đây là main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.blit(Background,(0,0))
    pygame.display.update()
    clock.tick(60)