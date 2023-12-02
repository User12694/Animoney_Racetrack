import sys, pygame, random
import pygame_menu
from LoginSignup import *

#Kích thước màn hình (Do chưa có pygame_menu nên tạm thời bỏ qua)
WINDOW_SIZES = [(1920, 1080)]
WINDOW_SIZE_INDEX = 0

#Khởi tạo các thứ
pygame.init()
screen = pygame.display.set_mode(WINDOW_SIZES[WINDOW_SIZE_INDEX], pygame.RESIZABLE)
pygame.display.set_caption("Race game")
clock = pygame.time.Clock()

#Chọn map
MAPS = [0, 1, 2, 3, 4]
MAP_INDEX = 0

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

#Các class
class player(pygame.sprite.Sprite):
    def __init__(self, speed, x, y, number, image):
        super().__init__()
        self.speed = speed
        self.x = x
        self.y = y
        self.number = number
        self.run = True
        self.count_run = 0
        self.image= pygame.image.load(image).convert_alpha()
        self.rect= self.image.get_rect(bottom = (x, y))
        self.count_run = 0
    def animation(self):
        #Vẽ nhân vật
        MAP = MAPS[MAP_INDEX]
        if self.count_run >= len(CharsMap1[0][self.number]):
            self.count_run = 0
        if MAP == 0:
            if self.number == 0:
                if self.run:
                    self.image = pygame.image.load(CharsMap1[0][int(self.count_run)]).convert_alpha()
                    self.count_run += 0.1
                else:
                    self.image = pygame.image.load(CharsMap1[0][int(self.count_run)]).convert_alpha()
            # if self.number == 1:
            #     if self.run:
            #         self.image = pygame.image.load(CharsMap2[0][int(self.count_run)]).convert_alpha()
            #         self.count_run += 0.1
            #     else:
            #         self.image = pygame.image.load(CharsMap2[0][int(self.count_run)]).convert_alpha()
            # if self.number == 2:
            #     if self.run:
            #         self.image = pygame.image.load(CharsMap3[0][int(self.count_run)]).convert_alpha()
            #         self.count_run += 0.1
            #     else:
            #         self.image = pygame.image.load(CharsMap3[0][int(self.count_run)]).convert_alpha()
            # if self.number == 3:
            #     if self.run:
            #         self.image = pygame.image.load(CharsMap4[0][int(self.count_run)]).convert_alpha()
            #         self.count_run += 0.1
            #     else:
            #         self.image = pygame.image.load(CharsMap4[0][int(self.count_run)]).convert_alpha()
            # if self.number == 4:
            #     if self.run:
            #         self.image = pygame.image.load(CharsMap5[0][int(self.count_run)]).convert_alpha()
            #         self.count_run += 0.1
            #     else:
            #         self.image = pygame.image.load(CharsMap5[0][int(self.count_run)]).convert_alpha()

    def move(self):
        if self.run:
            self.x += self.speed

    def update(self):
        self.animation()
        self.move()

class object(pygame.sprite.Sprite):
    def __init__(self, name, x, y, image):
        super().__init__()
        self.x = x
        self.y = y
        if self.name == "FinishLine":
            self.image = self.image= pygame.image.load(image).convert_alpha()
            self.rect= self.image.get_rect(topleft = (x, y))

Char1 = pygame.sprite.GroupSingle()
Char1.add(player(Speed[0], WINDOW_SIZES[WINDOW_SIZE_INDEX][0] * 0.1, WINDOW_SIZES[WINDOW_SIZE_INDEX][1] * 0.5, 1, CharsMap1[0][0]))
# Char2 = pygame.sprite.GroupSingle()
# Char2.add(player(Speed[1], WINDOW_SIZES[WINDOW_SIZE_INDEX][0] * 0.1, WINDOW_SIZES[WINDOW_SIZE_INDEX][1] * 0.6, 2, CharsMap1[0][0]))
# Char3 = pygame.sprite.GroupSingle()
# Char3.add(player(Speed[1], WINDOW_SIZES[WINDOW_SIZE_INDEX][0] * 0.1, WINDOW_SIZES[WINDOW_SIZE_INDEX][1] * 0.6, 3, CharsMap1[0][0]))
# Char4 = pygame.sprite.GroupSingle()
# Char4.add(player(Speed[1], WINDOW_SIZES[WINDOW_SIZE_INDEX][0] * 0.1, WINDOW_SIZES[WINDOW_SIZE_INDEX][1] * 0.6, 4, CharsMap1[0][0]))
# Char5 = pygame.sprite.GroupSingle()
# Char5.add(player(Speed[1], WINDOW_SIZES[WINDOW_SIZE_INDEX][0] * 0.1, WINDOW_SIZES[WINDOW_SIZE_INDEX][1] * 0.6, 5, CharsMap1[0][0]))

object_group = pygame.sprite.Group()
object_group.add(object('FinishLine', WINDOW_SIZES[WINDOW_SIZE_INDEX][0] * 0.1, WINDOW_SIZES[WINDOW_SIZE_INDEX][1] * 0.5, 'assets/terrains/FinishLine.png'))