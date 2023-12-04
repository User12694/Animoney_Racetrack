import pygame_menu, pygame, random, sys
from GameInit import *

#Check điều kiện thắng (Cái này xài cho lucky box đi)
def Lucky_Box(player, IG_Objects):
    if pygame.sprite.spritecollide(player.sprite, IG_Objects, True):
        return True
    return False

def FinishLine_Pass(player):
    if player.sprite.rect.x > screen.get_width() * 0.95:
        player.sprite.run = False
        return True
    return False

#Menu khi mới vào trò chơi
def menu():
    #Các loại nút
    PLAY_BUTTON = Button(pos = (screen.get_width() / 2, screen.get_height() / 2 + 50), text_base_color= "black", text_active_color = "white", textIn = "PLAY")
    SETTINGS_BUTTON = Button(pos = (screen.get_width() / 2, screen.get_height() / 2 + 100), text_base_color= "black", text_active_color = "white", textIn = "SETTINGS")
    QUIT_BUTTON = Button(pos = (screen.get_width() / 2, screen.get_height() / 2 + 150), text_base_color = "black", text_active_color = "white", textIn = "QUIT")
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
            button.update(mouse_pos)
        
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

        Return_To_Menu = Button(pos=(screen.get_width() / 2, screen.get_height() / 2), text_base_color="Black", text_active_color="white", textIn="BACK")
        Return_To_Menu.update(mouse_pos)

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
        if MAP_INDEX == 1:
             screen.blit(MAPS[0],(0,0))
        if MAP_INDEX == 2:
             screen.blit(MAPS[1],(0,0))
        if MAP_INDEX == 3:
             screen.blit(MAPS[2],(0,0))
        if MAP_INDEX == 4:
             screen.blit(MAPS[3],(0,0))
        if MAP_INDEX == 5:
             screen.blit(MAPS[4],(0,0))

        IG_Objects.draw(screen)
        IG_Objects.update()

        #Nhân vật
        Char1.draw(screen)
        Char2.draw(screen)
        Char3.draw(screen)
        Char4.draw(screen)
        Char5.draw(screen)

        Char1.update()
        Char2.update()
        Char3.update()
        Char4.update()
        Char5.update()

        #Check win + nhạc khi win (test)
        FinishLine_Pass1 = FinishLine_Pass(Char1) #Gọi hàm ở GameFunctions
        FinishLine_Pass2 = FinishLine_Pass(Char2)
        FinishLine_Pass3 = FinishLine_Pass(Char3)
        FinishLine_Pass4 = FinishLine_Pass(Char4)
        FinishLine_Pass5 = FinishLine_Pass(Char5)

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
        
        activate_LuckyBox1 = Lucky_Box(Char1, IG_Objects)
        activate_LuckyBox2 = Lucky_Box(Char2, IG_Objects)
        activate_LuckyBox3 = Lucky_Box(Char3, IG_Objects)
        activate_LuckyBox4 = Lucky_Box(Char4, IG_Objects)
        activate_LuckyBox5 = Lucky_Box(Char5, IG_Objects)

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
        # pygame.draw.rect(screen, "red", scoreBoard_Box, 6, 10)
        # screen.blit(scoreBoard, scoreBoard_Box)

        pygame.display.update()
        clock.tick(60)

def Pause_Game():
     while True:
        screen.blit(Background,(0,0))

        Settings_text = KieuChu1.render("PAUSE GAME", True, "Black")
        Settings_text_rect = Settings_text.get_rect(center=(screen.get_width() / 2, screen.get_height() / 2 - 50))
        screen.blit(Settings_text, Settings_text_rect)
        #Các nút ở trong Pause menu
        mouse_pos = pygame.mouse.get_pos()
        RETURN_TO_GAME = Button(pos=(screen.get_width() / 2, screen.get_height() / 2), text_base_color="Black", text_active_color="white", textIn="CONTINUE")
        QUIT = Button(pos=(screen.get_width() / 2, screen.get_height() / 2 + 50), text_base_color="Black", text_active_color="white", textIn="QUIT")

        BUTTONS = [RETURN_TO_GAME, QUIT]

        for button in BUTTONS:
            button.update(mouse_pos)

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
    
                    


