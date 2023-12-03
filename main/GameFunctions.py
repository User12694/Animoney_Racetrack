#Check điều kiện thắng
def FinishLine_Pass(player, IG_Objects):
    for IG_Object in IG_Objects:
        if IG_Object.name == "FinishLine" and player.sprite.rect.x > IG_Object.rect.x:
            player.sprite.run = False
            return True
    return False

#Class trò chơi dùng để hiển thị menu, check keys các thứ (Đang làm chưa xài)
# class Main():
#     #Khởi tao + các biến sử dụng trong class
#     global login_lock, Victory_sound_Play, screen
#     def __init__(self):
#         pygame.init()
#         self.Running = True
#         self.Play = True
#         self.ESC = False

#     def loop(self):
#         while self.Running:
#             self.check_events()
#             if self.Play:
#                 self.Playing()
#             if self.ESC:
#                 self.Pause()
#             pygame.display.update()
#             clock.tick(60)
#         pygame.quit()
            
#     #Kiểm tra điều kiện
#     def check_events(self):
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 self.Running = False
#             if event.type == pygame.KEYDOWN:
#                 if event.key == pygame.K_ESCAPE:
#                     self.ESC = True

#             Resize cửa sổ nếu cần
#             if event.type == pygame.VIDEORESIZE:
#                 screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
#                 WINDOW_SIZE_INDEX = 1
            
#             Code để tìm vị trí cụ thể trên màn hình
#             if event.type == pygame.MOUSEMOTION:
#                 print(event.pos)
    
                    


