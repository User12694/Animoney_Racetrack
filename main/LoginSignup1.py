# Import thư viện CustomTkinter
import customtkinter as ctk
import tkinter.messagebox
from PIL import Image, ImageTk
import smtplib
import random
import string
import os

code = None
login_lock = False
WINDOW_SIZES = [(1536,864),(768,432)]
WINDOW_SIZES_INDEX = 0
ratio = WINDOW_SIZES[WINDOW_SIZES_INDEX][0]/WINDOW_SIZES[0][0]
email = None
class LoginMenu:
    def __init__(self):
        # Tạo một cửa sổ mới với kích thước 1536x864 px và màu nền trắng
        self.window = ctk.CTk()
        self.window.geometry(f'{WINDOW_SIZES[WINDOW_SIZES_INDEX][0]}x{WINDOW_SIZES[WINDOW_SIZES_INDEX][1]}')
        self.window.config(bg='white')

        # Tạo hình ảnh 
        self.background = Image.open("./main/image.png")
        self.photo_background = ImageTk.PhotoImage(self.background)
        self.background_label = ctk.CTkLabel(self.window, image=self.photo_background,width=1173, height=864, text='')
        self.background_label.place(x=363, y=0)
        
        # Tạo một khung CTKFrame với màu nền là màu hex #2b95d1 và đặt ở vị trí x = 0, y = 0
        self.frame = ctk.CTkFrame(self.window,width=512, height=864, fg_color="#2b95d1")
        self.frame.place(x=0, y=0)

        # Tạo nhãn "Username/Email" và đặt ở tọa độ (92,334)
        self.username_label = ctk.CTkLabel(self.frame, text="Username/Email", font=("default", 20, "bold"))
        self.username_label.place(x=92, y=334)

        # Tạo nhãn "Password" và đặt ở tọa độ (92,443)
        self.password_label = ctk.CTkLabel(self.frame, text="Password", font=("default", 20, "bold"))
        self.password_label.place(x=92, y=443)

        # Tạo hộp nhập liệu thứ nhất và đặt ở tọa độ (92,370)
        self.username_entry = ctk.CTkEntry(self.frame, width=343, height=54, fg_color="white", border_width=2, border_color="black", corner_radius=20, font=("default", 20))
        self.username_entry.configure(text_color="black")
        self.username_entry.place(x=92, y=370)

        # Tạo hộp nhập liệu thứ hai và đặt ở tọa độ (92,478)
        self.password_entry = ctk.CTkEntry(self.frame, width=343, height=54, fg_color="white", border_width=2, border_color="black", corner_radius=20, font=("default", 20), show='•')
        self.password_entry.configure(text_color="black")
        self.password_entry.place(x=92, y=478)

        # Tạo nhãn "Don't have an account?" và đặt ở tọa độ (158,728)
        self.account_label = ctk.CTkLabel(self.frame, text="Don't have an account?", font=("default", 12, "bold"), fg_color="transparent", width=145, height=20)
        self.account_label.place(x=158, y=728)

        # Tạo nút "Sign up" và đặt ở tọa độ (303,728)
        self.signup_button = ctk.CTkButton(self.frame, text="Sign up", font=("default", 12, "bold"), fg_color="transparent", width=51, height=20, command=self.switch_to_register)
        self.signup_button.place(x=303, y=728)

        # Tạo nút "Login" và đặt ở tọa độ (213,608)
        self.login_button = ctk.CTkButton(self.frame, text="Login", font=("default", 20, "bold"), fg_color="#F7B104", width=169, height=47, corner_radius=30, command=self.login)
        self.login_button.place(x=179, y=575)

        # Tạo hình ảnh và đặt ở tọa độ (156,71)
        self.image = Image.open("./main/image_transparent.png")
        self.image = self.image.resize((200, 200))
        self.photo = ImageTk.PhotoImage(self.image)
        self.image_label = ctk.CTkLabel(self.frame, image=self.photo, width=200, height=200, text='')
        self.image_label.place(x=156, y=71)

        # Tạo nhãn "Login" và đặt ở tọa độ (167,271)
        self.login_label = ctk.CTkLabel(self.frame, text="Login", font=("default", 32, "bold"), fg_color="transparent", width=177, height=45)
        self.login_label.place(x=167, y=271)

        self.confirm_password_label = ctk.CTkLabel(self.frame, text="Password", font=("default", 20, "bold"))

        self.confirm_password_entry = ctk.CTkEntry(self.frame, width=343, height=54, fg_color="white", border_width=2, border_color="black", corner_radius=20, font=("default", 20),show='•')


    def draw(self):
        # Lặp vô tận để hiển thị cửa sổ
        self.window.mainloop()
    def switch_to_register(self):
        clear_entry(self.username_entry)
        clear_entry(self.password_entry)
        clear_entry(self.confirm_password_entry)
        self.login_label.configure(text="Register")
        self.username_label.configure(text="Email")
        self.password_label.place_forget()
        self.password_entry.place_forget()

        # Chuyển đổi text trên nút "Login" thành "Register"
        self.login_button.configure(text="Confirm Email", command= self.confirm_email)

        # Thay đổi chữ trong label "Don't have an account?" thành "Already have one?"
        self.account_label.configure(text="Already have one?")

        # Thay đổi chữ trên nút "Sign up" thành "Sign in"
        self.signup_button.configure(text="Sign in", command=self.switch_to_login)
    def switch_to_login(self):
        self.login_label.configure(text="Login")
        self.username_label.configure(text="Username/Email")
        self.login_button.configure(text="Login")
        self.confirm_password_entry.place_forget()
        self.confirm_password_label.place_forget()
        self.login_button.place_forget()
        self.password_label.place_forget()
        self.password_entry.place_forget()
        clear_entry(self.username_entry)
        clear_entry(self.password_entry)
        clear_entry(self.confirm_password_entry)
        self.login_button.configure(command=self.login)
        self.login_button.place(x = 179, y = 575)
        self.password_label.place(x = 92, y = 443)
        self.password_entry.place(x = 92, y = 478)
        self.account_label.configure(text="Don't have an account?")
        self.signup_button.configure(text="Sign up", command=self.switch_to_register)

    def confirm_email(self):
        global code, email
        email_input = self.username_entry.get()
        if email_input == '':
            tkinter.messagebox.showerror('Empty email', 'Email must be filled!')
        else:
            if check_gmail_in_string(email_input) == True:
                code = send_verification_code(email_input)
                email = email_input
                self.login_button.configure(text="Confirm", command= self.veri_confirm)
                self.login_label.configure(text="Confirmation")
                self.username_label.configure(text="Enter the code")
                self.username_entry.place_forget()
                self.username_entry.place(x=92, y = 370)
            else:
                code = send_verification_code(email_input + "@gmail.com")
                email = email_input
                self.login_button.configure(text="Confirm", command= self.veri_confirm)
                self.login_label.configure(text="Confirmation code")
                self.username_label.configure(text="Enter the code")
                self.username_entry.place_forget()
                self.username_entry.place(x=92, y = 370)
        return code
    
    def veri_confirm(self):
        global code, email
        self.login_label.configure(text="Confirmation code")
        self.username_label.configure(text="Enter the code")
        self.username_entry.place_forget()
        self.username_entry.place(x=92, y = 370)
        veri_code = self.username_entry.get()
        if veri_code == '':
            tkinter.messagebox.showinfo("Check")
        else:
            if veri_code == code:
                tkinter.messagebox.showinfo("Success!","Confirm success!")
                self.create_account()
            else:
                tkinter.messagebox.showerror("Invalid!","Invalid code!")

    def create_account(self):
        clear_entry(self.username_entry)
        clear_entry(self.password_entry)
        clear_entry(self.confirm_password_entry)
        self.username_label.place_forget()
        self.username_label.configure(text="Username")
        self.password_entry.place_forget()
        self.password_entry.place_forget()
        self.login_button.place_forget()
        self.username_label.place(x=92, y=334)
        self.password_label.place(x=92, y=443)
        self.password_entry.place(x=92, y=478)
        # Tạo nhãn "Password" và đặt ở tọa độ (92,443)
        self.confirm_password_label.place(x=92, y=549)

        # Tạo hộp nhập liệu thứ nhất và đặt ở tọa độ (92,370)
        self.confirm_password_entry.place(x=92, y=584)

        self.login_button.configure(text="Register", command=self.register)
        self.login_button.place(x = 179, y = 651)

    # Hàm xử lý sự kiện đăng nhập
    def login(self):
        global email
        username = self.username_entry.get()  # Lấy tên người dùng từ trường nhập liệu
        password = self.password_entry.get()  # Lấy mật khẩu từ trường nhập liệu
        emails = find_file_in_subdirectories('./assets/player',f'{username}.txt')
        if len(emails) == 0:
            tkinter.messagebox.showerror("Invalid username or password!", "Invalid username or password!")  # Hiển thị thông báo lỗi
        else: 
            if check_first_line_in_files(emails,password):
                tkinter.messagebox.showinfo("Success!", "Login successful!")  # Hiển thị thông báo 
                global login_lock
                login_lock = True
                self.window.quit()
            else:
                tkinter.messagebox.showerror("Invalid username or password!", "Invalid username or password!")  # Hiển thị thông báo lỗi
        if os.path.exists(f"assets/player/{username}/{username}.txt"):  # Kiểm tra xem tên người dùng có tồn tại không
            with open(f"assets/player/{username}/{username}.txt", "r") as file:  # Mở file tương ứng với tên người dùng
                if password == file.readline().strip():  # Kiểm tra xem mật khẩu có khớp không
                    tkinter.messagebox.showinfo("Login successful!", "Login successful!")  # Hiển thị thông báo thành công
                    global login_lock
                    login_lock = True
                    self.window.quit()  # Thoát chương trình
                else:
                    tkinter.messagebox.showerror("Invalid username or password!", "Invalid username or password!")  # Hiển thị thông báo lỗi
        else:
            tkinter.messagebox.showerror("Invalid username or password!", "Invalid username or password!")  # Hiển thị thông báo lỗi
    # Hàm xử lí sự kiện đăng nhập bằng khuôn mặt
    
    # Hàm xử lí sự kiện đăng kí bằng khuôn mặt

    # Hàm xử lý sự kiện đăng ký
    def register(self):
        global email
        username = self.username_entry.get()  # Lấy tên người dùng từ trường nhập liệu
        password = self.password_entry.get()  # Lấy mật khẩu từ trường nhập liệu
        repeat_password = self.repeat_password_entry.get()  # Lấy mật khẩu nhập lại từ trường nhập liệu
        if username == "" or password == "" or repeat_password == "":
            tkinter.messagebox.showerror("Have blank emulation!", "Have blank emulation!")
        else:
            if os.path.exists(f"assets/player/{username}/{username}.txt"):  # Kiểm tra xem tên người dùng có tồn tại không
                tkinter.messagebox.showerror("Username existed!", "Username existed!")  # Hiển thị thông báo lỗi
            elif password == repeat_password:  # Kiểm tra xem mật khẩu và mật khẩu nhập lại có khớp không
                os.makedirs(f"assets/player/{username}",exist_ok=True)
                with open(f"assets/player/{username}/{username}.txt", "w") as file:  # Tạo một file mới với tên người dùng
                    file.write(password + "\n")  # Ghi mật khẩu vào dòng đầu tiên của file
                    file.write("500" + "\n")  # Ghi "500" vào dòng thứ hai của file
                with open(f"assets/player/{username}/{email}.txt") as file:
                    file.write(email + '\n')
                tkinter.messagebox.showinfo("Register successful!", "Register successful!")  # Hiển thị thông báo thành công
                self.switch_to_login()  # Chuyển về chế độ đăng nhập
            else:
                tkinter.messagebox.showerror("Passwords do not match!", "Passwords do not match!")  # Hiển thị thông báo lỗi
