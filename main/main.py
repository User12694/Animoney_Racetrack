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
ChuChay1_pos = WINDOW_SIZES[WINDOW_SIZE_INDEX][0]
#
Background = pygame.image.load('assets/background/background(800x600).png')
#
#Đây là main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.blit(Background,(0,0))
    #Chữ chạy
    screen.blit(ChuChay1_surface,(ChuChay1_pos, 0))
    ChuChay1_pos -= 3
    if ChuChay1_pos < 0 - WINDOW_SIZES[WINDOW_SIZE_INDEX][0]:
        ChuChay1_pos = WINDOW_SIZES[WINDOW_SIZE_INDEX][0]
    #
    pygame.display.update()
    clock.tick(60)