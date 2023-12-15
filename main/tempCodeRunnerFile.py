import pygame, sys
from io import StringIO

pygame.init()
WINDOW_SIZES = [pygame.display.get_desktop_sizes()[0], (768,432)]
WINDOW_SIZE_INDEX = 1
screen_Width = WINDOW_SIZES[WINDOW_SIZE_INDEX][0]
screen_Height = WINDOW_SIZES[WINDOW_SIZE_INDEX][1]
screen_ratio = WINDOW_SIZES[WINDOW_SIZE_INDEX][0] * WINDOW_SIZES[WINDOW_SIZE_INDEX][1] / (WINDOW_SIZES[0][0] * WINDOW_SIZES[0][1])
screen = pygame.display.set_mode(WINDOW_SIZES[WINDOW_SIZE_INDEX])
clock = pygame.time.Clock()
login_lock = True
historyLine = StringIO()
MenuSound = False
gameSound = False
LANGUAGE = ["./assets/background/ENG/", "./assets/background/VIET/"]
LANGUAGE_INDEX = 0
VOLUME = [0,0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]
VOLUME_INDEX = 0
present_volume = VOLUME[VOLUME_INDEX]
user_id = ''
user_info = ''
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
        global LANGUAGE_INDEX
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            self.image = pygame.image.load(LANGUAGE[LANGUAGE_INDEX] + self.imageChanged).convert_alpha()

        else:
            self.image = pygame.image.load(LANGUAGE[LANGUAGE_INDEX] + self.imageNormal).convert_alpha()
        screen.blit(self.image, self.rect)
    '''def update_images(self, imageNormal, imageChanged):
        self.imageNormal = pygame.image.load(LANGUAGE[LANGUAGE_INDEX] + self.imageNormal).convert_alpha()
        self.imageChanged = pygame.image.load(LANGUAGE[LANGUAGE_INDEX] + self.imageChanged).convert_alpha()'''
class MenuClass: 
    #Khởi tạo các thuộc tính
    def __init__(self):
        global VOLUME_INDEX, present_volume
        self.playButton = Button(pos = (screen.get_width() / 2, screen.get_height() / 2 * 0.9), imageNormal = f"play.png", imageChanged = "play2.png") # Nút có dòng chữ "Play game"
        self.settingsButton = Button(pos = (screen.get_width() / 2, screen.get_height() / 2 * 1.15), imageNormal = "settings.png", imageChanged = "settings2.png") # Nút có dòng chữ "Settings"
        self.minigame = Button(pos = (screen.get_width() / 2, screen.get_height() / 2 * 1.35), imageNormal = "minigame.png", imageChanged = "minigame2.png")
        self.historyButton = Button (pos=(screen.get_width() / 2, screen.get_height() / 2 * 1.55),imageNormal="history.png",imageChanged="history2.png")
        self.quitButton = Button(pos = (screen.get_width() / 2, screen.get_height() / 2 * 1.8), imageNormal = "quit.png", imageChanged = "quit2.png") # Nút có dòng chữ "Quit"
        #v self.changeLanguageButton = Button(pos=(screen.get_width() - screen.get_width() / 16, screen.get_height() - screen.get_height() / 16), imageNormal= "lang40.png", imageChanged= "lang240.png") # Nút chuyển đổi ngôn ngữ
    #Vẽ các thuộc tính lên màn hình
    def draw(self, mouse_pos):
        global user_id, screen_info
        Background = pygame.image.load(LANGUAGE[LANGUAGE_INDEX]+'background.png').convert_alpha()
        Background = pygame.transform.smoothscale(Background, WINDOW_SIZES[WINDOW_SIZE_INDEX])
        screen.blit(Background, (0, 0))
        self.playButton.update(mouse_pos)
        self.settingsButton.update(mouse_pos)
        self.quitButton.update(mouse_pos)
        self.historyButton.update(mouse_pos)
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
                #     flappy_bird()
                # else:
                MenuSound = False
                gameSound = False
                pass
            if self.settingsButton.CheckClick(pos):
                pass
            if self.quitButton.CheckClick(pos):
                pygame.quit()
                sys.exit()
            if self.minigame.CheckClick(pos):
                pass
            if self.historyButton.CheckClick(pos):
                pass
                    
        return self
def main():
    global login_lock, list_image_load,historyLine, screen
    if not login_lock:
        pygame.quit()
        sys.exit()
    #Lớp phủ xuất hiện đầu tiên chính là màn hình cài đặt
    print(historyLine.read())
    current_class = MenuClass()
    #Vòng lặp chính
    while True:  # Vòng lặp vô hạn, chương trình sẽ chạy cho đến khi có sự kiện thoát
        for event in pygame.event.get():  # Duyệt qua tất cả sự kiện đang chờ xử lý trong hàng đợi sự kiện của Pygame
            if event.type == pygame.QUIT:  # Nếu sự kiện là loại thoát (như nhấn nút đóng cửa sổ)
                pygame.quit()  # Thoát khỏi Pygame
                sys.exit()  # Thoát khỏi chương trình
            if event.type == pygame.VIDEORESIZE:
                screen = pygame.display.set_mode(WINDOW_SIZES[WINDOW_SIZE_INDEX])
            current_class = current_class.update(event)  # Cập nhật trạng thái của đối tượng hiện tại dựa trên sự kiện
        mouse_pos = pygame.mouse.get_pos()
        current_class.draw(mouse_pos)  # Vẽ đối tượng hiện tại lên màn hình
        pygame.display.flip()  # Cập nhật toàn bộ cửa sổ
        clock.tick(60)  # Đảm bảo chương trình chạy không quá 60 khung hình/giây
main()