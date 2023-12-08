import random
import glob
import pygame
import sys
import time
import pygame.gfxdraw
from pygame.locals import *

user_id = ''
user_pwd = ''
user_money = 0
set_choice = 0
choice = 0
bet_money = 0
pygame.init()

volume = 0.2

clock = pygame.time.Clock()
screen_Width = 1500
screen_Height = 800
screen = pygame.display.set_mode((screen_Width, screen_Height), pygame.RESIZABLE)
pygame.display.set_caption('RACE')
running = True

black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
bright_red = pygame.Color(255, 0, 0)
old_red = pygame.Color(200, 0, 0)
color = pygame.Color('lightskyblue3')

# Phông chữ :
font = pygame.font.SysFont("comicsansms", int(screen_Width / 1500 * 32))
text_Font = pygame.font.Font(None, int(screen_Width / 1500 * 38))
menu_Font = pygame.font.Font(None, int(screen_Width / 1500 * 45))

# vẽ hình chữ nhật chứa text
rect_text = pygame.Rect(screen_Width / (1500 / 568), screen_Height / (800 / 440), screen_Width / (1500 / 350),
                        screen_Height / (800 / 40))

# Nút bấm
ok_button = font.render('OK', True, white)
play_game_button = font.render('Main Game', True, white)
play_minigame_button = font.render('Mini Game', True, white)
option_button = font.render('Option', True, white)
exit_button = font.render('Exit', True, white)
flappybird_game_button = font.render('Flappy Bird', True, white)
back_button = font.render('Back', True, white)

width = screen_Width / (15 / 2)
height = screen_Height / 16

x_back_button = screen_Width / (15 / 13)
y_back_button = screen_Height / (8 / 6)

# backgroundgame :
background = pygame.image.load('backgroundgamechinhthuc.jpg')
backgroundmenu = pygame.image.load('menugame.jpg')
backgroundmenu1 = pygame.image.load('menugame1.jpg')
# hinh anh text box
box1 = pygame.image.load('box.png')

rank = []
winner = 0
line = screen_Width - screen_Width / 20
start = screen_Width / 300


def create_account(usr_id, usr_pwd):
    with open('account.txt', 'a') as file:
        file.write(f'{usr_id},{usr_pwd},0\n')


def check_account(usr_id, usr_pwd):
    with open('account.txt', 'r') as file:
        for line in file:
            account = line.rstrip().split(',')
            if usr_id == account[0]:
                if usr_pwd == account[1]:
                    return account[2]
                else:
                    return -1
        create_account(usr_id, usr_pwd)
        return 0

def update_account(usr_id, money):
    data = []
    with open('account.txt', 'r') as old_file:
        for line in old_file:
            if line.split(',')[0] == usr_id:
                pos = line.rfind(',')
                line = line[:pos + 1] + str(money) + '\n'
            data.append(line)
    with open('account.txt', 'w') as new_file:
        for line in data:
            new_file.write(line)

class InputBox():
    def __init__(self, x, y):

        self.font = pygame.font.Font(None, 32)

        self.inputBox = pygame.Rect(x, y, screen_Width / (1500 / 140), screen_Height / (800 / 32))

        # self.colourInactive = pygame.Color('firebrick4')
        # self.colourActive = pygame.Color('gray24')

        self.colourInactive = pygame.Color(0, 0, 0)
        self.colourActive = pygame.Color(255, 255, 255)

        self.colour = self.colourInactive

        self.text = ''

        self.active = False
        self.isBlue = True

    def update_position(self, x, y):
        self.inputBox = pygame.Rect(x, y, screen_Width / (1500 / 140), screen_Height / (800 / 32))

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.active = self.inputBox.collidepoint(event.pos)
            self.colour = self.colourActive if self.active else self.colourInactive
        if event.type == pygame.KEYDOWN:
            if self.active:

                if event.key == pygame.K_RETURN:
                    return self.text
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                # if event.key == pygame.K_KP_ENTER:

    def draw(self, screen):
        txtSurface = self.font.render(self.text, True, self.colour)
        width = max(screen_Width / (15 / 2), txtSurface.get_width() + screen_Width / 150)
        self.inputBox.w = width  # PHAN NAY CHUA THAY DOI THEO WIDTH,HEIGHT
        screen.blit(txtSurface, (self.inputBox.x + screen_Width / (300), self.inputBox.y + screen_Height / 160))
        pygame.draw.rect(screen, self.colour, self.inputBox, 2)

        if self.isBlue:
            self.color = (0, 128, 255)
        else:
            self.color = (255, 100, 0)

def giaodien():
    global screen_Width, screen_Height, screen, text_Font, menu_Font, font
    global user_id, user_pwd, user_money
    file = 'Sounds/nhac2.wav'
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load(file)
    pygame.mixer.music.set_volume(volume)
    pygame.mixer.music.play()
    active = True
    user_text = ''
    input1 = InputBox(screen_Width / 2 - screen_Width / 12, screen_Height / 2 + screen_Height / 32)
    input2 = InputBox(screen_Width / 2 - screen_Width / 12, screen_Height / 2 + screen_Height / (800 / 70))
    while active:
        # screen.fill(white)
        input1.update_position(screen_Width / 2 - screen_Width / 12, screen_Height / 2 + screen_Height / 32)
        input2.update_position(screen_Width / 2 - screen_Width / 12, screen_Height / 2 + screen_Height / (800 / 70))
        global background
        background = pygame.transform.scale(background, (screen_Width, screen_Height))
        screen.blit(background, (0, 0))
        idName = text_Font.render('ID :', True, black)
        screen.blit(idName, (screen_Width / (1500 / 577), screen_Height / (800 / 428)))
        passwordName = text_Font.render('Password :', True, black)
        screen.blit(passwordName, (screen_Width / (1500 / 482), screen_Height / (800 / 473)))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                active = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.VIDEORESIZE:
                screen_Width, screen_Height = event.size
                screen = pygame.display.set_mode((screen_Width, screen_Height), pygame.RESIZABLE)
                text_Font = pygame.font.Font(None, int(screen_Width / 1500 * 38))
                menu_Font = pygame.font.Font(None, int(screen_Width / 1500 * 45))
                font = pygame.font.SysFont("comicsansms", int(screen_Width / 1500 * 32))
            name = input1.handle_event(event)
            if name is not None:
                user_id = name
            pwd = input2.handle_event(event)
            if pwd is not None:
                user_pwd = pwd
            if event.type == pygame.MOUSEBUTTONUP:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if (screen_Width / (1500 / 706) <= mouse_x <= screen_Width / (1500 / 706) + ok_button.get_width()) and (
                        screen_Height / (800 / 530) <= mouse_y <= screen_Height / (800 / 530) + ok_button.get_height()):
                    auth = check_account(user_id, user_pwd)
                    if auth == 0:
                        print(f'new account is created with id {user_id}')
                        user_money = 0
                        return
                    elif auth == -1:
                        print('Wrong password. Try again!')
                        print(f'{user_id}, {user_pwd}')
                    else:
                        user_money = int(auth)
                        return
        input1.draw(screen)
        input2.draw(screen)
        mouse = pygame.mouse.get_pos()
        if screen_Width / 2.2 + (screen_Width / 15) > mouse[0] > screen_Width / 2.2 and (
                screen_Height / 1.5) + screen_Height / 16 > mouse[
            1] > screen_Height / 1.5:  # tạo hiệu ứng khi click  vào logo
            pygame.draw.rect(screen, bright_red, (
                int(screen_Width / 2.2), int(screen_Height / 1.6 + screen_Height / float(800 / 30)), screen_Width / 15,
                screen_Height / 16))
        else:
            pygame.draw.rect(screen, old_red, (
                int(screen_Width / 2.2), int(screen_Height / 1.6 + screen_Height / float(800 / 30)), screen_Width / 15,
                screen_Height / 16))
        screen.blit(ok_button, (screen_Width / float(1500 / 706), screen_Height / float(80 / 53)))
        pygame.display.update()

