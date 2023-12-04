import pygame
import sys

# Quy định kích thước cửa sổ
WINDOWS_SCREEN_SIZE = [(1920,1080),(1366,768)]
global WINDOWS_INDEX
WINDOWS_INDEX = 0
# Nhạc menu chính
#Lí do cho việc khai báo ngoài là để dễ thay đổi luân phiên khi đưa vào hàm
my_sound = './assets/sounds/Panorama.wav'
#Quy định các thành phần âm lượng
VOLUME = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]
global VOLUME_INDEX
VOLUME_INDEX = 4
global present_volume
present_volume = VOLUME[VOLUME_INDEX]
global menu_track
#Quy định màu mặc định cho nút
button_color = (12, 53, 106) 
#Quy định các đối tượng dùng để tạo nút bấm cho menu
class Button:
    #Khởi tạo các thành phần của nút:
    def __init__(self, x, y, width, height, text=None, color=button_color, highlighted_color = (189,189,189)): 
        self.x = x # Tọa độ vị trí dưới dạng (x;y) trên màn hình
        self.y = y
        self.width = width #  Kích thước của nút, gồm chiều rộng, chiều cao
        self.height = height
        self.text = text # Chữ được hiển thị trên nút, mặc định là None
        self.color = color # Màu được hiển thị đầu tiên
        self.highlighted_color = highlighted_color # Màu được hiển thị khi tác động lên nút, ở đây là rê chuột vào
        self.font = pygame.font.Font('./assets/font/SVN-Retron_2000.ttf',60) #Phông mặc định. Ở đây là SVN-Retron_2000 để nhìn giống chữ Pixel
    #Gọi hàm vẽ nút, gồm các tham số như chính đối tượng Button, cửa sổ màn hình và đường viền, mặc định là None.
    def draw(self, win, outline=None):
        if outline: # Kiểm tra xem giá trị của đường viền được đưa vào: 
            pygame.draw.rect(win, outline, (self.x-2, self.y-2, self.width+4, self.height+4), 0) # Vẽ viền cho Button, rộng hơn một xí so với Button
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height), 0) # Vẽ hình chữ nhật làm biểu trưng cho Button
        if self.text: # Kiểm tra xem có giá trị text được đưa vào hay không
            font = pygame.font.Font('./assets/font/SVN-Retron_2000.ttf', 16) #Đặt giá trị font mặc định
            text = font.render(self.text, 1,(255,255,255)) #Màu text là màu đen, bật khử răng cưa cho text, áp dụng cho tất cả các text trong class
            win.blit(text, (self.x + (self.width / 2 - text.get_width() / 2), self.y + (self.height / 2 - text.get_height() / 2)))

    def isOver(self, pos): # Kiểm tra xem con trỏ chuột có nằm trong phạm vi kích thước của nút hay không
        if self.x < pos[0] < self.x + self.width: # Kiểm tra xem tọa độ x của con trỏ nằm trong khoảng (cạnh trái, cạnh phải = cạnh trái + giá trị chiều rộng)
            if self.y < pos[1] < self.y + self.height:# Kiểm tra xem tọa độ y của con trỏ nằm trong khoảng (cạnh trái, cạnh phải = cạnh trái + giá trị chiều cao)
                return True #Cả hai thỏa mãn,trả về True. Ngược lại, trả về False
        return False
#Quy định các thuộc tính chỉ tạo dòng chữ hiển thị trong menu
class Label: 
    # Khởi tạo các thuộc tính tương tự như các thuộc tính của Button
    def __init__(self, x, y, width, height, text=None, color=(73, 73, 73), highlighted_color=(189,189,189)):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.color = color
        self.highlighted_color = highlighted_color
        self.font = pygame.font.Font('./assets/font/SVN-Retron_2000.ttf',60) #Font mặc định
    # gọi hàm vẽ các Label, gồm các tham số như chính đối tượng Label, cửa sổ màn hình và đường viền, mặc định là None.
    def draw(self, win, outline=None):
        if self.text: # Kiểm tra xem có text được đưa vào hay không
            font = pygame.font.Font('./assets/font/SVN-Retron_2000.ttf', 16)
            text = font.render(self.text, 1, '#ffffff') #Màu text là màu đen, bật khử răng cưa cho text, áp dụng cho tất cả các text trong class
            win.blit(text, (self.x + (self.width / 2 - text.get_width() / 2), self.y + (self.height / 2 - text.get_height() / 2)))  #Đưa chữ lên cửa sổ màn hình
