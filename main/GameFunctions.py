import pygame_menu, pygame, random, sys, time
import GameInit
from GameInit import *
from money_bet import *


#Check điều kiện thắng
def FinishLine_Pass():
    global Victory_sound_Play
    if len(GameInit.rank) == 5:
        if Victory_sound_Play:
            pygame.mixer.music.load('assets/sounds/Victorious.ogg')
            pygame.mixer.music.play(loops = 0)
            Victory_sound_Play = False
            return True
    return False

#Đếm ngược
countDownCheck = True
NumberCountDown = ["assets/background/start.png", "assets/background/1.png", "assets/background/2.png", "assets/background/3.png"]
def count_down():
    global gameSound
    for i in range(3, -1, -1):
        screen.blit(MAPS[MAP_INDEX], (0, 0))
        image = pygame.image.load(NumberCountDown[i]).convert_alpha()
        image_rect = image.get_rect(center = (screen.get_width() / 2, screen.get_height() / 2))
        screen.blit(image, image_rect)

        pygame.display.update()
        pygame.time.wait(1000)
    pygame.mixer.music.set_volume(present_volume)
    pygame.mixer.music.load('assets/sounds/set1.mp3')
    pygame.mixer.music.play(loops = -1)
    gameSound = True

class Congratulations:
    def __init__(self):
        self.CONTINUE_BUTTON = Button(pos=(screen.get_width() / 2 * 1.05, screen.get_height() * 0.1), imageNormal = "continue.png", imageChanged = "continue2.png")
    #Vẽ các thuộc tính lên màn hình
    def draw(self, mouse_pos):
        global rank, rankSound,  WINDOW_SIZES
        BG = pygame.image.load(LANGUAGE[GameInit.LANGUAGE_INDEX]+'BG_congratulations.png').convert_alpha()
        BG = pygame.transform.smoothscale(BG, WINDOW_SIZES[GameInit.WINDOW_SIZE_INDEX])
        screen.blit(BG, (0, 0))
        self.CONTINUE_BUTTON.update(mouse_pos)

        if not rankSound:
            pygame.mixer.music.set_volume(present_volume)
            pygame.mixer.music.load('assets/sounds/rank.mp3')
            pygame.mixer.music.play(loops = -1)
            rankSound = True
        
        Congratulations_pos = [(WINDOW_SIZES[GameInit.WINDOW_SIZE_INDEX][0] / 2 * 1.05, WINDOW_SIZES[GameInit.WINDOW_SIZE_INDEX][1] * 0.78), 
                                (WINDOW_SIZES[GameInit.WINDOW_SIZE_INDEX][0] / 2 * 0.6, WINDOW_SIZES[GameInit.WINDOW_SIZE_INDEX][1]* 0.85), 
                                (WINDOW_SIZES[GameInit.WINDOW_SIZE_INDEX][0] / 2 * 1.5, WINDOW_SIZES[GameInit.WINDOW_SIZE_INDEX][1]* 0.85), 
                                (WINDOW_SIZES[GameInit.WINDOW_SIZE_INDEX][0] / 2 * 0.42, WINDOW_SIZES[GameInit.WINDOW_SIZE_INDEX][1] * 0.93), 
                                (WINDOW_SIZES[GameInit.WINDOW_SIZE_INDEX][0] / 2 * 1.7, WINDOW_SIZES[GameInit.WINDOW_SIZE_INDEX][1] * 0.93)]

        for i in range(5):
            GameInit.rank[i].rect = GameInit.rank[i].image.get_rect(midbottom = Congratulations_pos[i])
            screen.blit(GameInit.rank[i].image, GameInit.rank[i].rect)

        

    # Cập nhật các trạng thái của thuộc tính
    def update(self, event):
        global MenuSound, gameSound, InitGame
        if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                Back_To_Menu = Pause_Game()
                if Back_To_Menu:
                    InitGame = False
                    return MenuClass()
            
        return self

#Biến được sử dụng
InitGame = False
rankSound = False

