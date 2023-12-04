import pygame_menu, pygame, random, sys
from LoginSignup import *
#Khởi tạo các thứ
pygame.init()
pygame.display.set_caption("Race game")
clock = pygame.time.Clock()

#Màn hình cài đặt âm lượng
VOLUME = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]
VOLUME_INDEX = 4
present_volume = VOLUME[VOLUME_INDEX]

#Kích thước màn hình (Do chưa có pygame_menu nên tạm thời bỏ qua)
WINDOW_SIZES = [pygame.display.get_desktop_sizes()[0]]
WINDOW_SIZE_INDEX = 0
screen = pygame.display.set_mode(WINDOW_SIZES[WINDOW_SIZE_INDEX], pygame.RESIZABLE)

#Kiểu chữ
KieuChu1 = pygame.font.SysFont('./assets/font/SVN-Retron_2000.ttf',60)
KieuChu2 = pygame.font.SysFont('./assets/font/FVF Fernando 08',60)

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
Char2Map1 = ['assets/characters/Char2Map1_1.png', 'assets/characters/Char2Map1_2.png',
            'assets/characters/Char2Map1_3.png', 'assets/characters/Char2Map1_4.png']
Char3Map1 = ['assets/characters/Char3Map1_1.png', 'assets/characters/Char3Map1_2.png',
            'assets/characters/Char3Map1_3.png', 'assets/characters/Char3Map1_4.png']
Char4Map1 = ['assets/characters/Char4Map1_1.png', 'assets/characters/Char4Map1_2.png',
            'assets/characters/Char4Map1_3.png', 'assets/characters/Char4Map1_4.png']
Char5Map1 = ['assets/characters/Char5Map1_1.png', 'assets/characters/Char5Map1_2.png',
            'assets/characters/Char5Map1_3.png', 'assets/characters/Char5Map1_4.png']

#Nhân vật
CharsMap1 = [Char1Map1, Char2Map1, Char3Map1, Char4Map1, Char5Map1]
Speed = []
for x in range(5):
    Speed.append(random.uniform(2.0, 4.0))

#Các nhân vật trong game
class player(pygame.sprite.Sprite):
    def __init__(self, speed, pos, number, image, map):
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
        self.map = map
    def animation(self):
        #Vẽ nhân vật
        if self.count_run >= 3:
            self.count_run = 0
        if self.map == 0:
            if self.number == 0:
                if self.run:
                    self.image = pygame.image.load(CharsMap1[0][int(self.count_run)]).convert_alpha()
                    self.count_run += 0.1
                else:
                    self.image = pygame.image.load(CharsMap1[0][int(self.count_run)]).convert_alpha()
            if self.number == 1:
                if self.run:
                    self.image = pygame.image.load(CharsMap1[1][int(self.count_run)]).convert_alpha()
                    self.count_run += 0.1
                else:
                    self.image = pygame.image.load(CharsMap1[1][int(self.count_run)]).convert_alpha()
            if self.number == 2:
                if self.run:
                    self.image = pygame.image.load(CharsMap1[2][int(self.count_run)]).convert_alpha()
                    self.count_run += 0.1
                else:
                    self.image = pygame.image.load(CharsMap1[2][int(self.count_run)]).convert_alpha()
            if self.number == 3:
                if self.run:
                    self.image = pygame.image.load(CharsMap1[3][int(self.count_run)]).convert_alpha()
                    self.count_run += 0.1
                else:
                    self.image = pygame.image.load(CharsMap1[3][int(self.count_run)]).convert_alpha()
            if self.number == 4:
                if self.run:
                    self.image = pygame.image.load(CharsMap1[4][int(self.count_run)]).convert_alpha()
                    self.count_run += 0.1
                else:
                    self.image = pygame.image.load(CharsMap1[4][int(self.count_run)]).convert_alpha()

    def move(self):
        if self.run:
            self.rect.x += self.speed

    def update(self):
        self.animation()
        self.move()

Char1 = pygame.sprite.GroupSingle()
Char1.add(player(speed = Speed[0], 
                 pos = (screen.get_width() * 0.01, screen.get_height() * 0.55), 
                 number = 0, 
                 image = CharsMap1[0][0], 
                 map = 0))
Char2 = pygame.sprite.GroupSingle()
Char2.add(player(speed = Speed[1], 
                 pos = (screen.get_width() * 0.01, screen.get_height() * 0.66), 
                 number = 1, 
                 image = CharsMap1[1][0], 
                 map = 0))
Char3 = pygame.sprite.GroupSingle()
Char3.add(player(speed = Speed[2], 
                 pos = (screen.get_width() * 0.01, screen.get_height() * 0.76), 
                 number = 2, 
                 image = CharsMap1[2][0], 
                 map = 0))
Char4 = pygame.sprite.GroupSingle()
Char4.add(player(speed = Speed[3], 
                 pos = (screen.get_width() * 0.01, screen.get_height() * 0.87), 
                 number = 3, 
                 image = CharsMap1[3][0], 
                 map = 0))
Char5 = pygame.sprite.GroupSingle()
Char5.add(player(speed = Speed[4], 
                 pos = (screen.get_width() * 0.01, screen.get_height() * 0.98), 
                 number = 4, 
                 image = CharsMap1[4][0], 
                 map = 0))

