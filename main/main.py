from GameFunctions import *

#Đây là main loop
def main():
    #chạy menu
    menu()
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
