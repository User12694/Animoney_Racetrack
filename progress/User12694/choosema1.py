import pygame
import sys

class ChooseMap:
    def __init__(self):
        # Khởi tạo Pygame
        pygame.init()

        # Thiết lập kích thước cửa sổ
        self.window_width, self.window_height = 768, 432
        self.screen = pygame.display.set_mode((self.window_width, self.window_height))

        # Tạo một hình chữ nhật bo cong 20px, màu trắng, viền xanh ngọc, kích thước 100px
        self.rect = pygame.draw.rect(self.screen, (0, 255, 255), (self.window_width / 2 - 50, int(5 / 8 * self.window_height), 400, 50), border_radius=20)

        # Tạo một TextBox để có thể viết chữ lên hình chữ nhật
        self.font = pygame.font.Font(None, 32)
        self.text = self.font.render('anyf', True, (0, 0, 0))
        self.text_rect = self.text.get_rect(center=(self.rect.x + self.rect.width / 2, self.rect.y + self.rect.height / 2))

    def draw(self):
        # Vẽ hình chữ nhật và TextBox lên màn hình
        pygame.draw.rect(self.screen, (255, 255, 255), self.rect, border_radius=20)
        pygame.draw.rect(self.screen, (0, 255, 255), self.rect, 2, border_radius=20)
        self.screen.blit(self.text, self.text_rect)

    def update(self):
        pass

# Tạo một đối tượng ChooseMap và vẽ nó lên màn hình
choose_map = ChooseMap()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    choose_map.draw()
    pygame.display.flip()