class Play:
    def __init__(self):
        money_bet()
        self.playButton = Button(pos = (screen.get_width() / 2, screen.get_height() / 2), imageNormal = "play.png", imageChanged = "play2.png") # Nút có dòng chữ "Play game"
        self.settingsButton = Button(pos = (screen.get_width() / 2, screen.get_height() / 2 * 1.35), imageNormal = "settings.png", imageChanged = "settings2.png") # Nút có dòng chữ "Settings"
        self.quitButton = Button(pos = (screen.get_width() / 2, screen.get_height() / 2 * 1.7), imageNormal = "quit.png", imageChanged = "quit2.png") # Nút có dòng chữ "Quit"
        self.CheckPass = False #Check xem 5 nv có về đích chưa
    #Vẽ các thuộc tính lên màn hình
    def draw(self, mouse_pos):
        global VOLUME_INDEX, present_volume, countDownCheck, gameSound
        #Ảnh nền
        if MAP_INDEX == 0:
             screen.blit(MAPS[0],(0,0))
        if MAP_INDEX == 1:
             screen.blit(MAPS[1],(0,0))
        if MAP_INDEX == 2:
             screen.blit(MAPS[2],(0,0))
        if MAP_INDEX == 3:
             screen.blit(MAPS[3],(0,0))
        if MAP_INDEX == 4:
             screen.blit(MAPS[4],(0,0))
        
        #Đếm ngược trước khi vào game
        if countDownCheck:
            count_down()
            countDownCheck = False

        if not gameSound:
            pygame.mixer.music.set_volume(present_volume)
            pygame.mixer.music.load('assets/sounds/set1.mp3')
            pygame.mixer.music.play(loops = -1)
            gameSound = True

        #Chữ chạy
        ChuChay.update()
                
        #Update lucky box
        for i in range(10):
            if i < 5:
                LUCKYBOX[i].update(CHARACTERS[i])
            else:
                LUCKYBOX[i].update(CHARACTERS[i - 5])

        #Nhân vật
        for i in range(5):
            CHARACTERS[i].update()

        #Check xong game
        if FinishLine_Pass():
            self.CheckPass = True

    # Cập nhật các trạng thái của thuộc tính
    def update(self, event):
        global MenuSound, gameSound, InitGame
        if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                Back_To_Menu = Pause_Game()
                if Back_To_Menu:
                    InitGame = False
                    reset_game()
                    return MenuClass()
        if self.CheckPass:
            return Congratulations()
            
        return self

#Tạm dừng trò chơi
def Pause_Game():
     while True:
        #Ảnh nền
        Background = pygame.image.load(LANGUAGE[GameInit.LANGUAGE_INDEX]+'background.png').convert_alpha()
        Background = pygame.transform.smoothscale(Background, WINDOW_SIZES[GameInit.WINDOW_SIZE_INDEX])
        screen.blit(Background,(0,0))
        #Các nút ở trong Pause menu
        mouse_pos = pygame.mouse.get_pos()
        RETURN_TO_MENU = Button(pos=(screen.get_width() / 2, screen.get_height() / 2), imageNormal = "return.png", imageChanged = "return2.png")
        RETURN_TO_GAME = Button(pos=(screen.get_width() / 2, screen.get_height() / 2 * 1.35), imageNormal = "continue.png", imageChanged = "continue2.png")
        QUIT = Button(pos=(screen.get_width() / 2, screen.get_height() / 2 * 1.7), imageNormal = "quit.png", imageChanged = "quit2.png")
        BUTTONS = [RETURN_TO_MENU, RETURN_TO_GAME, QUIT]

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
                if RETURN_TO_MENU.CheckClick(mouse_pos):
                    if QuitConfirm():
                        return True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return

        pygame.display.update()
        clock.tick(60)

def QuitConfirm():
    while True:
        Background = pygame.image.load(LANGUAGE[GameInit.LANGUAGE_INDEX]+'quitprompt.png').convert_alpha()
        Background = pygame.transform.smoothscale(Background, WINDOW_SIZES[GameInit.WINDOW_SIZE_INDEX])
        screen.blit(Background,(0,0))
        mouse_pos = pygame.mouse.get_pos()
        #Các nút trong quit confirm
        yesButton = Button(pos=(screen.get_width() / 2 * 1.5, screen.get_height() / 2 * 1.2), imageNormal = "yes.png", imageChanged = "yes2.png")
        noButton = Button(pos=(screen.get_width() / 2 * 0.5, screen.get_height() / 2 * 1.2), imageNormal = "no.png", imageChanged = "no2.png")

        yesButton.update(mouse_pos)
        noButton.update(mouse_pos)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if yesButton.CheckClick(mouse_pos):
                    return True
                if noButton.CheckClick(mouse_pos):
                    return False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return False

        pygame.display.update()
        clock.tick(60)


