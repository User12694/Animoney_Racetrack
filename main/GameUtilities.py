from GameInit import *

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
    def __init__(self, speed, pos, number, image):
        super().__init__()
        self.speed = speed
        self.x = pos[0]
        self.y = pos[1]
        self.number = number
        self.run = True
        self.count_run = 0
        self.image= pygame.image.load(image).convert_alpha()
        self.rect= self.image.get_rect(midbottom = (self.x, self.y))
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
            self.rect.x += self.speed

    def update(self):
        self.animation()
        self.move()

Char1 = pygame.sprite.GroupSingle()
Char1.add(player(speed = Speed[0], pos = (screen.get_width() * 0.1, screen.get_height() * 0.3), number = 0, image = CharsMap1[0][0]))
# Char2 = pygame.sprite.GroupSingle()
# Char2.add(player(speed = Speed[1], pos = (screen.get_width() * 0.1, screen.get_height() * 0.45), number = 1, image = CharsMap1[0][0]))
# Char3 = pygame.sprite.GroupSingle()
# Char3.add(player(speed = Speed[1], pos = (screen.get_width() * 0.1, screen.get_height() * 0.6), number = 2, image = CharsMap1[0][0]))
# Char4 = pygame.sprite.GroupSingle()
# Char4.add(player(speed = Speed[1], pos = (screen.get_width() * 0.1, screen.get_height() * 0.75), number = 3, image = CharsMap1[0][0]))
# Char5 = pygame.sprite.GroupSingle()
# Char5.add(player(speed = Speed[1], pos = (screen.get_width() * 0.1, screen.get_height() * 0.9), number = 4, image = CharsMap1[0][0]))

#Các đối tượng trong game
class IG_Object(pygame.sprite.Sprite):
    def __init__(self, name, pos, image):
        super().__init__()
        self.x = pos[0]
        self.y = pos[1]
        self.name = name
        if self.name == "FinishLine":
            self.pic= pygame.image.load(image).convert_alpha()
        elif self.name == "ChuChay":
            self.pic = KieuChu1.render("THIS IS GROUP 12'S AMAZING RACE GAME!!!", False, (255, 102, 0))
        self.image = self.pic
        self.rect= self.image.get_rect(topleft = (self.x, self.y))
    def move(self):
        if self.name == "ChuChay":
            self.rect.x -= 2
            if self.rect.right <= 0:
                self.rect.x = WINDOW_SIZES[WINDOW_SIZE_INDEX][0]
    def update(self):
        if self.name == "ChuChay":
            self.move()

IG_Objects = pygame.sprite.Group()
IG_Objects.add(IG_Object(name = 'FinishLine', pos = (WINDOW_SIZES[WINDOW_SIZE_INDEX][0] * 0.9, 0), image = 'assets/terrains/FinishLine.png'))
IG_Objects.add(IG_Object( name = 'ChuChay', pos = (WINDOW_SIZES[WINDOW_SIZE_INDEX][0], 0), image = 'None'))

#Check điều kiện thắng
def FinishLine_Pass(player, IG_Objects):
    for IG_Object in IG_Objects:
        if IG_Object.name == "FinishLine" and player.sprite.rect.x > IG_Object.rect.x:
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
    
                    


