# Import các thư viện cần thiết
# import cv2. Thư viện này không hoạt động trên một số máy của nhóm. 
import numpy as np
import tkinter as tk
import tkinter.messagebox
from tkinter import filedialog
from PIL import Image, ImageTk
import os
import time
# import findPicture as fp . Tạm thời disbale tính năng nhận diện hình ảnh
import fnmatch

# Các khai báo cho biến toàn cục
login_lock = False
# img = fp.Browse() # Kiểm tra file được tìm thấy không
img_label = None
# confirm_button = None Nút xác nhận được gắn hàm kiểm tra trong FindPicture.py (hiện bị disable)
main_directory_path = 'C:/Users/nguye/OneDrive/Máy tính/Game_Project/assets/player/'

def disable_event():
    pass  
def filePath():
    anh = "captured_image.png"

    # Tách tên ảnh và đuôi file
    ten, duoi_file = anh.split('.')

    print("Tên ảnh:", ten)
    print("Đuôi file:", duoi_file)
    imgpath = f'{ten}.{duoi_file}'
    return imgpath

# Định nghĩa lớp LoginRegisterMenu
class LoginRegisterMenu:
    # Hàm khởi tạo
    def __init__(self, root):
        self.root = root  # Lưu trữ tham chiếu đến cửa sổ gốc
        self.img_label = None
        self.img_display = None
        self.confirm_button = None
        logo = Image.open("assets/icon/ic_launcher.png")
        self.logo = ImageTk.PhotoImage(logo)
        self.root.geometry('400x600')  # Đặt kích thước cửa sổ
        self.frame = tk.Frame(self.root)  # Tạo một frame để chứa các widget
        self.frame.pack()  # Đóng gói frame vào cửa sổ

        # Tạo các widget và đóng gói chúng vào frame
        self.game_logo = tk.Label(self.frame, image=self.logo)
        self.username_label = tk.Label(self.frame, text="Username")  # Nhãn cho trường nhập tên người dùng
        self.note_label = tk.Label(self.frame,text="(If you login by face, username must be filled)")
        self.username_entry = tk.Entry(self.frame)  # Trường nhập tên người dùng
        self.password_label = tk.Label(self.frame, text="Password")  # Nhãn cho trường nhập mật khẩu
        self.password_entry = tk.Entry(self.frame, show="*")  # Trường nhập mật khẩu
        self.login_button = tk.Button(self.frame, text="Login", command=self.login)  # Nút đăng nhập
        self.switch_button = tk.Button(self.frame, text="Don't have one? Register", command=self.switch_to_register) # Nút chuyển đổi giữa đăng nhập và đăng ký
        # self.open_button = tk.Button(self.frame,text="Other choice? Browse...",command = self.open_image)
        self.emptyname_error = tk.Label(self.frame,text="Error! Name must be filled!")
        
        # Đóng gói các widget vào frame
        self.game_logo.pack()
        self.username_label.pack()
        self.note_label.pack()
        self.username_entry.pack()
        self.password_label.pack()
        self.password_entry.pack()
        self.login_button.pack()
        self.switch_button.pack()
        # self.open_button.pack()
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
        self.repeat_password_label = tk.Label(self.frame, text="Repeat Password")  # Tạo nhãn cho trường nhập lại mật khẩu
        self.repeat_password_entry = tk.Entry(self.frame, show="*")  # Tạo trường nhập lại mật khẩu
        self.repeat_password_label.pack()  # Đóng gói nhãn vào frame
        self.repeat_password_entry.pack()  # Đóng gói trường nhập liệu vào frame
        self.login_button.pack_forget()  # Loại bỏ nút đăng nhập khỏi frame
        self.switch_button.pack_forget()  # Loại bỏ nút chuyển đổi khỏi frame
        # self.open_button.pack_forget()
        self.emptyname_error.pack_forget()
        self.login_button.pack()  # Đóng gói nút đăng nhập vào frame
        self.switch_button.pack()  # Đóng gói nút chuyển đổi vào frame
        # self.open_button.pack() # Đóng gói nút mở ảnh vào frame

    # Hàm chuyển đổi sang chế độ đăng nhập
    def switch_to_login(self):
        self.login_button.config(text="Login", command=self.login)  # Thay đổi nút đăng ký thành nút đăng nhập
        self.switch_button.config(text="Don't have one? Register", command=self.switch_to_register)  # Thay đổi nút chuyển đổi thành nút đăng ký
        self.note_label.config(text="(If you login by face, username must be filled.)")
        self.repeat_password_label.pack_forget()  # Loại bỏ nhãn khỏi frame
        self.repeat_password_entry.pack_forget()  # Loại bỏ trường nhập liệu khỏi frame
        self.login_button.pack_forget()  # Loại bỏ nút đăng nhập khỏi frame
        self.switch_button.pack_forget()  # Loại bỏ nút chuyển đổi khỏi frame
        # self.open_button.pack_forget() #Loại bỏ nút mở ảnh khỏi frame
        self.emptyname_error.pack_forget()
        self.login_button.pack()  # Đóng gói nút đăng nhập vào frame
        self.switch_button.pack()  # Đóng gói nút chuyển đổi vào frame
        # self.open_button.pack() # Loại bỏ nút mở ảnh khỏi frame
    '''# Hàm dùng để mở ảnh 
    def open_image(self):
        
        file_path = filedialog.askopenfilename(filetypes=[('Image Files', '*.jpg')])
        if file_path:
            if self.img_label:
                self.img_label.destroy()
            if self.confirm_button:
                self.confirm_button.destroy()
            img = Image.open(file_path)
            img.thumbnail((img.width // 10, img.height // 10))
            img = ImageTk.PhotoImage(img)
            self.img_label = tk.Label(image=img)
            self.img_label.config(image=img)
            self.img_label.image = img
            self.confirm_button = tk.Button(self.root, text="Confirm", command=self.confirm_image)
            self.img_label.pack_forget()
            self.confirm_button.pack_forget()
            self.img_label.pack()
            self.confirm_button.pack(pady= 10)
            return img
    def confirm_image(self):
        if self.open_image:
            # Chèn các lệnh xác minh thông tin
            username = self.username_entry.get()
            if username != '':
                if os.path.exists(f"../assets/player/{username}/{username}.txt"): # Kiểm tra xem tên người dùng có tồn tại không
                    print("Confirm!")
                    
            else:
                self.emptyname_error.pack(pady = 10)'''
           
# Tạo một cửa sổ gốc
root = tk.Tk()
root.wm_iconbitmap('assets/icon/ic_launcher.png')
root.protocol("WM_DELETE_WINDOW", disable_event)
root.title("Animoney RaceTrack - Login")
# Tạo một đối tượng LoginRegisterMenu và truyền cửa sổ gốc vào hàm khởi tạo
app = LoginRegisterMenu(root)
# Bắt đầu vòng lặp sự kiện của cửa sổ gốc
root.mainloop()