# Lớp menu chính
class MenuClass: 
    #Khởi tạo các thuộc tính
    def __init__(self):
        global VOLUME_INDEX, present_volume
        self.playButton = Button(pos = (screen.get_width() / 2, screen.get_height() / 2 * 0.95), imageNormal = f"play.png", imageChanged = "play2.png") # Nút có dòng chữ "Play game"
        self.settingsButton = Button(pos = (screen.get_width() / 2, screen.get_height() / 2 * 1.2), imageNormal = "settings.png", imageChanged = "settings2.png") # Nút có dòng chữ "Settings"
        self.minigame = Button(pos = (screen.get_width() / 2, screen.get_height() / 2 * 1.45), imageNormal = "continue.png", imageChanged = "continue2.png")
        self.quitButton = Button(pos = (screen.get_width() / 2, screen.get_height() / 2 * 1.7), imageNormal = "quit.png", imageChanged = "quit2.png") # Nút có dòng chữ "Quit"
        #v self.changeLanguageButton = Button(pos=(screen.get_width() - screen.get_width() / 16, screen.get_height() - screen.get_height() / 16), imageNormal= "lang40.png", imageChanged= "lang240.png") # Nút chuyển đổi ngôn ngữ
    #Vẽ các thuộc tính lên màn hình
    def draw(self, mouse_pos):
        read_data()
        Background = pygame.image.load(LANGUAGE[GameInit.LANGUAGE_INDEX]+'background.png').convert_alpha()
        Background = pygame.transform.smoothscale(Background, WINDOW_SIZES[GameInit.WINDOW_SIZE_INDEX])
        screen.blit(Background, (0, 0))
        self.playButton.update(mouse_pos)
        self.settingsButton.update(mouse_pos)
        self.quitButton.update(mouse_pos)
        self.minigame.update(mouse_pos)
        # self.changeLanguageButton.update(mouse_pos)

    # Cập nhật các trạng thái của thuộc tính
    def update(self, event):
        global MenuSound, gameSound, LANGUAGE
        if not MenuSound:
            pygame.mixer.music.set_volume(present_volume)
            pygame.mixer.music.load('assets/sounds/mainmenu.mp3')
            pygame.mixer.music.play(loops = -1)
            MenuSound = True
        pos = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if self.playButton.CheckClick(pos):
                # if user_money < min(money_bet_list):
                #     minigame.flappy_bird()
                # else:
                MenuSound = False
                gameSound = False
                return MapSelection()
            if self.settingsButton.CheckClick(pos):
                return SettingClass()
            if self.quitButton.CheckClick(pos):
                pygame.quit()
                sys.exit()
            if self.minigame.CheckClick(pos):
                minigame.flappy_bird()
                    
        return self

class SettingClass: #Khởi tạo các nút, label và Button. 
    def __init__(self):
        self.soundButton = Button(pos=(screen.get_width() / 2, screen.get_height() / 2 * 0.65), imageNormal = "sound.png", imageChanged = "sound2.png")
        self.screenButton = Button(pos=(screen.get_width() / 2, screen.get_height() / 2 * 0.9), imageNormal = "screen.png", imageChanged = "screen2.png")
        self.escButton = Button(pos=(screen.get_width() / 2, screen.get_height() / 2 * 1.4), imageNormal = "back.png", imageChanged = "back2.png")
        self.changeLanguageButton = Button(pos=(screen.get_width() / 2, screen.get_height() / 2 * 1.15), imageNormal = "lang.png", imageChanged = "lang2.png")
    #Vẽ các lớp phủ, các nút và chữ
    def draw(self, mouse_pos):
        Background = pygame.image.load(LANGUAGE[GameInit.LANGUAGE_INDEX] + 'settingsMenu.png').convert_alpha()
        Background = pygame.transform.smoothscale(Background, WINDOW_SIZES[GameInit.WINDOW_SIZE_INDEX])
        screen.blit(Background,(0,0)) #Tạo một lớp phủ hình chữ nhật kích thước tối đa
        #Vẽ nút
        self.soundButton.update(mouse_pos)
        self.screenButton.update(mouse_pos)
        self.escButton.update(mouse_pos)
        self.changeLanguageButton.update(mouse_pos)
    #Cập nhật trạng thái của class
    def update(self, event):
        mouse_pos = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Kiểm tra các đối tượng như nút chọn Âm lượng, chọn tùy chọn Màn hình, nút thoát; có được nhấn hay không. 
            # Nếu có thì trả về class tương ứng
            if self.soundButton.CheckClick(mouse_pos):
                return VolumeSettingClass()
            if self.screenButton.CheckClick(mouse_pos):
                return WindowModeSettingClass()
            if self.escButton.CheckClick(mouse_pos):
                return MenuClass()
            if self.changeLanguageButton.CheckClick(mouse_pos):
                if GameInit.LANGUAGE_INDEX == 0:
                    GameInit.LANGUAGE_INDEX = 1
                elif GameInit.LANGUAGE_INDEX == 1:
                    GameInit.LANGUAGE_INDEX = 0
        if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        return self


