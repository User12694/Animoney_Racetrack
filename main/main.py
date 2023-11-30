from GameUtilities import *

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
ChuChay1_Box = ChuChay1_surface.get_rect(topleft = (WINDOW_SIZES[WINDOW_SIZE_INDEX][0], WINDOW_SIZES[WINDOW_SIZE_INDEX][1] * 0.1))

#Chữ các thứ
Player_money = 0
KieuChu2 = pygame.font.SysFont('Verdana', 40, bold=True)
scoreBoard = KieuChu2.render(f"Money: {Player_money}", False, (0, 255, 255))
scoreBoard_Box = scoreBoard.get_rect(center = (WINDOW_SIZES[WINDOW_SIZE_INDEX][0] * 0.13, WINDOW_SIZES[WINDOW_SIZE_INDEX][1] * 0.92))

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

#Trạng thái game
STAGE = ["GamePlay", "Pause"]
STAGE_INDEX = 0

# #Các trạng thái
# Char1_TempSpeed = Speed[0]
# Activated = False
# #Làm chậm
# SlowTime = 150
# SlowTimeConst = SlowTime
# ActivateSlow = False
# #Tăng tốc
# SpeedTime = 20
# SpeedTimeConst = SpeedTime
# ActivateSpeed = False
# #Choáng
# DizzyTime = 60
# DizzyTimeConst = DizzyTime
# ActivateDizzy = False

#Quit
Running = True

#Đây là main loop
def main():
    global Running
    while Running:
        # Check đăng nhập
        if not login_lock:
            Running = False
        #Nhân vật

        Char1 = player(Speed[0], WINDOW_SIZES[WINDOW_SIZE_INDEX][0] * 0.1, WINDOW_SIZES[WINDOW_SIZE_INDEX][1] * 0.5, 1, Char1_Run, CharsMap1[0][0])
        # Char2 = player(Speed[1], WINDOW_SIZES[WINDOW_SIZE_INDEX][0] * 0.1, WINDOW_SIZES[WINDOW_SIZE_INDEX][1] * 0.6, 2, Char2_Run, CharsMap1[0][0])
        # Char3 = player(Speed[2], WINDOW_SIZES[WINDOW_SIZE_INDEX][0] * 0.1, WINDOW_SIZES[WINDOW_SIZE_INDEX][1] * 0.7, 3, Char3_Run, CharsMap1[0][0])
        # Char4 = player(Speed[3], WINDOW_SIZES[WINDOW_SIZE_INDEX][0] * 0.1, WINDOW_SIZES[WINDOW_SIZE_INDEX][1] * 0.8, 4, Char4_Run, CharsMap1[0][0])
        # Char5 = player(Speed[4], WINDOW_SIZES[WINDOW_SIZE_INDEX][0] * 0.1, WINDOW_SIZES[WINDOW_SIZE_INDEX][1] * 0.9, 5, Char5_Run, CharsMap1[0][0])
        
        Char1.draw()
        # Char2.draw()
        # Char3.draw()
        # Char4.draw()
        # Char5.draw()

        #nhạc nền + âm lượng
        Victory_sound.set_volume(VOLUME[VOLUME_INDEX])

        
        #Trạng thái game
        global STAGE_INDEX
        
        match STAGE[STAGE_INDEX]:
            case "GamePlay":
                #Ảnh nền
                screen.blit(Background,(0,0))
                screen.blit(FinishLine, FinishLine_Box)

                #Nhân vật + nhạc khi win (test)
                # global Victory_sound_Play
                # if Char1_Box.x > FinishLine_Box.x:
                #     Char1Map1_Run = False
                #     if Victory_sound_Play:
                #         pygame.mixer.music.stop()
                #         pygame.mixer.music.unload()
                #         Victory_sound.play()
                #         Victory_sound_Play = False
                        

                # #Lucky box
                # global activateLuckyBox

                # global SlowTime
                # global ActivateSlow

                # global SpeedTime
                # global ActivateSpeed

                # global ActivateDizzy
                # global DizzyTime
                
                # if not activateLuckyBox:
                #     screen.blit(luckyBox, luckyBox_Box)
                # if Char1_Box.colliderect(luckyBox_Box):
                #     if not activateLuckyBox:
                #         #Kích hoạt hiệu ứng(Tạm)
                #         match luckyBox_Effect:
                #             case 0:
                #                 ActivateSlow = True
                #             case 1:
                #                 ActivateSpeed = True
                #             case 2:
                #                 ActivateDizzy = True

                #         activateLuckyBox = True

                # global Char1_TempSpeed #Cái này để lưu tốc chạy cơ bản của nhân vật ở ngoài hàm main
                # global Activated

                # #Làm chậm
                # if ActivateSlow == True:
                #     if not Activated:
                #         Char1Map1_Speed -= 2
                #         Activated = True
                #     SlowTime -= 1
                # if SlowTime == 0:
                #     SlowTime = SlowTimeConst
                #     Char1Map1_Speed = Char1_TempSpeed
                #     ActivateSlow = False
                
                # #Tăng tốc
                # if ActivateSpeed == True:
                #     if not Activated:
                #         Char1Map1_Speed += 3
                #         Activated = True
                #     SpeedTime -= 1
                # if SpeedTime == 0:
                #     SpeedTime = DizzyTimeConst
                #     Char1Map1_Speed = Char1_TempSpeed
                #     ActivateSpeed = False

                # #Choáng
                # if ActivateDizzy == True:
                #     Char1Map1_Speed = 0
                #     DizzyTime -= 1
                # if DizzyTime == 0:
                #     Char1Map1_Speed = Char1_TempSpeed
                #     DizzyTime = DizzyTimeConst
                #     ActivateDizzy = False

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
                #Countinue button
                Countinue_Button = KieuChu2.render("Countinue", False, "white")
                Countinue_Button_Box = Countinue_Button.get_rect(center = (WINDOW_SIZES[WINDOW_SIZE_INDEX][0] / 2, WINDOW_SIZES[WINDOW_SIZE_INDEX][1] / 2))
                pygame.draw.rect(screen, "white", Countinue_Button_Box, 6, 10)
                screen.blit(Countinue_Button, (Countinue_Button_Box))
                
                #Quit button
                Quit_Button = KieuChu2.render("Quit", False, "white")
                Quit_Button_Box = Quit_Button.get_rect(center = (WINDOW_SIZES[WINDOW_SIZE_INDEX][0] / 2, WINDOW_SIZES[WINDOW_SIZE_INDEX][1] / 2 + 70))
                pygame.draw.rect(screen, "white", Quit_Button_Box, 6, 10)
                screen.blit(Quit_Button, (Quit_Button_Box))

                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            STAGE_INDEX = 0
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if Countinue_Button_Box.collidepoint(event.pos):
                            STAGE_INDEX = 0
                        if Quit_Button_Box.collidepoint(event.pos):
                            Running = False
                    

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
