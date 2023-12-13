import pygame, sys

black = (0,0,0)
white = (255,255,255)

WINDOWS_SIZE = [(1536,864),(768,432)]
WINDOWS_INDEX = 0
screen_Width = WINDOWS_SIZE[WINDOWS_INDEX][0]
screen_Height = WINDOWS_SIZE[WINDOWS_INDEX][1]
screen = pygame.set_mode
backgroundmenu1 = pygame.image.load('./assets/background/background-80.png')
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
    global screen, screen_Width, screen_Height, screen, text_Font, menu_Font, font
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

def main():

    pygame.init()
    screen = pygame.display.set_mode(WINDOWS_SIZE[WINDOWS_INDEX])
    running = True
    while running:
        set_choosing()
        character_choosing()  # nv chọn
        pygame.mixer.init()
        pygame.mixer.music.load('Sounds/nhac3.wav')
        pygame.mixer.music.set_volume(0.4)
        pygame.mixer.music.play()
        keep_playing = 1
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
            return 0
            # reset_game()
        pygame.display.flip()
main()