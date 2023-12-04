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


#Gameplay
CheckPass = True

def Play():
    global CheckPass
    pygame.mixer.music.set_volume(present_volume)
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

        if FinishLine_Pass1 and Victory_sound_Play or FinishLine_Pass2 or FinishLine_Pass3 or FinishLine_Pass4 or FinishLine_Pass5:
            if CheckPass:
                pygame.mixer.music.load('assets/sounds/Victorious.ogg')
                pygame.mixer.music.play(loops = 0)
                Victory_sound_Play = False
                CheckPass = False
                
        
        activate_LuckyBox1 = Lucky_Box(Char1, IG_Objects)
        activate_LuckyBox2 = Lucky_Box(Char2, IG_Objects)
        activate_LuckyBox3 = Lucky_Box(Char3, IG_Objects)
        activate_LuckyBox4 = Lucky_Box(Char4, IG_Objects)
        activate_LuckyBox5 = Lucky_Box(Char5, IG_Objects)

        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    Back_To_Menu = Pause_Game()
                    if Back_To_Menu:
                        pygame.mixer.music.set_volume(present_volume)
                        pygame.mixer.music.load('assets/sounds/mainmenu.mp3')
                        pygame.mixer.music.play(loops = -1)
                        return

        #Bảng tiền
        # pygame.draw.rect(screen, "red", scoreBoard_Box, 6, 10)
        # screen.blit(scoreBoard, scoreBoard_Box)

        pygame.display.update()
        clock.tick(60)

#Tạm dừng trò chơi
def Pause_Game():
     while True:
        screen.blit(Background,(0,0))
        #Các nút ở trong Pause menu
        mouse_pos = pygame.mouse.get_pos()
        RETURN_TO_MENU = Button(pos=(screen.get_width() / 2, screen.get_height() / 2 - 50), text_base_color="Black", text_active_color="white", textIn="RETURN TO MENU")
        RETURN_TO_GAME = Button(pos=(screen.get_width() / 2, screen.get_height() / 2), text_base_color="Black", text_active_color="white", textIn="CONTINUE")
        QUIT = Button(pos=(screen.get_width() / 2, screen.get_height() / 2 + 50), text_base_color="Black", text_active_color="white", textIn="QUIT")

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
        screen.blit(Background,(0,0))
        mouse_pos = pygame.mouse.get_pos()
        #Các nút trong quit confirm
        Promptlabel = Label(screen.get_width() / 2 * 0.85, screen.get_height() / 2 * 0.7, 125, 50, 'Want to back the Menu Screen?')
        yesButton = Button(pos=(screen.get_width() / 2 * 1.2, screen.get_height() / 2), text_base_color="Black", text_active_color="white", textIn="YES")
        noButton = Button(pos=(screen.get_width() / 2 * 0.8, screen.get_height() / 2), text_base_color="Black", text_active_color="white", textIn="NO")

        Promptlabel.draw(screen)
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
        pygame.mixer.music.set_volume(present_volume)
        pygame.mixer.music.load('assets/sounds/mainmenu.mp3')
        pygame.mixer.music.play(loops = -1)
        self.playButton = Button(pos = (screen.get_width() / 2, screen.get_height() / 2 * 0.8), text_base_color= "black", text_active_color = "white", textIn = "PLAY") # Nút có dòng chữ "Play game"
        self.settingsButton = Button(pos = (screen.get_width() / 2, screen.get_height() / 2), text_base_color= "black", text_active_color = "white", textIn = "SETTINGS") # Nút có dòng chữ "Settings"
        self.quitButton = Button(pos = (screen.get_width() / 2, screen.get_height() / 2 * 1.2), text_base_color = "black", text_active_color = "white", textIn = "QUIT") # Nút có dòng chữ "Quit"
    #Vẽ các thuộc tính lên màn hình
    def draw(self, mouse_pos):
        screen.blit(Background, (0, 0))
        self.playButton.update(mouse_pos)
        self.settingsButton.update(mouse_pos)
        self.quitButton.update(mouse_pos)

    # Cập nhật các trạng thái của thuộc tính
    def update(self, event):
        pos = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if self.playButton.CheckClick(pos):
                Play()
            if self.settingsButton.CheckClick(pos):
                return SettingClass()
            if self.quitButton.CheckClick(pos):
                pygame.quit()
                sys.exit()
            
        return self

