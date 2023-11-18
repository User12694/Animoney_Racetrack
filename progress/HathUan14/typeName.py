from sys import exit
import pygame
import time


pygame.init()
screen = pygame.display.set_mode((800, 400))

name_text = '<Type your name here>'
font = pygame.font.SysFont(None, 48)
name_textbox = font.render(name_text, True, 'Red')
name_textboxRect = name_textbox.get_rect()
name_textboxRect.topleft = (20, 20)
cursor = pygame.Rect(name_textboxRect.topright, (3, name_textboxRect.height))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                if len(name_text)>0:
                    name_text = name_text[:-1]
            else:
                name_text += event.unicode
            name_textbox = font.render(name_text, True, 'Red')
            name_textboxRect.size=name_textbox.get_size()
            cursor.topleft = name_textboxRect.topright


    screen.fill('Gray')
    screen.blit(name_textbox, name_textboxRect)
    if time.time() % 1 > 0.5:
        pygame.draw.rect(screen, 'Red', cursor)



    pygame.display.update()
    pygame.time.Clock().tick(60)