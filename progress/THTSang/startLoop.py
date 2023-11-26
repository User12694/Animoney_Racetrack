import sys, pygame, random
#Khởi tạo tất cả
pygame.init()
#Kích thước màn hình (Do chưa có pygame_menu nên tạm thời bỏ qua)
WINDOW_SIZES = [(800, 600), (1080, 720), (1366, 768), (1920, 1080)]
WINDOW_SIZE_INDEX = 0
#Một số biến được sử dụng
screen = pygame.display.set_mode(WINDOW_SIZES[WINDOW_SIZE_INDEX])
pygame.display.set_caption("Race game")
clock = pygame.time.Clock()
#Chữ chạy (Chủ yếu để trang trí)
KieuChu1 = pygame.font.Font(None, 30)
ChuChay1_surface = KieuChu1.render("THIS IS GROUP 12'S AMAZING RACE GAME!!!", False, 'blue')
ChuChay1_Box = ChuChay1_surface.get_rect(topleft = (WINDOW_SIZES[WINDOW_SIZE_INDEX][0], 0))
#Nhân vật (Sau này có thể đặt vào trong class để dễ quản lý)
Character1_Suf = pygame.image.load('assets/characters/Testchar.png').convert_alpha()
Character1_Box = Character1_Suf.get_rect(midbottom = (50, 300))
Character1_Run = True
#Âm thanh
VOLUME = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]
VOLUME_INDEX = 4
Victory_sound = pygame.mixer.Sound('assets/sounds/Victorious.ogg')
Victory_sound.set_volume(VOLUME[VOLUME_INDEX])
Victory_sound_Play = True
#Ảnh
Background = pygame.image.load('assets/background/background(800x600).png').convert()
#FinishLine(Test)
FinishLine = pygame.image.load('assets/terrains/FinishLine.png').convert_alpha()
FinishLine_Box = FinishLine.get_rect(topright = (WINDOW_SIZES[WINDOW_SIZE_INDEX][0] - 50, 0))
#
#Đây là main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # Code để tìm vị trí cụ thể trên màn hình
        # if event.type == pygame.MOUSEMOTION:
        #     print(event.pos)
    screen.blit(Background,(0,0))
    screen.blit(FinishLine, FinishLine_Box)
    #Nhân vật + nhạc khi win (test)
    screen.blit(Character1_Suf, Character1_Box)
    if Character1_Run == True:
        Character1_Box.x += 5
    if Character1_Box.colliderect(FinishLine_Box):
        Character1_Run = False
        if Victory_sound_Play:
            Victory_sound.play()
            Victory_sound_Play = False
    #Chữ chạy
    screen.blit(ChuChay1_surface, ChuChay1_Box)
    ChuChay1_Box.x -= 3
    if ChuChay1_Box.right <= 0: ChuChay1_Box.x = WINDOW_SIZES[WINDOW_SIZE_INDEX][0]
    #
    pygame.display.update()
    clock.tick(60)