#Class này chỉ là phụ trợ cho việc kiểm tra xem có đang tắt âm hay không
class PressedTime:
    def __init__(self):
        self.count = 0
    def update(self,event):
        if event.type == pygame.KEYDOWN:
            self.count = self.count + 1
#Minh họa cho class chính. Có thể thay thế bằng bất kì đối tượng hay chương trình nào
class MainloopClass:
    def __init__(self):
        self.active = True
        self.x_position = 20 
        
    def draw(self, screen):
        pygame.draw.line(screen, (255, 0, 0), (self.x_position, 20), (self.x_position, 1060), 5)
        self.x_position += 5

    def update(self, event):
        if event.type == pygame.KEYDOWN:
            if self.active and self.x_position > 1900:
                self.x_position = 20
                return MenuClass()
            if event.key == pygame.K_ESCAPE or event.key == pygame.K_SPACE:  # Kiểm tra xem phím "Esc" hoặc phím cách có được nhấn không
                return PauseClass()  # Nếu phím "Esc" hoặc phím cách được nhấn, quay lại PauseClass
        return self
#Màn hình cài đặt
class SettingClass: #Khởi tạo các nút, label và Button. 
    def __init__(self):
        self.soundButton = Button(835, 300, 125, 50, 'Sound')
        self.screenButton = Button(835, 360, 125, 50, 'Screen')
        self.escButton = Button(235, 150, 60, 50, 'Back')
        #Quy định màu cho nút
        self.highlighted_color = (240, 178, 39)
        self.color = (12, 53, 106)
    #Vẽ các lớp phủ, các nút và chữ
    def draw(self, screen):
        pygame.draw.rect(screen,(44,150,210),pygame.Rect(0,0,WINDOWS_SCREEN_SIZE[WINDOWS_INDEX][0],WINDOWS_SCREEN_SIZE[WINDOWS_INDEX][1])) #Tạo một lớp phủ hình chữ nhật kích thước tối đa. Sau này nên chỉnh lại
        #Vẽ nút
        self.soundButton.draw(screen)
        self.screenButton.draw(screen)
        self.escButton.draw(screen)
    #Cập nhật trạng thái của class
    def update(self, event):
        pos = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Kiểm tra các đối tượng như nút chọn Âm lượng, chọn tùy chọn Màn hình, nút thoát; có được nhấn hay không. 
            # Nếu có thì trả về class tương ứng
            if self.soundButton.isOver(pos):
                return VolumeSettingClass()
            if self.screenButton.isOver(pos):
                return WindowModeSettingClass()
            if self.escButton.isOver(pos):
                return MenuClass()
            
        if event.type == pygame.MOUSEMOTION:
            # Kiểm tra con trỏ chuột có rê đến các nút như nút chọn Âm lượng, chọn tùy chọn Màn hình, nút thoát hay không. 
            # Nếu có thì trả về màu tô sáng tương ứng, ngược lại vẫn giữ nguyên màu đã định
            if self.soundButton.isOver(pos):
                self.soundButton.color = self.highlighted_color
            else:
                self.soundButton.color = self.color
            if self.screenButton.isOver(pos):
                self.screenButton.color = self.highlighted_color
            else:
                self.screenButton.color = self.color
            if self.escButton.isOver(pos):
                self.escButton.color = self.highlighted_color
            else:
                self.escButton.color = self.color
        return self
