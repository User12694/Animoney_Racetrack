import pygame_menu, pygame, random, sys
from LoginSignup import *
from GameFunctions import *

#Khởi tạo các thứ
pygame.init()
pygame.display.set_caption("Race game")
clock = pygame.time.Clock()

#Âm thanh
VOLUME = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]
VOLUME_INDEX = 4

#Chọn map
MAPS = [0, 1, 2, 3, 4]
MAP_INDEX = 0

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
scoreBoard_Box = scoreBoard.get_rect(center = (WINDOW_SIZES[WINDOW_SIZE_INDEX][0] * 0.13, WINDOW_SIZES[WINDOW_SIZE_INDEX][1] * 0.92))

#Ảnh
Background = pygame.image.load('assets/background/background.png').convert_alpha()

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

#Class nút
class Button():
	def __init__(self, image, pos, textIn, font, base_color, active_color):
		self.image = image
		self.x = pos[0]
		self.y = pos[1]
		self.font = font
		self.base_color, self.active_color = base_color, active_color
		self.textIn = textIn
		self.text = self.font.render(self.textIn, True, self.base_color)
		if self.image is None:
			self.image = self.text
		self.rect = self.image.get_rect(center=(self.x, self.y))
		self.text_rect = self.text.get_rect(center=(self.x, self.y))

	def update(self):
		screen.blit(self.image, self.rect)
		screen.blit(self.text, self.text_rect)

	def CheckClick(self, position):
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			return True
		return False

	def DoiMau(self, position):
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			self.text = self.font.render(self.textIn, True, self.active_color)
		else:
			self.text = self.font.render(self.textIn, True, self.base_color)

#Cách xài class button
# 1. Khởi tạo nút
# button_surface = pygame.image.load("button.png")
# button = Button(button_surface, (400, 300), "Button", KieuChu1, "black", "white")
# 2. Check click
#     if event.type == pygame.MOUSEBUTTONDOWN:
#         button.CheckClick(pygame.mouse.get_pos())
# 3. Update button
# 	button.update()
# 	button.DoiMau(pygame.mouse.get_pos())

#Menu khi mới vào trò chơi
def menu():
    #Các loại nút
    PLAY_BUTTON = Button(image = pygame.image.load("assets/icon/button.png"), pos = (screen.get_width() / 2, screen.get_height() / 2 + 50), textIn = "PLAY", font = KieuChu1, base_color= "black", active_color = "white")
    SETTINGS_BUTTON = Button(image = pygame.image.load("assets/icon/button.png"), pos = (screen.get_width() / 2, screen.get_height() / 2 + 100), textIn = "SETTINGS", font = KieuChu1, base_color= "black", active_color = "white")
    QUIT_BUTTON = Button(image = pygame.image.load("assets/icon/button.png"), pos = (screen.get_width() / 2, screen.get_height() / 2 + 150), textIn = "QUIT", font = KieuChu1, base_color = "black", active_color = "white")
    BUTTONS = [PLAY_BUTTON, SETTINGS_BUTTON, QUIT_BUTTON]
    pygame.mixer.music.set_volume(VOLUME[VOLUME_INDEX])
    pygame.mixer.music.load('assets/sounds/mainmenu.mp3')
    pygame.mixer.music.play(loops = -1)
    while True:
        # Check đăng nhập
        if not login_lock:
            pygame.quit()
            sys.exit()

        screen.blit(Background, (0, 0))

        menu_title = KieuChu1.render("MENU", False, "black")
        menu_title_rect = menu_title.get_rect(center = (screen.get_width() / 2, screen.get_height() / 2 - 50))
        
        screen.blit(menu_title, menu_title_rect)

        mouse_pos = pygame.mouse.get_pos()

        for button in BUTTONS:
            button.DoiMau(mouse_pos)
            button.update()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.CheckClick(mouse_pos):
                    Play()
                if SETTINGS_BUTTON.CheckClick(mouse_pos):
                    Settings()
                if QUIT_BUTTON.CheckClick(mouse_pos):
                    pygame.quit()
                    sys.exit()
        pygame.display.update()
        clock.tick(60)

#Tạm dừng trò chơi
def Settings():
    #check events
    while True:
        mouse_pos = pygame.mouse.get_pos()
        screen.blit(Background,(0,0))

        Settings_text = KieuChu1.render("SETTINGS", True, "Black")
        Settings_text_rect = Settings_text.get_rect(center=(screen.get_width() / 2, screen.get_height() / 2 - 50))
        screen.blit(Settings_text, Settings_text_rect)

        Return_To_Menu = Button(image= pygame.image.load("assets/icon/button.png"), pos=(screen.get_width() / 2, screen.get_height() / 2), textIn="BACK", font=KieuChu1, base_color="Black", active_color="white")
        Return_To_Menu.DoiMau(mouse_pos)
        Return_To_Menu.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if Return_To_Menu.CheckClick(mouse_pos):
                    return

        pygame.display.update()
        clock.tick(60)

