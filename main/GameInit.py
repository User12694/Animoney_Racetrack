import pygame_menu, pygame, random, sys, time
from datetime import datetime
from LoginSignup import *
#Khởi tạo các thứ
pygame.init()
pygame.display.set_caption("Race game")
clock = pygame.time.Clock()
random.seed(datetime.now().timestamp())

#Các biến cần dùng
user_id = ''
user_pwd = ''
user_money = 0
set_choice = 1
choice = 0
bet_money = 0
# store 5 characters
CHARACTERS = []
LUCKYBOX = []
GROUP = []
rank = []
winner = 0


#Ngôn ngữ
LANGUAGE = ["./assets/background/ENG/", "./assets/background/VIET/"]
LANGUAGE_INDEX = 0

#Màn hình cài đặt âm lượng
VOLUME = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]
VOLUME_INDEX = 4
present_volume = VOLUME[VOLUME_INDEX]
MenuSound = False
gameSound = False
#Kích thước màn hình (Do chưa có pygame_menu nên tạm thời bỏ qua)
WINDOW_SIZES = [pygame.display.get_desktop_sizes()[0], (768,432)]
WINDOW_SIZE_INDEX = 0
SCREEN_SIZE = ['assets/characters/']
SCREEN_SIZE_INDEX = 0
screen = pygame.display.set_mode(WINDOW_SIZES[WINDOW_SIZE_INDEX], pygame.RESIZABLE)
halfScreen_active = False

#Kiểu chữ
KieuChu1 = pygame.font.SysFont('./assets/font/SVN-Retron_2000.ttf',60)
KieuChu2 = pygame.font.SysFont('./assets/font/FVF Fernando 08',60)

#Chữ các thứ
Player_money = 0
scoreBoard = KieuChu2.render(f"Money: {Player_money}", False, (0, 255, 255))
scoreBoard_Box = scoreBoard.get_rect(center = (screen.get_width() * 0.13, screen.get_height() * 0.92))

#Ảnh các loại
map1 = pygame.image.load('assets/background/map1.png').convert_alpha()
map1 = pygame.transform.smoothscale(map1, WINDOW_SIZES[WINDOW_SIZE_INDEX])
map2 = pygame.image.load('assets/background/map2.png').convert_alpha()
map2 = pygame.transform.smoothscale(map1, WINDOW_SIZES[WINDOW_SIZE_INDEX])
map3 = pygame.image.load('assets/background/map3.png').convert_alpha()
map3 = pygame.transform.smoothscale(map1, WINDOW_SIZES[WINDOW_SIZE_INDEX])
map4 = pygame.image.load('assets/background/map4.png').convert_alpha()
map4 = pygame.transform.smoothscale(map1, WINDOW_SIZES[WINDOW_SIZE_INDEX])
map5 = pygame.image.load('assets/background/map5.png').convert_alpha()
map5 = pygame.transform.smoothscale(map1, WINDOW_SIZES[WINDOW_SIZE_INDEX])
MAPS = [map1, map2, map3, map4, map5]
MAP_INDEX = 0

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

#Nhân vật, tốc độ, vị trí
CharsMap1 = [Char1Map1, Char2Map1, Char3Map1, Char4Map1, Char5Map1]
RandSpeed = [2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4]
Speed = []
for x in range(5):
    Speed.append(random.choice(RandSpeed))
Position = [(WINDOW_SIZES[WINDOW_SIZE_INDEX][0] * 0.01, WINDOW_SIZES[WINDOW_SIZE_INDEX][1] * 0.55), (WINDOW_SIZES[WINDOW_SIZE_INDEX][0] * 0.01, WINDOW_SIZES[WINDOW_SIZE_INDEX][1] * 0.66), (WINDOW_SIZES[WINDOW_SIZE_INDEX][0] * 0.01, WINDOW_SIZES[WINDOW_SIZE_INDEX][1] * 0.76), (WINDOW_SIZES[WINDOW_SIZE_INDEX][0] * 0.01, WINDOW_SIZES[WINDOW_SIZE_INDEX][1] * 0.87), (WINDOW_SIZES[WINDOW_SIZE_INDEX][0] * 0.01, WINDOW_SIZES[WINDOW_SIZE_INDEX][1] * 0.98)]

