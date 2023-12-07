# Import các thư viện cần thiết
import cv2
import numpy as np
import tkinter as tk
import tkinter.messagebox
from tkinter import filedialog
from PIL import Image, ImageTk
import os
import time
import findPicture as fp
import fnmatch
import subprocess

# Các khai báo cho biến toàn cục
login_lock = False
img = fp.find_images('assets/player') # Kiểm tra file được tìm thấy không
img_label = None
# confirm_button = None Nút xác nhận được gắn hàm kiểm tra trong FindPicture.py (hiện bị disable)
bg_color = "#2b95d1"
image_load_path = None 

def filePath():
    anh = "captured_image.png"

    # Tách tên ảnh và đuôi file
    ten, duoi_file = anh.split('.')

    print("Tên ảnh:", ten)
    print("Đuôi file:", duoi_file)
    imgpath = f'{ten}.{duoi_file}'
    return imgpath
def face_detect(image_path):
    img = cv2_read_image(image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

    # Khởi tạo Haar cascade
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    # Phát hiện khuôn mặt trong hình ảnh
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # Kiểm tra xem có phát hiện được khuôn mặt nào không
    if len(faces) == 0:
        text = "Không tìm thấy khuôn mặt nào. Vui lòng đưa lại ảnh"
        return False, text
    else:
        text = "Phát hiện khuôn mặt."
        return True, text
#Đọc đường dẫn file chứa kí tự Unicode (nếu có)
def cv2_read_image(image_path):
    print(image_path)
    image_data = np.fromfile(image_path, dtype=np.uint8)
    # Giải mã mảng byte thành ảnh
    image = cv2.imdecode(image_data, cv2.IMREAD_UNCHANGED)
    return image
def compare_faces(image1_path, image2_path):
    # Đọc hai hình ảnh từ đường dẫn
    img1 = cv2_read_image(image1_path)
    img2 = cv2_read_image(image2_path)

    #Chuyển đổi hình ảnh sang hệ màu xám 
    changed_img1 = cv2.cvtColor(img1, cv2.COLOR_RGB2GRAY)
    changed_img2 = cv2.cvtColor(img2, cv2.COLOR_RGB2GRAY)
    # Khởi tạo Haar cascade
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    # Phát hiện khuôn mặt trong hai hình ảnh
    faces1 = face_cascade.detectMultiScale(changed_img1, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    faces2 = face_cascade.detectMultiScale(changed_img2, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

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
    return compare_val

# Định nghĩa lớp LoginRegisterMenu
class LoginRegisterMenu:
    # Hàm khởi tạo
    def __init__(self, root):
        self.root = root  # Lưu trữ tham chiếu đến cửa sổ gốc
        self.img_label = None
        self.img_display = None
        self.confirm_button = None
        logo = Image.open("assets/icon/banner.png")
        self.logo = ImageTk.PhotoImage(logo)
        self.root.geometry('400x600')  # Đặt kích thước cửa sổ
        self.frame = tk.Frame(self.root,bg=bg_color)  # Tạo một frame để chứa các widget
        self.frame.pack()  # Đóng gói frame vào cửa sổ

        # Tạo các widget và đóng gói chúng vào frame
        self.game_logo = tk.Label(self.frame, image=self.logo)
        self.username_label = tk.Label(self.frame, text="Username", bg=bg_color)  # Nhãn cho trường nhập tên người dùng
        self.note_label = tk.Label(self.frame,text="(If you login by face, username must be filled)",bg=bg_color)
        self.username_entry = tk.Entry(self.frame)  # Trường nhập tên người dùng
        self.password_label = tk.Label(self.frame, text="Password",bg=bg_color)  # Nhãn cho trường nhập mật khẩu
        self.password_entry = tk.Entry(self.frame, show="*")  # Trường nhập mật khẩu
        self.login_button = tk.Button(self.frame, text="Login", command=self.login)  # Nút đăng nhập
        self.switch_button = tk.Button(self.frame, text="Don't have one? Register", command=self.switch_to_register) # Nút chuyển đổi giữa đăng nhập và đăng ký
        self.open_button = tk.Button(self.frame,text="Login by your face? Browse...",command = self.open_image)
        self.image_label = tk.Label(self.frame,bg=bg_color)
        
        self.confirm_button = tk.Button(self.frame,text="Confirm image",command=self.confirm_image)
        self.confirmed_notification = tk.Label(self.frame, text="Image loaded!", bg=bg_color)
        self.face_detected = tk.Label(self.frame, text="Have faces!", bg=bg_color)
        self.noface_detected = tk.Label(self.frame, text="No faces!", bg=bg_color)
        # Đóng gói các widget vào frame
        self.game_logo.pack()
        self.username_label.pack()
        self.note_label.pack()
        self.username_entry.pack()
        self.password_label.pack()
        self.password_entry.pack()
        self.login_button.pack(pady=10)
        self.switch_button.pack()
        self.open_button.pack()
        self.image_label.pack()
    # Hàm xử lý sự kiện đăng nhập
    def login(self):
        username = self.username_entry.get()  # Lấy tên người dùng từ trường nhập liệu
        password = self.password_entry.get()  # Lấy mật khẩu từ trường nhập liệu
        if os.path.exists(f"assets/player/{username}/{username}.txt"):  # Kiểm tra xem tên người dùng có tồn tại không
            with open(f"assets/player/{username}/{username}.txt", "r") as file:  # Mở file tương ứng với tên người dùng
                if password == file.readline().strip():  # Kiểm tra xem mật khẩu có khớp không
                    tk.messagebox.showinfo("Login successful!", "Login successful!")  # Hiển thị thông báo thành công
                    global login_lock
                    login_lock = True
                    self.root.quit()  # Thoát chương trình
                else:
                    tk.messagebox.showerror("Invalid username or password!", "Invalid username or password!")  # Hiển thị thông báo lỗi
        else:
            tk.messagebox.showerror("Invalid username or password!", "Invalid username or password!")  # Hiển thị thông báo lỗi
    # Hàm xử lí sự kiện đăng nhập bằng khuôn mặt
    
    # Hàm xử lí sự kiện đăng kí bằng khuôn mặt

    # Hàm xử lý sự kiện đăng ký
    def register(self):
        username = self.username_entry.get()  # Lấy tên người dùng từ trường nhập liệu
        password = self.password_entry.get()  # Lấy mật khẩu từ trường nhập liệu
        repeat_password = self.repeat_password_entry.get()  # Lấy mật khẩu nhập lại từ trường nhập liệu
        if username == "" or password == "" or repeat_password == "":
            tk.messagebox.showerror("Have blank emulation!", "Have blank emulation!")
        else:
            if os.path.exists(f"assets/player/{username}/{username}.txt"):  # Kiểm tra xem tên người dùng có tồn tại không
                tk.messagebox.showerror("Username existed!", "Username existed!")  # Hiển thị thông báo lỗi
            elif password == repeat_password:  # Kiểm tra xem mật khẩu và mật khẩu nhập lại có khớp không
                os.makedirs(f"assets/player/{username}",exist_ok=True)
                with open(f"assets/player/{username}/{username}.txt", "w") as file:  # Tạo một file mới với tên người dùng
                    file.write(password + "\n")  # Ghi mật khẩu vào dòng đầu tiên của file
                    file.write("5000")  # Ghi "5000" vào dòng thứ hai của file
                tk.messagebox.showinfo("Register successful!", "Register successful!")  # Hiển thị thông báo thành công
                self.switch_to_login()  # Chuyển về chế độ đăng nhập
            else:
                tk.messagebox.showerror("Passwords do not match!", "Passwords do not match!")  # Hiển thị thông báo lỗi

    # Hàm chuyển đổi sang chế độ đăng ký
    def switch_to_register(self):
        self.login_button.config(text="Register", command=self.register)  # Thay đổi nút đăng nhập thành nút đăng ký
        self.switch_button.config(text="Already have an account? Login", command=self.switch_to_login)  # Thay đổi nút chuyển đổi thành nút đăng nhập
        self.note_label.config(text="(If you register by face, username must be filled.)")
        self.open_button.config(text="Register by your face? Browse...",command=self.open_image)
        self.repeat_password_label = tk.Label(self.frame, text="Repeat Password",bg=bg_color)  # Tạo nhãn cho trường nhập lại mật khẩu
        self.repeat_password_entry = tk.Entry(self.frame, show="*")  # Tạo trường nhập lại mật khẩu
        self.repeat_password_label.pack()  # Đóng gói nhãn vào frame
        self.repeat_password_entry.pack()  # Đóng gói trường nhập liệu vào frame
        self.login_button.pack_forget()  # Loại bỏ nút đăng nhập khỏi frame
        self.switch_button.pack_forget()  # Loại bỏ nút chuyển đổi khỏi frame
        self.open_button.pack_forget() #Loại bỏ nút mở ảnh khỏi fame
        self.image_label.pack_forget()
        self.confirm_button.pack_forget()
        self.confirmed_notification.pack_forget()
        self.face_detected.pack_forget()
        self.noface_detected.pack_forget()
        self.login_button.pack(pady=10)  # Đóng gói nút đăng nhập vào frame
        self.switch_button.pack()  # Đóng gói nút chuyển đổi vào frame
        self.open_button.pack() # Đóng gói nút mở ảnh vào frame
        self.login_button.pack()

    # Hàm chuyển đổi sang chế độ đăng nhập
    def switch_to_login(self):
        self.login_button.config(text="Login", command=self.login)  # Thay đổi nút đăng ký thành nút đăng nhập
        self.switch_button.config(text="Don't have one? Register", command=self.switch_to_register)  # Thay đổi nút chuyển đổi thành nút đăng ký
        self.note_label.config(text="(If you login by face, username must be filled.)")
        self.open_button.config(text="Login by your face? Browse...",command=self.open_image)
        self.repeat_password_label.pack_forget()  # Loại bỏ nhãn khỏi frame
        self.repeat_password_entry.pack_forget()  # Loại bỏ trường nhập liệu khỏi frame
        self.login_button.pack_forget()  # Loại bỏ nút đăng nhập khỏi frame
        self.switch_button.pack_forget()  # Loại bỏ nút chuyển đổi khỏi frame
        self.open_button.pack_forget() #Loại bỏ nút mở ảnh khỏi frame
        self.image_label.pack_forget()
        self.confirm_button.pack_forget()
        self.confirmed_notification.pack_forget()
        self.face_detected.pack_forget()
        self.noface_detected.pack_forget()
        self.login_button.pack(pady=10)  # Đóng gói nút đăng nhập vào frame
        self.switch_button.pack()  # Đóng gói nút chuyển đổi vào frame
        self.open_button.pack() # Loại bỏ nút mở ảnh khỏi frame
        
    # Hàm dùng để mở ảnh 
    def open_image(self):
        global image_load, image_load_path
        # Mở cửa sổ chọn file để chọn ảnh
        self.file_path = filedialog.askopenfilename(filetypes=[('Image Files', '*.jpg')])
        # Mở ảnh và điều chỉnh kích thước
        self.image = Image.open(self.file_path)
        self.image.thumbnail((self.image.width // 10, self.image.height // 10))
        # Chuyển ảnh sang định dạng phù hợp để hiển thị trong tkinter
        self.photo = ImageTk.PhotoImage(self.image)
        # Hiển thị ảnh trong cửa sổ tkinter
        self.image_label.pack_forget()
        self.image_label.config(image=self.photo)
        self.image_label.pack()
        self.image_label.image = self.photo
        self.confirmed_notification.pack_forget()
        self.noface_detected.pack_forget()
        self.face_detected.pack_forget()
        self.confirm_button.pack_forget()
        # Hiển thị nút "Xác nhận ảnh"
        self.confirm_button.pack()
        # self.login_button.config(command=self.result)
        image_load_path = self.file_path
        return image_load_path
        
    def confirm_image(self):
        global image_paths, image_load_path
        if image_load_path:
            self.confirmed_notification.pack_forget()
            self.confirmed_notification.pack()
            # self.login_button.config(command=self.result())
        else:
            self.confirmed_notification.pack_forget()
            self.confirmed_notification.config(text="No image loaded! Try again.",bg=bg_color)
            self.confirmed_notification.pack()
    def result(self):
        global image_paths, image_load_path
        result, text = face_detect(image_load_path)
        if result:
            result_list = []
            for path in image_paths:
                result_list.append(compare_faces(image_load_path, path))
            print(result_list)
        else:
            self.noface_detected.pack_forget()
            self.noface_detected.pack()
            
#Thực hiện lệnh shell để nhận đường dẫn Unicode:
subprocess.run(['cmd', '/c', 'chcp', '65001'])
# Tạo một cửa sổ gốc
root = tk.Tk()
root.wm_iconbitmap('assets/icon/ic_launcher.png')
# root.protocol("WM_DELETE_WINDOW", disable_event)
root.title("Animoney RaceTrack - Login")
root.config(bg=bg_color)
# Tạo một đối tượng LoginRegisterMenu và truyền cửa sổ gốc vào hàm khởi tạo
app = LoginRegisterMenu(root)
# Bắt đầu vòng lặp sự kiện của cửa sổ gốc
root.mainloop()