def Play():
    pygame.mixer.music.load('assets/sounds/set1.mp3')
    pygame.mixer.music.play(loops = -1)
    Victory_sound_Play = True
    while True:
        
        #Ảnh nền
        screen.blit(Background,(0,0))
        IG_Objects.draw(screen)
        IG_Objects.update()

        #Nhân vật
        Char1.draw(screen)
        # Char2.draw(screen)
        # Char3.draw(screen)
        # Char4.draw(screen)
        # Char5.draw(screen)

        Char1.update()
        # Char2.update()
        # Char3.update()
        # Char4.update()
        # Char5.update()

        #Nhân vật + nhạc khi win (test)
        FinishLine_Pass1 = FinishLine_Pass(Char1, IG_Objects) #Gọi hàm ở GameFunctions
        # FinishLine_Pass2 = FinishLine_Pass(Char2, IG_Objects)
        # FinishLine_Pass3 = FinishLine_Pass(Char3, IG_Objects)
        # FinishLine_Pass4 = FinishLine_Pass(Char4, IG_Objects)
        # FinishLine_Pass5 = FinishLine_Pass(Char5, IG_Objects)

        if FinishLine_Pass1 and Victory_sound_Play: #or FinishLine_Pass2 or FinishLine_Pass3 or FinishLine_Pass4 or FinishLine_Pass5
            pygame.mixer.music.load('assets/sounds/Victorious.ogg')
            pygame.mixer.music.play(loops = 0)
            Victory_sound_Play = False
                

        # #Lucky box
        # global activateLuckyBox

        # global SlowTime
        # global ActivateSlow

        # global SpeedTime
        # global ActivateSpeed

        # global ActivateDizzy
        # global DizzyTime
        
        # if not activateLuckyBox:
        #     screen.blit(luckyBox, luckyBox_Box)
        # if Char1_Box.colliderect(luckyBox_Box):
        #     if not activateLuckyBox:
        #         #Kích hoạt hiệu ứng(Tạm)
        #         match luckyBox_Effect:
        #             case 0:
        #                 ActivateSlow = True
        #             case 1:
        #                 ActivateSpeed = True
        #             case 2:
        #                 ActivateDizzy = True

        #         activateLuckyBox = True

        # global Char1_TempSpeed #Cái này để lưu tốc chạy cơ bản của nhân vật ở ngoài hàm main
        # global Activated

        # #Làm chậm
        # if ActivateSlow == True:
        #     if not Activated:
        #         Char1Map1_Speed -= 2
        #         Activated = True
        #     SlowTime -= 1
        # if SlowTime == 0:
        #     SlowTime = SlowTimeConst
        #     Char1Map1_Speed = Char1_TempSpeed
        #     ActivateSlow = False
        
        # #Tăng tốc
        # if ActivateSpeed == True:
        #     if not Activated:
        #         Char1Map1_Speed += 3
        #         Activated = True
        #     SpeedTime -= 1
        # if SpeedTime == 0:
        #     SpeedTime = DizzyTimeConst
        #     Char1Map1_Speed = Char1_TempSpeed
        #     ActivateSpeed = False

        # #Choáng
        # if ActivateDizzy == True:
        #     Char1Map1_Speed = 0
        #     DizzyTime -= 1
        # if DizzyTime == 0:
        #     Char1Map1_Speed = Char1_TempSpeed
        #     DizzyTime = DizzyTimeConst
        #     ActivateDizzy = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    Pause_Game()

        #Bảng tiền
        pygame.draw.rect(screen, "red", scoreBoard_Box, 6, 10)
        screen.blit(scoreBoard, scoreBoard_Box)

        pygame.display.update()
        clock.tick(60)

def Pause_Game():
     while True:
        screen.blit(Background,(0,0))

        Settings_text = KieuChu1.render("PAUSE GAME", True, "Black")
        Settings_text_rect = Settings_text.get_rect(center=(screen.get_width() / 2, screen.get_height() / 2 - 50))
        screen.blit(Settings_text, Settings_text_rect)

        mouse_pos = pygame.mouse.get_pos()
        RETURN_TO_GAME = Button(image=pygame.image.load("assets/icon/button.png"), pos=(screen.get_width() / 2, screen.get_height() / 2), textIn="CONTINUE", font=KieuChu1, base_color="Black", active_color="white")
        QUIT = Button(image=pygame.image.load("assets/icon/button.png"), pos=(screen.get_width() / 2, screen.get_height() / 2 + 50), textIn="QUIT", font=KieuChu1, base_color="Black", active_color="white")

        BUTTONS = [RETURN_TO_GAME, QUIT]

        for button in BUTTONS:
            button.DoiMau(mouse_pos)
            button.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if RETURN_TO_GAME.CheckClick(mouse_pos):
                    return
                if QUIT.CheckClick(mouse_pos):
                    pygame.quit()
                    sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return

        pygame.display.update()
        clock.tick(60)