import pygame, random, sys, time
import LoginSignup1
from datetime import datetime
from io import StringIO 
from LoginSignup1 import *
from flappybird import minigame
import re
#Khởi tạo các thứ

# Luôn đặt cửa sổ xuất hiện từ góc trái màn hình
pygame.init()
pygame.display.set_caption("Race game")
clock = pygame.time.Clock()
random.seed(datetime.now().timestamp())

# Đường dẫn đén file thông tin người chơi
account_sub_path = './assets/player/'
#Ngôn ngữ
LANGUAGE = ["./assets/background/ENG/", "./assets/background/VIET/"]
LANGUAGE_INDEX = 0
money_bet_list = [200,500,1000]
#Các biến cần dùng
user_id = LoginSignup1.user_id
user_pwd = ''
historyLine = StringIO() # một dòng cần xem của history
traceBackCount = 0
user_money = int(LoginSignup1.user_money)
set_choice = 1
choice = 0
list_image_load = []
list_charImage = [] # Lưu trữ lại giá trị của list_image_load
money_choice = 0
bet_money = 0
bua_money = 0
# store 5 characters
CHARACTERS = []
LUCKYBOX = []
GROUP = []
rank = [] #List nhân vật khi thắng đc thêm vào
winner = 0
last = 0
doesWin = 1
#################Khu vực để Minigame####################
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
bright_red = pygame.Color(255, 0, 0)
old_red = pygame.Color(200, 0, 0)
color = pygame.Color('lightskyblue3')
#Lấy các biến từ file khác

#Mod lại subpath để có thể đưa menugame vào:
subpath = './main/flappybird'
account_sub_path = './assets/player/'
pygame.init()
clock = pygame.time.Clock()
WINDOW_SIZES = [pygame.display.get_desktop_sizes()[0], (768,432)]
WINDOW_SIZE_INDEX = 0
screen_Width = WINDOW_SIZES[WINDOW_SIZE_INDEX][0]
screen_Height = WINDOW_SIZES[WINDOW_SIZE_INDEX][1]
screen = pygame.display.set_mode(WINDOW_SIZES[WINDOW_SIZE_INDEX], pygame.RESIZABLE)
pygame.display.set_caption('Flappy Bird')
running = True
# Phông chữ :
font = pygame.font.SysFont("comicsansms", int(screen_Width / screen_Width * 32))
text_Font = pygame.font.Font(None, int(screen_Width / screen_Width * 38))
menu_Font = pygame.font.Font(None, int(screen_Width / screen_Width * 45))

# vẽ hình chữ nhật chứa text
rect_text = pygame.Rect(screen_Width / (screen_Width / 568), screen_Height / (screen_Height / 440), screen_Width / (screen_Width / 350),
                        screen_Height / (screen_Height / 40))

# Nút bấm

width = screen_Width / (15 / 2)
height = screen_Height / 16

x_back_button = screen_Width / (15 / 13)
y_back_button = screen_Height / (8 / 6)

#Cập nhật trạng thái account. Cần sửa file này
def update_account(usr_id, money):
    with open(f'{account_sub_path}/{user_id}/{user_id}.txt', 'r') as old_file:
        lines = old_file.readlines()
        lines[1] = str(money) + '\n'
    with open(f'{account_sub_path}/{user_id}/{user_id}.txt', 'w') as new_file:
        new_file.writelines(lines)


def show_fps(screen, clock):
    # Tạo font chữ
    font = pygame.font.Font(None, 30)
    # Tính toán FPS
    fps = str(int(clock.get_fps()))
    # Tạo text surface
    text = font.render("FPS: " + fps, 1, pygame.Color("red"))
    # Vẽ text surface lên màn hình
    screen.blit(text, (0, 0))

