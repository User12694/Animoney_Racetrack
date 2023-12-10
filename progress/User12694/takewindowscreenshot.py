import pygame
import pyautogui
import pygetwindow as gw

# Khởi tạo pygame
pygame.init()

# Tạo cửa sổ pygame
screen = pygame.display.set_mode((500, 500))

# Biến để kiểm tra xem chúng ta đã chụp ảnh màn hình hay chưa
screenshot_taken = False

def take_screenshot():
    global screenshot_taken
    if not screenshot_taken:
        # Lấy cửa sổ pygame
        window = gw.getWindowsWithTitle('pygame window')[0]
        # Lấy vị trí và kích thước của cửa sổ
        x, y, width, height = window.left, window.top, window.width, window.height
        # Chụp ảnh màn hình của cửa sổ pygame
        screenshot = pyautogui.screenshot(region=(x, y, width, height))
        screenshot.save('screenshot.png')
        screenshot_taken = True

# Vòng lặp chính của game
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:  # Nhấn phím space để chụp ảnh màn hình
                take_screenshot()

    # Vẽ một hình vuông màu xanh lên cửa sổ
    pygame.draw.rect(screen, (0, 128, 255), pygame.Rect(30, 30, 60, 60))

    # Cập nhật màn hình
    pygame.display.flip()

# Thoát pygame khi kết thúc vòng lặp chính
pygame.quit()
