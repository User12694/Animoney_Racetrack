import cv2
import numpy as np

def compare_faces(image1_path, image2_path):
    # Đọc hai hình ảnh từ đường dẫn
    img1 = cv2.imread(image1_path, cv2.COLOR_RGBA2GRAY)
    img2 = cv2.imread(image2_path, cv2.COLOR_RGBA2GRAY)

    # Khởi tạo Haar cascade
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    # Phát hiện khuôn mặt trong hai hình ảnh
    faces1 = face_cascade.detectMultiScale(img1, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    faces2 = face_cascade.detectMultiScale(img2, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # Kiểm tra xem có phát hiện được khuôn mặt không
    if len(faces1) == 0 or len(faces2) == 0:
        print("Không tìm thấy khuôn mặt trong một hoặc cả hai hình ảnh.")
        return

    # Chọn khuôn mặt lớn nhất trong mỗi hình ảnh
    x1, y1, w1, h1 = faces1[0]
    x2, y2, w2, h2 = faces2[0]

    # Cắt hai hình ảnh để chỉ giữ lại khuôn mặt lớn nhất
    cropped_img1 = img1[y1:y1+h1, x1:x1+w1]
    cropped_img2 = img2[y2:y2+h2, x2:x2+w2]

    # Tính toán histogram cho hai hình ảnh
    hist1 = cv2.calcHist([cropped_img1], [0], None, [256], [0, 256])
    hist2 = cv2.calcHist([cropped_img2], [0], None, [256], [0, 256])

    # So sánh hai histogram
    compare_val = cv2.compareHist(hist1, hist2, cv2.HISTCMP_CORREL)
    
    print("Độ tương đồng giữa hai khuôn mặt:", compare_val)

# Thay 'path_to_your_image1.jpg' và 'path_to_your_image2.jpg' bằng đường dẫn thực tế đến hai hình ảnh bạn muốn so sánh
compare_faces('findImageTest/image1.jpg', 'findImageTest/image5.jpg')
