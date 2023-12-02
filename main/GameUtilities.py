import sys, pygame, random
import pygame_menu
from LoginSignup import *

#Khởi tạo các thứ
pygame.init()
pygame.display.set_caption("Race game")
clock = pygame.time.Clock()

#Kích thước màn hình (Do chưa có pygame_menu nên tạm thời bỏ qua)
WINDOW_SIZES = [(800, 500), (1920, 1080)]
WINDOW_SIZE_INDEX = 0
screen = pygame.display.set_mode(WINDOW_SIZES[WINDOW_SIZE_INDEX], pygame.RESIZABLE)

#Kiểu chữ
KieuChu1 = pygame.font.SysFont('arial', 20, bold=True)
KieuChu2 = pygame.font.SysFont('arial', 40, bold=True)


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

#Các nhân vật trong game
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
        self.rect= self.image.get_rect(midbottom = (x, y))
        self.count_run = 0
    def animation(self):
        #Vẽ nhân vật
        MAP = MAPS[MAP_INDEX]
        if self.count_run >= 3:
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

Char1 = pygame.sprite.GroupSingle()
Char1.add(player(Speed[0], WINDOW_SIZES[WINDOW_SIZE_INDEX][0] * 0.1, WINDOW_SIZES[WINDOW_SIZE_INDEX][1] * 0.3, 0, CharsMap1[0][0]))
# Char2 = pygame.sprite.GroupSingle()
# Char2.add(player(Speed[1], WINDOW_SIZES[WINDOW_SIZE_INDEX][0] * 0.1, WINDOW_SIZES[WINDOW_SIZE_INDEX][1] * 0.45, 1, CharsMap1[0][0]))
# Char3 = pygame.sprite.GroupSingle()
# Char3.add(player(Speed[1], WINDOW_SIZES[WINDOW_SIZE_INDEX][0] * 0.1, WINDOW_SIZES[WINDOW_SIZE_INDEX][1] * 0.6, 2, CharsMap1[0][0]))
# Char4 = pygame.sprite.GroupSingle()
# Char4.add(player(Speed[1], WINDOW_SIZES[WINDOW_SIZE_INDEX][0] * 0.1, WINDOW_SIZES[WINDOW_SIZE_INDEX][1] * 0.75, 3, CharsMap1[0][0]))
# Char5 = pygame.sprite.GroupSingle()
# Char5.add(player(Speed[1], WINDOW_SIZES[WINDOW_SIZE_INDEX][0] * 0.1, WINDOW_SIZES[WINDOW_SIZE_INDEX][1] * 0.9, 4, CharsMap1[0][0]))

#Các đối tượng trong game
class IG_Object(pygame.sprite.Sprite):
    def __init__(self, name, x, y, image):
        super().__init__()
        self.x = x
        self.y = y
        self.name = name
        if self.name == "FinishLine":
            self.pic= pygame.image.load(image).convert_alpha()
        elif self.name == "ChuChay":
            self.pic = KieuChu1.render("THIS IS GROUP 12'S AMAZING RACE GAME!!!", False, (255, 102, 0))
        self.image = self.pic
        self.rect= self.image.get_rect(topleft = (x, y))
    def move(self):
        self.rect.x -= 2
        if self.rect.right <= 0:
            self.rect.x = WINDOW_SIZES[WINDOW_SIZE_INDEX][0]
            self.kill()
    def update(self):
        if self.name == "ChuChay":
            self.move()

IG_Objects = pygame.sprite.Group()
IG_Objects.add(IG_Object('FinishLine', WINDOW_SIZES[WINDOW_SIZE_INDEX][0] * 0.9, 0, 'assets/terrains/FinishLine.png'))
IG_Objects.add(IG_Object('ChuChay', WINDOW_SIZES[WINDOW_SIZE_INDEX][0], 0, 'None'))

def FinishLine_Pass(player, IG_Objects):
    for IG_Object in IG_Objects:
        if IG_Object.name == "FinishLine" and pygame.sprite.spritecollide(player.sprite, IG_Objects, False):
            player.run = False
            return True
    return False