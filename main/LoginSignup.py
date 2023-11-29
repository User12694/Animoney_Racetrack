# Import các thư viện cần thiết
import tkinter as tk
import tkinter.messagebox
import os
import time

login_lock = True
# Định nghĩa hàm đóng cửa sổ
def close_window():
    root.destroy()

# Định nghĩa các hàm di chuyển cửa sổ trong khi không có thanh tiêu đề
def start_move(event):
    root.x = event.x
    root.y = event.y

def stop_move(event):
    global root
    root.x = None
    root.y = None

def do_move(event):
    dx = event.x - root.x
    dy = event.y - root.y
    x = root.winfo_x() + dx
    y = root.winfo_y() + dy
    root.geometry(f"+{x}+{y}")

# Định nghĩa lớp LoginRegisterMenu
class LoginRegisterMenu:
    # Hàm khởi tạo
    def __init__(self, root):
        self.root = root  # Lưu trữ tham chiếu đến cửa sổ gốc
        self.root.geometry('300x400')  # Đặt kích thước cửa sổ
        self.frame = tk.Frame(self.root)  # Tạo một frame để chứa các widget
        self.frame.pack()  # Đóng gói frame vào cửa sổ

        # Tạo các widget và đóng gói chúng vào frame
        self.username_label = tk.Label(self.frame, text="Username")  # Nhãn cho trường nhập tên người dùng
        self.username_entry = tk.Entry(self.frame)  # Trường nhập tên người dùng
        self.password_label = tk.Label(self.frame, text="Password")  # Nhãn cho trường nhập mật khẩu
        self.password_entry = tk.Entry(self.frame, show="*")  # Trường nhập mật khẩu
        self.login_button = tk.Button(self.frame, text="Login", command=self.login)  # Nút đăng nhập
        self.switch_button = tk.Button(self.frame, text="Register", command=self.switch_to_register) # Nút chuyển đổi giữa đăng nhập và đăng ký

        # Đóng gói các widget vào frame
        self.username_label.pack()
        self.username_entry.pack()
        self.password_label.pack()
        self.password_entry.pack()
        self.login_button.pack()
        self.switch_button.pack()

    # Hàm xử lý sự kiện đăng nhập
    def login(self):
        username = self.username_entry.get()  # Lấy tên người dùng từ trường nhập liệu
        password = self.password_entry.get()  # Lấy mật khẩu từ trường nhập liệu
        if os.path.exists(f"{username}.txt"):  # Kiểm tra xem tên người dùng có tồn tại không
            with open(f"{username}.txt", "r") as file:  # Mở file tương ứng với tên người dùng
                if password == file.readline().strip():  # Kiểm tra xem mật khẩu có khớp không
                    tk.messagebox.showinfo("Login successful!", "Login successful!")  # Hiển thị thông báo thành công
                    login_lock = False
                    self.root.quit()  # Thoát chương trình
                else:
                    tk.messagebox.showerror("Invalid username or password!", "Invalid username or password!")  # Hiển thị thông báo lỗi
        else:
            tk.messagebox.showerror("Invalid username or password!", "Invalid username or password!")  # Hiển thị thông báo lỗi

    # Hàm xử lý sự kiện đăng ký
    def register(self):
        username = self.username_entry.get()  # Lấy tên người dùng từ trường nhập liệu
        password = self.password_entry.get()  # Lấy mật khẩu từ trường nhập liệu
        repeat_password = self.repeat_password_entry.get()  # Lấy mật khẩu nhập lại từ trường nhập liệu
        if username == "" or password == "" or repeat_password == "":
            tk.messagebox.showerror("Have blank emulation!", "Have blank emulation!")
        else:
            if os.path.exists(f"{username}.txt"):  # Kiểm tra xem tên người dùng có tồn tại không
                tk.messagebox.showerror("Username existed!", "Username existed!")  # Hiển thị thông báo lỗi
            elif password == repeat_password:  # Kiểm tra xem mật khẩu và mật khẩu nhập lại có khớp không
                with open(f"{username}.txt", "w") as file:  # Tạo một file mới với tên người dùng
                    file.write(password + "\n")  # Ghi mật khẩu vào dòng đầu tiên của file
                    file.write("5000")  # Ghi "5000" vào dòng thứ hai của file
                tk.messagebox.showinfo("Register successful!", "Register successful!")  # Hiển thị thông báo thành công
                self.switch_to_login()  # Chuyển về chế độ đăng nhập
            else:
                tk.messagebox.showerror("Passwords do not match!", "Passwords do not match!")  # Hiển thị thông báo lỗi

    # Hàm chuyển đổi sang chế độ đăng ký
    def switch_to_register(self):
        self.login_button.config(text="Register", command=self.register)  # Thay đổi nút đăng nhập thành nút đăng ký
        self.switch_button.config(text="Login", command=self.switch_to_login)  # Thay đổi nút chuyển đổi thành nút đăng nhập
        self.repeat_password_label = tk.Label(self.frame, text="Repeat Password")  # Tạo nhãn cho trường nhập lại mật khẩu
        self.repeat_password_entry = tk.Entry(self.frame, show="*")  # Tạo trường nhập lại mật khẩu
        self.repeat_password_label.pack()  # Đóng gói nhãn vào frame
        self.repeat_password_entry.pack()  # Đóng gói trường nhập liệu vào frame
        self.login_button.pack_forget()  # Loại bỏ nút đăng nhập khỏi frame
        self.switch_button.pack_forget()  # Loại bỏ nút chuyển đổi khỏi frame
        self.login_button.pack()  # Đóng gói nút đăng nhập vào frame
        self.switch_button.pack()  # Đóng gói nút chuyển đổi vào frame

    # Hàm chuyển đổi sang chế độ đăng nhập
    def switch_to_login(self):
        self.login_button.config(text="Login", command=self.login)  # Thay đổi nút đăng ký thành nút đăng nhập
        self.switch_button.config(text="Register", command=self.switch_to_register)  # Thay đổi nút chuyển đổi thành nút đăng ký
        self.repeat_password_label.pack_forget()  # Loại bỏ nhãn khỏi frame
        self.repeat_password_entry.pack_forget()  # Loại bỏ trường nhập liệu khỏi frame
        self.login_button.pack_forget()  # Loại bỏ nút đăng nhập khỏi frame
        self.switch_button.pack_forget()  # Loại bỏ nút chuyển đổi khỏi frame
        self.login_button.pack()  # Đóng gói nút đăng nhập vào frame
        self.switch_button.pack()  # Đóng gói nút chuyển đổi vào frame

# Tạo một cửa sổ gốc
root = tk.Tk()
#Loại bỏ thanh tiêu đề
root.overrideredirect(True)
root.bind("<ButtonPress-1>", start_move)
root.bind("<ButtonRelease-1>", stop_move)
root.bind("<B1-Motion>", do_move)
# Tạo một đối tượng LoginRegisterMenu và truyền cửa sổ gốc vào hàm khởi tạo
app = LoginRegisterMenu(root)
# Bắt đầu vòng lặp sự kiện của cửa sổ gốc
root.mainloop()
