import os
from PIL import Image
import string

# Đường dẫn đến thư mục chính
main_directory_path = 'C:/Users/nguye/OneDrive/Máy tính/Game_Project/assets/player/'

# Duyệt qua tất cả các thư mục con trong thư mục chính
def Browse():
    image_list = []  # Danh sách chứa các ảnh
    image_path_list = []  # Danh sách chứa các đường dẫn đến các tệp ảnh

    for player_directory_name in os.listdir(main_directory_path):
        player_directory_path = os.path.join(main_directory_path, player_directory_name)

        # Kiểm tra xem đường dẫn hiện tại có phải là thư mục không
        if os.path.isdir(player_directory_path):
            # Duyệt qua tất cả các file trong thư mục con
            for file_name in os.listdir(player_directory_path):
                # Kiểm tra xem file có phải là ảnh không
                if file_name.endswith('.png') or file_name.endswith('.jpg') or file_name.endswith('.jpeg'):
                    # Tạo đường dẫn đầy đủ đến file ảnh
                    image_path = os.path.join(player_directory_path, file_name)
                    image_path = image_path.replace('\\','/')
                    image_path_list.append(image_path)

    return image_path_list