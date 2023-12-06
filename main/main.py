from GameFunctions import *

#Đây là main loop
def main():
    global login_lock
    if not login_lock:
        pygame.quit()
        sys.exit()
    #Lớp phủ xuất hiện đầu tiên chính là màn hình cài đặt
    current_class = MenuClass()
    #Vòng lặp chính
    while True:  # Vòng lặp vô hạn, chương trình sẽ chạy cho đến khi có sự kiện thoát
        for event in pygame.event.get():  # Duyệt qua tất cả sự kiện đang chờ xử lý trong hàng đợi sự kiện của Pygame
            if event.type == pygame.QUIT:  # Nếu sự kiện là loại thoát (như nhấn nút đóng cửa sổ)
                pygame.quit()  # Thoát khỏi Pygame
                sys.exit()  # Thoát khỏi chương trình
            current_class = current_class.update(event)  # Cập nhật trạng thái của đối tượng hiện tại dựa trên sự kiện
        mouse_pos = pygame.mouse.get_pos()
        current_class.draw(mouse_pos)  # Vẽ đối tượng hiện tại lên màn hình

        pygame.display.flip()  # Cập nhật toàn bộ cửa sổ
        clock.tick(60)  # Đảm bảo chương trình chạy không quá 60 khung hình/giây
main()