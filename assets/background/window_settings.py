import pygame
import pygame_menu

# Khởi tạo Pygame
pygame.init()

# Định nghĩa các kích thước cửa sổ
WINDOW_SIZES = [(800, 600), (1080, 720), (1366, 768), (1920, 1080)]
WINDOW_SIZE_INDEX = 0

# Tạo cửa sổ
window = pygame.display.set_mode(WINDOW_SIZES[WINDOW_SIZE_INDEX])

# Tạo menu
menu = pygame_menu.Menu(300, 400, 'Settings',
                        theme=pygame_menu.themes.THEME_BLUE)

# Thêm nút chọn kích thước cửa sổ
menu.add_selector('Window Size :', WINDOW_SIZES, onchange=lambda a, b: change_window_size(b))

# Thêm nút chuyển đổi chế độ toàn màn hình
menu.add_selector('Full Screen :', [('OFF', False), ('ON', True)], onchange=lambda a, b: toggle_fullscreen(b))

# Định nghĩa hàm thay đổi kích thước cửa sổ
def change_window_size(index):
    global window
    window = pygame.display.set_mode(WINDOW_SIZES[index])

# Định nghĩa hàm chuyển đổi chế độ toàn màn hình
def toggle_fullscreen(enabled):
    global window
    if enabled:
        window = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    else:
        window = pygame.display.set_mode(WINDOW_SIZES[WINDOW_SIZE_INDEX])

# Vòng lặp chính
running = True
while running:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False
    if menu.is_enabled():
        menu.update(events)
        menu.draw(window)
    pygame.display.update()

pygame.quit()