def flappy_bird():
    #Khai báo các thành phần toàn cục
    global screen_Width, screen_Height, screen, text_Font, menu_Font, font, tube1_height, tube2_height, tube3_height, tube4_height
    global user_id, user_money
    running = True
    # Màu đen 
    BLACK = (0, 0, 0)
    screen = pygame.display.set_mode((screen_Width, screen_Height), pygame.RESIZABLE)
    clock = pygame.time.Clock()
    #Quy định các thành phần cục bộ: Chiều rộng ống, tốc độ của ống để di chuyển
    TUBE_WIDTH = int(screen_Width / 30)
    TUBE_VELOCITY = int(screen_Width / 250)
    TUBE_GAP = int(screen_Height * 23 / 80)
    #Quy định các vị trí ống xuất hiện
    tube1_x = int(screen_Width * 6 / 15)
    tube2_x = int(screen_Width * 8 / 15)
    tube3_x = int(screen_Width * 10 / 15)
    # Quy định chiều cao spawn ống ngẫu nhiên
    tube1_height = random.randint(int(screen_Height / 8), int(screen_Height * 5 / 16))
    tube2_height = random.randint(int(screen_Height / 8), int(screen_Height * 5 / 16))
    tube3_height = random.randint(int(screen_Height / 8), int(screen_Height * 5 / 16))
    #Các quy định về tốc độ chim bay, vị trí của chim, trong lực
    BIRD_X = screen_Width * 2 / 15
    bird_y = screen_Height / (2)
    BIRD_WIDTH = int(screen_Width * 7 / 300)
    BIRD_HEIGHT = int(screen_Height * 7 / 300)
    bird_drop_velocity = 0
    GRAVITY = 0.7
    #Điểm. Sẽ reset khi nhấn nút chơi lại
    score = 0
    #Load font. Sau này chỉnh sửa chỗ này lại cho dùng font mình
    fontend = pygame.font.SysFont('sans', 50)
    # Các biến thông báo chim vượt qua ống hay chưa
    tube1_pass = False
    tube2_pass = False
    tube3_pass = False

    pausing = False
    run = False
    begin = False
    dem = 0
    check = 0
    
    while running:
        global user_id, user_money
        #pygame.mixer.music.pause()
        #clock.tick(60) đã được quy định. Có thể xóa dòng này
        clock.tick(120)
        #Khởi tạo và vẽ ảnh lên màn hình
        background_image = pygame.image.load(f"{subpath}/flappybird/background.png").convert_alpha()
        background_image = pygame.transform.scale(background_image, (screen_Width, screen_Height))
        screen.blit(background_image, (0, 0))
        
        #Load các thông số người chơi: ID, money
        user_info = text_Font.render('ID: ' + user_id, True, black)
        money_info = text_Font.render('Money: ' + str(user_money), True, black)
        #Tạo nút back có text màu trăng
        back_button = font.render('Back', True, black)
        #Viết thông tin ID và số tiền. Hiện tại k lấy đc
        screen.blit(user_info, (screen_Width - user_info.get_width() - money_info.get_width() - 40, 10))
        screen.blit(money_info,
                    (screen_Width - money_info.get_width() - screen_Width / (screen_Width / 20), screen_Height / (screen_Height / 10)))
        bird_image = pygame.image.load(f"{subpath}/flappybird/bird.png").convert_alpha()
        bird_image = pygame.transform.scale(bird_image, (BIRD_WIDTH, BIRD_HEIGHT))
        base_image = pygame.image.load(f"{subpath}/flappybird/base.png").convert_alpha()
        base_image = pygame.transform.scale(base_image, (screen_Width, screen_Height // 4))

        tube_image1 = pygame.image.load(f"{subpath}/flappybird/pipe1.png").convert_alpha()
        tube_image1 = pygame.transform.scale(tube_image1, (TUBE_WIDTH, tube1_height))
        tube_inv_image1 = pygame.image.load(f"{subpath}/flappybird/pipe2.png").convert_alpha()
        tube_inv_image1 = pygame.transform.scale(tube_inv_image1, (TUBE_WIDTH, screen_Height - tube1_height - TUBE_GAP))

        tube_image2 = pygame.image.load(f"{subpath}/flappybird/pipe1.png").convert_alpha()
        tube_image2 = pygame.transform.scale(tube_image2, (TUBE_WIDTH, tube2_height))
        tube_inv_image2 = pygame.image.load(f"{subpath}/flappybird/pipe2.png").convert_alpha()
        tube_inv_image2 = pygame.transform.scale(tube_inv_image2, (TUBE_WIDTH, screen_Height - tube2_height - TUBE_GAP))

        tube_image3 = pygame.image.load(f"{subpath}/flappybird/pipe1.png").convert_alpha()
        tube_image3 = pygame.transform.scale(tube_image3, (TUBE_WIDTH, tube3_height))
        tube_inv_image3 = pygame.image.load(f"{subpath}/flappybird/pipe2.png").convert_alpha()
        tube_inv_image3 = pygame.transform.scale(tube_inv_image3, (TUBE_WIDTH, screen_Height - tube3_height - TUBE_GAP))

        # Draw tube
        tube1_rect = screen.blit(tube_image1, (tube1_x, 0))
        tube2_rect = screen.blit(tube_image2, (tube2_x, 0))
        tube3_rect = screen.blit(tube_image3, (tube3_x, 0))


        # Draw tube inverse
        tube1_rect_inv = screen.blit(tube_inv_image1, (tube1_x, tube1_height + TUBE_GAP))
        tube2_rect_inv = screen.blit(tube_inv_image2, (tube2_x, tube2_height + TUBE_GAP))
        tube3_rect_inv = screen.blit(tube_inv_image3, (tube3_x, tube3_height + TUBE_GAP))


        # draw sand
        sand_rect = screen.blit(base_image, (0, screen_Height / (8 / 6)))
        # draw bird
        bird_rect = screen.blit(bird_image, (BIRD_X, bird_y))
        if begin == False:
            begin_txt = fontend.render("Press Space to Play", True, BLACK)
            screen.blit(begin_txt, (screen_Width / 2, screen_Height / 2))
        if run == True:
            # move tube to the left
            tube1_x = tube1_x - TUBE_VELOCITY
            tube2_x = tube2_x - TUBE_VELOCITY
            tube3_x = tube3_x - TUBE_VELOCITY

            # bird falls
            bird_y += bird_drop_velocity
            bird_drop_velocity += GRAVITY
            # generate new tubes
            if tube1_x < -TUBE_WIDTH:
                tube1_x = screen_Width / (screen_Width / 550)
                tube1_height = random.randint(screen_Height // (screen_Width // 100), screen_Height // (screen_Width // 250))
                tube1_pass = False
            if tube2_x < -TUBE_WIDTH:
                tube2_x = screen_Width / (screen_Width / 550)
                tube2_height = random.randint(screen_Height // (screen_Width // 100), screen_Height // (screen_Width // 250))
                tube2_pass = False
            if tube3_x < -TUBE_WIDTH:
                tube3_x = screen_Width / (screen_Width / 550)
                tube3_height = random.randint(screen_Height // (screen_Width // 100), screen_Height // (screen_Width // 250))
                tube3_pass = False

            score_txt = fontend.render("Score: " + str(score) + ", max score = 20", True, BLACK)
            screen.blit(score_txt, (screen_Width / (15 / 8), screen_Height / 2))
        # update điểm. Chạy âm tăng điểm khi chim đi qua
        if tube1_x + TUBE_WIDTH <= BIRD_X and tube1_pass == False:
            pygame.mixer.Sound(f'{subpath}/flappybird/sounds/point.wav').play()
            score += 1
            tube1_pass = True
        if tube2_x + TUBE_WIDTH <= BIRD_X and tube2_pass == False:
            pygame.mixer.Sound(f'{subpath}/flappybird/sounds/point.wav').play()
            score += 1
            tube2_pass = True
        if tube3_x + TUBE_WIDTH <= BIRD_X and tube3_pass == False:
            pygame.mixer.Sound(f'{subpath}/flappybird/sounds/point.wav').play()
            score += 1
            tube3_pass = True

        mouse = pygame.mouse.get_pos()
        # check collision
        for tube in [tube1_rect, tube2_rect, tube3_rect, tube1_rect_inv, tube2_rect_inv, tube3_rect_inv, sand_rect]:
            if bird_rect.colliderect(tube) or score == 20:
                pausing = True
                run = False
                TUBE_VELOCITY = 0
                bird_drop_velocity = 0
                if dem == 0:
                    pygame.mixer.Sound(f'{subpath}/flappybird/sounds/hit.wav').play()
                    dem = 1
                game_over_txt = fontend.render("Game over, score: " + str(score), True, BLACK)
                screen.blit(game_over_txt, (screen_Width / (screen_Width / 750), screen_Height / (screen_Height / 170)))
                money_receiver = fontend.render("the money you get: " + str(score * 10), True, BLACK)
                screen.blit(money_receiver, (screen_Width / (screen_Width / 750), screen_Height / (screen_Height / 270)))
                press_space_txt = fontend.render("Press Space to Play again", True, BLACK)
                screen.blit(press_space_txt, (screen_Width / (screen_Width / 750), screen_Height / (screen_Height / 370)))
                
                if check == 0:
                    user_money += (score * 10)
                    update_account(user_id, user_money)
                    check = 1
                if x_back_button + width > mouse[0] > x_back_button and y_back_button + height > mouse[
                    1] > y_back_button:  # tạo hiệu ứng khi click  vào logo
                    pygame.draw.rect(screen, bright_red,
                                     (x_back_button, y_back_button, screen_Width / (15), screen_Height / (16)))
                else:
                    pygame.draw.rect(screen, old_red,
                                     (x_back_button, y_back_button, screen_Width / (15), screen_Height / (16)))
                screen.blit(back_button, (x_back_button + 10, y_back_button))
        # Nền hoạt động chính của game. Chú ý cái video resize
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.VIDEORESIZE:
                screen_Width, screen_Height = event.size
                screen = pygame.display.set_mode((screen_Width, screen_Height), pygame.RESIZABLE)
                #Sửa vị trí
                text_Font = pygame.font.Font(None, int(screen_Width / screen_Width * 28)) # Thay thế bằng font của ta
                menu_Font = pygame.font.Font(None, int(screen_Width / screen_Width * 45))
                font = pygame.font.SysFont("comicsansms", int(screen_Width / screen_Width * 32))
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    # reset 
                    if pausing:
                        bird_y = screen_Height / (2)
                        TUBE_VELOCITY = 8
                        tube1_x = screen_Width / (screen_Width / 600)
                        tube2_x = screen_Width / (screen_Width / 800)
                        tube3_x = screen_Width / (screen_Width / 1000)


                        tube1_height = random.randint(int(screen_Height / 8), int(screen_Height * 5 / 16))
                        tube2_height = random.randint(int(screen_Height / 8), int(screen_Height * 5 / 16))
                        tube3_height = random.randint(int(screen_Height / 8), int(screen_Height * 5 / 16))

                        score = 0
                        dem = 0
                        check = 0
                        pausing = False
                    if run == False:
                        run = True
                        begin = True
                        dem = 0
                    pygame.mixer.Sound(f'{subpath}/flappybird/sounds/wing.wav').play()
                    pygame.mixer.music.set_volume(present_volume)
                    bird_drop_velocity = 0
                    bird_drop_velocity -= screen_Height/80
            if event.type == pygame.MOUSEBUTTONUP:
                if x_back_button + width > mouse[0] > x_back_button and y_back_button + height > mouse[
                    1] > y_back_button:
                    print('end game')
                    update_account(user_id, user_money)
                    pygame.mixer.music.load(f'./assets/sounds/mainmenu.mp3')
                    pygame.mixer.music.set_volume(present_volume)
                    pygame.mixer.music.play()
                    return 2

        show_fps(screen, clock)
        pygame.display.flip()
        pygame.mixer.init()
        pygame.mixer.music.load(f'{subpath}/Sounds/nhac2.wav')
        pygame.mixer.music.set_volume(present_volume)
        pygame.mixer.music.play()
##############################################################

class Money:
    global user_money, user_id
    global bet_money, bua_money
    global historyLine
    global traceBackCount
    global doesWin

    def writeMoney():
        with open(f'./assets/player/{user_id}/{user_id}.txt') as f:
            lines = f.readlines()
        lines[1] = f"{user_money}\n" # Thay đổi dòng cần thiết. Ở đây thay thế money.
        with open(f'./assets/player/{user_id}/{user_id}.txt','w') as f:
            f.writelines(lines) # Ghi lại tien
    
    def updateMoneyAndWriteHistory():
        global traceBackCount
        if doesWin:
            user_money += bet_money * 3 
            result = f"win +{bet_money * 3}"
        else:
            user_money -= bet_money
            result = f'lose -{bet_money}'
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        result_to_write = f"{current_time}: {user_id} {result}, balance: {user_money}"

        with open(f'./assets/player/{user_id}/{user_id}.txt', 'a') as file:
            file.write('\n'+ result_to_write)
        traceBackCount = 0

    def updateMuaBuaMoney():
        user_money -= bua_money

class History:
    global traceBackCount, user_id, historyLine
    def readHistorLineFromFile():
        with open(f'./assets/player/{user_id}/{user_id}.txt', 'r') as file:
            lines = file.readlines()
            line_number = len(lines) - 1 - traceBackCount
            if line_number < len(lines) and line_number >= 2:
                historyLine.truncate(0) #cắt ngắn hết ký tự ở historyline
                historyLine.seek(0) #trỏ vào đầu chuỗi đấy
                historyLine.write(lines[line_number]) #viết mới vào biến đệm str historyline
    #def buttonBack():
    #def buttonNext():
    #def traceBack():


#Màn hình cài đặt âm lượng
VOLUME = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]
VOLUME_INDEX = 4
present_volume = VOLUME[VOLUME_INDEX]
MenuSound = False
gameSound = False
#Kích thước màn hình (Do chưa có pygame_menu nên tạm thời bỏ qua)
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
map2 = pygame.transform.smoothscale(map2, WINDOW_SIZES[WINDOW_SIZE_INDEX])
map3 = pygame.image.load('assets/background/map3.png').convert_alpha()
map3 = pygame.transform.smoothscale(map3, WINDOW_SIZES[WINDOW_SIZE_INDEX])
map4 = pygame.image.load('assets/background/map4.png').convert_alpha()
map4 = pygame.transform.smoothscale(map4, WINDOW_SIZES[WINDOW_SIZE_INDEX])
map5 = pygame.image.load('assets/background/map5.png').convert_alpha()
map5 = pygame.transform.smoothscale(map5, WINDOW_SIZES[WINDOW_SIZE_INDEX])
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

Char1Map2 = ['assets/characters/Char1Map2_1.png', 'assets/characters/Char1Map2_2.png',
            'assets/characters/Char1Map2_3.png', 'assets/characters/Char1Map2_4.png']
Char2Map2 = ['assets/characters/Char2Map2_1.png', 'assets/characters/Char2Map2_2.png',
            'assets/characters/Char2Map2_3.png', 'assets/characters/Char2Map2_4.png']
Char3Map2 = ['assets/characters/Char3Map2_1.png', 'assets/characters/Char3Map2_2.png',
            'assets/characters/Char3Map2_3.png', 'assets/characters/Char3Map2_4.png']
Char4Map2 = ['assets/characters/Char4Map2_1.png', 'assets/characters/Char4Map2_2.png',
            'assets/characters/Char4Map2_3.png', 'assets/characters/Char4Map2_4.png']
Char5Map2 = ['assets/characters/Char5Map2_1.png', 'assets/characters/Char5Map2_2.png',
            'assets/characters/Char5Map2_3.png', 'assets/characters/Char5Map2_4.png']

Char1Map3 = ['assets/characters/Char1Map3_1.png', 'assets/characters/Char1Map3_2.png',
            'assets/characters/Char1Map3_3.png', 'assets/characters/Char1Map3_4.png']
Char2Map3 = ['assets/characters/Char2Map3_1.png', 'assets/characters/Char2Map3_2.png',
            'assets/characters/Char2Map3_3.png', 'assets/characters/Char2Map3_4.png']
Char3Map3 = ['assets/characters/Char3Map3_1.png', 'assets/characters/Char3Map3_2.png',
            'assets/characters/Char3Map3_3.png', 'assets/characters/Char3Map3_4.png']
Char4Map3 = ['assets/characters/Char4Map3_1.png', 'assets/characters/Char4Map3_2.png',
            'assets/characters/Char4Map3_3.png', 'assets/characters/Char4Map3_4.png']
Char5Map3 = ['assets/characters/Char5Map3_1.png', 'assets/characters/Char5Map3_2.png',
            'assets/characters/Char5Map3_3.png', 'assets/characters/Char5Map3_4.png']

Char1Map4 = ['assets/characters/Char1Map4_1.png', 'assets/characters/Char1Map4_2.png',
            'assets/characters/Char1Map4_3.png', 'assets/characters/Char1Map4_4.png']
Char2Map4 = ['assets/characters/Char2Map4_1.png', 'assets/characters/Char2Map4_2.png',
            'assets/characters/Char2Map4_3.png', 'assets/characters/Char2Map4_4.png']
Char3Map4 = ['assets/characters/Char3Map4_1.png', 'assets/characters/Char3Map4_2.png',
            'assets/characters/Char3Map4_3.png', 'assets/characters/Char3Map4_4.png']
Char4Map4 = ['assets/characters/Char4Map4_1.png', 'assets/characters/Char4Map4_2.png',
            'assets/characters/Char4Map4_3.png', 'assets/characters/Char4Map4_4.png']
Char5Map4 = ['assets/characters/Char5Map4_1.png', 'assets/characters/Char5Map4_2.png',
            'assets/characters/Char5Map4_3.png', 'assets/characters/Char5Map4_4.png']

Char1Map5 = ['assets/characters/Char1Map5_1.png', 'assets/characters/Char1Map5_2.png',
            'assets/characters/Char1Map5_3.png', 'assets/characters/Char1Map5_4.png']
Char2Map5 = ['assets/characters/Char2Map5_1.png', 'assets/characters/Char2Map5_2.png',
            'assets/characters/Char2Map5_3.png', 'assets/characters/Char2Map5_4.png']
Char3Map5 = ['assets/characters/Char3Map5_1.png', 'assets/characters/Char3Map5_2.png',
            'assets/characters/Char3Map5_3.png', 'assets/characters/Char3Map5_4.png']
Char4Map5 = ['assets/characters/Char4Map5_1.png', 'assets/characters/Char4Map5_2.png',
            'assets/characters/Char4Map5_3.png', 'assets/characters/Char4Map5_4.png']
Char5Map5 = ['assets/characters/Char5Map5_1.png', 'assets/characters/Char5Map5_2.png',
            'assets/characters/Char5Map5_3.png', 'assets/characters/Char5Map5_4.png']


#Nhân vật, tốc độ, vị trí
CharsMap1 = [Char1Map1, Char2Map1, Char3Map1, Char4Map1, Char5Map1]
CharsMap2 = [Char1Map2, Char2Map2, Char3Map2, Char4Map2, Char5Map2]
CharsMap3 = [Char1Map3, Char2Map3, Char3Map3, Char4Map3, Char5Map3]
CharsMap4 = [Char1Map4, Char2Map4, Char3Map4, Char4Map4, Char5Map4]
CharsMap5 = [Char1Map5, Char2Map5, Char3Map5, Char4Map5, Char5Map5]
RandSpeed = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4]
Speed = []
for x in range(5):
    Speed.append(random.choice(RandSpeed))
Position = [(WINDOW_SIZES[WINDOW_SIZE_INDEX][0] * 0.01, WINDOW_SIZES[WINDOW_SIZE_INDEX][1] * 0.55), 
            (WINDOW_SIZES[WINDOW_SIZE_INDEX][0] * 0.01, WINDOW_SIZES[WINDOW_SIZE_INDEX][1] * 0.66), 
            (WINDOW_SIZES[WINDOW_SIZE_INDEX][0] * 0.01, WINDOW_SIZES[WINDOW_SIZE_INDEX][1] * 0.76), 
            (WINDOW_SIZES[WINDOW_SIZE_INDEX][0] * 0.01, WINDOW_SIZES[WINDOW_SIZE_INDEX][1] * 0.87), 
            (WINDOW_SIZES[WINDOW_SIZE_INDEX][0] * 0.01, WINDOW_SIZES[WINDOW_SIZE_INDEX][1] * 0.98)]

#Ktra nhạc đã phát chưa
Victory_sound_Play = True

#Các nhân vật trong game
class Character():
    def __init__(self, speed, pos, number, image, map):
        global set_choice, SCREEN_SIZE_INDEX
        self.speed = speed
        self.tempSpeed = speed
        self.pos = pos
        self.x = self.pos[0]
        self.y = self.pos[1]
        self.number = number
        self.run = True
        self.count_run = 0
        self.image_path = image
        self.image = pygame.image.load(image).convert_alpha()
        self.original_image = pygame.image.load(SCREEN_SIZE[SCREEN_SIZE_INDEX] + 'Char' + str(self.number + 1) + 'Map' + str(int(set_choice)) + '_4.png').convert_alpha()
        self.rect= self.image.get_rect(midbottom = (self.x, self.y))
        self.count_run = 0
        self.map = map
        self.Finish = False
        self.isGoBack = False
        self.PhanKhich = False
        self.TroiHon = False
        self.NhanhNhen = False
        self.KichHoatBua = False
        self.active_time = pygame.time.get_ticks()
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
        elif self.map == 1:
            if self.number == 0:
                if self.run:
                    self.image = pygame.image.load(CharsMap2[0][int(self.count_run)]).convert_alpha()
                    self.count_run += 0.1
                else:
                    self.image = pygame.image.load(CharsMap2[0][int(self.count_run)]).convert_alpha()
            if self.number == 1:
                if self.run:
                    self.image = pygame.image.load(CharsMap2[1][int(self.count_run)]).convert_alpha()
                    self.count_run += 0.1
                else:
                    self.image = pygame.image.load(CharsMap2[1][int(self.count_run)]).convert_alpha()
            if self.number == 2:
                if self.run:
                    self.image = pygame.image.load(CharsMap2[2][int(self.count_run)]).convert_alpha()
                    self.count_run += 0.1
                else:
                    self.image = pygame.image.load(CharsMap2[2][int(self.count_run)]).convert_alpha()
            if self.number == 3:
                if self.run:
                    self.image = pygame.image.load(CharsMap2[3][int(self.count_run)]).convert_alpha()
                    self.count_run += 0.1
                else:
                    self.image = pygame.image.load(CharsMap2[3][int(self.count_run)]).convert_alpha()
            if self.number == 4:
                if self.run:
                    self.image = pygame.image.load(CharsMap2[4][int(self.count_run)]).convert_alpha()
                    self.count_run += 0.1
                else:
                    self.image = pygame.image.load(CharsMap2[4][int(self.count_run)]).convert_alpha()
        elif self.map == 2:
            if self.number == 0:
                if self.run:
                    self.image = pygame.image.load(CharsMap3[0][int(self.count_run)]).convert_alpha()
                    self.count_run += 0.1
                else:
                    self.image = pygame.image.load(CharsMap3[0][int(self.count_run)]).convert_alpha()
            if self.number == 1:
                if self.run:
                    self.image = pygame.image.load(CharsMap3[1][int(self.count_run)]).convert_alpha()
                    self.count_run += 0.1
                else:
                    self.image = pygame.image.load(CharsMap3[1][int(self.count_run)]).convert_alpha()
            if self.number == 2:
                if self.run:
                    self.image = pygame.image.load(CharsMap3[2][int(self.count_run)]).convert_alpha()
                    self.count_run += 0.1
                else:
                    self.image = pygame.image.load(CharsMap3[2][int(self.count_run)]).convert_alpha()
            if self.number == 3:
                if self.run:
                    self.image = pygame.image.load(CharsMap3[3][int(self.count_run)]).convert_alpha()
                    self.count_run += 0.1
                else:
                    self.image = pygame.image.load(CharsMap3[3][int(self.count_run)]).convert_alpha()
            if self.number == 4:
                if self.run:
                    self.image = pygame.image.load(CharsMap3[4][int(self.count_run)]).convert_alpha()
                    self.count_run += 0.1
                else:
                    self.image = pygame.image.load(CharsMap3[4][int(self.count_run)]).convert_alpha()
        elif self.map == 3:
            if self.number == 0:
                if self.run:
                    self.image = pygame.image.load(CharsMap4[0][int(self.count_run)]).convert_alpha()
                    self.count_run += 0.1
                else:
                    self.image = pygame.image.load(CharsMap4[0][int(self.count_run)]).convert_alpha()
            if self.number == 1:
                if self.run:
                    self.image = pygame.image.load(CharsMap4[1][int(self.count_run)]).convert_alpha()
                    self.count_run += 0.1
                else:
                    self.image = pygame.image.load(CharsMap4[1][int(self.count_run)]).convert_alpha()
            if self.number == 2:
                if self.run:
                    self.image = pygame.image.load(CharsMap4[2][int(self.count_run)]).convert_alpha()
                    self.count_run += 0.1
                else:
                    self.image = pygame.image.load(CharsMap4[2][int(self.count_run)]).convert_alpha()
            if self.number == 3:
                if self.run:
                    self.image = pygame.image.load(CharsMap4[3][int(self.count_run)]).convert_alpha()
                    self.count_run += 0.1
                else:
                    self.image = pygame.image.load(CharsMap4[3][int(self.count_run)]).convert_alpha()
            if self.number == 4:
                if self.run:
                    self.image = pygame.image.load(CharsMap4[4][int(self.count_run)]).convert_alpha()
                    self.count_run += 0.1
                else:
                    self.image = pygame.image.load(CharsMap4[4][int(self.count_run)]).convert_alpha()
        elif self.map == 4:
            if self.number == 0:
                if self.run:
                    self.image = pygame.image.load(CharsMap5[0][int(self.count_run)]).convert_alpha()
                    self.count_run += 0.1
                else:
                    self.image = pygame.image.load(CharsMap5[0][int(self.count_run)]).convert_alpha()
            if self.number == 1:
                if self.run:
                    self.image = pygame.image.load(CharsMap5[1][int(self.count_run)]).convert_alpha()
                    self.count_run += 0.1
                else:
                    self.image = pygame.image.load(CharsMap5[1][int(self.count_run)]).convert_alpha()
            if self.number == 2:
                if self.run:
                    self.image = pygame.image.load(CharsMap5[2][int(self.count_run)]).convert_alpha()
                    self.count_run += 0.1
                else:
                    self.image = pygame.image.load(CharsMap5[2][int(self.count_run)]).convert_alpha()
            if self.number == 3:
                if self.run:
                    self.image = pygame.image.load(CharsMap5[3][int(self.count_run)]).convert_alpha()
                    self.count_run += 0.1
                else:
                    self.image = pygame.image.load(CharsMap5[3][int(self.count_run)]).convert_alpha()
            if self.number == 4:
                if self.run:
                    self.image = pygame.image.load(CharsMap5[4][int(self.count_run)]).convert_alpha()
                    self.count_run += 0.1
                else:
                    self.image = pygame.image.load(CharsMap5[4][int(self.count_run)]).convert_alpha()


    def move(self):
        if self.run:
            self.rect.x += self.speed
    #Check điều kiện thắng
    def checkFinishLine(self):
        global list_image_load, doesWin
        if self.rect.x > WINDOW_SIZES[WINDOW_SIZE_INDEX][0] * 0.95:
            if not self.Finish:
                rank.append(self)
                list_image_load.append(self.number)
                self.run = False
                self.Finish = True
        # Kiểm tra xem có chiến thắng hay không
            if list_image_load[0] == choice - 1:
                doesWin = 1
                
            else:
                doesWin = 0
            

    def update(self):
        global choice
        self.animation()
        self.move()
        self.checkFinishLine()
        if self.PhanKhich:
            if not self.KichHoatBua:
                self.KichHoatBua = True
            self.Bua()
        if self.NhanhNhen:
            if not self.KichHoatBua:
                self.active_time = pygame.time.get_ticks()
                self.speed += 2
                self.KichHoatBua = True
            self.Bua()
        if self.TroiHon:
            if not self.KichHoatBua:
                self.active_time = pygame.time.get_ticks()
                for i in range(5):
                        if(i != (choice - 1)):
                            CHARACTERS[i].run = False
                self.KichHoatBua = True
            self.Bua()
        if self.isGoBack: #Đi ngược lại
            goBackImage = pygame.transform.flip(self.image, True, False)
            screen.blit(goBackImage, self.rect)
        else:
            screen.blit(self.image, self.rect)

    def Bua(self):
        if self.PhanKhich:
            effectImage = pygame.image.load("assets/effects/hieuung_phankhich.png").convert_alpha() #Ảnh tạm
            effectImage_rect = effectImage.get_rect(midbottom = self.rect.midleft)
            screen.blit(effectImage, effectImage_rect)
        if self.NhanhNhen:
            effectImage = pygame.image.load("assets/effects/hieuung_nhanhnhen.png").convert_alpha()
            effectImage_rect = effectImage.get_rect(midbottom = self.rect.midleft)
            screen.blit(effectImage, effectImage_rect)
            current_time = pygame.time.get_ticks() #Lấy thời gian hiện tại
            elapsed_time = current_time - self.active_time
            if elapsed_time >= 2000:
                    self.NhanhNhen = False
                    if not self.isGoBack:
                        self.speed = self.tempSpeed
        if self.TroiHon:
            effectImage = pygame.image.load("assets/effects/hieuung_troihon.png").convert_alpha()
            effectImage_rect = effectImage.get_rect(midbottom = self.rect.midleft)
            screen.blit(effectImage, effectImage_rect)
            current_time = pygame.time.get_ticks() #Lấy thời gian hiện tại
            elapsed_time = current_time - self.active_time
            if elapsed_time >= 1000:
                    self.TroiHon = False
                    for i in range(5):
                        if(i != (choice - 1)):
                            CHARACTERS[i].run = True
                    
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
        if not activated and not self.isGoBack:
            self.speed *= -1
            self.isGoBack = True

#Vị trí lucky box
LuckyBox_Pos = []
LuckyBox_Height = [0.55, 0.66, 0.76, 0.87, 0.98]
for i in range(10):
    if i < 5:
        LuckyBox_Pos.append((WINDOW_SIZES[WINDOW_SIZE_INDEX][0] * random.uniform(0.28, 0.5), WINDOW_SIZES[WINDOW_SIZE_INDEX][1] * LuckyBox_Height[i]))
    else:
        LuckyBox_Pos.append((WINDOW_SIZES[WINDOW_SIZE_INDEX][0] * random.uniform(0.65, 0.75), WINDOW_SIZES[WINDOW_SIZE_INDEX][1] * LuckyBox_Height[i - 5]))

def init_character_luckybox():
    global set_choice, SCREEN_SIZE_INDEX
    #khởi tạo tốc độ ngẫu nhiên
    for x in range(5):
        Speed.append(random.choice(RandSpeed))
    #Khởi tại vị trí lucky box
    for i in range(10):
        if i < 5:
            LuckyBox_Pos.append((WINDOW_SIZES[WINDOW_SIZE_INDEX][0] * random.uniform(0.28, 0.5), WINDOW_SIZES[WINDOW_SIZE_INDEX][1] * LuckyBox_Height[i]))
        else:
            LuckyBox_Pos.append((WINDOW_SIZES[WINDOW_SIZE_INDEX][0] * random.uniform(0.65, 0.75), WINDOW_SIZES[WINDOW_SIZE_INDEX][1] * LuckyBox_Height[i - 5]))

    for i in range(5):
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

class LuckyBox():
    def __init__(self, pos, character):
        self.x = pos[0]
        self.y = pos[1]
        self.activated = False #Cái này để check xem lucky box đã kích hoạt chưa
        self.active_effect = None #Kích hoạt hiệu ứng
        self.effect_duration = random.randint(1000, 3000) #Tính theo mili giây
        self.activation_time = None #Check lúc nào kích hoạt hiệu ứng
        self.effects = ["stun", "stun", "stun", "stun", "stun", "stun", "slow", "slow", "slow", "slow", "slow", "slow", "slow", "accelerate", "accelerate", "accelerate", "accelerate", "accelerate", "teleport","goback"] #Các hiệu ứng, nếu muốn hiệu ứng nào xuất hiện nhiều chỉ cần spam
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
            if character.PhanKhich:
                self.active_effect = None
                character.PhanKhich = False
            else:
                character.stop(self.activated)
        elif self.active_effect == "slow":
            if character.PhanKhich == True:
                self.active_effect = None
                character.PhanKhich = False
            else:
                character.slow(self.activated)
        elif self.active_effect == "accelerate":
            character.accelerate(self.activated)
        elif self.active_effect == "teleport":
            character.teleport(self.activated)
        elif self.active_effect == "goback":
            if character.PhanKhich:
                self.active_effect = None
                character.PhanKhich = False
            else:
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
            if not character.isGoBack:
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
            if self.active_effect == "slow" or self.active_effect == "accelerate" or self.active_effect == "teleport":
                if elapsed_time >= self.effect_duration:
                    self.active_effect = None
                    if not character.isGoBack:
                        character.speed = self.tempSpeed
                    
            elif self.active_effect == "stun":
                if elapsed_time >= self.effect_duration:
                    self.active_effect = None
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
        global LANGUAGE_INDEX
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


#Check điều kiện thắng
def FinishLine_Pass():
    global Victory_sound_Play
    if len(rank) == 5:
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
        #Các biến của pháo hoa
        self.last_time = pygame.time.get_ticks()
        self.interval = 50
        self.current_image = 0
        
    #Vẽ các thuộc tính lên màn hình
    def draw(self, mouse_pos):
        global rank, rankSound,  WINDOW_SIZES, winner
        BG = pygame.image.load(LANGUAGE[LANGUAGE_INDEX]+'BG_congratulations.png').convert_alpha()
        BG = pygame.transform.smoothscale(BG, WINDOW_SIZES[WINDOW_SIZE_INDEX])
        screen.blit(BG, (0, 0))
        self.CONTINUE_BUTTON.update(mouse_pos)

        if not rankSound:
            pygame.mixer.music.set_volume(present_volume)
            pygame.mixer.music.load('assets/sounds/rank.mp3')
            pygame.mixer.music.play(loops = -1)
            rankSound = True
        
        #Pháo hoa
        firework_images = ["assets/background/phaoHoa_1.png", "assets/background/phaoHoa_2.png", "assets/background/phaoHoa_3.png", "assets/background/phaoHoa_4.png", "assets/background/phaoHoa_5.png", "assets/background/phaoHoa_6.png", "assets/background/phaoHoa_7.png"]
        firework_surface = pygame.image.load(firework_images[self.current_image]).convert_alpha()

        #Ảnh pháo hoa
        current_time = pygame.time.get_ticks()
        elapsed_time = current_time - self.last_time

        if elapsed_time >= self.interval:
            self.current_image = (self.current_image + 1) % len(firework_images)
            firework_surface = pygame.image.load(firework_images[self.current_image]).convert_alpha()
            self.last_time = current_time

        screen.blit(firework_surface, ((WINDOW_SIZES[WINDOW_SIZE_INDEX][0] / 2 * 1.05, WINDOW_SIZES[WINDOW_SIZE_INDEX][1] * 0.4)))
        screen.blit(firework_surface, ((WINDOW_SIZES[WINDOW_SIZE_INDEX][0] / 2 * 0.7, WINDOW_SIZES[WINDOW_SIZE_INDEX][1] * 0.4)))
        screen.blit(firework_surface, ((WINDOW_SIZES[WINDOW_SIZE_INDEX][0] / 2 * 0.9, WINDOW_SIZES[WINDOW_SIZE_INDEX][1] * 0.25)))

        #Bảng xếp hạng
        Congratulations_pos = [(WINDOW_SIZES[WINDOW_SIZE_INDEX][0] / 2 * 1.05, WINDOW_SIZES[WINDOW_SIZE_INDEX][1] * 0.78), 
                                (WINDOW_SIZES[WINDOW_SIZE_INDEX][0] / 2 * 0.6, WINDOW_SIZES[WINDOW_SIZE_INDEX][1]* 0.85), 
                                (WINDOW_SIZES[WINDOW_SIZE_INDEX][0] / 2 * 1.5, WINDOW_SIZES[WINDOW_SIZE_INDEX][1]* 0.85), 
                                (WINDOW_SIZES[WINDOW_SIZE_INDEX][0] / 2 * 0.42, WINDOW_SIZES[WINDOW_SIZE_INDEX][1] * 0.93), 
                                (WINDOW_SIZES[WINDOW_SIZE_INDEX][0] / 2 * 1.7, WINDOW_SIZES[WINDOW_SIZE_INDEX][1] * 0.93)]

        for i in range(5):
            original_width, original_height = rank[i].original_image.get_size()
            new_width, new_height = original_width * 2, original_height * 2
            scaledImage = pygame.transform.smoothscale(rank[i].original_image, (new_width, new_height))
            scaledImage_rect = scaledImage.get_rect(midbottom = Congratulations_pos[i])
            screen.blit(scaledImage, scaledImage_rect)


    # Cập nhật các trạng thái của thuộc tính
    def update(self, event):
        global MenuSound, gameSound, InitGame
        pos = pygame.mouse.get_pos()
        if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                Back_To_Menu = Pause_Game()
                if Back_To_Menu:
                    InitGame = False
                    return MenuClass()
        if event.type == pygame.MOUSEBUTTONDOWN:
        #Hàm isOver kiểm tra xem con trỏ chuột có đè lên các thuộc tính Button trong khi đang nhấn nút chuột trái hay không
            if self.CONTINUE_BUTTON.CheckClick(pos):
                return Result()
                '''if QuitConfirm():
                    InitGame = False
                    reset_game()
                    return MenuClass()'''
                
        # pos = pygame.mouse.get_pos()
        # if self.CONTINUE_BUTTON.CheckClick(pos):
        #     if event.type == pygame.MOUSEBUTTONDOWN:
        #         pass
        #     if event.type == pygame.MOUSEMOTION:
        #         pass # Chuyen mau vang cho nut
        return self

class Result:
    def __init__(self):
        global doesWin, bet_money
        if doesWin:
            self.image = pygame.image.load(f'{LANGUAGE[LANGUAGE_INDEX]}/win{bet_money*3}.png').convert_alpha()
            self.image = pygame.transform.smoothscale(self.image, WINDOW_SIZES[WINDOW_SIZE_INDEX])
        else:
            self.image = pygame.image.load(f'{LANGUAGE[LANGUAGE_INDEX]}/lose{bet_money}.png').convert_alpha()
            self.image = pygame.transform.smoothscale(self.image, WINDOW_SIZES[WINDOW_SIZE_INDEX])
        self.continueButton = pygame.image.load(f"{LANGUAGE[LANGUAGE_INDEX]}/continue.png").convert_alpha()
        self.continueButton = pygame.transform.smoothscale(self.continueButton, (WINDOW_SIZES[WINDOW_SIZE_INDEX][0]*0.1,WINDOW_SIZES[WINDOW_SIZE_INDEX][1]*0.1))
        self.CONTINUE_BUTTON = Button(pos=(screen.get_width() / 2 * 1.05, screen.get_height() * 0.75), imageNormal = "continue.png", imageChanged = "continue2.png")

    def draw(self, mouse_pos):
        screen.blit(self.image,(0,0))
        screen.blit(self.continueButton,((WINDOW_SIZES[WINDOW_SIZE_INDEX][0] //2- self.continueButton.get_width() // 2), (WINDOW_SIZES[WINDOW_SIZE_INDEX][1] //16* 14)))
        self.CONTINUE_BUTTON.update(mouse_pos)
    def update(self, event):
        pos = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.CONTINUE_BUTTON.CheckClick(pos):
                return MenuClass()
        return self


#Biến được sử dụng
InitGame = False
rankSound = False

class Play:
    def __init__(self):
        # money_bet()
        self.playButton = Button(pos = (screen.get_width() / 2, screen.get_height() / 2), imageNormal = "play.png", imageChanged = "play2.png") # Nút có dòng chữ "Play game"
        self.settingsButton = Button(pos = (screen.get_width() / 2, screen.get_height() / 2 * 1.35), imageNormal = "settings.png", imageChanged = "settings2.png") # Nút có dòng chữ "Settings"
        self.quitButton = Button(pos = (screen.get_width() / 2, screen.get_height() / 2 * 1.7), imageNormal = "quit.png", imageChanged = "quit2.png") # Nút có dòng chữ "Quit"
        self.CheckPass = False #Check xem 5 nv có về đích chưa
    #Vẽ các thuộc tính lên màn hình
    def draw(self, mouse_pos):
        global VOLUME_INDEX, present_volume, countDownCheck, gameSound, set_choice, MAP_INDEX
        #Ảnh nền
        MAP_INDEX = set_choice - 1
        if MAP_INDEX == set_choice - 1 :
            screen.blit(MAPS[MAP_INDEX],(0,0))
        
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
        
        # Vẽ trạng thái tiền vs user ID
        update_account(user_id, user_money)
        DrawInfo()
            

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
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return Congratulations()
            
        return self

#Tạm dừng trò chơi
def Pause_Game():
     while True:
        #Ảnh nền
        Background = pygame.image.load(LANGUAGE[LANGUAGE_INDEX]+'background.png').convert_alpha()
        Background = pygame.transform.smoothscale(Background, WINDOW_SIZES[WINDOW_SIZE_INDEX])
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
        Background = pygame.image.load(LANGUAGE[LANGUAGE_INDEX]+'quitprompt.png').convert_alpha()
        Background = pygame.transform.smoothscale(Background, WINDOW_SIZES[WINDOW_SIZE_INDEX])
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

#Hàm read_data để đọc dữ liệu
def update_account(usr_id, money):
    with open(f'{account_sub_path}/{user_id}/{user_id}.txt', 'r') as old_file:
        lines = old_file.readlines()
        lines[1] = str(money) + '\n'
    with open(f'{account_sub_path}/{user_id}/{user_id}.txt', 'w') as new_file:
        new_file.writelines(lines)

      
def DrawInfo():
    # Lấy kích thước màn hình hiện tại
    screen_info = pygame.display.Info()
    # Tính toán kích thước của hình chữ nhật
    rect_width = screen_info.current_w // 8
    rect_height = screen_info.current_h // 8
    # Vẽ hình chữ nhật
    image = pygame.image.load('./assets/menu/nameAndMoney.png').convert_alpha()
    image = pygame.transform.smoothscale(image,(image.get_width(), image.get_height()))
    # Tạo font chữ
    font = pygame.font.Font('./assets/font/SVN-Retron_2000.ttf', 36)
    update_account(user_id, user_money)
    # Render thông tin user_id và user_money
    text_id = font.render(user_id, True, '#2B95D1')
    text_money = font.render(str(user_money), True, '#2B95D1')

    # Hiển thị thông tin lên hình chữ nhật
    screen.blit(image,(0,0))
    screen.blit(text_id, (40, 0))
    screen.blit(text_money, (40, 60))


# Lớp menu chính
class MenuClass: 
    #Khởi tạo các thuộc tính
    def __init__(self):
        reset_game()
        global VOLUME_INDEX, present_volume
        self.playButton = Button(pos = (screen.get_width() / 2, screen.get_height() / 2 * 0.95), imageNormal = f"play.png", imageChanged = "play2.png") # Nút có dòng chữ "Play game"
        self.settingsButton = Button(pos = (screen.get_width() / 2, screen.get_height() / 2 * 1.2), imageNormal = "settings.png", imageChanged = "settings2.png") # Nút có dòng chữ "Settings"
        self.minigame = Button(pos = (screen.get_width() / 2, screen.get_height() / 2 * 1.45), imageNormal = "minigame.png", imageChanged = "minigame2.png")
        self.quitButton = Button(pos = (screen.get_width() / 2, screen.get_height() / 2 * 1.7), imageNormal = "quit.png", imageChanged = "quit2.png") # Nút có dòng chữ "Quit"
        #v self.changeLanguageButton = Button(pos=(screen.get_width() - screen.get_width() / 16, screen.get_height() - screen.get_height() / 16), imageNormal= "lang40.png", imageChanged= "lang240.png") # Nút chuyển đổi ngôn ngữ
    #Vẽ các thuộc tính lên màn hình
    def draw(self, mouse_pos):
        global user_id, screen_info
        Background = pygame.image.load(LANGUAGE[LANGUAGE_INDEX]+'background.png').convert_alpha()
        Background = pygame.transform.smoothscale(Background, WINDOW_SIZES[WINDOW_SIZE_INDEX])
        screen.blit(Background, (0, 0))
        update_account(user_id, user_money)
        DrawInfo()
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
                #     flappy_bird()
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
                flappy_bird()
                    
        return self

class SettingClass: #Khởi tạo các nút, label và Button. 
    def __init__(self):
        self.soundButton = Button(pos=(screen.get_width() / 2, screen.get_height() / 2 * 0.65), imageNormal = "sound.png", imageChanged = "sound2.png")
        self.screenButton = Button(pos=(screen.get_width() / 2, screen.get_height() / 2 * 0.9), imageNormal = "screen.png", imageChanged = "screen2.png")
        self.escButton = Button(pos=(screen.get_width() / 2, screen.get_height() / 2 * 1.4), imageNormal = "back.png", imageChanged = "back2.png")
        self.changeLanguageButton = Button(pos=(screen.get_width() / 2, screen.get_height() / 2 * 1.15), imageNormal = "lang.png", imageChanged = "lang2.png")
    #Vẽ các lớp phủ, các nút và chữ
    def draw(self, mouse_pos):
        Background = pygame.image.load(LANGUAGE[LANGUAGE_INDEX] + 'settingsMenu.png').convert_alpha()
        Background = pygame.transform.smoothscale(Background, WINDOW_SIZES[WINDOW_SIZE_INDEX])
        screen.blit(Background,(0,0)) #Tạo một lớp phủ hình chữ nhật kích thước tối đa
        #Vẽ nút
        self.soundButton.update(mouse_pos)
        self.screenButton.update(mouse_pos)
        self.escButton.update(mouse_pos)
        self.changeLanguageButton.update(mouse_pos)
    #Cập nhật trạng thái của class
    def update(self, event):
        global LANGUAGE_INDEX
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
                if LANGUAGE_INDEX == 0:
                    LANGUAGE_INDEX = 1
                elif LANGUAGE_INDEX == 1:
                    LANGUAGE_INDEX = 0
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
        Background = pygame.image.load(LANGUAGE[LANGUAGE_INDEX]+'soundMenu.png').convert_alpha()
        Background = pygame.transform.smoothscale(Background, WINDOW_SIZES[WINDOW_SIZE_INDEX])
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
        Background = pygame.image.load(LANGUAGE[LANGUAGE_INDEX]+'background.png').convert_alpha()
        Background = pygame.transform.smoothscale(Background, WINDOW_SIZES[WINDOW_SIZE_INDEX])
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
                halfScreen_active = not halfScreen_active
                WINDOW_SIZE_INDEX = 0
                SCREEN_SIZE_INDEX = 0
                return self
            elif self.halfScreenButton.CheckClick(pos):
                WINDOW_SIZE_INDEX = 1
                SCREEN_SIZE_INDEX = 1
                halfScreen_active = True
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
        Background = pygame.image.load(LANGUAGE[LANGUAGE_INDEX]+'mapselection.png').convert_alpha()
        Background = pygame.transform.smoothscale(Background, WINDOW_SIZES[WINDOW_SIZE_INDEX])
        screen.blit(Background, (0, 0))
    #Cập nhật trạng thái cho các thuộc tính
    def update(self, event):
        global InitGame, MAP_INDEX, set_choice
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
                set_choice = 1
                MAP_INDEX = 0
                return CharacterSelection()
            if event.key == pygame.K_2:
                set_choice = 2
                MAP_INDEX = 1
                return CharacterSelection()
            if event.key == pygame.K_3:
                set_choice = 3
                MAP_INDEX = 2
                return CharacterSelection()
            if event.key == pygame.K_4:
                set_choice = 4
                MAP_INDEX = 3
                return CharacterSelection()
            if event.key == pygame.K_5:
                set_choice = 5
                MAP_INDEX = 4
                return CharacterSelection()
                
        return self
    
class CharacterSelection: 
    global InitGame, MAP_INDEX, set_choice, choice
    def draw(self, mouse_pos):
        Background = pygame.image.load(LANGUAGE[LANGUAGE_INDEX]+f'choose_char{set_choice}.png').convert_alpha()
        Background = pygame.transform.smoothscale(Background, WINDOW_SIZES[WINDOW_SIZE_INDEX])
        screen.blit(Background, (0, 0))
    #Cập nhật trạng thái cho các thuộc tính
    def update(self, event):
        global InitGame, choice
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
                choice = 1
                return Shop()
            if event.key == pygame.K_2:
                choice = 2
                return Shop()
            if event.key == pygame.K_3:
                choice = 3
                return Shop()
            if event.key == pygame.K_4:
                choice = 4
                return Shop()
            if event.key == pygame.K_5:
                choice = 5
                return Shop()
                
        return self


class Shop: 
    def draw(self, mouse_pos):
        Background = pygame.image.load(LANGUAGE[LANGUAGE_INDEX]+'shopee.png').convert_alpha()
        Background = pygame.transform.smoothscale(Background, WINDOW_SIZES[WINDOW_SIZE_INDEX])
        screen.blit(Background, (0, 0))
        update_account(user_id, user_money)
        DrawInfo()
    #Cập nhật trạng thái cho các thuộc tính
    def update(self, event):
        global InitGame, choice, bua_money, user_money
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
                CHARACTERS[choice - 1].NhanhNhen = True
                bua_money = 300 # Gán giá tiền cho bùa
                user_money -= bua_money
                return MoneyBet()
            if event.key == pygame.K_2:
                CHARACTERS[choice - 1].TroiHon = True
                bua_money = 400 # Gán giá tiền cho bùa
                user_money -= bua_money
                return MoneyBet()
            if event.key == pygame.K_3:
                CHARACTERS[choice - 1].PhanKhich = True
                bua_money = 500 # Gán giá tiền cho bùa
                user_money -= bua_money
                return MoneyBet()
            if event.key == pygame.K_RETURN:
                bua_money = 0
                user_money -= bua_money
                return MoneyBet()
        return self

class MoneyBet: 
    global InitGame, MAP_INDEX, set_choice, choice, bet_money, user_money, money_bet
    def draw(self, mouse_pos):
        Background = pygame.image.load(LANGUAGE[LANGUAGE_INDEX]+'moneyshop.png').convert_alpha()
        Background = pygame.transform.smoothscale(Background, WINDOW_SIZES[WINDOW_SIZE_INDEX])
        screen.blit(Background, (0, 0))
        update_account(user_id, user_money)
        DrawInfo()
    #Cập nhật trạng thái cho các thuộc tính
    def update(self, event):
        global InitGame, MAP_INDEX, set_choice, choice, bet_money, user_money, money_choice
        bet_values = {1: 200, 2: 500, 3: 1000}
        if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                Back_To_Menu = Pause_Game()
                if Back_To_Menu:
                    InitGame = False
                    return MenuClass()
            if event.key in [pygame.K_1, pygame.K_2, pygame.K_3]:
                money_choice = event.key - pygame.K_0
                bet_money = bet_values[money_choice]
                if user_money < bet_money:
                    self.show_insufficient_funds_message()
                else:
                    user_money -= bet_money
                    return Play()
        return self

    def show_insufficient_funds_message(self):
        messages = {
            'ENG': "You don't have enough money. You can play Minigame to earn",
            'VIE': "Bạn không đủ tiền để chơi. Bạn có thể chơi minigame để lấy thêm tiền"
        }
        spilt_text = []
        for item in LANGUAGE:
            parts = item.split('/')
            spilt_text.append(parts[-3])
        if LANGUAGE_INDEX == 0:
            message = messages['ENG']
            font = pygame.font.Font(None, 36)
            text = font.render(message, True, (255, 255, 255))
            screen.blit(text, (10,10))
        elif LANGUAGE_INDEX == 1:
            message = messages[LANGUAGE_INDEX]
            font = pygame.font.Font(None, 36)
            text = font.render(message, True, '#F97C04')
            screen.blit(text, (10, 10))

        #pygame.display.flip()

# Đây là hàm reset game
def reset_game():
    global set_choice, choice, bet_money, CHARACTERS, LUCKYBOX, GROUP, rank, winner, last, Speed, Victory_sound_Play
    global rankSound, InitGame, countDownCheck, gameSound, Position, LuckyBox_Pos, doesWin
    file = './assets/sounds/mainmenu.mp3'
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load(file)
    pygame.mixer.music.set_volume(VOLUME[VOLUME_INDEX])
    pygame.mixer.music.play()
    set_choice = 1
    choice = 0
    bet_money = 0
    doesWin = 1
    CHARACTERS = []
    LUCKYBOX = []
    GROUP = []
    rank = [] #List nhân vật khi thắng đc thêm vào
    Speed = []
    LuckyBox_Pos = []
    winner = 0
    last = 0
    Victory_sound_Play = True
    rankSound = True
    InitGame = False
    countDownCheck = False
    gameSound = True
    countDownCheck = True

def show_fps(screen, clock):
    # Tạo font chữ
    font = pygame.font.Font(None, 30)
    # Tính toán FPS
    fps = str(int(clock.get_fps()))
    # Tạo text surface
    text = font.render("FPS: " + fps, 1, pygame.Color("red"))
    # Vẽ text surface lên màn hình
    screen.blit(text, (0, 0))

#Đây là main loop
def main():
    global login_lock, list_image_load
    if not login_lock:
        pygame.quit()
        sys.exit()
    #Lớp phủ xuất hiện đầu tiên chính là màn hình cài đặt
    current_class = MenuClass()
    #Vòng lặp chính
    while True:  # Vòng lặp vô hạn, chương trình sẽ chạy cho đến khi có sự kiện thoát
        for event in pygame.event.get():  # Duyệt qua tất cả sự kiện đang chờ xử lý trong hàng đợi sự kiện của Pygame
            if event.type == pygame.QUIT:  # Nếu sự kiện là loại thoát (như nhấn nút đóng cửa sổ)
                pygame.quit()  # Thoát khỏi Pygame
                sys.exit()  # Thoát khỏi chương trình
            current_class = current_class.update(event)  # Cập nhật trạng thái của đối tượng hiện tại dựa trên sự kiện
        mouse_pos = pygame.mouse.get_pos()
        current_class.draw(mouse_pos)  # Vẽ đối tượng hiện tại lên màn hình
        pygame.display.flip()  # Cập nhật toàn bộ cửa sổ
        show_fps(screen, clock)
        clock.tick(60)  # Đảm bảo chương trình chạy không quá 60 khung hình/giây
main()