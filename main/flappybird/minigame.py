import pygame
import random
import sys
import main.LoginSignup as LoginSignup
#quy định các màu
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
bright_red = pygame.Color(255, 0, 0)
old_red = pygame.Color(200, 0, 0)
color = pygame.Color('lightskyblue3')
#Lấy các biến từ file khác
user_id = LoginSignup.user_id
user_money = int(LoginSignup.user_money)

#Mod lại subpath để có thể đưa menugame vào:
subpath = './main/flappybird'
account_sub_path = './assets/player/'
pygame.init()

volume = 0.2

clock = pygame.time.Clock()
WINDOW_SIZES = [pygame.display.get_desktop_sizes()[0], (768,432)]
WINDOW_SIZE_INDEX = 0
screen_Width = WINDOW_SIZES[WINDOW_SIZE_INDEX][0]
screen_Height = WINDOW_SIZES[WINDOW_SIZE_INDEX][1]
screen = pygame.display.set_mode(WINDOW_SIZES[WINDOW_SIZE_INDEX], pygame.RESIZABLE)
pygame.display.set_caption('Flappy Bird')
running = True

black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
bright_red = pygame.Color(255, 0, 0)
old_red = pygame.Color(200, 0, 0)
color = pygame.Color('lightskyblue3')

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
                    pygame.mixer.music.set_volume(volume)
                    bird_drop_velocity = 0
                    bird_drop_velocity -= screen_Height/80
            if event.type == pygame.MOUSEBUTTONUP:
                if x_back_button + width > mouse[0] > x_back_button and y_back_button + height > mouse[
                    1] > y_back_button:
                    print('end game')
                    update_account(user_id, user_money)
                    return 2

        show_fps(screen, clock)
        pygame.display.flip()
        pygame.mixer.init()
        pygame.mixer.music.load(f'{subpath}/Sounds/nhac2.wav')
        pygame.mixer.music.set_volume(volume)
        pygame.mixer.music.play()
