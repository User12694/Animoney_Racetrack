import pygame
import sys

class TextBox:
    def __init__(self, font, rect, text=""):
        self.font = font
        self.rect = rect
        self.text = text

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                self.text = self.text[:-1]
            else:
                if len(self.text) < 10:
                    self.text += event.unicode

    def draw(self, screen):
        text_surface = self.font.render(self.text, True, (255, 255, 255))
        screen.blit(text_surface, (self.rect.x+5, self.rect.y+5))

class RectText:
    def __init__(self, rect, color):
        self.rect = rect
        self.color = color

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)

# Khởi tạo Pygame
pygame.init()

# Thiết lập kích thước cửa sổ
screen = pygame.display.set_mode((800, 600))

# Tạo font chữ
font = pygame.font.Font(None, 50)

# Tạo hình chữ nhật và hộp văn bản
rect_text = RectText(pygame.Rect(200, 200, 200, 100), (0, 0, 255))
text_box = TextBox(font, pygame.Rect(200, 200, 200, 100))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        else:
            text_box.handle_event(event)

    # Vẽ hình chữ nhật và hộp văn bản
    rect_text.draw(screen)
    text_box.draw(screen)

    # Cập nhật màn hình
    pygame.display.flip()
