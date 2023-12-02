from GameUtilities import *

# #Hàm viết chữ
# def WriteText(Text, Font, Color, x, y):
#     Txt = Font.render(Text, False, Color)
#     screen.blit(Txt, (x, y))

#Chữ các thứ
Player_money = 0
scoreBoard = KieuChu2.render(f"Money: {Player_money}", False, (0, 255, 255))
scoreBoard_Box = scoreBoard.get_rect(center = (WINDOW_SIZES[WINDOW_SIZE_INDEX][0] * 0.13, WINDOW_SIZES[WINDOW_SIZE_INDEX][1] * 0.92))

#Lucky box
# activateLuckyBox = False
# luckyBox_Pos = random.randint(150, 400)
# luckyBox_Effect = random.randint(0, 2)
# luckyBox = CreateImg("assets/item/luckyBox.png")
# luckyBox_Box = luckyBox.get_rect(midbottom = (luckyBox_Pos, 300))

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


#Đây là main loop
def main():
    global Running
    global screen
    global WINDOW_SIZE_INDEX
    global login_lock
    while Running:
        #Chỉnh âm lượng
        pygame.mixer.music.set_volume(VOLUME[VOLUME_INDEX])

        # Check đăng nhập
        if not login_lock:
            Running = False

        #Trạng thái game
        global STAGE_INDEX
        
        match STAGE[STAGE_INDEX]:
            case "GamePlay":
                #Ảnh nền
                screen.blit(Background,(0,0))
                IG_Objects.draw(screen)
                IG_Objects.update()

                #Nhân vật
                Char1.draw(screen)
                # Char2.draw(screen)
                # Char3.draw(screen)
                # Char4.draw(screen)
                # Char5.draw(screen)

                Char1.update()
                # Char2.update()
                # Char3.update()
                # Char4.update()
                # Char5.update()

                #Nhân vật + nhạc khi win (test)
                global Victory_sound_Play
                FinishLine_Pass1 = FinishLine_Pass(Char1, IG_Objects)
                # FinishLine_Pass2 = FinishLine_Pass(Char2, IG_Objects)
                # FinishLine_Pass3 = FinishLine_Pass(Char3, IG_Objects)
                # FinishLine_Pass4 = FinishLine_Pass(Char4, IG_Objects)
                # FinishLine_Pass5 = FinishLine_Pass(Char5, IG_Objects)

                if FinishLine_Pass1: #or FinishLine_Pass2 or FinishLine_Pass3 or FinishLine_Pass4 or FinishLine_Pass5
                    if Victory_sound_Play:
                        pygame.mixer.music.stop()
                        pygame.mixer.music.unload()
                        pygame.mixer.music.load('assets/sounds/Victorious.ogg')
                        pygame.mixer.music.play(loops = 0)
                        Victory_sound_Play = False
                        

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
            #Tạm dừng trò chơi
            case "Pause":
                screen.fill('black')
                #Countinue button
                Countinue_Button = KieuChu2.render("Continue", False, "white")
                Countinue_Button_Box = Countinue_Button.get_rect(center = (WINDOW_SIZES[WINDOW_SIZE_INDEX][0] / 2, WINDOW_SIZES[WINDOW_SIZE_INDEX][1] / 2))
                pygame.draw.rect(screen, "white", Countinue_Button_Box, 2, 10)
                screen.blit(Countinue_Button, (Countinue_Button_Box))
                
                #Quit button
                Quit_Button = KieuChu2.render("Quit", False, "white")
                Quit_Button_Box = Quit_Button.get_rect(center = (WINDOW_SIZES[WINDOW_SIZE_INDEX][0] / 2, WINDOW_SIZES[WINDOW_SIZE_INDEX][1] / 2 + 70))
                pygame.draw.rect(screen, "white", Quit_Button_Box, 2, 10)
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
                Running = False
            if event.type == pygame.VIDEORESIZE:
                screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
                WINDOW_SIZE_INDEX = 1
            # Nhấn phím ESC sẽ kích hoạt Pause
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    STAGE_INDEX = 1
            # Code để tìm vị trí cụ thể trên màn hình
            # if event.type == pygame.MOUSEMOTION:
            #     print(event.pos)

        pygame.display.update()
        clock.tick(60)
    pygame.quit()
main()
