import sys, pygame, random
import pygame_menu
from LoginSignup import *

#Kích thước màn hình (Do chưa có pygame_menu nên tạm thời bỏ qua)
WINDOW_SIZES = [(1920, 1080)]
WINDOW_SIZE_INDEX = 0

#Khởi tạo các thứ
pygame.init()
screen = pygame.display.set_mode(WINDOW_SIZES[WINDOW_SIZE_INDEX])
pygame.display.set_caption("Race game")
clock = pygame.time.Clock()

#Chọn map
MAPS = [0, 1, 2, 3, 4]
MAP_INDEX = 0
MAP = MAPS[MAP_INDEX]

#Các ảnh cần dùng đến
#1. Nhân vật (Đặt tên theo dạng Char#Map#_#)
Char1Map1 = ['assets/characters/Char1Map1_1.png', 'assets/characters/Char1Map1_2.png',
            'assets/characters/Char1Map1_3.png', 'assets/characters/Char1Map1_4.png']
# Char2Map1 = ['assets/characters/Char2Map1_1.png', 'assets/characters/Char2Map_2.png',
#             'assets/characters/Char2Map1_3.png', 'assets/characters/Char2Map1_4.png']
# Char3Map1 = ['assets/characters/Char3Map1_1.png', 'assets/characters/Char3Map_2.png',
#             'assets/characters/Char3Map1_3.png', 'assets/characters/Char3Map1_4.png']
# Char4Map1 = ['assets/characters/Char4Map1_1.png', 'assets/characters/Char4Map_2.png',
#             'assets/characters/Char4Map1_3.png', 'assets/characters/Char4Map1_4.png']
# Char5Map1 = ['assets/characters/Char5Map1_1.png', 'assets/characters/Char5Map_2.png',
#             'assets/characters/Char5Map1_3.png', pygame.image.load('assets/characters/Char5Map1_4.png']

#Nhân vật
CharsMap1 = [Char1Map1]
Speed = [2, 2, 2, 2, 2]
Char1_Run = True
Char2_Run = True
Char3_Run = True
Char4_Run = True
Char5_Run = True

#Các class
class player:
    def __init__(self, speed, x, y, number, run, image):
        self.speed = speed
        self.x = x
        self.y = y
        self.number = number
        self.run = run
        self.count_run = 0
        self.image= pygame.image.load(image)
        self.rect= self.image.get_rect(center = (x, y))
        self.count_run = 0
    def draw(self):
        MAP = MAPS[MAP_INDEX]
        if self.count_run > 3:
            self.walkCount = 0
        if MAP == 1:
            if self.number == 1:
                if self.run:
                    screen.blit(CharsMap1[0][self.count_run % 4], (self.x, self.y))
                    self.count_run += 1

                else:
                    screen.blit(CharsMap1[0][0], (self.x, self.y))
    #         if self.number == 2:
    #             if self.run:
    #                 screen.blit(Char2Map1[self.count_run % 3], (self.x, self.y))
    #                 self.count_run += 1
    #             else:
    #                 screen.blit(Char2Map1[0], (self.x, self.y))
    #         if self.number == 3:
    #             if self.run:
    #                 screen.blit(Char3Map1[self.count_run % 3], (self.x, self.y))
    #                 self.count_run += 1
    #             else:
    #                 screen.blit(Char3Map1[0], (self.x, self.y))
    #         if self.number == 4:
    #             if self.run:
    #                 screen.blit(Char4Map1[self.count_run % 3], (self.x, self.y))
    #                 self.count_run += 1
    #             else:
    #                 screen.blit(Char4Map1[0], (self.x, self.y))
    #         if self.number == 5:
    #             if self.run:
    #                 screen.blit(Char5Map1[self.count_run % 3], (self.x, self.y))
    #                 self.count_run += 1
    #             else:
    #                 screen.blit(Char5Map1[0], (self.x, self.y))