class VolumeSettingClass:
    #Khai báo các thuộc tính của class: 
    def __init__(self):
        # Khởi tạo các thuộc tính. 
        # Chú ý các thành phần như âm lượng hiện tại và chỉ số âm lượng được đánh dấu toàn cục. Sau này sẽ thêm các thuộc tính WINDOW
        global present_volume, VOLUME_INDEX
        # self.label1 = Label(screen.get_width() / 2 * 0.95, screen.get_height() / 2 * 0.4,125,50,'Mute Volume') # Dòng chữ 'Mute Volume'  
        self.esc_button = Button((screen.get_width() / 2, screen.get_height() / 2 * 1.5),imageNormal = "back.png", imageChanged = "back2.png")    # Nút có chữ 'Back'
        self.mute_button = Button((screen.get_width() / 2, screen.get_height() / 2 * 0.55),imageNormal = "mute.png", imageChanged = "mute2.png") # Nút có chữ 'Mute'
        # self.label2 = Label(screen.get_width() / 2 * 0.92, screen.get_height() / 2 * 0.8,125,50,'Volume')     # dòng chữ "Volume"
        self.minusVol_button = Button((screen.get_width() / 2 * 0.6, screen.get_height() / 2 * 0.95),imageNormal = "low.png", imageChanged = "low2.png") #Các nút +, - để tăng giảm âm lượng
        self.plusVol_button = Button((screen.get_width() / 2 * 1.4, screen.get_height() / 2 * 0.95),imageNormal = "high.png", imageChanged = "high2.png")
        self.display_volume_label = Label(screen.get_width() / 2 * 0.95, screen.get_height() / 2,50,50, f"{present_volume * 100}") # Trường hiển thị âm lượng hiện tại
        
        self.isMute = False #Các biến khai báo. Ở đây là biến xác định xem có đang tắt âm hay không
        #Các khai báo cho xác định âm lượng của âm thanh
        self.volume_list = VOLUME
        self.volume = present_volume
        self.previous_volume = self.volume
        
    #Hàm vẽ các đối tượng trên màn hình
    def draw(self, mouse_pos):
        #Vẽ lớp phủ hình chữ nhật kích thước bằng kích thước cửa sổ hiện hành
        Background = pygame.image.load(LANGUAGE[GameInit.LANGUAGE_INDEX]+'soundMenu.png').convert_alpha()
        Background = pygame.transform.smoothscale(Background, WINDOW_SIZES[GameInit.WINDOW_SIZE_INDEX])
        screen.blit(Background,(0,0))
        #Vẽ các thuộc tính khác đã nêu
        # self.label1.draw(screen)
        # self.label2.draw(screen)
        self.esc_button.update(mouse_pos)
        self.mute_button.update(mouse_pos)
        self.plusVol_button.update(mouse_pos)
        self.minusVol_button.update(mouse_pos)
        self.display_volume_label.draw(screen)
    #Cập nhật các trạng thái. Khai báo biến toàn cục là để giữ trạng thái âm lượng
    def update(self, event):
        global present_volume
        global VOLUME_INDEX
        #Lấy vị trí đầu con trỏ chuột
        pos = pygame.mouse.get_pos()
        #Kiểm tra xem có nhấn chuột không
        if event.type == pygame.MOUSEBUTTONDOWN:
            #Hàm isOver kiểm tra xem con trỏ chuột có đè lên các thuộc tính Button trong khi đang nhấn nút chuột trái hay không
            if self.esc_button.CheckClick(pos):
                return SettingClass() #Nếu nhấn chuột vào esc_button, trả về màn hình cài đặt
            #Kiểm tra xem các nút cộng, trừ, có được nhấn hay không
            if self.plusVol_button.CheckClick(pos): 
                # Kiểm tra chỉ số VOLUME_INDEX. Chừa giá trị biên phải ra vì khi điều kiện thỏa mãn 
                # VOLUME_INDEX + 1 vượt quá chỉ số max của list
                if 0 <= VOLUME_INDEX < len(self.volume_list) -1:
                    VOLUME_INDEX += 1 #Lưu trữ các giá trị ra biến toàn cục
                    self.volume = self.volume_list[VOLUME_INDEX] #gán giá trị cho biến volume của class
                    present_volume = self.volume
                    self.isMute = False
                    if not self.isMute:
                        self.mute_button.textIn = 'Mute'
                    pygame.mixer.music.set_volume(present_volume) #Đặt âm lượng theo giá trị vừa gán
                    self.display_volume_label.text = f'{present_volume * 100}'
            if self.minusVol_button.CheckClick(pos):
                # Kiểm tra chỉ số VOLUME_INDEX. Chừa giá trị biên trái ra vì khi điều kiện thỏa mãn 
                # VOLUME_INDEX - 1 vượt quá chỉ số min của list
                if len(self.volume_list) - 1 >= VOLUME_INDEX > 0 :
                    VOLUME_INDEX -= 1 #Lưu trữ các giá trị ra biến toàn cục
                    self.volume = self.volume_list[VOLUME_INDEX] #gán giá trị cho biến volume của class
                    present_volume = self.volume
                    self.isMute = False
                    if not self.isMute:
                        self.mute_button.textIn = 'Mute'
                    pygame.mixer.music.set_volume(present_volume) #Đặt âm lượng theo giá trị vừa gán
                    self.display_volume_label.text = f'{present_volume * 100}' #Đặt nội dung label hiển thị âm lượng là âm lượng hiện tại
            # Hàm kiểm tra xem nút Mute có được nhấn hay không:     
            if self.mute_button.CheckClick(pos):
                if self.isMute == False:
                    self.isMute = True #Trả về True cho isMute rồi thực hiện lệnh setvolume về 0
                    if self.isMute:
                        self.mute_button.imageNormal = 'unmute.png'
                        self.mute_button.imageChanged = 'unmute2.png'
                        self.volume = present_volume #Lưu trữ giá trị âm lượng
                        present_volume = 0
                        self.display_volume_label.text = "0" #Đưa giá trị âm lượng về 0
                        pygame.mixer.music.set_volume(present_volume)
                #Kiểm tra xem liệu có nhấn lại nút tắt âm hay nhấn nút cộng trừ hay không
                elif self.isMute == True:
                    self.isMute = False
                    if not self.isMute:
                        self.mute_button.imageNormal = 'mute.png'
                        self.mute_button.imageChanged = 'mute2.png'
                        present_volume=self.volume  # Khôi phục giá trị âm lượng
                        self.display_volume_label.text = f'{present_volume * 100}' #Khôi phục giá trị hiển thị âm lượng hiện tại
                        pygame.mixer.music.set_volume(present_volume)
        return self
    