#Ktra nhạc đã phát chưa
Victory_sound_Play = True

#List nhân vật thắng (Sẽ được thêm khi các nhân vật về đích)
RankList = []
#Các nhân vật trong game
class Character():
    def __init__(self, speed, pos, number, image, map):
        self.speed = speed
        self.pos = pos
        self.x = self.pos[0]
        self.y = self.pos[1]
        self.number = number
        self.run = True
        self.count_run = 0
        self.image = pygame.image.load(image).convert_alpha()
        self.rect= self.image.get_rect(midbottom = (self.x, self.y))
        self.count_run = 0
        self.map = map
        self.Finish = False
        self.isGoBack = False
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
    #Check điều kiện thắng
    def FinishLine_Pass(self):
        global Victory_sound_Play
        if self.rect.x > WINDOW_SIZES[WINDOW_SIZE_INDEX][0] * 0.95:
            if not self.Finish:
                rank.append(self)
                self.run = False
                if Victory_sound_Play:
                    pygame.mixer.music.load('assets/sounds/Victorious.ogg')
                    pygame.mixer.music.play(loops = 0)
                    Victory_sound_Play = False
        

    def update(self):
        self.animation()
        self.move()
        self.FinishLine_Pass()
        if self.isGoBack: #Đi ngược lại
            goBackImage = pygame.transform.flip(self.image, True, False)
            screen.blit(goBackImage, self.rect)
        else:
            screen.blit(self.image, self.rect)

    def stop(self, activated):
        if not activated:
            self.run = False

    def slow(self, activated):
        if not activated:
            if self.speed <= 3:
                self.speed = 1
            elif self.speed >= 5:
                self.speed -= 4
            else:
                self.speed -= 2

    def accelerate(self, activated):
        if not activated:
            if self.speed >= 3:
                self.speed += 1
            else:
                self.speed += 2

    def teleport(self, activated):
        if not activated:
            self.rect.x = WINDOW_SIZES[WINDOW_SIZE_INDEX][0] * 0.8

    def goback(self, activated):
        if not activated:
            self.speed *= -1
            self.isGoBack = True

def init_character_luckybox():
    for i in range(5):
        global set_choice
        new_character = Character(speed = Speed[i], 
                                  pos = Position[i], 
                                  number = i, 
                                  image = SCREEN_SIZE[SCREEN_SIZE_INDEX] + 'Char' + str(i + 1) + 'Map' + str(int(set_choice)) + '_1.png', 
                                  map = int(set_choice - 1))
        CHARACTERS.append(new_character)
    for i in range(10):
            if i < 5:
                luckyBox = LuckyBox(pos = LuckyBox_Pos[i], character = CHARACTERS[i])
            else:
                luckyBox = LuckyBox(pos = LuckyBox_Pos[i], character = CHARACTERS[i - 5])
            LUCKYBOX.append(luckyBox)

#Các đối tượng trong game (Hiện tại chỉ đang có chữ chạy)
class IG_Objects():
    def __init__(self, name, pos):
        self.x = pos[0]
        self.y = pos[1]
        self.name = name
        if self.name == "ChuChay":
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
            screen.blit(self.image, self.rect)

#Add object
ChuChay = IG_Objects(name = 'ChuChay', pos = (WINDOW_SIZES[WINDOW_SIZE_INDEX][0], 0))

