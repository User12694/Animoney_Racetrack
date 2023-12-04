from GameFunctions import *

#Đây là main loop
def main():
    global login_lock
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
        clock.tick(60)  # Đảm bảo chương trình chạy không quá 60 khung hình/giây
main()

# #Hàm viết chữ
# def WriteText(Text, Font, Color, x, y):
#     Txt = Font.render(Text, False, Color)
#     screen.blit(Txt, (x, y))

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


#Lucky Box
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