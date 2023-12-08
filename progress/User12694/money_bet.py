import pygame, sys


user_id = ''
user_money = 0
set_choice = 0
choice = 0
bet_money = 0
pygame.init()


clock = pygame.time.Clock()
WINDOW_SIZE = [(1536,864),(768,432)]
WINDOW_INDEX = 0
screen_Width = WINDOW_SIZE[WINDOW_INDEX][0]
screen_Height = WINDOW_SIZE[WINDOW_INDEX][1]
screen = pygame.display.set_mode((screen_Width, screen_Height), pygame.RESIZABLE)
pygame.display.set_caption('RACE')
running = True

black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
bright_red = pygame.Color(255, 0, 0)
old_red = pygame.Color(200, 0, 0)
color = pygame.Color('lightskyblue3')
orange = "#EE7214"

LANGUAGE = ["./assets/background/ENG/", "./assets/background/VIET/"]
LANGUAGE_INDEX = 0

volume = 0.4
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
background = pygame.image.load(f'{LANGUAGE[LANGUAGE_INDEX]}/background.png')
backgroundmenu = pygame.image.load(f'{LANGUAGE[LANGUAGE_INDEX]}/background.png')
backgroundmenu1 = pygame.image.load(f'{LANGUAGE[LANGUAGE_INDEX]}/background.png')
# hinh anh text box
# box1 = pygame.image.load('box.png')

rank = []
winner = 0
line = screen_Width - screen_Width / 20
start = screen_Width / 300
# Tạo một hàm read_data lên
def read_data():
    global user_money
    username = 'phuoc'
    with open(f'./assets/player/{username}/{username}.txt','r') as f:
        lines = f.readlines()
    user_money = int(lines[1])
    return username, user_money
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
        user_id, user_money = read_data()
        user_info = text_Font.render('ID: ' + user_id, True, black)
        money_info = text_Font.render('Money: ' + str(user_money), True, black)
        store = menu_Font.render('BUY RANDOM SPELL (100$)', True, white)
        mustHaveMoney = menu_Font.render('You must enter the money you bet!', True, white)
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
        title = menu_Font.render('Enter the money you bet', True, orange)
        screen.blit(title, (screen_Width / 2 - title.get_width() / 2, screen_Height / 2 - screen_Height /24))

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
                    if money_bet == '':
                        screen.blit(mustHaveMoney, (x_done - 50, y_done - 50))
                    else:
                        if int(user_money) >= int(money_bet):
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
                    # menu(0), thay thế thành MenuClass()
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
def update_account(usr_id, money):
    global user_id
    username = user_id
    data = []
    with open(f'./assets/player/{username}/{username}.txt', 'r') as old_file:
        for line in old_file:
            if line.split(',')[0] == usr_id:
                pos = line.rfind(',')
                line = line[:pos + 1] + str(money) + '\n'
            data.append(line)
    with open(f'./assets/player/{username}/{username}.txt', 'w') as new_file:
        for line in data:
            new_file.write(line)

def reset_game():
    file = './assets/sounds/mainmenu.mp3'
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load(file)
    pygame.mixer.music.set_volume(volume)
    pygame.mixer.music.play()
    global rank, winner, CHARACTERS, choice, bet_money, GROUP, set_choice, last
    rank, winner, CHARACTERS, choice, bet_money, GROUP, set_choice, last = [], 0, [], 0, 0, [], 0, 0
money_bet()