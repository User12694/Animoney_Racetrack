import cv2
import numpy as np

# Mở camera
cap = cv2.VideoCapture(0)

while True:
    # Đọc hình ảnh từ camera
    ret, frame = cap.read()

    # Hiển thị hình ảnh trên cửa sổ
    cv2.imshow('Press Enter to Capture', frame)

    # Nếu người dùng nhấn Enter, chụp hình ảnh và so sánh nó với "image.png"
    if cv2.waitKey(1) == 13:  # 13 là mã ASCII của phím Enter
        cv2.imwrite('captured_image.jpg', frame)
        img = cv2.imread('image.png')
        difference = cv2.absdiff(img, frame)
        print('Difference:', np.sum(difference))
        break

# Giải phóng camera và đóng tất cả cửa sổ
cap.release()
cv2.destroyAllWindows()