def check_gmail_in_string(s):
    return "@gmail.com" in s
def send_verification_code(receiver_email):
    # Tạo mã xác minh ngẫu nhiên
    global code
    veri_code = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(6))
    code = veri_code
    # Tạo nội dung email
    subject = "Your verification code confirm the email to login/signup into Animal RaceTrack"
    body = f"""Hello {receiver_email}.
    We have sent a verificaion code to verify your login or registration.
    Your verification code is: {veri_code}
    You have sent this email because you requested the registration or login into your account.
    If not, you can ignore this."""
    message = f"Subject: {subject}\n\n{body}"

    # Thông tin tài khoản Gmail của bạn
    sender_email = "devteam.animalracetrack@gmail.com"
    password = "dzlh mowf obyr bfei"

    # Gửi email
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)

    print(f"Verification code sent to {receiver_email}.")
    return code
def clear_entry(entry):
    entry.delete(0,'end')
def find_file_in_subdirectories(relative_path, filename):
    # Chuyển đổi đường dẫn phụ thuộc thành đường dẫn tuyệt đối
    directory = os.path.abspath(relative_path)
    
    matching_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file == filename + '.txt':
                # Chuyển đổi đường dẫn tuyệt đối thành đường dẫn phụ thuộc
                matching_files.append(os.path.relpath(os.path.join(root, file), directory))
    return matching_files
def check_first_line_in_files(file_list, target_string):
    for file_path in file_list:
        with open(file_path, 'r') as file:
            first_line = file.readline().strip()
            if first_line == target_string:
                return True
    return False
# Tạo một đối tượng LoginMenu và vẽ nó
login_menu = LoginMenu()
login_menu.draw()