#Vị trí lucky box
LuckyBox_Pos = [(WINDOW_SIZES[WINDOW_SIZE_INDEX][0] * random.uniform(0.28, 0.5), WINDOW_SIZES[WINDOW_SIZE_INDEX][1] * 0.55), 
                (WINDOW_SIZES[WINDOW_SIZE_INDEX][0] * random.uniform(0.28, 0.5), WINDOW_SIZES[WINDOW_SIZE_INDEX][1] * 0.66), 
                (WINDOW_SIZES[WINDOW_SIZE_INDEX][0] * random.uniform(0.28, 0.5), WINDOW_SIZES[WINDOW_SIZE_INDEX][1] * 0.76), 
                (WINDOW_SIZES[WINDOW_SIZE_INDEX][0] * random.uniform(0.28, 0.5), WINDOW_SIZES[WINDOW_SIZE_INDEX][1] * 0.87),
                (WINDOW_SIZES[WINDOW_SIZE_INDEX][0] * random.uniform(0.28, 0.5), WINDOW_SIZES[WINDOW_SIZE_INDEX][1] * 0.98),
                (WINDOW_SIZES[WINDOW_SIZE_INDEX][0] * random.uniform(0.65, 0.75), WINDOW_SIZES[WINDOW_SIZE_INDEX][1] * 0.55),
                (WINDOW_SIZES[WINDOW_SIZE_INDEX][0] * random.uniform(0.65, 0.75), WINDOW_SIZES[WINDOW_SIZE_INDEX][1] * 0.66),
                (WINDOW_SIZES[WINDOW_SIZE_INDEX][0] * random.uniform(0.65, 0.75), WINDOW_SIZES[WINDOW_SIZE_INDEX][1] * 0.76),
                (WINDOW_SIZES[WINDOW_SIZE_INDEX][0] * random.uniform(0.65, 0.75), WINDOW_SIZES[WINDOW_SIZE_INDEX][1] * 0.87),
                (WINDOW_SIZES[WINDOW_SIZE_INDEX][0] * random.uniform(0.65, 0.75), WINDOW_SIZES[WINDOW_SIZE_INDEX][1] * 0.98)]
