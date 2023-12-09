import pygame
from datetime import datetime
# Khởi tạo Pygame
pygame.init()

screen = pygame.display.set_mode((800, 600))
# Tạo một cửa sổ
def screenshot():
    time = datetime.now()
    rounded_now = time.replace(microsecond=0)
    time = rounded_now.strftime('%d%m%y %H%M%S')
    while True:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:  # Nhấn phím 's' để chụp màn hình
                pygame.image.save(screen, f'./screenshots/screenshot {time}.png')

# Vòng lặp chính của trò chơi
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Vẽ một hình vuông màu xanh lên cửa sổ
    pygame.draw.rect(screen, (0, 128, 255), pygame.Rect(30, 30, 60, 60))

    # Cập nhật màn hình
    pygame.display.flip()

# Kết thúc Pygame
pygame.quit()
