import pygame_menu, pygame, random, sys
from LoginSignup import *

#Khởi tạo các thứ
pygame.init()
pygame.display.set_caption("Race game")
clock = pygame.time.Clock()

#Âm thanh
VOLUME = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]
VOLUME_INDEX = 4

#Kích thước màn hình (Do chưa có pygame_menu nên tạm thời bỏ qua)
WINDOW_SIZES = [pygame.display.get_desktop_sizes()[0]]
WINDOW_SIZE_INDEX = 0
screen = pygame.display.set_mode(WINDOW_SIZES[WINDOW_SIZE_INDEX], pygame.RESIZABLE)

#Kiểu chữ
KieuChu1 = pygame.font.SysFont('arial', 20, bold=True)
KieuChu2 = pygame.font.SysFont('arial', 40, bold=True)

#Chữ các thứ
Player_money = 0
scoreBoard = KieuChu2.render(f"Money: {Player_money}", False, (0, 255, 255))
scoreBoard_Box = scoreBoard.get_rect(center = (screen.get_width() * 0.13, screen.get_height() * 0.92))

#Ảnh các loại
Background = pygame.image.load('assets/background/background.png').convert_alpha()

map1 = pygame.image.load('assets/background/map1.png').convert_alpha()
map1 = pygame.transform.smoothscale(map1, pygame.display.get_desktop_sizes()[0])
map2 = pygame.image.load('assets/background/map2.png').convert_alpha()
map2 = pygame.transform.smoothscale(map1, pygame.display.get_desktop_sizes()[0])
map3 = pygame.image.load('assets/background/map3.png').convert_alpha()
map3 = pygame.transform.smoothscale(map1, pygame.display.get_desktop_sizes()[0])
map4 = pygame.image.load('assets/background/map4.png').convert_alpha()
map4 = pygame.transform.smoothscale(map1, pygame.display.get_desktop_sizes()[0])
map5 = pygame.image.load('assets/background/map5.png').convert_alpha()
map5 = pygame.transform.smoothscale(map1, pygame.display.get_desktop_sizes()[0])
MAPS = [map1, map2, map3, map4, map5]
MAP_INDEX = 1

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

#Check điều kiện thắng (Cái này xài cho lucky box đi)
# def FinishLine_Pass(player, IG_Objects):
#     for IG_Object in IG_Objects:
#         if IG_Object.name == "FinishLine" and player.sprite.rect.x > IG_Object.rect.x:
#             player.sprite.run = False
#             return True
#     return False

def FinishLine_Pass(player):
    if player.sprite.rect.x > screen.get_width() * 0.98:
        player.sprite.run = False
        return True
    return False

#Class trò chơi dùng để hiển thị menu, check keys các thứ (Đang làm chưa xài)
# class Main():
#     #Khởi tao + các biến sử dụng trong class
#     global login_lock, Victory_sound_Play, screen
#     def __init__(self):
#         pygame.init()
#         self.Running = True
#         self.Play = True
#         self.ESC = False

#     def loop(self):
#         while self.Running:
#             self.check_events()
#             if self.Play:
#                 self.Playing()
#             if self.ESC:
#                 self.Pause()
#             pygame.display.update()
#             clock.tick(60)
#         pygame.quit()
            
#     #Kiểm tra điều kiện
#     def check_events(self):
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 self.Running = False
#             if event.type == pygame.KEYDOWN:
#                 if event.key == pygame.K_ESCAPE:
#                     self.ESC = True

#             Resize cửa sổ nếu cần
#             if event.type == pygame.VIDEORESIZE:
#                 screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
#                 WINDOW_SIZE_INDEX = 1
            
#             Code để tìm vị trí cụ thể trên màn hình
#             if event.type == pygame.MOUSEMOTION:
#                 print(event.pos)
    
                    