#Màn hình cài đặt âm lượng
class VolumeSettingClass:
    #Khai báo các thuộc tính của class: 
    def __init__(self):
        # Khởi tạo các thuộc tính. 
        # Chú ý các thành phần như âm lượng hiện tại và chỉ số âm lượng được đánh dấu toàn cục. Sau này sẽ thêm các thuộc tính WINDOW
        global present_volume
        global VOLUME_INDEX
        self.label1 = Label(835,300,125,50,'Mute Volume') # Dòng chữ 'Mute Volume' 
        self.esc_button = Button(235,150,60,50,'Back')    # Nút có chữ 'Back'
        self.mute_button = Button(835,360,125,50, "Mute") # Nút có chữ 'Mute'
        self.label2 = Label(835,420,125,50,'Volume')     # dòng chữ "Volume"
        self.minusVol_button = Button(805,480,50,50,'-') #Các nút +, - để tăng giảm âm lượng
        self.plusVol_button = Button(935,480,50,50,'+')
        self.display_volume_label = Label((805 + 935) / 2,480,50,50, f"{present_volume * 100}") # Trường hiển thị âm lượng hiện tại
        
        self.isMute = False #Các biến khai báo. Ở đây là biến xác định xem có đang tắt âm hay không
        #Các khai báo cho xác định âm lượng của âm thanh
        self.volume_list = VOLUME 
        self.volume = present_volume
        self.previous_volume = self.volume
        #Các khai báo cho màu
        self.color = (12, 53, 106) 
        self.highlighted_color = (240, 178, 39)
        self.muted_color = (179,19,18)
    #Hàm vẽ các đối tượng trên màn hình
    def draw(self, screen):
        #Vẽ lớp phủ hình chữ nhật kích thước bằng kích thước cửa sổ hiện hành
        pygame.draw.rect(screen,(44,150,210),pygame.Rect(0,0,WINDOWS_SCREEN_SIZE[WINDOWS_INDEX][0],WINDOWS_SCREEN_SIZE[WINDOWS_INDEX][1]))
        #Vẽ các thuộc tính khác đã nêu
        self.label1.draw(screen)
        self.label2.draw(screen)
        self.esc_button.draw(screen)
        self.mute_button.draw(screen)
        self.plusVol_button.draw(screen)
        self.minusVol_button.draw(screen)
        self.display_volume_label.draw(screen)
    #Cập nhật các trạng thái. Khai báo biến toàn cục là để giữ trạng thái âm lượng
    def update(self, event):
        #Đánh dấu toàn cục cho thuộc tính
        global present_volume
        global VOLUME_INDEX
        #Lấy vị trí đầu con trỏ chuột
        pos = pygame.mouse.get_pos()
        #Kiểm tra xem có nhấn chuột không
        if event.type == pygame.MOUSEBUTTONDOWN:
            #Hàm isOver kiểm tra xem con trỏ chuột có đè lên các thuộc tính Button trong khi đang nhấn nút chuột trái hay không
            if self.esc_button.isOver(pos):
                return SettingClass() #Nếu nhấn chuột vào esc_button, trả về màn hình cài đặt
            #Kiểm tra xem các nút cộng, trừ, có được nhấn hay không
            if self.plusVol_button.isOver(pos): 
                # Kiểm tra chỉ số VOLUME_INDEX. Chừa giá trị biên phải ra vì khi điều kiện thỏa mãn 
                # VOLUME_INDEX + 1 vượt quá chỉ số max của list
                if 0 <= VOLUME_INDEX < len(self.volume_list) -1:
                    VOLUME_INDEX += 1 #Lưu trữ các giá trị ra biến toàn cục
                    self.volume = self.volume_list[VOLUME_INDEX] #gán giá trị cho biến volume của class
                    present_volume = self.volume
                    pygame.mixer.music.set_volume(present_volume) #Đặt âm lượng theo giá trị vừa gán
                    self.display_volume_label.text = f'{present_volume * 100}'
            if self.minusVol_button.isOver(pos):
                # Kiểm tra chỉ số VOLUME_INDEX. Chừa giá trị biên trái ra vì khi điều kiện thỏa mãn 
                # VOLUME_INDEX - 1 vượt quá chỉ số min của list
                if len(self.volume_list) - 1 >= VOLUME_INDEX > 0 :
                    VOLUME_INDEX -= 1 #Lưu trữ các giá trị ra biến toàn cục
                    self.volume = self.volume_list[VOLUME_INDEX] #gán giá trị cho biến volume của class
                    present_volume = self.volume
                    pygame.mixer.music.set_volume(present_volume) #Đặt âm lượng theo giá trị vừa gán
                    self.display_volume_label.text = f'{present_volume * 100}' #Đặt nội dung label hiển thị âm lượng là âm lượng hiện tại
            # Hàm kiểm tra xem nút Mute có được nhấn hay không:     
            if self.mute_button.isOver(pos):
                if self.isMute == False:
                    self.isMute = True #Trả về True cho isMute rồi thực hiện lệnh setvolume về 0
                    if self.isMute:
                        self.mute_button.text = 'Muted' 
                        self.mute_button.color = self.muted_color
                        self.volume = present_volume #Lưu trữ giá trị âm lượng
                        present_volume = 0
                        self.display_volume_label.text = "0" #Đưa giá trị âm lượng về 0
                        pygame.mixer.music.set_volume(present_volume)
                #Kiểm tra xem liệu có nhấn lại nút tắt âm hay nhấn nút cộng trừ hay không
                elif self.isMute == True:
                    self.isMute = False
                    if not self.isMute:
                        self.mute_button.text = 'Mute'
                        self.mute_button.color = self.color
                        present_volume=self.volume  # Khôi phục giá trị âm lượng
                        self.display_volume_label.text = f'{present_volume * 100}' #Khôi phục giá trị hiển thị âm lượng hiện tại
                        pygame.mixer.music.set_volume(present_volume)    
        # Kiểm tra xem có đang rê chuột trên nút hay không
        if event.type == pygame.MOUSEMOTION:
            #Cấu trúc chung của nhóm này là khi phát hiện con trở nằm trên thuộc tính nút, nút sẽ đổi sang màu vàng, ngược lại thì giữ nguyên
            if self.esc_button.isOver(pos):
                self.esc_button.color = self.highlighted_color
            else:
                self.esc_button.color = self.color
            if self.mute_button.isOver(pos):
                self.mute_button.color = self.highlighted_color
            else:
                if self.mute_button.text == "Muted":
                    self.mute_button.color = self.muted_color
                elif self.mute_button.text == "Mute":
                    self.mute_button.color = self.color
        return self
