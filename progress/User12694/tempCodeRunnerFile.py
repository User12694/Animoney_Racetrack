#Quy định đối tượng màn hình cài đặt kích thước cửa sổ
class WindowModeSettingClass:
    def __init__(self):
        #Khởi tạo các thuộc tính
        self.label1 = Label(835, 300, 125, 50, 'Window Mode') # Dòng chữ "Window Mode"
        self.button1 = Button(835, 360, 125, 50, 'Window') # Nút để chỉnh chế độ cửa sổ, mặc định có text "Window"
        self.label2 = Label(835, 420, 125, 50, 'Screen Ratio') # Dòng chữ "Screen Ratio"
        self.button2 = Button(835, 480, 125, 50, '1920x1080') # Nút chuyển kích thước cửa sổ. Mặc định là 1920x1080
        self.esc_button = Button(235,150,60,50,'Back') # Nút quay về
        self.color = (12, 53, 106)
        self.highlighted_color = (240, 178, 39)
        self.button2_active = True
    #Vẽ các thuộc tính lên bề mặt
    def draw(self, screen):
        pygame.draw.rect(screen,(44,150,210),pygame.Rect(0,0,1920,1080))
        self.label1.draw(screen)
        self.button1.draw(screen)
        self.label2.draw(screen)
        self.button2.draw(screen)
        self.esc_button.draw(screen)
    #Cập nhật trạng thái cho các thuộc tính
    def update(self, event):
        #Lấy vị trí đầu con trỏ chuột
        pos = pygame.mouse.get_pos()
        #Kiểm tra xem có nhấn chuột không
        if event.type == pygame.MOUSEBUTTONDOWN:
            #Hàm isOver kiểm tra xem con trỏ chuột có đè lên các thuộc tính Button trong khi đang nhấn nút chuột trái hay không
            if self.button1.isOver(pos):
                #Kiểm tra xem nút đầu tiên có được nhấn hay không
                self.button2_active = not self.button2_active
                pass
            if self.button2.isOver(pos):
                pass
            if self.esc_button.isOver(pos):
                return SettingClass() #Trả về màn hình cài đặt
        # Kiểm tra xem có đang rê chuột trên nút hay không
        if event.type == pygame.MOUSEMOTION:
            #Hàm isOver kiểm tra xem con trỏ chuột có đè lên các thuộc tính Button trong khi đang nhấn nút chuột trái hay không
            # Điểm chung của các thuộc tính ở đây là: Nếu được rê chuột lên thì chuyển thành màu vàng, không thì trả về màu hiện tại
            if self.button1.isOver(pos):
                self.button1.color =  self.highlighted_color
            else:
                self.button1.color = self.color
            if self.button2.isOver(pos):
                self.button2.color = self.highlighted_color
            else:
                self.button2.color = self.color
            if self.esc_button.isOver(pos):
                self.esc_button.color = self.highlighted_color
            else:
                self.esc_button.color = self.color
        return self