#Quy định đối tượng màn hình cài đặt kích thước cửa sổ
class WindowModeSettingClass:
    def __init__(self):
        #Khởi tạo các thuộc tính
        self.fullScreenButton = Button(pos=(screen.get_width() / 2, screen.get_height() / 2 * 0.9), imageNormal = "continue.png", imageChanged = "continue2.png") # Nút để chỉnh chế độ cửa sổ, mặc định có text "Window"
        self.halfScreenButton = Button(pos=(screen.get_width() / 2, screen.get_height() / 2 * 0.9), imageNormal = "continue.png", imageChanged = "continue2.png") # Nút chuyển kích thước cửa sổ. Mặc định là 1920x1080
        self.esc_button = Button(pos=(screen.get_width() / 2, screen.get_height() / 2 * 1.2), imageNormal = "back.png", imageChanged = "back2.png") # Nút quay về
    #Vẽ các thuộc tính lên bề mặt
    def draw(self, mouse_pos):
        global LANGUAGE_INDEX
        Background = pygame.image.load(LANGUAGE[GameInit.LANGUAGE_INDEX]+'background.png').convert_alpha()
        Background = pygame.transform.smoothscale(Background, WINDOW_SIZES[GameInit.WINDOW_SIZE_INDEX])
        screen.blit(Background, (0, 0))
        if halfScreen_active:
            self.fullScreenButton.update(mouse_pos)
        else:
            self.halfScreenButton.update(mouse_pos)
        self.esc_button.update(mouse_pos)
    #Cập nhật trạng thái cho các thuộc tính
    def update(self, event):
        global halfScreen_active, screen
        #Lấy vị trí đầu con trỏ chuột
        pos = pygame.mouse.get_pos()
        #Kiểm tra xem có nhấn chuột không
        if event.type == pygame.MOUSEBUTTONDOWN:
            #Hàm isOver kiểm tra xem con trỏ chuột có đè lên các thuộc tính Button trong khi đang nhấn nút chuột trái hay không
            if self.fullScreenButton.CheckClick(pos):
                GameInit.halfScreen_active = not GameInit.halfScreen_active
                GameInit.WINDOW_SIZE_INDEX = 0
                GameInit.SCREEN_SIZE_INDEX = 0
                return self
            elif self.halfScreenButton.CheckClick(pos):
                GameInit.WINDOW_SIZE_INDEX = 1
                GameInit.SCREEN_SIZE_INDEX = 1
                GameInit.halfScreen_active = True
                return self
            if self.esc_button.CheckClick(pos):
                return SettingClass() #Trả về màn hình cài đặt
            elif event.type == pygame.VIDEORESIZE:
                # Xử lý sự kiện resize màn hình
                width, height = event.w, event.h
                screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)
        return self
        