#Quy định đối tượng màn hình cài đặt kích thước cửa sổ
class WindowModeSettingClass:
    def __init__(self):
        #Khởi tạo các thuộc tính
        self.label1 = Label(835, 300, 125, 50, 'Window Mode') # Dòng chữ "Window Mode"
        self.button1 = Button(835, 360, 125, 50, 'Window') # Nút để chỉnh chế độ cửa sổ, mặc định có text "Window"
        self.label2 = Label(835, 420, 125, 50, 'Screen Ratio') # Dòng chữ "Screen Ratio"
        self.button2 = Button(835, 480, 125, 50, '1920x1080') # Nút chuyển kích thước cửa sổ. Mặc định là 1920x1080
        self.esc_button = Button(235,150,60,50,'Back') # Nút quay về
        self.color = (12, 53, 106)
        self.highlighted_color = (240, 178, 39)
    #Vẽ các thuộc tính lên bề mặt
    def draw(self, screen):
        pygame.draw.rect(screen,(44,150,210),pygame.Rect(0,0,1920,1080))
        self.label1.draw(screen)
        self.button1.draw(screen)
        self.label2.draw(screen)
        self.button2.draw(screen)
        self.esc_button.draw(screen)
    #Cập nhật trạng thái cho các thuộc tính
    def update(self, event):
        #Lấy vị trí đầu con trỏ chuột
        pos = pygame.mouse.get_pos()
        #Kiểm tra xem có nhấn chuột không
        if event.type == pygame.MOUSEBUTTONDOWN:
            #Hàm isOver kiểm tra xem con trỏ chuột có đè lên các thuộc tính Button trong khi đang nhấn nút chuột trái hay không
            if self.button1.isOver(pos):
                # Thêm mã để thay đổi chế độ cửa sổ tại đây
                pass
            if self.button2.isOver(pos):
                # Thêm mã để thay đổi tỷ lệ màn hình tại đây
                pass
            if self.esc_button.isOver(pos):
                return SettingClass() #Trả về màn hình cài đặt
        # Kiểm tra xem có đang rê chuột trên nút hay không
        if event.type == pygame.MOUSEMOTION:
            #Hàm isOver kiểm tra xem con trỏ chuột có đè lên các thuộc tính Button trong khi đang nhấn nút chuột trái hay không
            # Điểm chung của các thuộc tính ở đây là: Nếu được rê chuột lên thì chuyển thành màu vàng, không thì trả về màu hiện tại
            if self.button1.isOver(pos):
                self.button1.color =  self.highlighted_color
            else:
                self.button1.color = self.color
            if self.button2.isOver(pos):
                self.button2.color = self.highlighted_color
            else:
                self.button2.color = self.color
            if self.esc_button.isOver(pos):
                self.esc_button.color = self.highlighted_color
            else:
                self.esc_button.color = self.color
        return self
# Lớp menu chính
class MenuClass: 
    #Khởi tạo các thuộc tính
    def __init__(self):
        self.playButton = Button(835, 450, 125, 50, 'Play game') # Nút có dòng chữ "Play game"
        self.settingsButton = Button(835, 530, 125, 50, 'Settings') # Nút có dòng chữ "Settings"
        self.quitButton = Button(835, 610, 125, 50, 'Quit') # Nút có dòng chữ "Quit"
        self.color = (12, 53, 106)
        self.highlighted_color = (240, 178, 39)
    #Vẽ các thuộc tính lên màn hình
    def draw(self, screen):
        pygame.draw.rect(screen,(44,150,210),pygame.Rect(0,0,1920,1080))
        self.playButton.draw(screen)
        self.settingsButton.draw(screen)
        self.quitButton.draw(screen)
    # Cập nhật các trạng thái của thuộc tính
    def update(self, event):
        pos = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.playButton.isOver(pos):
                return MainloopClass()
            if self.settingsButton.isOver(pos):
                return SettingClass()
            if self.quitButton.isOver(pos):
                pygame.quit()
                sys.exit()
        if event.type == pygame.MOUSEMOTION:
            if self.playButton.isOver(pos):
                self.playButton.color = self.highlighted_color
            else:
                self.playButton.color = self.color
            if self.settingsButton.isOver(pos):
                self.settingsButton.color = self.highlighted_color
            else:
                self.settingsButton.color = self.color
            if self.quitButton.isOver(pos):
                self.quitButton.color = self.highlighted_color
            else:
                self.quitButton.color = self.color
        return self