class LuckyBox():
    def __init__(self, pos, character):
        self.x = pos[0]
        self.y = pos[1]
        self.activated = False #Cái này để check xem lucky box đã kích hoạt chưa
        self.active_effect = None #Kích hoạt hiệu ứng
        self.effect_duration = random.randint(1000, 3000) #Tính theo mili giây
        self.activation_time = None #Check lúc nào kích hoạt hiệu ứng
        self.effects = ["stun", "stun", "stun", "stun", "stun", "stun", "slow", "slow", "slow", "slow", "slow", "slow", "slow", "accelerate", "accelerate", "accelerate", "accelerate", "accelerate", "teleport", "goback"] #Các hiệu ứng, nếu muốn hiệu ứng nào xuất hiện nhiều chỉ cần spam
        self.image = pygame.image.load('assets/item/luckyBox.png').convert_alpha()
        self.rect= self.image.get_rect(midbottom = (self.x, self.y))
        self.tempSpeed = character.speed #Dùng để lưu tốc chạy của nhân vật tạm thời

    def check_activate(self, character):
        if character.rect.colliderect(self.rect) and (not self.activated):
            self.activate_effect(character)
            self.activated = True

    def activate_effect(self, character):

        self.active_effect = random.choice(self.effects)
        self.activation_time = pygame.time.get_ticks()

        if self.active_effect == "stun":
            character.stop(self.activated)
        elif self.active_effect == "slow":
            character.slow(self.activated)
        elif self.active_effect == "accelerate":
            character.accelerate(self.activated)
        elif self.active_effect == "teleport":
            character.teleport(self.activated)
        elif self.active_effect == "goback":
            character.goback(self.activated)

    def effect_Image(self, character):
        if self.active_effect == "stun":
            effectImage = pygame.image.load("assets/effects/hieuung_choang.png").convert_alpha()
            effectImage_rect = effectImage.get_rect(center = character.rect.midtop)
            effectImage2 = pygame.image.load("assets/effects/tangDa.png").convert_alpha()
            effectImage_rect2 = effectImage.get_rect(bottomleft = self.rect.midleft)
            screen.blit(effectImage, effectImage_rect)
            screen.blit(effectImage2, effectImage_rect2)
        elif self.active_effect == "slow":
            effectImage = pygame.image.load("assets/effects/hieuung_cham.png").convert_alpha()
            effectImage_rect = effectImage.get_rect(midbottom = character.rect.midleft)
            effectImage2 = pygame.image.load("assets/effects/hoNuoc.png").convert_alpha()
            effectImage_rect2 = effectImage.get_rect(midleft = self.rect.bottomleft)
            screen.blit(effectImage, effectImage_rect)
            screen.blit(effectImage2, effectImage_rect2)
        elif self.active_effect == "accelerate":
            effectImage = pygame.image.load("assets/effects/hieuung_tangtoc.png").convert_alpha()
            effectImage_rect = effectImage.get_rect(bottomright = character.rect.bottomleft)
            screen.blit(effectImage, effectImage_rect)
        elif self.active_effect == "teleport":
            effectImage = pygame.image.load("assets/effects/hieuung_dichchuyen.png").convert_alpha()
            effectImage_rect = effectImage.get_rect(bottomleft = self.rect.midbottom)
            screen.blit(effectImage, effectImage_rect)
        elif self.active_effect == "goback":
            effectImage = pygame.image.load("assets/effects/hieuung_quayve.png").convert_alpha()
            effectImage_rect = effectImage.get_rect(bottomleft = self.rect.midbottom)
            screen.blit(effectImage, effectImage_rect)

    def update(self, character):
        self.check_activate(character)
        if self.active_effect is not None:
            self.effect_Image(character)
            current_time = pygame.time.get_ticks() #Lấy thời gian hiện tại
            elapsed_time = current_time - self.activation_time
            if self.active_effect == "stun" or self.active_effect == "slow" or self.active_effect == "accelerate" or self.active_effect == "teleport":
                if elapsed_time >= self.effect_duration:
                    self.active_effect = None
                    character.speed = self.tempSpeed
                    character.run = True
            elif self.active_effect == "goback":
                if character.rect.x < 0:
                    self.active_effect = None
                    character.speed = self.tempSpeed
                    character.isGoBack = False


        if not self.activated:
                screen.blit(self.image, self.rect)

#Class nút
class Button():
    def __init__(self, pos, imageNormal, imageChanged):
        self.imageNormal = imageNormal
        self.imageChanged = imageChanged
        self.image = pygame.image.load(LANGUAGE[LANGUAGE_INDEX] + imageNormal).convert_alpha()
        self.x = pos[0]
        self.y = pos[1]
        self.rect = self.image.get_rect(center=(self.x, self.y * 1.01))

    def CheckClick(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            return True
        return False
    
    def update(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            self.image = pygame.image.load(LANGUAGE[LANGUAGE_INDEX] + self.imageChanged).convert_alpha()
        else:
            self.image = pygame.image.load(LANGUAGE[LANGUAGE_INDEX] + self.imageNormal).convert_alpha()
        screen.blit(self.image, self.rect)
    '''def update_images(self, imageNormal, imageChanged):
        self.imageNormal = pygame.image.load(LANGUAGE[LANGUAGE_INDEX] + self.imageNormal).convert_alpha()
        self.imageChanged = pygame.image.load(LANGUAGE[LANGUAGE_INDEX] + self.imageChanged).convert_alpha()'''

#Cách xài class button
# 1. Khởi tạo nút
# button = Button( pos = (400, 300), imageNỏmal = "Button.png", imageChanged = "Button2.png") Chú ý: Button.png là ảnh khi chưa rê chuột vào, Button2.png là ảnh khi rê chuột vào
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