class MapSelection:
    def draw(self, mouse_pos):
        Background = pygame.image.load(LANGUAGE[GameInit.LANGUAGE_INDEX]+'mapselection.png').convert_alpha()
        Background = pygame.transform.smoothscale(Background, WINDOW_SIZES[GameInit.WINDOW_SIZE_INDEX])
        screen.blit(Background, (0, 0))
    #Cập nhật trạng thái cho các thuộc tính
    def update(self, event):
        global InitGame, MAP_INDEX
        if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                Back_To_Menu = Pause_Game()
                if Back_To_Menu:
                    InitGame = False
                    return MenuClass()
            if event.key == pygame.K_1:
                GameInit.set_choice = 1
                MAP_INDEX = 0
                return CharacterSelection()
            if event.key == pygame.K_2:
                GameInit.set_choice = 2
                MAP_INDEX = 1
                return CharacterSelection()
            if event.key == pygame.K_3:
                GameInit.set_choice = 3
                MAP_INDEX = 2
                return CharacterSelection()
            if event.key == pygame.K_4:
                GameInit.set_choice = 4
                MAP_INDEX = 3
                return CharacterSelection()
            if event.key == pygame.K_5:
                GameInit.set_choice = 5
                MAP_INDEX = 4
                return CharacterSelection()
                
        return self
    
class CharacterSelection: 
    def draw(self, mouse_pos):
        Background = pygame.image.load(LANGUAGE[GameInit.LANGUAGE_INDEX]+'choose.png').convert_alpha()
        Background = pygame.transform.smoothscale(Background, WINDOW_SIZES[GameInit.WINDOW_SIZE_INDEX])
        screen.blit(Background, (0, 0))
    #Cập nhật trạng thái cho các thuộc tính
    def update(self, event):
        global InitGame
        if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                Back_To_Menu = Pause_Game()
                if Back_To_Menu:
                    InitGame = False
                    return MenuClass()
            if event.key == pygame.K_1:
                GameInit.choice = 1
                return Shop()
            if event.key == pygame.K_2:
                GameInit.choice = 2
                return Shop()
            if event.key == pygame.K_3:
                GameInit.choice = 3
                return Shop()
            if event.key == pygame.K_4:
                GameInit.choice = 4
                return Shop()
            if event.key == pygame.K_5:
                GameInit.choice = 5
                return Shop()
                
        return self


class Shop: 
    def draw(self, mouse_pos):
        Background = pygame.image.load(LANGUAGE[GameInit.LANGUAGE_INDEX]+'shopee.png').convert_alpha()
        Background = pygame.transform.smoothscale(Background, WINDOW_SIZES[GameInit.WINDOW_SIZE_INDEX])
        screen.blit(Background, (0, 0))
    #Cập nhật trạng thái cho các thuộc tính
    def update(self, event):
        global InitGame
        if not InitGame:
            init_character_luckybox()
            InitGame = True
        if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                Back_To_Menu = Pause_Game()
                if Back_To_Menu:
                    InitGame = False
                    return MenuClass()
            if event.key == pygame.K_1:
                GameInit.CHARACTERS[GameInit.choice - 1].NhanhNhen = True
                return Play()
            if event.key == pygame.K_2:
                GameInit.CHARACTERS[GameInit.choice - 1].TroiHon = True
                return Play()
            if event.key == pygame.K_3:
                GameInit.CHARACTERS[GameInit.choice - 1].PhanKhich = True
                return Play()
                
        return self