class SettingClass: #Khởi tạo các nút, label và Button. 
    def __init__(self):
        self.soundButton = Button(pos=(screen.get_width() / 2, screen.get_height() / 2 * 0.8), text_base_color="Black", text_active_color="white", textIn="SOUND")
        self.screenButton = Button(pos=(screen.get_width() / 2, screen.get_height() / 2), text_base_color="Black", text_active_color="white", textIn="SCREEN")
        self.escButton = Button(pos=(screen.get_width() / 2, screen.get_height() / 2 * 1.2), text_base_color="Black", text_active_color="white", textIn="BACK")
    #Vẽ các lớp phủ, các nút và chữ
    def draw(self, mouse_pos):
        screen.blit(Background,(0,0)) #Tạo một lớp phủ hình chữ nhật kích thước tối đa
        #Vẽ nút
        self.soundButton.update(mouse_pos)
        self.screenButton.update(mouse_pos)
        self.escButton.update(mouse_pos)
    #Cập nhật trạng thái của class
    def update(self, event):
        mouse_pos = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # Kiểm tra các đối tượng như nút chọn Âm lượng, chọn tùy chọn Màn hình, nút thoát; có được nhấn hay không. 
            # Nếu có thì trả về class tương ứng
            if self.soundButton.CheckClick(mouse_pos):
                return VolumeSettingClass()
            if self.screenButton.CheckClick(mouse_pos):
                pass
                # return WindowModeSettingClass()
            if self.escButton.CheckClick(mouse_pos):
                return MenuClass()
        return self


class VolumeSettingClass:
    #Khai báo các thuộc tính của class: 
    def __init__(self):
        # Khởi tạo các thuộc tính. 
        # Chú ý các thành phần như âm lượng hiện tại và chỉ số âm lượng được đánh dấu toàn cục. Sau này sẽ thêm các thuộc tính WINDOW
        global present_volume, VOLUME_INDEX
        self.label1 = Label(screen.get_width() / 2 * 0.95, screen.get_height() / 2 * 0.4,125,50,'Mute Volume') # Dòng chữ 'Mute Volume'  
        self.esc_button = Button((screen.get_width() / 2, screen.get_height() / 2 * 1.5),"black", "white",'Back')    # Nút có chữ 'Back'
        self.mute_button = Button((screen.get_width() / 2, screen.get_height() / 2 * 0.75),"black", "white", "Mute") # Nút có chữ 'Mute'
        self.label2 = Label(screen.get_width() / 2 * 0.92, screen.get_height() / 2 * 0.8,125,50,'Volume')     # dòng chữ "Volume"
        self.minusVol_button = Button((screen.get_width() / 2 * 0.8, screen.get_height() / 2 * 0.85),"black", "white",'-') #Các nút +, - để tăng giảm âm lượng
        self.plusVol_button = Button((screen.get_width() / 2 * 1.2, screen.get_height() / 2 * 0.85),"black", "white",'+')
        self.display_volume_label = Label(screen.get_width() / 2 * 0.95, screen.get_height() / 2,50,50, f"{present_volume * 100}") # Trường hiển thị âm lượng hiện tại
        
        self.isMute = False #Các biến khai báo. Ở đây là biến xác định xem có đang tắt âm hay không
        #Các khai báo cho xác định âm lượng của âm thanh
        self.volume_list = VOLUME
        self.volume = present_volume
        self.previous_volume = self.volume
        
    #Hàm vẽ các đối tượng trên màn hình
    def draw(self, mouse_pos):
        #Vẽ lớp phủ hình chữ nhật kích thước bằng kích thước cửa sổ hiện hành
        screen.blit(Background,(0,0))
        #Vẽ các thuộc tính khác đã nêu
        self.label1.draw(screen)
        self.label2.draw(screen)
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
                        self.mute_button.textIn = 'Muted' 
                        self.volume = present_volume #Lưu trữ giá trị âm lượng
                        present_volume = 0
                        self.display_volume_label.text = "0" #Đưa giá trị âm lượng về 0
                        pygame.mixer.music.set_volume(present_volume)
                #Kiểm tra xem liệu có nhấn lại nút tắt âm hay nhấn nút cộng trừ hay không
                elif self.isMute == True:
                    self.isMute = False
                    if not self.isMute:
                        self.mute_button.textIn = 'Mute'
                        present_volume=self.volume  # Khôi phục giá trị âm lượng
                        self.display_volume_label.text = f'{present_volume * 100}' #Khôi phục giá trị hiển thị âm lượng hiện tại
                        pygame.mixer.music.set_volume(present_volume)
        return self
    
