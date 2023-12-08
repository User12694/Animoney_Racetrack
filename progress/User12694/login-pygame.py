import pygame  # Import thư viện pygame
import sys  # Import thư viện sys

WINDOWS_SIZE = [(1536,864),(768,432)]  # Định nghĩa kích thước cửa sổ
WINDOWS_INDEX = 0  # Chỉ số cửa sổ

white = (255,255,255)  # Màu trắng
black = (0,0,0)  # Màu đen

class Cursor:  # Định nghĩa lớp Cursor
    def __init__(self, rect):  # Hàm khởi tạo
        self.rect = rect  # Định nghĩa hình chữ nhật
        self.blink = True  # Định nghĩa nháy
        self.blink_speed = 60 // 60  # Tốc độ nháy của con trỏ
        self.blink_counter = 0  # Đếm số khung hình

    def draw(self, screen, active, text_surface):  # Hàm vẽ
        if active and self.blink:  # Nếu hoạt động và nháy
            pygame.draw.line(screen, (255, 255, 255), (self.rect.x + 5 + text_surface.get_width(), self.rect.y + 5), (self.rect.x + 5 + text_surface.get_width(), self.rect.y + self.rect.height - 5))  # Vẽ đường thẳng

    def update(self):  # Hàm cập nhật
        self.blink_counter += 1 #Đếm số khung hình
        if self.blink_counter % self.blink_speed == 0: #Khi khung hình == 60, thực hiện
            self.blink = not self.blink  # Cập nhật trạng thái nháy

class RectText:
    def __init__(self, rect, color):
        self.rect = rect
        self.color = color

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect, border_radius=10)  # Bo cong hình chữ nhật

class Button:
    def __init__(self, image_path, position):
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect(topleft=position)

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                print("Pressed!")
    def isOver(self, pos): # Kiểm tra xem con trỏ chuột có nằm trong phạm vi kích thước của nút hay không
        if self.x < pos[0] < self.x + self.width: # Kiểm tra xem tọa độ x của con trỏ nằm trong khoảng (cạnh trái, cạnh phải = cạnh trái + giá trị chiều rộng)
            if self.y < pos[1] < self.y + self.height:# Kiểm tra xem tọa độ y của con trỏ nằm trong khoảng (cạnh trái, cạnh phải = cạnh trái + giá trị chiều cao)
                return True #Cả hai thỏa mãn,trả về True. Ngược lại, trả về False
        return False

class LoginRegisterField:
    def __init__(self, screen_size, color, border_radius):
        self.rect = pygame.Rect(0, 0, 400, 500)  # Kích thước hình chữ nhật
        self.rect.center = (screen_size[0] // 2, 150 + screen_size[1] // 2)  # Đặt hình chữ nhật ở giữa màn hình
        self.color = pygame.Color(color)  # Màu sắc hình chữ nhật
        self.border_radius = border_radius  # Độ bo cong của hình chữ nhật

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect, border_radius=self.border_radius)

class Label:
    def __init__(self, font, text, position):
        self.font = font
        self.text = text
        self.position = position

    def draw(self, screen):
        text_surface = self.font.render(self.text, True, (255, 255, 255))
        screen.blit(text_surface, self.position)
class TextBox:
    def __init__(self, font, rect, text=""):
        self.font = font
        self.rect = pygame.Rect(rect.left + 10, rect.top + 10, rect.width - 20, rect.height - 20)  # Điều chỉnh vị trí TextBox
        self.text = text
        self.active = False
        self.cursor = Cursor(self.rect)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.active = not self.active
            else:
                self.active = False
        elif event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    if len(self.text) < 10:
                        self.text += event.unicode

    def draw(self, screen):
        text_surface = self.font.render(self.text, True, white)
        screen.blit(text_surface, (self.rect.x+5, self.rect.y+5))
        self.cursor.draw(screen, self.active, text_surface)

    def update(self):
        self.cursor.update()
class TextArea:
    def __init__(self, font, rect, text="", color=(255, 255, 255)):
        self.textbox = TextBox(font, rect, text)
        self.recttext = RectText(rect, color)

    def handle_event(self, event):
        self.textbox.handle_event(event)

    def draw(self, screen):
        self.recttext.draw(screen)
        self.textbox.draw(screen)

    def update(self):
        self.textbox.update()

class LoginMenu:
    def __init__(self, screen):
        pass
    def draw(self, screen):
        pass
    def handle_event(self, screen):
        pass


# Khởi tạo Pygame
def main():
    # Khởi tạo Pygame
    pygame.init()

    # Thiết lập kích thước cửa sổ
    screen = pygame.display.set_mode(WINDOWS_SIZE[0])
    # Tải hình ảnh nền
    background = pygame.image.load("./assets/background/background-80.png").convert_alpha()

    # Tạo font chữ
    font = pygame.font.Font('./assets/font/SVN-Retron_2000.ttf', 50)
    # Tạo hình chữ nhật, hộp văn bản và nút
    login_register_field = LoginRegisterField(screen.get_size(), '#DBDBDB', 20)
    textArea1 = TextArea(font,pygame.rect.Rect(WINDOWS_SIZE[WINDOWS_INDEX][0] // 2 - WINDOWS_SIZE[WINDOWS_INDEX][0] // 8,WINDOWS_SIZE[WINDOWS_INDEX][1] // 2 + WINDOWS_SIZE[WINDOWS_INDEX][1] // 16 ,380,40) ,text="",color='white')
    button = Button("./assets/icon/button/Normal.png", (200, 300))
    #Vẽ các đối tượng lên màn hình

    #Vẽ nền lên
    screen.blit(background,(0,0))
    login_register_field.draw(screen)
    textArea1.draw(screen)
    button.draw(screen)
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            else:
                textArea1.handle_event(event)
                button.handle_event(event)
        # Cập nhật màn hình
        pygame.display.flip()
main()
'''
class Person:
    name = 'Adam'
p = Person()  # Tạo một đối tượng của lớp Person
setattr(p, 'name', 'John')  # Thay đổi thuộc tính 'name' thành 'John'
print('Name is:', p.name)  # In ra: Name is: John


class Example:
    def __init__(self):
        self.attribute = "old value"

    def update_attribute(self, new_value):
        setattr(self, 'attribute', new_value)
'''