#Các đối tượng trong game
class IG_Object(pygame.sprite.Sprite):
    def __init__(self, name, pos, image):
        super().__init__()
        self.x = pos[0]
        self.y = pos[1]
        self.name = name
        if self.name == "LuckyBox":
            self.pic= pygame.image.load(image).convert_alpha()
            self.image = self.pic
            self.rect= self.image.get_rect(midbottom = (self.x, self.y))
        elif self.name == "ChuChay":
            self.pic = KieuChu1.render("THIS IS GROUP 12'S AMAZING RACE GAME!!!", False, (255, 102, 0))
            self.image = self.pic
            self.rect= self.image.get_rect(topleft = (self.x, self.y))
    def move(self):
        if self.name == "ChuChay":
            self.rect.x -= 2
            if self.rect.right <= 0:
                self.rect.x = screen.get_width()
    def update(self):
        if self.name == "ChuChay":
            self.move()

#Add object
IG_Objects = pygame.sprite.Group()
LuckyBox_Spawn = [0.2, 0.25, 0.3, 4.5, 4.5, 0.5, 0.55, 0.6, 0.6, 0.62, 0.65, 0.66, 0.7, 0.75, 0.75, 0.8, 0.8, 0.8] #Các biến để random vị trí lucky box
IG_Objects.add(IG_Object(name = 'LuckyBox',
                         pos = (screen.get_width() * random.choice(LuckyBox_Spawn),
                         screen.get_height() * 0.55),
                         image = 'assets/item/luckyBox.png'))
IG_Objects.add(IG_Object(name = 'LuckyBox', 
                         pos = (screen.get_width() * random.choice(LuckyBox_Spawn), 
                         screen.get_height() * 0.66), 
                         image = 'assets/item/luckyBox.png'))
IG_Objects.add(IG_Object(name = 'LuckyBox', 
                         pos = (screen.get_width() * random.choice(LuckyBox_Spawn), 
                         screen.get_height() * 0.76), 
                         image = 'assets/item/luckyBox.png'))
IG_Objects.add(IG_Object(name = 'LuckyBox', 
                         pos = (screen.get_width() * random.choice(LuckyBox_Spawn), 
                         screen.get_height() * 0.87), 
                         image = 'assets/item/luckyBox.png'))
IG_Objects.add(IG_Object(name = 'LuckyBox', 
                         pos = (screen.get_width() * random.choice(LuckyBox_Spawn), 
                         screen.get_height() * 0.98), 
                         image = 'assets/item/luckyBox.png'))
IG_Objects.add(IG_Object(name = 'ChuChay', pos = (screen.get_width(), 0), image = 'None'))

#Class nút
BUTTON_STATE = ['assets/icon/button/Normal.png', 'assets/icon/button/Clicked.png', 'assets/icon/button/Hover.png'] #Trạng thái nút
class Button():
    def __init__(self, pos, text_base_color, text_active_color, textIn = None, font = pygame.font.Font('./assets/font/SVN-Retron_2000.ttf', 30)):
        self.image = pygame.image.load(BUTTON_STATE[0]).convert_alpha()
        self.x = pos[0]
        self.y = pos[1]
        self.font = font
        self.base_color, self.active_color = text_base_color, text_active_color
        self.textIn = textIn
        self.text = self.font.render(self.textIn, True, self.base_color)
        self.text_rect = self.text.get_rect(center=(self.x, self.y))
        self.image = pygame.transform.smoothscale(self.image, (self.text.get_width(), self.text.get_height()))
        self.rect = self.image.get_rect(center=(self.x, self.y * 1.01))

    def CheckClick(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            self.image = pygame.image.load(BUTTON_STATE[1]).convert_alpha()
            self.image = pygame.transform.smoothscale(self.image, (self.text.get_width(), self.text.get_height()))
            pygame.time.wait(200)
            return True
        return False
    
    def update(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            self.image = pygame.image.load(BUTTON_STATE[2]).convert_alpha()
            self.image = pygame.transform.smoothscale(self.image, (self.text.get_width(), self.text.get_height()))
            self.text = self.font.render(self.textIn, True, self.active_color)
        else:
            self.image = pygame.image.load(BUTTON_STATE[0]).convert_alpha()
            self.image = pygame.transform.smoothscale(self.image, (self.text.get_width(), self.text.get_height()))
            self.text = self.font.render(self.textIn, True, self.base_color)
        screen.blit(self.image, self.rect)
        screen.blit(self.text, self.text_rect)

#Cách xài class button
# 1. Khởi tạo nút
# button = Button((400, 300), "black", "white", "Chữ", Ảnh)
# 2. Check click
#     if event.type == pygame.MOUSEBUTTONDOWN:
#         button.CheckClick(pygame.mouse.get_pos())
# 3. Update button
# 	button.update()
# 	button.DoiMau(pygame.mouse.get_pos())

#Quy định các thuộc tính chỉ tạo dòng chữ hiển thị trong menu
class Label: 
    # Khởi tạo các thuộc tính tương tự như các thuộc tính của Button
    def __init__(self, x, y, width, height, text=None):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.font = pygame.font.Font('./assets/font/SVN-Retron_2000.ttf',40) #Font mặc định
    # gọi hàm vẽ các Label, gồm các tham số như chính đối tượng Label, cửa sổ màn hình và đường viền, mặc định là None.
    def draw(self, screen):
        if self.text: # Kiểm tra xem có text được đưa vào hay không
            text = self.font.render(self.text, 1, '#ffffff') #Màu text là màu đen, bật khử răng cưa cho text, áp dụng cho tất cả các text trong class
            screen.blit(text, (self.x + (self.width / 2 - text.get_width() / 2), self.y + (self.height / 2 - text.get_height() / 2)))  #Đưa chữ lên cửa sổ màn hình

#Cách xài class label
#label = Label(x, y, width, height, "Chữ")
