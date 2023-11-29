import sys, pygame, random
import pygame_menu
from LoginSignup import *

#Khởi tạo tất cả
pygame.init()

#Kích thước màn hình (Do chưa có pygame_menu nên tạm thời bỏ qua)
WINDOW_SIZES = [(800, 600), (1080, 720), (1366, 768), (1920, 1080)]
WINDOW_SIZE_INDEX = 0

#Một số biến được sử dụng
screen = pygame.display.set_mode(WINDOW_SIZES[WINDOW_SIZE_INDEX])
pygame.display.set_caption("Race game")
clock = pygame.time.Clock()
#Hàm tạo ảnh
def CreateImg(Address):
    Img = pygame.image.load(Address).convert_alpha()
    return Img

#Hàm viết chữ
def WriteText(Text, Font, Color, x, y):
    Txt = Font.render(Text, False, Color)
    screen.blit(Txt, (x, y))

#Chữ chạy (Chủ yếu để trang trí)
KieuChu1 = pygame.font.SysFont('arial', 20, bold=True)
ChuChay1_surface = KieuChu1.render("THIS IS GROUP 12'S AMAZING RACE GAME!!!", False, (255, 102, 0))
ChuChay1_Box = ChuChay1_surface.get_rect(topleft = (WINDOW_SIZES[WINDOW_SIZE_INDEX][0], 0))

#Chữ các thứ
Player_money = 0
KieuChu2 = pygame.font.SysFont('Verdana', 40, bold=True)
scoreBoard = KieuChu2.render(f"Money: {Player_money}", False, (0, 255, 255))
scoreBoard_Box = scoreBoard.get_rect(center = (WINDOW_SIZES[WINDOW_SIZE_INDEX][0] * 0.13, WINDOW_SIZES[WINDOW_SIZE_INDEX][1] * 0.92))

#Nhân vật (Sau này có thể đặt vào trong class để dễ quản lý)
Character1_Speed = 2.5
Character1_Suf = CreateImg('assets/characters/Testchar.png')
Character1_Box = Character1_Suf.get_rect(midbottom = (50, 300))
Character1_Run = True

#Lucky box
activateLuckyBox = False
luckyBox_Pos = random.randint(150, 400)
luckyBox_Effect = random.randint(0, 2)
luckyBox = CreateImg("assets/item/luckyBox.png")
luckyBox_Box = luckyBox.get_rect(midbottom = (luckyBox_Pos, 300))

#Âm thanh
VOLUME = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]
VOLUME_INDEX = 4
Victory_sound = pygame.mixer.Sound('assets/sounds/Victorious.ogg')
Victory_sound_Play = True
pygame.mixer.music.load('assets/sounds/Panorama.wav')
pygame.mixer.music.play(loops = -1)

#Ảnh
Background = CreateImg('assets/background/background(800x600).png')

#FinishLine(Test)
FinishLine = CreateImg('assets/terrains/FinishLine.png')
FinishLine_Box = FinishLine.get_rect(topright = (WINDOW_SIZES[WINDOW_SIZE_INDEX][0] * 0.9, 0))

#Các trạng thái
tempSpeed = Character1_Speed
Activated = False
#Làm chậm
SlowTime = 150
SlowTimeConst = SlowTime
ActivateSlow = False
#Tăng tốc
SpeedTime = 20
SpeedTimeConst = SpeedTime
ActivateSpeed = False
#Choáng
DizzyTime = 60
DizzyTimeConst = DizzyTime
ActivateDizzy = False

#Trạng thái game
STAGE = ["GamePlay", "Pause"]
STAGE_INDEX = 0

#Đây là main loop
def main():
    while True:
        #Check đăng nhập
        if not login_lock:
            break
        #nhạc nền + âm lượng
        Victory_sound.set_volume(VOLUME[VOLUME_INDEX])

        #Kích thước màn hình
        global WINDOW_SIZE_INDEX
        
        #Trạng thái game
        global STAGE_INDEX
        
        match STAGE[STAGE_INDEX]:
            case "GamePlay":
                #Ảnh nền
                screen.blit(Background,(0,0))
                screen.blit(FinishLine, FinishLine_Box)

                #Nhân vật + nhạc khi win (test)
                global Character1_Speed
                global Character1_Run
                global Victory_sound_Play
                screen.blit(Character1_Suf, Character1_Box)
                if Character1_Run:
                    Character1_Box.x += Character1_Speed
                if Character1_Box.x > FinishLine_Box.x:
                    Character1_Run = False
                    if Victory_sound_Play:
                        pygame.mixer.music.stop()
                        Victory_sound.play()
                        Victory_sound_Play = False
                        

                #Lucky box
                global activateLuckyBox

                global SlowTime
                global ActivateSlow

                global SpeedTime
                global ActivateSpeed

                global ActivateDizzy
                global DizzyTime
                
                if not activateLuckyBox:
                    screen.blit(luckyBox, luckyBox_Box)
                if Character1_Box.colliderect(luckyBox_Box):
                    if not activateLuckyBox:
                        #Kích hoạt hiệu ứng(Tạm)
                        match luckyBox_Effect:
                            case 0:
                                ActivateSlow = True
                            case 1:
                                ActivateSpeed = True
                            case 2:
                                ActivateDizzy = True

                        activateLuckyBox = True

                global tempSpeed #Cái này để lưu tốc chạy cơ bản của nhân vật ở ngoài hàm main
                global Activated
                #Làm chậm
                if ActivateSlow == True:
                    if not Activated:
                        Character1_Speed -= 2
                        Activated = True
                    SlowTime -= 1
                if SlowTime == 0:
                    SlowTime = SlowTimeConst
                    Character1_Speed = tempSpeed
                    ActivateSlow = False
                
                #Tăng tốc
                if ActivateSpeed == True:
                    if not Activated:
                        Character1_Speed += 3
                        Activated = True
                    SpeedTime -= 1
                if SpeedTime == 0:
                    SpeedTime = DizzyTimeConst
                    Character1_Speed = tempSpeed
                    ActivateSpeed = False

                #Choáng
                if ActivateDizzy == True:
                    Character1_Speed = 0
                    DizzyTime -= 1
                if DizzyTime == 0:
                    Character1_Speed = tempSpeed
                    DizzyTime = DizzyTimeConst
                    ActivateDizzy = False

                #Bảng tiền
                pygame.draw.rect(screen, "red", scoreBoard_Box, 6, 10)
                screen.blit(scoreBoard, scoreBoard_Box)
                

                #Chữ chạy
                screen.blit(ChuChay1_surface, ChuChay1_Box)
                ChuChay1_Box.x -= 2
                if ChuChay1_Box.right <= 0:
                    ChuChay1_Box.x = WINDOW_SIZES[WINDOW_SIZE_INDEX][0]
            case "Pause":
                screen.fill('black')
                button = KieuChu2.render("Countinue", False, "white")
                button_Box = button.get_rect(center = (WINDOW_SIZES[WINDOW_SIZE_INDEX][0] / 2, WINDOW_SIZES[WINDOW_SIZE_INDEX][1] / 2))
                pygame.draw.rect(screen, "white", button_Box, 6, 10)
                screen.blit(button, (button_Box))
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            STAGE_INDEX = 0
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if button_Box.collidepoint(event.pos):
                            STAGE_INDEX = 0

        #Chuyển trạng thái game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # Nhấn phím ESC sẽ kích hoạt Pause
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    STAGE_INDEX = 1
            # Code để tìm vị trí cụ thể trên màn hình
            # if event.type == pygame.MOUSEMOTION:
            #     print(event.pos)

        pygame.display.update()
        clock.tick(60)
main()