class PauseClass:
    def __init__(self):
        self.continueLabel = Label(835, 250, 125, 50, 'Want to continue?')
        self.continueButton = Button(835, 300, 125, 50, 'Continue')
        self.quitButton = Button(835, 360, 125, 50, 'Quit')
        self.color = (12, 53, 106)
        self.highlighted_color = (240, 178, 39)

    def draw(self, screen):
        pygame.draw.rect(screen,(44,150,210),pygame.Rect(0,0,1920,1080))
        self.continueLabel.draw(screen)
        self.continueButton.draw(screen)
        self.quitButton.draw(screen)

    def update(self, event):
        pos = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.continueButton.isOver(pos):
                return MainloopClass() # Ở đây MainloopClass bị trả về trạng thái ban đầu
            if self.quitButton.isOver(pos):
                return QuitConfirmClass()
        if event.type == pygame.MOUSEMOTION:
            if self.continueButton.isOver(pos):
                self.continueButton.color = self.highlighted_color
            else:
                self.continueButton.color = self.color
            if self.quitButton.isOver(pos):
                self.quitButton.color = self.highlighted_color
            else:
                self.quitButton.color = self.color
        return self

class QuitConfirmClass:
    def __init__(self):
        self.label = Label(835, 300, 125, 50, 'Want to back the Menu Screen?')
        self.yesButton = Button(835, 360, 125, 50, 'Yes')
        self.noButton = Button(835, 420, 125, 50, 'No')
        self.color = (12, 53, 106)
        self.highlighted_color = (240, 178, 39)

    def draw(self, screen):
        pygame.draw.rect(screen,(44,150,210),pygame.Rect(0,0,1920,1080))
        self.label.draw(screen)
        self.yesButton.draw(screen)
        self.noButton.draw(screen)

    def update(self, event):
        pos = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.yesButton.isOver(pos):
                return MenuClass()
            if self.noButton.isOver(pos):
                return PauseClass()
        if event.type == pygame.MOUSEMOTION:
            if self.yesButton.isOver(pos):
                self.yesButton.color = self.highlighted_color
            else:
                self.yesButton.color = self.color
            if self.noButton.isOver(pos):
                self.noButton.color = self.highlighted_color
            else:
                self.noButton.color = self.color
        return self

def main(): #Hàm chính của vòng lặp
    #Khởi tạo pygame và pygame.mixer để chạy vòng lặp với tạo mixer cho nhạc
    pygame.init()
    pygame.mixer.init()
    menu_track = pygame.mixer.music.load(my_sound) #Load nhạc
    pygame.mixer.music.play() #Lên nhạc
    pygame.mixer.music.set_volume(VOLUME[VOLUME_INDEX]) #Đặt âm lượng mặc định
    screen = pygame.display.set_mode((1920, 1080)) #Đặt cửa sổ mặc định
    clock = pygame.time.Clock() #Đặt đồng hồ
    #Lớp phủ xuất hiện đầu tiên chính là màn hình cài đặt
    current_class = MenuClass()
#Vòng lặp chính
    while True:  # Vòng lặp vô hạn, chương trình sẽ chạy cho đến khi có sự kiện thoát
        for event in pygame.event.get():  # Duyệt qua tất cả sự kiện đang chờ xử lý trong hàng đợi sự kiện của Pygame
            if event.type == pygame.QUIT:  # Nếu sự kiện là loại thoát (như nhấn nút đóng cửa sổ)
                pygame.quit()  # Thoát khỏi Pygame
                sys.exit()  # Thoát khỏi chương trình
            current_class = current_class.update(event)  # Cập nhật trạng thái của đối tượng hiện tại dựa trên sự kiện

        screen.fill((0, 0, 0))  # Điền màn hình với màu đen
        current_class.draw(screen)  # Vẽ đối tượng hiện tại lên màn hình

        pygame.display.flip()  # Cập nhật toàn bộ cửa sổ
        clock.tick(60)  # Đảm bảo chương trình chạy không quá 60 khung hình/giây

if __name__ == "__main__":
    main()