def flappy_bird():
   
    global screen_Width, screen_Height, screen, text_Font, menu_Font, font, tube1_height, tube2_height, tube3_height
    global user_id, user_money
    running = True
    BLACK = (0, 0, 0)
    screen = pygame.display.set_mode((screen_Width, screen_Height), pygame.RESIZABLE)
    clock = pygame.time.Clock()
    TUBE_WIDTH = int(screen_Width / 30)
    TUBE_VELOCITY = int(screen_Width / 250)
    TUBE_GAP = int(screen_Height * 23 / 80)
    tube1_x = int(screen_Width * 6 / 15)
    tube2_x = int(screen_Width * 8 / 15)
    tube3_x = int(screen_Width * 10 / 15)
    tube1_height = random.randint(int(screen_Height / 8), int(screen_Height * 5 / 16))
    tube2_height = random.randint(int(screen_Height / 8), int(screen_Height * 5 / 16))
    tube3_height = random.randint(int(screen_Height / 8), int(screen_Height * 5 / 16))
    BIRD_X = screen_Width * 2 / 15
    bird_y = screen_Height / (2)
    BIRD_WIDTH = int(screen_Width * 7 / 300)
    BIRD_HEIGHT = int(screen_Height * 7 / 300)
    bird_drop_velocity = 0
    GRAVITY = 0.7
    score = 0
    fontend = pygame.font.SysFont('sans', 50)
    tube1_pass = False
    tube2_pass = False
    tube3_pass = False
    pausing = False
    run = False
    begin = False
    dem = 0
    check = 0
    
    while running:
        #pygame.mixer.music.pause()
        clock.tick(60)
        background_image = pygame.image.load("flappybird/background.png")
        background_image = pygame.transform.scale(background_image, (screen_Width, screen_Height))
        screen.blit(background_image, (0, 0))
        
        user_info = text_Font.render('ID: ' + user_id, True, black)
        money_info = text_Font.render('Money: ' + str(user_money), True, black)
        back_button = font.render('Back', True, white)
        screen.blit(user_info, (screen_Width - user_info.get_width() - money_info.get_width() - 40, 10))
        screen.blit(money_info,
                    (screen_Width - money_info.get_width() - screen_Width / (1500 / 20), screen_Height / (800 / 10)))
        bird_image = pygame.image.load("flappybird/bird.png")
        bird_image = pygame.transform.scale(bird_image, (BIRD_WIDTH, BIRD_HEIGHT))
        base_image = pygame.image.load("flappybird/base.png")
        base_image = pygame.transform.scale(base_image, (screen_Width, screen_Height // 4))

        tube_image1 = pygame.image.load("flappybird/pipe1.png")
        tube_image1 = pygame.transform.scale(tube_image1, (TUBE_WIDTH, tube1_height))
        tube_inv_image1 = pygame.image.load("flappybird/pipe2.png")
        tube_inv_image1 = pygame.transform.scale(tube_inv_image1, (TUBE_WIDTH, screen_Height - tube1_height - TUBE_GAP))

        tube_image2 = pygame.image.load("flappybird/pipe1.png")
        tube_image2 = pygame.transform.scale(tube_image2, (TUBE_WIDTH, tube2_height))
        tube_inv_image2 = pygame.image.load("flappybird/pipe2.png")
        tube_inv_image2 = pygame.transform.scale(tube_inv_image2, (TUBE_WIDTH, screen_Height - tube2_height - TUBE_GAP))

        tube_image3 = pygame.image.load("flappybird/pipe1.png")
        tube_image3 = pygame.transform.scale(tube_image3, (TUBE_WIDTH, tube3_height))
        tube_inv_image3 = pygame.image.load("flappybird/pipe2.png")
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
                tube1_x = screen_Width / (1500 / 550)
                tube1_height = random.randint(screen_Height // (1500 // 100), screen_Height // (1500 // 250))
                tube1_pass = False
            if tube2_x < -TUBE_WIDTH:
                tube2_x = screen_Width / (1500 / 550)
                tube2_height = random.randint(screen_Height // (1500 // 100), screen_Height // (1500 // 250))
                tube2_pass = False
            if tube3_x < -TUBE_WIDTH:
                tube3_x = screen_Width / (1500 / 550)
                tube3_height = random.randint(screen_Height // (1500 // 100), screen_Height // (1500 // 250))
                tube3_pass = False
            score_txt = fontend.render("Score: " + str(score) + ", max score = 20", True, BLACK)
            screen.blit(score_txt, (screen_Width / (15 / 8), screen_Height / 2))
        # update score
        if tube1_x + TUBE_WIDTH <= BIRD_X and tube1_pass == False:
            pygame.mixer.Sound('flappybird/sounds/point.wav').play()
            score += 1
            tube1_pass = True
        if tube2_x + TUBE_WIDTH <= BIRD_X and tube2_pass == False:
            pygame.mixer.Sound('flappybird/sounds/point.wav').play()
            score += 1
            tube2_pass = True
        if tube3_x + TUBE_WIDTH <= BIRD_X and tube3_pass == False:
            pygame.mixer.Sound('flappybird/sounds/point.wav').play()
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
                    pygame.mixer.Sound('flappybird/sounds/hit.wav').play()
                    dem = 1
                game_over_txt = fontend.render("Game over, score: " + str(score), True, BLACK)
                screen.blit(game_over_txt, (screen_Width / (1500 / 750), screen_Height / (800 / 170)))
                money_receiver = fontend.render("the money you get: " + str(score * 10), True, BLACK)
                screen.blit(money_receiver, (screen_Width / (1500 / 750), screen_Height / (800 / 270)))
                press_space_txt = fontend.render("Press Space to Play again", True, BLACK)
                screen.blit(press_space_txt, (screen_Width / (1500 / 750), screen_Height / (800 / 370)))
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
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.VIDEORESIZE:
                screen_Width, screen_Height = event.size
                screen = pygame.display.set_mode((screen_Width, screen_Height), pygame.RESIZABLE)
                text_Font = pygame.font.Font(None, int(screen_Width / 1500 * 38))
                menu_Font = pygame.font.Font(None, int(screen_Width / 1500 * 45))
                font = pygame.font.SysFont("comicsansms", int(screen_Width / 1500 * 32))
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    # reset 
                    if pausing:
                        bird_y = screen_Height / (2)
                        TUBE_VELOCITY = 6
                        tube1_x = screen_Width / (1500 / 600)
                        tube2_x = screen_Width / (1500 / 800)
                        tube3_x = screen_Width / (1500 / 1000)
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
                    pygame.mixer.Sound('flappybird/sounds/wing.wav').play()
                    pygame.mixer.music.set_volume(volume)
                    bird_drop_velocity = 0
                    bird_drop_velocity -= screen_Height/80
            if event.type == pygame.MOUSEBUTTONUP:
                if x_back_button + width > mouse[0] > x_back_button and y_back_button + height > mouse[
                    1] > y_back_button:
                    print('end game')
                    return 2
        pygame.display.flip()
        pygame.mixer.init()
        pygame.mixer.music.load('Sounds/nhac2.wav')
        pygame.mixer.music.set_volume(volume)
        pygame.mixer.music.play()
#basketball game
clock = pygame.time.Clock()
text_x = int(screen_Width / 100)
text_y = int(screen_Height * 15 / 800)
court = pygame.transform.scale(pygame.image.load('basketball_court2.jpg'), (screen_Width, screen_Height))
basket_width = int(screen_Width / 12)
basket_pos_x = int(screen_Width / (1500 / 450))
basket_pos_y = int(screen_Height / (800 / 600))
basket_y_line = basket_pos_y + int(screen_Height / (800 / 17))
basket_x_start_co = basket_pos_x + int(screen_Width / (1500 / 40))
basket_x_end_co = basket_pos_x + int(screen_Width / (1500 / 85))
basket = pygame.image.load('basket.png')
basket_speed_x = int(screen_Width / (1500 / 10))
present_basket_speed_x = 0
# ball variables
ball_size = int(screen_Height / (8))
ball_position_x = int(screen_Width / (1500 / 50))
ball_position_y = int(screen_Height / (800 / 50))
ball_x_co = ball_position_x + int(screen_Width / (1500 / 50))
ball_y_co = ball_position_y + int(screen_Height / (800 / 50))
speed_dir_x = 0
speed_dir_y = int(screen_Height / (800 / 4))
basketball = pygame.image.load('basketball.png')
score = 0
running = True
ballshot = pygame.mixer.Sound("Sounds/ballshot.wav")
gameoversound = pygame.mixer.Sound("Sounds/gameover.mp3")
x_back_button = int(screen_Width / (15 / 13))
y_back_button = int(screen_Height / (8 / 6))
Red = pygame.Color(199, 107, 80)
BLACK = (0, 0, 0)
fontend = pygame.font.SysFont('sans', 50)
back_button = font.render('Back', True, white)
def display():
    global user_id, user_money
    display_court()
    display_basketball(ball_position_x, ball_position_y)
    display_basket(basket_pos_x, basket_pos_y)
    user_info = text_Font.render('ID: ' + user_id, True, black)
    money_info = text_Font.render('Money: ' + str(user_money), True, black)
    screen.blit(user_info, (screen_Width - user_info.get_width() - money_info.get_width() - screen_Width / (1500 / 40),
                            screen_Height / (800 / 10)))
    screen.blit(money_info,
                (screen_Width - money_info.get_width() - screen_Width / (1500 / 20), screen_Height / (800 / 10)))
def display_court():
    screen.blit(court, (0, 0))
def display_basketball(pos_x, pos_y):
    screen.blit(basketball, (pos_x, pos_y))
    update_ball_pos()
def display_basket(pos_x, pos_y):
    screen.blit(basket, (pos_x, pos_y))
def check_for_basket(x):
    if ball_y_co in range(basket_y_line - (int(speed_dir_y) // 2), basket_y_line + (int(speed_dir_y) // 2)):
        if ball_x_co in range(int(basket_x_start_co) - 1, int(basket_x_end_co) + 1):
            x += 1
            ballshot.play()
        else:
            x = 0
            gameoversound.play()
            gameOver()
    return x
def display_score(score, text_pos_x, text_pos_y):
    score_disp = font.render("Score: " + str(score), True, (0, 0, 0))
    screen.blit(score_disp, (text_pos_x, text_pos_y))
def check_for_event():
    global running, present_basket_speed_x
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        present_basket_speed_x = - basket_speed_x
    elif keys[pygame.K_RIGHT]:
        present_basket_speed_x = basket_speed_x
    else:
        present_basket_speed_x = 0
def enforce_border():
    global basket_pos_x
    if basket_pos_x > (screen_Width - basket_width):
        basket_pos_x = screen_Width - basket_width
    if basket_pos_x < 0:
        basket_pos_x = 0
def random_ball_initialise():
    global ball_position_y, ball_position_x, speed_dir_y
    if ball_position_y > (screen_Height + ball_size):
        speed_dir_y = 3
        temp_num = int(screen_Width / (1500 / 924))
        ball_position_x = random.randint(0, temp_num)
        ball_position_y = 0
def update_basket_score_region():
    global basket_x_start_co, basket_x_end_co
    basket_x_start_co = basket_pos_x + screen_Width / (1500 / 40)
    basket_x_end_co = basket_pos_x + screen_Width / (1500 / 85)
def update_ball_pos():
    global ball_x_co, ball_y_co, basket_pos_x, ball_position_y, speed_dir_y
    ball_x_co = ball_position_x + screen_Width / (1500 / 50)
    ball_y_co = ball_position_y + screen_Height / (800 / 50)
    basket_pos_x += present_basket_speed_x
    ball_position_y += int(speed_dir_y)
    speed_dir_y += (speed_dir_y * 0.02)
    random_ball_initialise()
def initialise_event():
    check_for_event()
    enforce_border()
def gameOver():
    global screen_Width, screen_Height, screen, text_Font, menu_Font, font
    global user_money, user_id
    check = True
    while check:
        game_over_txt = fontend.render("Game over, score: " + str(score), True, BLACK)
        screen.blit(game_over_txt, (screen_Width / (1500 / 550), screen_Height / (800 / 250)))
        money_receiver = fontend.render("The money you get: " + str(score * 10), True, BLACK)
        screen.blit(money_receiver, (screen_Width / (1500 / 550), screen_Height / (800 / 350)))
        press_space_txt = fontend.render("Press Space to Play again", True, BLACK)
        screen.blit(press_space_txt, (screen_Width / (1500 / 520), screen_Height / (800 / 450)))
        mouse = pygame.mouse.get_pos()
        if x_back_button + width > mouse[0] > x_back_button and y_back_button + height > mouse[
            1] > y_back_button:  # tạo hiệu ứng khi click  vào logo
            pygame.draw.rect(screen, bright_red,
                             (x_back_button, y_back_button, screen_Width / (1500 / 100), screen_Height / (800 / 50)))
        else:
            pygame.draw.rect(screen, old_red,
                             (x_back_button, y_back_button, screen_Width / (1500 / 100), screen_Height / (800 / 50)))
        screen.blit(back_button, (x_back_button + screen_Width / (150), y_back_button))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.VIDEORESIZE:
                screen_Width, screen_Height = event.size
                screen = pygame.display.set_mode((screen_Width, screen_Height), pygame.RESIZABLE)
                text_Font = pygame.font.Font(None, int(screen_Width / 1500 * 38))
                menu_Font = pygame.font.Font(None, int(screen_Width / 1500 * 45))
                font = pygame.font.SysFont("comicsansms", int(screen_Width / 1500 * 32))
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    check = False
                    user_money += score * 10
                    update_account(user_id, user_money)
            if event.type == pygame.MOUSEBUTTONUP:
                if x_back_button + width > mouse[0] > x_back_button and y_back_button + height > mouse[
                    1] > y_back_button:
                    user_money += score * 10
                    update_account(user_id, user_money)
                    menu(2)
        pygame.display.update()
        pygame.mixer.init()
        pygame.mixer.music.load('Sounds/nhac2.wav')
        pygame.mixer.music.set_volume(volume)
        pygame.mixer.music.play()
def basketballgame():
    global screen_Width, screen_Height, screen, text_Font, menu_Font, font
    global score
    check = True
    mouse = pygame.mouse.get_pos()
    while check:
        
        pygame.mixer.music.stop()
        clock.tick(60)
        initialise_event()
        display()
        update_basket_score_region()
        score = check_for_basket(score)
        display_score(score, text_x, text_y)
        pygame.display.flip()
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.VIDEORESIZE:
                screen_Width, screen_Height = event.size
                screen = pygame.display.set_mode((screen_Width, screen_Height), pygame.RESIZABLE)
                text_Font = pygame.font.Font(None, int(screen_Width / 1500 * 38))
                menu_Font = pygame.font.Font(None, int(screen_Width / 1500 * 45))
                font = pygame.font.SysFont("comicsansms", int(screen_Width / 1500 * 32))
            if event.type == pygame.MOUSEBUTTONUP:
                if x_back_button + width > mouse[0] > x_back_button and y_back_button + height > mouse[1] > y_back_button:
                    user_money += score * 10
                    update_account(user_id, user_money)
                    check = False
                    return 0
def memorytest():
    file = 'sounds/_audio_the_labyrinth.mp3'
    pygame.mixer.init()
    pygame.mixer.music.load(file)
    pygame.mixer.music.set_volume(volume)
    pygame.mixer.music.play()
    FPS = 30  # frames per second, the general speed of the program
    REVEALSPEED = 7  # speed boxes' sliding reveals and covers
    BOXSIZE = int(screen_Height / 20)  # size of box height & width in pixels
    GAPSIZE = 10  # size of gap between boxes in pixels
    BOARDWIDTH = 10  # number of columns of icons
    BOARDHEIGHT = 7  # number of rows of icons
    assert (BOARDWIDTH * BOARDHEIGHT) % 2 == 0, 'Board needs to have an even number of boxes for pairs of matches.'
    XMARGIN = int((screen_Width - (BOARDWIDTH * (BOXSIZE + GAPSIZE))) / 2)
    YMARGIN = int((screen_Height - (BOARDHEIGHT * (BOXSIZE + GAPSIZE))) / 2)
    #            R    G    B
    GRAY = (100, 100, 100)
    NAVYBLUE = (60, 60, 100)
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    YELLOW = (255, 255, 0)
    ORANGE = (255, 128, 0)
    PURPLE = (255, 0, 255)
    CYAN = (0, 255, 255)
    BGCOLOR = NAVYBLUE
    LIGHTBGCOLOR = GRAY
    BOXCOLOR = WHITE
    HIGHLIGHTCOLOR = BLUE
    DONUT = 'donut'
    SQUARE = 'square'
    DIAMOND = 'diamond'
    LINES = 'lines'
    OVAL = 'oval'
    ALLCOLORS = (RED, GREEN, BLUE, YELLOW, ORANGE, PURPLE, CYAN)
    ALLSHAPES = (DONUT, SQUARE, DIAMOND, LINES, OVAL)
    global revealBoxes
    assert len(ALLCOLORS) * len(
        ALLSHAPES) * 2 >= BOARDWIDTH * BOARDHEIGHT, "Board is too big for the number of shapes/colors defined."
    def main():
        global FPSCLOCK, DISPLAYSURF, user_id, user_money, screen_Width, screen_Height, screen, text_Font, menu_Font, font
        FPSCLOCK = pygame.time.Clock()
        DISPLAYSURF = pygame.display.set_mode((screen_Width, screen_Height), pygame.RESIZABLE)

        chay = True
        mousex = 0  # used to store x coordinate of mouse event
        mousey = 0  # used to store y coordinate of mouse event

        mainBoard = getRandomizedBoard()
        revealedBoxes = generateRevealedBoxesData(False)

        firstSelection = None  # stores the (x, y) of the first box clicked.

        DISPLAYSURF.fill(BGCOLOR)
        startGameAnimation(mainBoard)

        while chay:  # main game loop
            mouseClicked = False
            x_back_button = screen_Width / (15 / 13)
            y_back_button = screen_Height / (8 / 6)
            DISPLAYSURF.fill(BGCOLOR)  # drawing the window
            drawBoard(mainBoard, revealedBoxes)
            user_info = text_Font.render('ID: ' + user_id, True, white)
            money_info = text_Font.render('Money: ' + str(user_money), True, white)
            screen.blit(user_info, (
                screen_Width - user_info.get_width() - money_info.get_width() - screen_Width / (1500 / 40),
                screen_Height / (800 / 10)))
            screen.blit(money_info, (
                screen_Width - money_info.get_width() - screen_Width / (1500 / 20), screen_Height / (800 / 10)))
            tien_thuong = text_Font.render('you CAN get 2000 point game by win this game !', True, bright_red)
            screen.blit(tien_thuong, (screen_Width / 3.5, screen_Height / 8))
            mouse = pygame.mouse.get_pos()
            if x_back_button + width > mouse[0] > x_back_button and y_back_button + height > mouse[
                1] > y_back_button:  # tạo hiệu ứng khi click  vào logo
                pygame.draw.rect(screen, bright_red, (
                    x_back_button, y_back_button, screen_Width / (1500 / 100), screen_Height / (800 / 50)))
            else:
                pygame.draw.rect(screen, old_red, (
                    x_back_button, y_back_button, screen_Width / (1500 / 100), screen_Height / (800 / 50)))
            screen.blit(back_button, (x_back_button + screen_Width / (1500 / 10), y_back_button))

            for event in pygame.event.get():  # event handling loop
                if event.type == pygame.VIDEORESIZE:
                    screen_Width, screen_Height = event.size
                    screen = pygame.display.set_mode((screen_Width, screen_Height), pygame.RESIZABLE)
                    text_Font = pygame.font.Font(None, int(screen_Width / 1500 * 38))
                    menu_Font = pygame.font.Font(None, int(screen_Width / 1500 * 45))
                if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                    chay = False
                    pygame.quit()
                    sys.exit()
                elif event.type == MOUSEMOTION:
                    mousex, mousey = event.pos
                elif event.type == MOUSEBUTTONUP:
                    mousex, mousey = event.pos
                    mouseClicked = True
                    if x_back_button + width > mouse[0] > x_back_button and y_back_button + height > mouse[
                        1] > y_back_button:
                        pygame.mixer.music.stop()
                        chay = False
                        pygame.mixer.init()
                        pygame.mixer.music.load('Sounds/nhac2.wav')
                        pygame.mixer.music.set_volume(volume)
                        pygame.mixer.music.play()
                        return 0

            boxx, boxy = getBoxAtPixel(mousex, mousey)
            if boxx != None and boxy != None:
                # The mouse is currently over a box.
                if not revealedBoxes[boxx][boxy]:
                    drawHighlightBox(boxx, boxy)
                if not revealedBoxes[boxx][boxy] and mouseClicked:
                    revealBoxesAnimation(mainBoard, [(boxx, boxy)])
                    revealedBoxes[boxx][boxy] = True  # set the box as "revealed"
                    if firstSelection == None:  # the current box was the first box clicked
                        firstSelection = (boxx, boxy)
                    else:  # the current box was the second box clicked
                        # Check if there is a match between the two icons.
                        icon1shape, icon1color = getShapeAndColor(mainBoard, firstSelection[0], firstSelection[1])
                        icon2shape, icon2color = getShapeAndColor(mainBoard, boxx, boxy)

                        if icon1shape != icon2shape or icon1color != icon2color:
                            # Icons don't match. Re-cover up both selections.
                            pygame.time.wait(1000)  # 1000 milliseconds = 1 sec
                            coverBoxesAnimation(mainBoard, [(firstSelection[0], firstSelection[1]), (boxx, boxy)])
                            revealedBoxes[firstSelection[0]][firstSelection[1]] = False
                            revealedBoxes[boxx][boxy] = False
                        elif hasWon(revealedBoxes):  # check if all pairs found
                            gameWonAnimation(mainBoard)
                            pygame.time.wait(2000)
                            user_money += 2000
                            update_account(user_id, user_money)
                            # Reset the board
                            mainBoard = getRandomizedBoard()
                            revealedBoxes = generateRevealedBoxesData(False)

                            # Show the fully unrevealed board for a second.
                            drawBoard(mainBoard, revealedBoxes)
                            pygame.display.update()
                            pygame.time.wait(1000)

                            # Replay the start game animation.
                            startGameAnimation(mainBoard)
                        firstSelection = None  # reset firstSelection variable

            # Redraw the screen and wait a clock tick.
            pygame.display.update()
            FPSCLOCK.tick(FPS)
    def generateRevealedBoxesData(val):
        revealedBoxes = []
        for i in range(BOARDWIDTH):
            revealedBoxes.append([val] * BOARDHEIGHT)
        return revealedBoxes
    def getRandomizedBoard():
        # Get a list of every possible shape in every possible color.
        icons = []
        for color in ALLCOLORS:
            for shape in ALLSHAPES:
                icons.append((shape, color))
        random.shuffle(icons)  # randomize the order of the icons list
        numIconsUsed = int(BOARDWIDTH * BOARDHEIGHT / 2)  # calculate how many icons are needed
        icons = icons[:numIconsUsed] * 2  # make two of each
        random.shuffle(icons)
        # Create the board data structure, with randomly placed icons.
        board = []
        for x in range(BOARDWIDTH):
            column = []
            for y in range(BOARDHEIGHT):
                column.append(icons[0])
                del icons[0]  # remove the icons as we assign them
            board.append(column)
        return board
    def splitIntoGroupsOf(groupSize, theList):
        # splits a list into a list of lists, where the inner lists have at
        # most groupSize number of items.
        result = []
        for i in range(0, len(theList), groupSize):
            result.append(theList[i:i + groupSize])
        return result
    def leftTopCoordsOfBox(boxx, boxy):
        # Convert board coordinates to pixel coordinates
        left = boxx * (BOXSIZE + GAPSIZE) + XMARGIN
        top = boxy * (BOXSIZE + GAPSIZE) + YMARGIN
        return (left, top)
    def getBoxAtPixel(x, y):
        for boxx in range(BOARDWIDTH):
            for boxy in range(BOARDHEIGHT):
                left, top = leftTopCoordsOfBox(boxx, boxy)
                boxRect = pygame.Rect(left, top, BOXSIZE, BOXSIZE)
                if boxRect.collidepoint(x, y):
                    return (boxx, boxy)
        return (None, None)
    def drawIcon(shape, color, boxx, boxy):
        quarter = int(BOXSIZE * 0.25)  # syntactic sugar
        half = int(BOXSIZE * 0.5)  # syntactic sugar
        left, top = leftTopCoordsOfBox(boxx, boxy)  # get pixel coords from board coords
        # Draw the shapes
        if shape == DONUT:
            pygame.draw.circle(DISPLAYSURF, color, (left + half, top + half), half - 5)
            pygame.draw.circle(DISPLAYSURF, BGCOLOR, (left + half, top + half), quarter - 5)
        elif shape == SQUARE:
            pygame.draw.rect(DISPLAYSURF, color, (left + quarter, top + quarter, BOXSIZE - half, BOXSIZE - half))
        elif shape == DIAMOND:
            pygame.draw.polygon(DISPLAYSURF, color, (
                (left + half, top), (left + BOXSIZE - 1, top + half), (left + half, top + BOXSIZE - 1),
                (left, top + half)))
        elif shape == LINES:
            for i in range(0, BOXSIZE, 4):
                pygame.draw.line(DISPLAYSURF, color, (left, top + i), (left + i, top))
                pygame.draw.line(DISPLAYSURF, color, (left + i, top + BOXSIZE - 1), (left + BOXSIZE - 1, top + i))
        elif shape == OVAL:
            pygame.draw.ellipse(DISPLAYSURF, color, (left, top + quarter, BOXSIZE, half))
    def getShapeAndColor(board, boxx, boxy):
        # shape value for x, y spot is stored in board[x][y][0]
        # color value for x, y spot is stored in board[x][y][1]
        return board[boxx][boxy][0], board[boxx][boxy][1]
    def drawBoxCovers(board, boxes, coverage):
        # Draws boxes being covered/revealed. "boxes" is a list
        # of two-item lists, which have the x & y spot of the box.
        for box in boxes:
            left, top = leftTopCoordsOfBox(box[0], box[1])
            pygame.draw.rect(DISPLAYSURF, BGCOLOR, (left, top, BOXSIZE, BOXSIZE))
            shape, color = getShapeAndColor(board, box[0], box[1])
            drawIcon(shape, color, box[0], box[1])
            if coverage > 0:  # only draw the cover if there is an coverage
                pygame.draw.rect(DISPLAYSURF, BOXCOLOR, (left, top, coverage, BOXSIZE))
        pygame.display.update()
        FPSCLOCK.tick(FPS)
    def revealBoxesAnimation(board, boxesToReveal):
        # Do the "box reveal" animation.
        for coverage in range(BOXSIZE, (-REVEALSPEED) - 1, -REVEALSPEED):
            drawBoxCovers(board, boxesToReveal, coverage)
    def coverBoxesAnimation(board, boxesToCover):
        # Do the "box cover" animation.
        for coverage in range(0, BOXSIZE + REVEALSPEED, REVEALSPEED):
            drawBoxCovers(board, boxesToCover, coverage)
    def drawBoard(board, revealed):
        # Draws all of the boxes in their covered or revealed state.
        for boxx in range(BOARDWIDTH):
            for boxy in range(BOARDHEIGHT):
                left, top = leftTopCoordsOfBox(boxx, boxy)
                if not revealed[boxx][boxy]:
                    # Draw a covered box.
                    pygame.draw.rect(DISPLAYSURF, BOXCOLOR, (left, top, BOXSIZE, BOXSIZE))
                else:
                    # Draw the (revealed) icon.
                    shape, color = getShapeAndColor(board, boxx, boxy)
                    drawIcon(shape, color, boxx, boxy)
    def drawHighlightBox(boxx, boxy):
        left, top = leftTopCoordsOfBox(boxx, boxy)
        pygame.draw.rect(DISPLAYSURF, HIGHLIGHTCOLOR, (
            left - screen_Width / (1500 / 5), top - screen_Height / (800 / 5), BOXSIZE + 10, BOXSIZE + 10), 4)
    def startGameAnimation(board):
        # Randomly reveal the boxes 8 at a time.
        coveredBoxes = generateRevealedBoxesData(False)
        boxes = []
        for x in range(BOARDWIDTH):
            for y in range(BOARDHEIGHT):
                boxes.append((x, y))
        random.shuffle(boxes)
        boxGroups = splitIntoGroupsOf(8, boxes)
        drawBoard(board, coveredBoxes)
        for boxGroup in boxGroups:
            revealBoxesAnimation(board, boxGroup)
            coverBoxesAnimation(board, boxGroup)
    def gameWonAnimation(board):
        # flash the background color when the player has won
        coveredBoxes = generateRevealedBoxesData(True)
        color1 = LIGHTBGCOLOR
        color2 = BGCOLOR
        for i in range(13):
            color1, color2 = color2, color1  # swap colors
            DISPLAYSURF.fill(color1)
            drawBoard(board, coveredBoxes)
            pygame.display.update()
            pygame.time.wait(300)
    def hasWon(revealedBoxes):
        # Returns True if all the boxes have been revealed, otherwise False
        for i in revealedBoxes:
            if False in i:
                return False  # return False if any boxes are covered.
        return True
    def money():
        global revealedBoxes
        if hasWon(revealedBoxes) == True:
            return 1000
    if __name__ == '__main__':
        main()
def update_records(user_id, money_bet, state):
    with open('records.txt', 'a') as record:
        record.write(f'{user_id}\t-\t{state}\t-\t{money_bet}\n')
def get_records(user_id):
    result = []
    with open('records.txt', 'r') as record:
        for line in record:
            if line.split('\t')[0] == user_id:
                result.append(line)
    return result[-5:]
def menu(chucnang):
    menu = True
    global user_id, user_money, screen_Width, screen_Height, screen, text_Font, menu_Font, font, volume
    while menu:
        play_game_button = font.render('Main Game', True, white)
        play_minigame_button = font.render('Mini Game', True, white)
        option_button = font.render('Audio', True, white)
        exit_button = font.render('Exit', True, white)
        flappybird_game_button = font.render('Flappy Bird', True, white)
        basketball_game_button = font.render('Basketball', True, white)
        memorytest_game_button = font.render('Memory test', True, white)
        back_button = text_Font.render('Back', True, black)
        increase_button = font.render('  >', True, white)
        decrease_button = font.render('<  ', True, white)
        sound = font.render(str(round(volume*100)), True, black)
        x_play_game_button = screen_Width / (1500 / 380)
        y_play_game_button = screen_Height / (800 / 400)

        x_flappybird_game_button = screen_Width / (1500 / (380 + 230))
        y_flappybird_game_button = screen_Height / 2

        x_basketball_game_button = screen_Width / (1500 / 610)
        y_basketball_game_button = screen_Height / (800 / 460)

        x_memorytest_game_button = screen_Width / (1500 / 610)
        y_memorytest_game_button = screen_Height / (800 / 520)

        x_play_minigame_button = screen_Width / (1500 / 380)
        y_play_minigame_button = screen_Height / (800 / 460)
        x_option_button = screen_Width * 19 / 75
        y_option_button = screen_Height * 13 / 20
        x_exit_button = screen_Width * 19 / 75
        y_exit_button = screen_Height * 29 / 40

        x_decrease_button = screen_Width/2 - decrease_button.get_width()/2
        y_decrease_button = y_memorytest_game_button
        x_increase_button = screen_Width/2 + increase_button.get_width()/2
        y_increase_button = y_memorytest_game_button

        records = get_records(user_id)
        global backgroundmenu
        backgroundmenu = pygame.transform.scale(backgroundmenu, (screen_Width, screen_Height))
        screen.blit(backgroundmenu, (0, 0))
        # pygame.draw.rect(screen, bright_red, (int(0.7 * screen_Width), int(0.4 * screen_Height), 350, 400))
        pygame.gfxdraw.box(screen, pygame.Rect(int(0.7 * screen_Width) - screen_Width / 75,
                                               int(0.4 * screen_Height) - screen_Height / 40,
                                               screen_Width / (1500 / 350), screen_Height / 2),
                           (175, 119, 107, 200))
        history = menu_Font.render('History', True, black)
        screen.blit(history, (
            int(0.7 * screen_Width + screen_Width / (1500 / 10)), int(0.4 * screen_Height) + screen_Height / 80))
        for i in range(len(records)):
            records[i] = records[i].rstrip().replace('\t', '    ')
            record = text_Font.render(records[i], True, white)
            screen.blit(record, (int(0.7 * screen_Width + screen_Width / 150),
                                 int(0.4 * screen_Height) + screen_Height / (80) + (i + 1) * screen_Height / (
                                         800 / 50)))
        user_info = text_Font.render('ID: ' + user_id, True, black)
        money_info = text_Font.render('Money: ' + str(user_money), True, black)
        screen.blit(user_info, (
            screen_Width - user_info.get_width() - money_info.get_width() - screen_Width / (75 / 2),
            screen_Height / 80))
        screen.blit(money_info, (screen_Width - money_info.get_width() - screen_Width / 75, screen_Height / 80))

        mouse = pygame.mouse.get_pos()
        if chucnang == 0:
            if x_play_game_button + width > mouse[0] > x_play_game_button and y_play_game_button + height > mouse[
                1] > y_play_game_button:  # tạo hiệu ứng khi click  vào logo
                pygame.draw.rect(screen, bright_red, (
                    x_play_game_button, y_play_game_button, screen_Width / (1500 / 200), screen_Height / 16))
            else:
                pygame.draw.rect(screen, old_red, (
                    x_play_game_button, y_play_game_button, screen_Width / (1500 / 200), screen_Height / 16))
            if x_play_minigame_button + width > mouse[0] > x_play_minigame_button and y_play_minigame_button + height > \
                    mouse[1] > y_play_minigame_button:  # tạo hiệu ứng khi click  vào logo
                pygame.draw.rect(screen, bright_red, (
                    x_play_minigame_button, y_play_minigame_button, screen_Width / (1500 / 200), screen_Height / 16))
            else:
                pygame.draw.rect(screen, old_red, (
                    x_play_minigame_button, y_play_minigame_button, screen_Width / (1500 / 200), screen_Height / 16))
            if x_option_button + width > mouse[0] > x_option_button and y_option_button + height > mouse[
                1] > y_option_button:  # tạo hiệu ứng khi click  vào logo
                pygame.draw.rect(screen, bright_red,
                                 (x_option_button, y_option_button, screen_Width / (1500 / 200), screen_Height / 16))
            else:
                pygame.draw.rect(screen, old_red,
                                 (x_option_button, y_option_button, screen_Width / (1500 / 200), screen_Height / 16))
            if x_exit_button + width > mouse[0] > x_exit_button and y_exit_button + height > mouse[
                1] > y_exit_button:  # tạo hiệu ứng khi click  vào logo
                pygame.draw.rect(screen, bright_red,
                                 (x_exit_button, y_exit_button, screen_Width / (1500 / 200), screen_Height / 16))
            else:
                pygame.draw.rect(screen, old_red,
                                 (x_exit_button, y_exit_button, screen_Width / (1500 / 200), screen_Height / 16))
            screen.blit(play_game_button, (x_play_game_button + screen_Width / 150, y_play_game_button))
            screen.blit(play_minigame_button, (x_play_minigame_button + screen_Width / 150, y_play_minigame_button))
            screen.blit(option_button, (x_option_button + screen_Width / 150, y_option_button))
            screen.blit(exit_button, (x_exit_button + screen_Width / 150, y_exit_button))

        if chucnang == 2:
            if x_flappybird_game_button + width > mouse[
                0] > x_flappybird_game_button and y_flappybird_game_button + height > mouse[
                1] > y_flappybird_game_button:  # tạo hiệu ứng khi click  vào logo
                pygame.draw.rect(screen, bright_red, (
                    x_flappybird_game_button, y_flappybird_game_button, screen_Width / (1500 / 210),
                    screen_Height / 16))
            else:
                pygame.draw.rect(screen, old_red, (
                    x_flappybird_game_button, y_flappybird_game_button, screen_Width / (1500 / 210),
                    screen_Height / 16))
            screen.blit(flappybird_game_button,
                        (x_flappybird_game_button + screen_Width / 300, y_flappybird_game_button))

            if x_basketball_game_button + width > mouse[
                0] > x_basketball_game_button and y_basketball_game_button + height > mouse[
                1] > y_basketball_game_button:  # tạo hiệu ứng khi click  vào logo
                pygame.draw.rect(screen, bright_red, (
                    x_basketball_game_button, y_basketball_game_button, screen_Width / (1500 / 210),
                    screen_Height / 16))
            else:
                pygame.draw.rect(screen, old_red, (
                    x_basketball_game_button, y_basketball_game_button, screen_Width / (1500 / 210),
                    screen_Height / 16))
            screen.blit(basketball_game_button,
                        (x_basketball_game_button + screen_Width / 300, y_basketball_game_button))

            if x_memorytest_game_button + width > mouse[
                0] > x_memorytest_game_button and y_memorytest_game_button + height > mouse[
                1] > y_memorytest_game_button:  # tạo hiệu ứng khi click  vào logo
                pygame.draw.rect(screen, bright_red, (
                    x_memorytest_game_button, y_memorytest_game_button, screen_Width / (1500 / 210),
                    screen_Height / 16))
            else:
                pygame.draw.rect(screen, old_red, (
                    x_memorytest_game_button, y_memorytest_game_button, screen_Width / (1500 / 210),
                    screen_Height / 16))
            screen.blit(memorytest_game_button,
                        (x_memorytest_game_button + screen_Width / 300, y_memorytest_game_button))

            if int(screen_Width * 0.85) - screen_Width / (1500 / 20) <= mouse[0] <= int(
                    screen_Width * 0.85) + screen_Width / (
                    1500 / 20) + back_button.get_width() and screen_Height - screen_Height / (800 / 115) <= mouse[
                1] <= screen_Height - screen_Height / (800 / 115) + back_button.get_height() + screen_Height / (
                    800 / 30):
                pygame.draw.rect(screen, bright_red, (
                    int(screen_Width * 0.85) - screen_Width / (1500 / 20), screen_Height - screen_Height / (800 / 115),
                    back_button.get_width() + screen_Width / (1500 / 40),
                    back_button.get_height() + screen_Height / (800 / 30)))
            else:
                pygame.draw.rect(screen, old_red, (
                    int(screen_Width * 0.85) - screen_Width / (1500 / 20), screen_Height - screen_Height / (800 / 115),
                    back_button.get_width() + screen_Width / (1500 / 40),
                    back_button.get_height() + screen_Height / (800 / 30)))
            screen.blit(back_button, (int(screen_Width * 0.85), screen_Height - screen_Height / (8)))

        if chucnang == 3:
            if int(screen_Width * 0.85) - screen_Width / (1500 / 20) <= mouse[0] <= int(
                    screen_Width * 0.85) + screen_Width / (
                    1500 / 20) + back_button.get_width() and screen_Height - screen_Height / (800 / 115) <= mouse[
                1] <= screen_Height - screen_Height / (800 / 115) + back_button.get_height() + screen_Height / (
                    800 / 30):
                pygame.draw.rect(screen, bright_red, (
                    int(screen_Width * 0.85) - (screen_Width / (1500 / 20)),
                    screen_Height - screen_Height / (800 / 115),
                    back_button.get_width() + screen_Width / (1500 / 40),
                    back_button.get_height() + screen_Height / (800 / 30)))
            else:
                pygame.draw.rect(screen, old_red, (
                    int(screen_Width * 0.85) - (screen_Width / (1500 / 20)),
                    screen_Height - screen_Height / (800 / 115),
                    back_button.get_width() + screen_Width / (1500 / 40),
                    back_button.get_height() + screen_Height / (800 / 30)))
            if x_memorytest_game_button + width > mouse[
                0] > x_memorytest_game_button and y_memorytest_game_button + height > mouse[
                1] > y_memorytest_game_button:  # tạo hiệu ứng khi click  vào logo
                pygame.draw.rect(screen, bright_red, (
                    x_memorytest_game_button, y_memorytest_game_button, screen_Width / (1500 / 210),
                    screen_Height / 16))
            else:
                pygame.draw.rect(screen, old_red, (
                    x_memorytest_game_button, y_memorytest_game_button, screen_Width / (1500 / 210),
                    screen_Height / 16))
            screen.blit(sound,
                        (x_memorytest_game_button + screen_Width / 300, y_memorytest_game_button))

            screen.blit(back_button, (int(screen_Width * 0.85), screen_Height - screen_Height / (8)))
            screen.blit(increase_button,(x_increase_button, y_increase_button))
            screen.blit(decrease_button,(x_decrease_button, y_decrease_button))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                menu = False
                pygame.quit()
                sys.exit(0)
            if event.type == pygame.VIDEORESIZE:
                screen_Width, screen_Height = event.size
                screen = pygame.display.set_mode((screen_Width, screen_Height), pygame.RESIZABLE)
                text_Font = pygame.font.Font(None, int(screen_Width / 1500 * 38))
                menu_Font = pygame.font.Font(None, int(screen_Width / 1500 * 45))
                font = pygame.font.SysFont("comicsansms", int(screen_Width / 1500 * 32))
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and volume > 0.05:
                    volume = volume - 0.05
                if event.key == pygame.K_RIGHT:
                    volume = volume + 0.05
            if event.type == pygame.MOUSEBUTTONUP:

                if chucnang == 0 and x_exit_button + width > mouse[0] > x_exit_button and y_exit_button + height > \
                        mouse[1] > y_exit_button:
                    menu = False
                    pygame.quit()
                    sys.exit(0)

                if chucnang == 0 and x_play_game_button + width > mouse[
                    0] > x_play_game_button and y_play_game_button + height > mouse[1] > y_play_game_button:
                    chucnang = 1

                if chucnang == 0 and x_option_button + width > mouse[0] > x_option_button and y_option_button + height > \
                        mouse[1] > y_option_button:
                    chucnang = 3

                if chucnang == 0 and x_play_minigame_button + width > mouse[
                    0] > x_play_minigame_button and y_play_minigame_button + height > mouse[1] > y_play_minigame_button:
                    chucnang = 2

                if chucnang == 3:
                    if int(screen_Width * 0.85) - screen_Width / 75 <= mouse[0] <= int(
                            screen_Width * 0.85) + screen_Width / 75 + back_button.get_width():
                        if screen_Height - screen_Height / (800 / 115) <= mouse[1] <= screen_Height - screen_Height / (
                                800 / 115) + back_button.get_height() + screen_Height / (800 / 30):
                            chucnang = 0

                if chucnang == 2:
                    if x_flappybird_game_button + width > mouse[
                        0] > x_flappybird_game_button and y_flappybird_game_button + height > mouse[
                        1] > y_flappybird_game_button:
                        chucnang = flappy_bird()

                    if x_basketball_game_button + width > mouse[
                        0] > x_basketball_game_button and y_basketball_game_button + height > mouse[
                        1] > y_basketball_game_button:
                        basketballgame()

                    if x_memorytest_game_button + width > mouse[
                        0] > x_memorytest_game_button and y_memorytest_game_button + height > mouse[
                        1] > y_memorytest_game_button:
                        print('hihi')
                        memorytest()

                    if int(screen_Width * 0.85) - screen_Width / 75 <= mouse[0] <= int(
                            screen_Width * 0.85) + screen_Width / 75 + back_button.get_width():
                        if screen_Height - screen_Height / (800 / 115) <= mouse[1] <= screen_Height - screen_Height / (
                                800 / 115) + back_button.get_height() + screen_Height / (800 / 30):
                            chucnang = 0
                if chucnang == 1:
                    chucnang = main_game()

        pygame.display.update()

class Character:
    def __init__(self, name=None, average_speed=10, image=None, affect=None, x_pos=None, y_pos=None):
        self.char_name = name
        self.char_avg_speed = average_speed
        self.char_image = image
        self.char_affect = affect
        self.x_position = x_pos
        self.y_position = y_pos
# store 5 characters
CHARACTERS = []
GROUP = []
# initiate character set with folder directory parameter
def init_character():
    for i in range(5):
        global set_choice
        new_character = Character()
        new_character.char_name = 'Character ' + str(i + 1)
        image_name = 'set' + str(int(set_choice)) + '/' + str(i + 1) + '.jpg'
        new_character.char_image = pygame.transform.scale(pygame.image.load(image_name),
                                                          (screen_Width // 5 - screen_Width // 30,
                                                           screen_Width // 5 - screen_Width // 16))  # chưa đổi biến '//'
        CHARACTERS.append(new_character)
def set_choosing():
    global screen_Width, screen_Height, screen, text_Font, menu_Font, font
    choosing = True
    while choosing:
        global backgroundmenu1
        backgroundmenu1 = pygame.transform.scale(backgroundmenu1, (screen_Width, screen_Height))
        screen.blit(backgroundmenu1, (0, 0))
        global user_id, user_money
        user_info = text_Font.render('ID: ' + user_id, True, black)
        money_info = text_Font.render('Money: ' + str(user_money), True, black)
        screen.blit(user_info, (
            screen_Width - user_info.get_width() - money_info.get_width() - screen_Width / (75 / 2),
            screen_Height / (80)))
        screen.blit(money_info,
                    (screen_Width - money_info.get_width() - screen_Width / (1500 / 20), screen_Height / (80)))
        title = menu_Font.render('Choose the MAP', True, white)
        screen.blit(title, (screen_Width / 2 - title.get_width() / (screen_Width / 750), screen_Height / (16)))
        for i in range(5):
            set_name = str(i + 1) + '.jpg'
            set_image = pygame.transform.scale(pygame.image.load(set_name),
                                               (screen_Width // 5 - screen_Width // 30, (screen_Height * 500) // 800))
            rect = pygame.Rect(i * screen_Width / 5, 0, screen_Width / 5, screen_Height)
            screen.blit(set_image,
                        ((screen_Width / 5) * i + (screen_Width / 10 - set_image.get_width() / 2), screen_Height / 3))
            if rect.collidepoint(pygame.mouse.get_pos()):
                pygame.draw.rect(screen, white,
                                 pygame.Rect(i * screen_Width / 5, screen_Height / 8, screen_Width / 5,
                                             screen_Height - screen_Height / 8), 2)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                choosing = False
                pygame.quit()
                sys.exit(0)
            if event.type == pygame.VIDEORESIZE:
                screen_Width, screen_Height = event.size
                screen = pygame.display.set_mode((screen_Width, screen_Height), pygame.RESIZABLE)
                text_Font = pygame.font.Font(None, int(screen_Width / 1500 * 38))
                menu_Font = pygame.font.Font(None, int(screen_Width / 1500 * 45))
                font = pygame.font.SysFont("comicsansms", int(screen_Width / 1500 * 32))
            if event.type == pygame.MOUSEBUTTONUP:
                x_pos, y_pos = pygame.mouse.get_pos()
                temp = x_pos // (screen_Width / 5)
                global set_choice
                set_choice = temp + 1
                return
        pygame.display.update()
# choosing character screen and return a number representing player choice
def character_choosing():
    global screen_Width, screen_Height, screen, text_Font, menu_Font, font
    init_character()
    choosing = True
    while choosing:
        global backgroundmenu1
        backgroundmenu1 = pygame.transform.scale(backgroundmenu1, (screen_Width, screen_Height))
        screen.blit(backgroundmenu1, (0, 0))
        global user_id, user_money
        user_info = text_Font.render('ID: ' + user_id, True, black)
        money_info = text_Font.render('Money: ' + str(user_money), True, black)
        screen.blit(user_info, (
            screen_Width - user_info.get_width() - money_info.get_width() - screen_Width / (75 / 2),
            screen_Height / 80))
        screen.blit(money_info, (screen_Width - money_info.get_width() - screen_Width / 75, screen_Height / 80))
        title = menu_Font.render('Choose the Character you bet', True, white)
        screen.blit(title, (screen_Width / 2 - title.get_width() / 2, screen_Height / 16))
        for i in range(5):
            new_character = CHARACTERS[i]
            rect = pygame.Rect(i * screen_Width / 5, 0, screen_Width / 5, screen_Height)
            screen.blit(new_character.char_image,
                        ((screen_Width / 5) * i + (screen_Width / 10 - new_character.char_image.get_width() / 2),
                         screen_Height / 3))
            name_rendering = text_Font.render(new_character.char_name, True, white)
            screen.blit(name_rendering,
                        ((screen_Width / 5) * i + (screen_Width / 10 - name_rendering.get_width() / 2),
                         screen_Height / 3 - screen_Height / (80 / 3)))
            if rect.collidepoint(pygame.mouse.get_pos()):
                pygame.draw.rect(screen, white,
                                 pygame.Rect(i * screen_Width / 5, screen_Height / 8, screen_Width / 5,
                                             screen_Height - screen_Height / 8), 2)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                choosing = False
                pygame.quit()
                sys.exit(0)
            if event.type == pygame.VIDEORESIZE:
                screen_Width, screen_Height = event.size
                screen = pygame.display.set_mode((screen_Width, screen_Height), pygame.RESIZABLE)
                text_Font = pygame.font.Font(None, int(screen_Width / 1500 * 38))
                menu_Font = pygame.font.Font(None, int(screen_Width / 1500 * 45))
                font = pygame.font.SysFont("comicsansms", int(screen_Width / 1500 * 32))
            if event.type == pygame.MOUSEBUTTONUP:
                x_pos, y_pos = pygame.mouse.get_pos()
                temp = x_pos // (screen_Width / 5)
                global choice
                choice = temp + 1
                return
        pygame.display.update()
def money_bet():
    global screen_Width, screen_Height, screen, text_Font, menu_Font, font
    active = True
    user_text = ''
    money_bet = 0
    hihi = 0
    global bought
    bought = 0
    check = 0
    while active:
        rect_text = pygame.Rect(screen_Width / (1500 / 568), screen_Height / (800 / 440), screen_Width / (1500 / 350),
                        screen_Height / (800 / 40))
        x_back_button = screen_Width / (15 / 13)
        y_back_button = screen_Height / (8 / 6)
        global backgroundmenu1
        backgroundmenu1 = pygame.transform.scale(backgroundmenu1, (screen_Width, screen_Height))
        screen.blit(backgroundmenu1, (0, 0))
        global user_id, user_money, back_button
        user_info = text_Font.render('ID: ' + user_id, True, black)
        money_info = text_Font.render('Money: ' + str(user_money), True, black)
        store = menu_Font.render('BUY RANDOM SPELL (100$)', True, white)
        done = menu_Font.render('DONE!', True, white)
        ok_button = font.render('OK', True, white)
        back_button = font.render('Back', True, white)
        x_store = screen_Width / 2 - store.get_width() / 2
        y_store = screen_Height * 0.8
        x_store_button = screen_Width / 2 - store.get_width() * 1.5 / 2
        y_store_button = y_store - store.get_height() / 4
        x_done = screen_Width / 2 - done.get_width() / 2
        y_done = screen_Height * 0.8 + store.get_height() * 1.55
        screen.blit(user_info, (
            screen_Width - user_info.get_width() - money_info.get_width() - screen_Width / (75 / 2),
            screen_Height / (80)))
        screen.blit(money_info, (screen_Width - money_info.get_width() - screen_Width / 75, screen_Height / (80)))
        mouse = pygame.mouse.get_pos()
        if x_back_button + width > mouse[0] > x_back_button and y_back_button + height > mouse[
            1] > y_back_button:  # tạo hiệu ứng khi click  vào logo
            pygame.draw.rect(screen, bright_red, (x_back_button, y_back_button, screen_Width / 15, screen_Height / 16))
        else:
            pygame.draw.rect(screen, old_red, (x_back_button, y_back_button, screen_Width / 15, screen_Height / 16))
        screen.blit(back_button, (x_back_button + 10, y_back_button))
        title = menu_Font.render('Enter the money you bet', True, white)
        screen.blit(title, (screen_Width / 2 - title.get_width() / 2, screen_Height / 4))

        if hihi == 1:
            title2 = text_Font.render('Dont have enough money? play mini game to get more !', True, white)
            screen.blit(title2, (screen_Width / 2 - title2.get_width() / 2, screen_Height / (8 / 6)))

        if (x_store_button + store.get_width() * 1.5 > mouse[
            0] > x_store_button and y_store_button + store.get_height() * 1.5 > mouse[
                1] > y_store_button) or bought == 0:  # tạo hiệu ứng khi click  vào logo
            pygame.draw.rect(screen, bright_red,
                             (x_store_button, y_store_button, store.get_width() * 1.5, store.get_height() * 1.5))
        else:
            pygame.draw.rect(screen, old_red,
                             (x_store_button, y_store_button, store.get_width() * 1.5, store.get_height() * 1.5))
        screen.blit(store, (x_store, y_store))
        if bought == 1:
            screen.blit(done, (x_done, y_done))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                active = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.VIDEORESIZE:
                screen_Width, screen_Height = event.size
                screen = pygame.display.set_mode((screen_Width, screen_Height), pygame.RESIZABLE)
                text_Font = pygame.font.Font(None, int(screen_Width / 1500 * 38))
                menu_Font = pygame.font.Font(None, int(screen_Width / 1500 * 45))
                font = pygame.font.SysFont("comicsansms", int(screen_Width / 1500 * 32))
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    user_text = user_text[:-1]
                else:
                    user_text += event.unicode
            
            if event.type == pygame.MOUSEBUTTONUP:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if (screen_Width / (1500 / 706) <= mouse_x <= screen_Width / (1500 / 706) + ok_button.get_width()) and (
                        screen_Height / (8 / 5) <= mouse_y <= screen_Height / (8 / 5) + ok_button.get_height()):
                    money_bet = user_text
                    
                    if int(user_money) >= int(money_bet) :
                        return money_bet
                    else:
                        hihi = 1
                if (x_store_button + store.get_width() * 1.5 > mouse[
                    0] > x_store_button and y_store_button + store.get_height() * 1.5 > mouse[
                        1] > y_store_button) and bought != 1:
                    if int(user_money) >= 100:
                        bought = 1
                        user_money -= 100
                        update_account(user_id, user_money)
                    else:
                        hihi = 1
                if x_back_button + width > mouse[0] > x_back_button and y_back_button + height > mouse[
                    1] > y_back_button:
                    if bought == 1:
                        user_money += 100
                        update_account(user_id, user_money)
                    reset_game()
                    menu(0)
            if (event.type == pygame.KEYDOWN) and (event.key == pygame.K_RETURN):
                money_bet = user_text
                if int(user_money) >= int(money_bet):
                    return money_bet
                else:
                    hihi = 1
        mouse = pygame.mouse.get_pos()
        if screen_Width / 2.2 + screen_Width / 15 > mouse[
            0] > screen_Width / 2.2 and screen_Height / 1.6 + screen_Height / 16 > mouse[
            1] > screen_Height / 1.6:  # tạo hiệu ứng khi click  vào logo
            pygame.draw.rect(screen, bright_red,
                             (int(screen_Width / 2.2), int(screen_Height / 1.6), screen_Width / 15, screen_Height / 16))
        else:
            pygame.draw.rect(screen, old_red,
                             (int(screen_Width / 2.2), int(screen_Height / 1.6), screen_Width / 15, screen_Height / 16))
        screen.blit(ok_button, (screen_Width / (1500 / 706), screen_Height / (800 / 498)))
        pygame.draw.rect(screen, white, rect_text, 3)
        text_surface = text_Font.render(user_text, True, white)
        screen.blit(text_surface, (rect_text.x + 5, rect_text.y + 5))  # căn đều lề khi input // doi bien sau 
        pygame.display.update()
class my_sprite(pygame.sprite.Sprite):
    global RATIOS
    RATIOS = [1, 1, 1,1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 6, 2, 2, 2, 3, 3, 7, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4,
              4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5]
    def __init__(self, number, x_pos, y_pos):
        super(my_sprite, self).__init__()
        global set_choice
        self.x_position = x_pos
        self.y_position = y_pos
        self.number = number
        action = 'run'
        self.images = [pygame.transform.scale(pygame.image.load(img), (screen_Width // 25, screen_Height // 8)) for img
                       in
                       glob.glob(f"set{int(set_choice)}/c{number}/{action}*.png")]
        self.index = 0
        self.running = 0
        self.rank = 0
        self.x_box = random.randint(screen_Width // 6, screen_Width // 3)
        self.y_box = self.y_position + screen_Height / 40
        self.dem = 0
        self.curse = RATIOS[random.randint(0, 46)]
        self.time = 0
        self.box = pygame.transform.scale(box1, (screen_Width // 25, screen_Height // 13))

        self.time_sound = 0
        self.sound = 0

        self.demSound = 0

    def update(self):
        global dem, bought
        dem = 0
        finish = 20
        if self.index >= len(self.images):
            self.index = 0
        self.image = self.images[self.index]
        self.index += 1
        if self.number == choice and bought == 1:
            self.curse = RATIOS[random.randint(0, 46)]
        if self.running == 0:
            self.time = 0
            self.action = 'run'
            self.x_position += int(random.uniform(3, 7))
            self.rect = pygame.Rect(self.x_position, self.y_position, screen_Width // 25, screen_Height // 8)
        if self.running == 1 and self.time != 1:  # run slow
            self.action = 'walk'
            number = self.number
            self.images = [pygame.transform.scale(pygame.image.load(img), (screen_Width // 25, screen_Height // 8)) for
                           img in
                           glob.glob(f"set{int(set_choice)}/c{number}/{self.action}*.png")]
            self.x_position += int(random.uniform(2, 4))
            self.rect = pygame.Rect(self.x_position, self.y_position, screen_Width // 25, screen_Height // 8)
            self.time += 1
            if self.time == 1:
                self.running = 0
                self.action = 'run'
                number = self.number
                self.images = [pygame.transform.scale(pygame.image.load(img), (screen_Width // 25, screen_Height // 8))
                               for img in
                               glob.glob(f"set{int(set_choice)}/c{number}/{self.action}*.png")]
                self.x_position += int(random.uniform(3, 7))

        if self.running == 2 and self.time != 20:  # run fast
            self.action = 'run'
            number = self.number
            self.images = [pygame.transform.scale(pygame.image.load(img), (screen_Width // 25, screen_Height // 8)) for
                           img in
                           glob.glob(f"set{int(set_choice)}/c{number}/{self.action}*.png")]
            self.x_position += int(random.uniform(10, 14))
            self.rect = pygame.Rect(self.x_position, self.y_position, screen_Width // 25, screen_Height // 8)
            self.time += 1
            if self.time == 20:
                self.running = 0
                self.action = 'run'
                number = self.number
                self.images = [pygame.transform.scale(pygame.image.load(img), (screen_Width // 25, screen_Height // 8))
                               for img in
                               glob.glob(f"set{int(set_choice)}/c{number}/{self.action}*.png")]
                self.x_position += int(random.uniform(3, 7))

        if self.running == 3 and self.time != 12:  # hiệu ứng bị choáng
            self.action = 'stun'
            number = self.number
            self.images = [pygame.transform.scale(pygame.image.load(img), (screen_Width // 25, screen_Height // 8)) for
                           img in
                           glob.glob(f"set{int(set_choice)}/c{number}/{self.action}*.png")]
            self.x_position += 0
            self.rect = pygame.Rect(self.x_position, self.y_position, screen_Width // 25, screen_Height // 8)
            self.time += 1
            if self.time == 12:
                self.running = 0
                self.action = 'run'
                number = self.number
                self.images = [pygame.transform.scale(pygame.image.load(img), (screen_Width // 25, screen_Height // 8))
                               for img in
                               glob.glob(f"set{int(set_choice)}/c{number}/{self.action}*.png")]
                self.x_position += int(random.uniform(3, 7))

        if self.running == 4 and self.time != 16:  # hiệu ứng chạy ngược lại
            self.action = 'r'
            number = self.number
            self.images = [pygame.transform.scale(pygame.image.load(img), (screen_Width // 25, screen_Height // 8)) for
                           img in
                           glob.glob(f"set{int(set_choice)}/c{number}/{self.action}*.png")]
            self.x_position -= int(random.uniform(2, 4))
            self.rect = pygame.Rect(self.x_position, self.y_position, screen_Width // 25, screen_Height // 8)
            self.time += 1
            if self.time == 16:
                self.running = 0
                self.action = 'run'
                number = self.number
                self.images = [pygame.transform.scale(pygame.image.load(img), (screen_Width // 25, screen_Height // 8))
                               for img in
                               glob.glob(f"set{int(set_choice)}/c{number}/{self.action}*.png")]
                self.x_position += int(random.uniform(2, 4))

        if self.running == 5 and self.time != 1:  # hiệu ứng dịch chuyển tức thời
            self.action = 'run'
            number = self.number
            self.images = [pygame.transform.scale(pygame.image.load(img), (screen_Width // 25, screen_Height // 8)) for
                           img in
                           glob.glob(f"set{int(set_choice)}/c{number}/{self.action}*.png")]
            self.x_position += int(random.uniform(20, 40))
            self.rect = pygame.Rect(self.x_position, self.y_position, screen_Width // 25, screen_Height // 8)
            self.time += 1
            if self.x_position > screen_Width / (1500 / 1309):
                self.dem = 3
            if self.time == 1:
                self.running = 0
                self.action = 'run'
                number = self.number
                self.images = [pygame.transform.scale(pygame.image.load(img), (screen_Width // 25, screen_Height // 8))
                               for img in
                               glob.glob(f"set{int(set_choice)}/c{number}/{self.action}*.png")]
                self.x_position += int(random.uniform(3, 7))

        if self.running == 6 and self.time != 1:  # Dịch chuyển về đích
            self.dem = 3
            self.action = 'run'
            number = self.number
            self.images = [pygame.transform.scale(pygame.image.load(img), (screen_Width // 25, screen_Height // 8)) for
                           img in
                           glob.glob(f"set{int(set_choice)}/c{number}/{self.action}*.png")]
            self.x_position = screen_Width / (1500 / 1396)
            self.rect = pygame.Rect(self.x_position, self.y_position, screen_Width // 25, screen_Height // 8)
            self.time += 1
            if self.time == 1:
                self.running = 0
                self.action = 'run'
                number = self.number
                self.images = [pygame.transform.scale(pygame.image.load(img), (screen_Width // 25, screen_Height // 8))
                               for img in
                               glob.glob(f"set{int(set_choice)}/c{number}/{self.action}*.png")]
                self.x_position += int(random.uniform(3, 7))
                self.rect = pygame.Rect(self.x_position, self.y_position, screen_Width // 25, screen_Height // 8)

        if self.running == 7 and self.time != 1:  # Dịch chuyển về xuất phát
            self.action = 'run'
            self.dem = 2
            number = self.number
            self.images = [pygame.transform.scale(pygame.image.load(img), (screen_Width // 25, screen_Height // 8)) for
                           img in
                           glob.glob(f"set{int(set_choice)}/c{number}/{self.action}*.png")]
            self.x_position = 0
            self.rect = pygame.Rect(self.x_position, self.y_position, screen_Width // 25, screen_Height // 8)
            self.time += 1
            if self.time == 1:
                self.running = 0
                self.action = 'run'
                number = self.number
                self.images = [pygame.transform.scale(pygame.image.load(img), (screen_Width // 25, screen_Height // 8))
                               for img in
                               glob.glob(f"set{int(set_choice)}/c{number}/{self.action}*.png")]
                self.x_position += int(random.uniform(3, 7))
                self.rect = pygame.Rect(self.x_position, self.y_position, screen_Width // 25, screen_Height // 8)

        if self.dem <= 2:
            screen.blit(self.box, (self.x_box, self.y_box))  # tạo hộp ngại vật

            if self.x_position >= self.x_box or bought == 1:  # vi tri đạp chướng ngại vật
                bought = 0
                if self.curse == 1:
                    self.running = 1
                    stunSound = pygame.mixer.Sound('Sounds/stun.wav')
                    pygame.mixer.music.set_volume(volume)
                    stunSound.play()
                if self.curse == 2:
                    self.running = 2
                    fastSound = pygame.mixer.Sound('Sounds/ding.wav')
                    pygame.mixer.music.set_volume(volume)
                    fastSound.play()
                if self.curse == 3:
                    self.running = 3
                    slowSound = pygame.mixer.Sound('Sounds/hit.wav')
                    pygame.mixer.music.set_volume(volume)
                    slowSound.play()
                if self.curse == 4:
                    self.running = 4
                    slowSound = pygame.mixer.Sound('Sounds/hit.wav')
                    pygame.mixer.music.set_volume(volume)
                    slowSound.play()
                if self.curse == 5:
                    self.running = 5
                    slowSound = pygame.mixer.Sound('Sounds/hit.wav')
                    pygame.mixer.music.set_volume(volume)
                    slowSound.play()
                if self.curse == 6:
                    self.running = 6
                    fastSound = pygame.mixer.Sound('Sounds/ding.wav')
                    pygame.mixer.music.set_volume(volume)
                    fastSound.play()
                if self.curse == 7:
                    self.running = 7
                    fastSound = pygame.mixer.Sound('Sounds/ding.wav')
                    pygame.mixer.music.set_volume(volume)
                    fastSound.play()
                self.dem += 1
                self.time = 0
                if self.dem <= 2:
                    random_x = int(self.x_position + screen_Width // 5)
                    self.x_box = random.randint(random_x, random_x)
                    if self.x_box >= line:
                        self.x_box = random.randint(self.x_position, line)
                        self.dem = 3
                    self.curse = RATIOS[random.randint(0, 46)]
        if self.x_position >= line:
            while self.rank == 0:
                self.rank = 1
                global rank, winner
                rank.append(self.number)
                winner += 1
                winSound = pygame.mixer.Sound('Sounds/oh_yeah.wav')
                winSound.set_volume(volume)
                winSound.play()
                if rank[0] == self.number:
                    # winSound=pygame.mixer.Sound('Sounds\winner.wav')
                    winSound = pygame.mixer.Sound('Sounds/oh_yeah.wav')
                    winSound.set_volume(volume)
                    winSound.play()
            number = self.number
            self.action = 'pic'
            self.images = [pygame.transform.scale(pygame.image.load(img), (screen_Width // 25, screen_Height // 8)) for
                           img in
                           glob.glob(f"set{int(set_choice)}/c{number}/{self.action}*.png")]
            self.running = -1
def race():
    global bet_money, GROUP, set_choice, last
    global screen_Width, screen_Height, screen, text_Font, menu_Font, font
    last = 0
    bet_money = int(money_bet())
    setchoice = int(set_choice)
    if setchoice == 1:
        race_map = pygame.image.load("set1/race.png")
    if setchoice == 2:
        race_map = pygame.image.load("set2/race.png")
    if setchoice == 3:
        race_map = pygame.image.load("set3/race.png")
    if setchoice == 4:
        race_map = pygame.image.load("set4/race.png")
    if setchoice == 5:
        race_map = pygame.image.load("set5/race.png")
    for i in range(5):
        GROUP.append(pygame.sprite.Group(my_sprite(i + 1, start, int(
            screen_Height * 3 / 8 + (i - 1) * screen_Height * 5 / 32))))  # chưa dám đổi biến
    while True:
        clock.tick(60)
        race_map = pygame.transform.scale(race_map, (screen_Width, screen_Height))
        screen.blit(race_map, (0, 0))

        for i in range(5):
            GROUP[i].update()
            GROUP[i].draw(screen)
            if winner == 5 and last <= 150:
                last += 1
            if winner == 5 and last > 150:

                global choice, user_money
                if choice == rank[0]:
                    user_money += bet_money
                else:
                    user_money -= bet_money
                return

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit(0)
            if event.type == pygame.VIDEORESIZE:
                screen_Width, screen_Height = event.size
                screen = pygame.display.set_mode((screen_Width, screen_Height), pygame.RESIZABLE)
                text_Font = pygame.font.Font(None, int(screen_Width / 1500 * 38))
                menu_Font = pygame.font.Font(None, int(screen_Width / 1500 * 45))
                font = pygame.font.SysFont("comicsansms", int(screen_Width / 1500 * 32))
        pygame.display.update()
def ranking_list():
    global screen_Width, screen_Height, screen, text_Font, menu_Font, font
    global user_id, user_money, rank, CHARACTERS
    file = 'Sounds/ranking.wav'
    pygame.mixer.init()
    pygame.mixer.music.load(file)
    pygame.mixer.music.set_volume(volume)
    pygame.mixer.music.play()
    hangnhat = rank[0]
    dem = 0
    if choice == rank[0]:
        update_records(user_id, bet_money, 'Win')
    else:
        update_records(user_id, -bet_money, 'Lose')
    while True:
        global backgroundmenu1
        backgroundmenu1 = pygame.transform.scale(backgroundmenu1, (screen_Width, screen_Height))
        screen.blit(backgroundmenu1, (0, 0))
        user_info = text_Font.render('ID: ' + user_id, True, black)
        money_info = text_Font.render('Money: ' + str(user_money), True, black)
        screen.blit(user_info, (
            screen_Width - user_info.get_width() - money_info.get_width() - screen_Width / (75 / 2),
            screen_Height / 80))
        screen.blit(money_info, (screen_Width - money_info.get_width() - screen_Width / 75, screen_Height / 80))
        title = menu_Font.render('Ranking list', True, (255, 153, 51))
        screen.blit(title, (screen_Width / 2 - title.get_width() / 2, screen_Height / 16))
        if choice == rank[0]:
            news = text_Font.render('YOU WIN', True, white)
            money = text_Font.render('money : + ' + str(bet_money), True, white)
            screen.blit(news, (screen_Width / (1500 / 685), screen_Height / (800 / 90)))
            screen.blit(money, (screen_Width / (1500 / 668), screen_Height / (800 / 130)))
        else:
            news = text_Font.render('YOU LOSE', True, white)
            money = text_Font.render('money : - ' + str(bet_money), True, white)
            screen.blit(news, (screen_Width / (1500 / 685), screen_Height / (800 / 90)))
            screen.blit(money, (screen_Width / (1500 / 668), screen_Height / (800 / 130)))
        for i in range(5):
            new_character = CHARACTERS[i]
            rect = pygame.Rect(i * screen_Width / 5, 0, screen_Width / 5, screen_Height)
            screen.blit(new_character.char_image,
                        ((screen_Width / 5) * i + (screen_Width / 10 - new_character.char_image.get_width() / 2),
                         screen_Height / 3))
            name_rendering = text_Font.render(new_character.char_name, True, white)
            screen.blit(name_rendering,
                        ((screen_Width / 5) * i + (screen_Width / 10 - name_rendering.get_width() / 2),
                         screen_Height / 3 - screen_Height / (80 / 3)))
            character_rank = text_Font.render('rank ' + ': ' + str(rank[i]), True, white)
            screen.blit(character_rank,
                        ((screen_Width / 5) * i + (screen_Width / 10 - name_rendering.get_width() / 2),
                         screen_Height / 3 + screen_Height / (800 / 270)))

        continue_button = text_Font.render('Play again', True, white)
        exit_button = text_Font.render('Back', True, white)
        pygame.draw.rect(screen, bright_red,
                         (int(screen_Width * 0.65) - screen_Width / 75, screen_Height - screen_Height / (800 / 115),
                          continue_button.get_width() + screen_Width / (75 / 2),
                          continue_button.get_height() + screen_Height / (80 / 3)))
        screen.blit(continue_button, (int(screen_Width * 0.65), screen_Height - screen_Height / 8))
        pygame.draw.rect(screen, bright_red,
                         (int(screen_Width * 0.85) - screen_Width / 75, screen_Height - screen_Height / (800 / 115),
                          exit_button.get_width() + screen_Width / (75 / 2),
                          exit_button.get_height() + screen_Height / (80 / 3)))
        screen.blit(exit_button, (int(screen_Width * 0.85), screen_Height - screen_Height / 8))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                choosing = False
                pygame.quit()
                sys.exit(0)
            if event.type == pygame.VIDEORESIZE:
                screen_Width, screen_Height = event.size
                screen = pygame.display.set_mode((screen_Width, screen_Height), pygame.RESIZABLE)
                text_Font = pygame.font.Font(None, int(screen_Width / 1500 * 38))
                menu_Font = pygame.font.Font(None, int(screen_Width / 1500 * 45))
                font = pygame.font.SysFont("comicsansms", int(screen_Width / 1500 * 32))
            if event.type == pygame.MOUSEBUTTONUP:
                x_pos, y_pos = pygame.mouse.get_pos()
                if int(screen_Width * 0.65) - screen_Width / 75 <= x_pos <= int(
                        screen_Width * 0.65) + screen_Width / 75 + continue_button.get_width():
                    if screen_Height - screen_Height / (800 / 115) <= y_pos <= screen_Height - screen_Height / (
                            800 / 115) + continue_button.get_height() + screen_Height / (800 / 30):
                        return 1
                if int(screen_Width * 0.85) - screen_Width / 75 <= x_pos <= int(
                        screen_Width * 0.85) + screen_Width / 75 + exit_button.get_width():
                    if screen_Height - screen_Height / (800 / 115) <= y_pos <= screen_Height - screen_Height / (
                            800 / 115) + exit_button.get_height() + screen_Height / (800 / 30):
                        return 0
        pygame.display.update()
def reset_game():
    file = 'Sounds/nhac2.wav'
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load(file)
    pygame.mixer.music.set_volume(volume)
    pygame.mixer.music.play()
    global rank, winner, CHARACTERS, choice, bet_money, GROUP, set_choice, last
    rank, winner, CHARACTERS, choice, bet_money, GROUP, set_choice, last = [], 0, [], 0, 0, [], 0, 0
def main_game():
    global screen_Width, screen_Height, screen, text_Font, menu_Font, font
    running = True
    while running:
        set_choosing()
        character_choosing()  # nv chọn
        pygame.mixer.init()
        pygame.mixer.music.load('Sounds/nhac3.wav')
        pygame.mixer.music.set_volume(volume)
        pygame.mixer.music.play()
        race()
        keep_playing = ranking_list()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.VIDEORESIZE:
                screen_Width, screen_Height = event.size
                screen = pygame.display.set_mode((screen_Width, screen_Height), pygame.RESIZABLE)
                text_Font = pygame.font.Font(None, int(screen_Width / 1500 * 38))
                menu_Font = pygame.font.Font(None, int(screen_Width / 1500 * 45))
                font = pygame.font.SysFont("comicsansms", int(screen_Width / 1500 * 32))
        if keep_playing == 0:
            running = False
            update_account(user_id, user_money)
            reset_game()
            return 0
        else:
            reset_game()
        pygame.display.flip()
while True:
    giaodien()
    menu(0)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.flip()
