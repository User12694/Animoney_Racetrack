# Import thư viện CustomTkinter
import customtkinter as ctk
import tkinter.messagebox
from PIL import Image, ImageTk
import smtplib
import random
import string
class LoginMenu:
    def __init__(self):
        # Tạo một cửa sổ mới với kích thước 1536x864 px và màu nền trắng
        self.window = ctk.CTk()
        self.window.geometry('1536x864')
        self.window.config(bg='white')

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
        self.username_entry.place(x=92, y=370)

        # Tạo hộp nhập liệu thứ hai và đặt ở tọa độ (92,478)
        self.password_entry = ctk.CTkEntry(self.frame, width=343, height=54, fg_color="white", border_width=2, border_color="black", corner_radius=20, font=("default", 20))
        self.password_entry.place(x=92, y=478)

        # Tạo nhãn "Don't have an account?" và đặt ở tọa độ (158,728)
        self.account_label = ctk.CTkLabel(self.frame, text="Don't have an account?", font=("default", 12, "bold"), fg_color="transparent", width=145, height=20)
        self.account_label.place(x=158, y=728)

        # Tạo nút "Sign up" và đặt ở tọa độ (303,728)
        self.signup_button = ctk.CTkButton(self.frame, text="Sign up", font=("default", 12, "bold"), fg_color="transparent", width=51, height=20, command=self.switch_to_register)
        self.signup_button.place(x=303, y=728)

        # Tạo nút "Login" và đặt ở tọa độ (213,608)
        self.login_button = ctk.CTkButton(self.frame, text="Login", font=("default", 20, "bold"), fg_color="#F7B104", width=169, height=47, corner_radius=30)
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

    def draw(self):
        # Lặp vô tận để hiển thị cửa sổ
        self.window.mainloop()
    def switch_to_register(self):
        self.login_label.configure(text="Register")
        self.password_label.place_forget()
        self.password_entry.place_forget()

        # Chuyển đổi text trên nút "Login" thành "Register"
        self.login_button.configure(text="Confirm Email", command= self.confirm_email)

        # Thay đổi chữ trong label "Don't have an account?" thành "Already have one?"
        self.account_label.configure(text="Already have one?")

        # Thay đổi chữ trên nút "Sign up" thành "Sign in"
        self.signup_button.configure(text="Sign in", command=self.switch_to_login)
    def switch_to_login(self):
        self.login_button.configure(text="Login")
        self.password_label.place(x = 92, y = 443)
        self.password_entry.place(x = 92, y = 478)
        self.account_label.configure(text="Don't have an account?")
        self.signup_button.configure(text="Sign up", command=self.switch_to_register)
    def confirm_email(self):
        email = self.username_entry.get()
        if email == '':
            tkinter.messagebox.showerror('Empty email', 'Email must be filled!')
        else:
            if check_gmail_in_string(email) == True:
                send_verification_code(email)
                self.login_button.configure(text="Create account", command= self.create_account)
            else:
                send_verification_code(email + "@gmail.com")
                self.login_button.configure(text="Create account", command= self.create_account)
    def create_account(self):
        self.username_label.place_forget()
        self.password_entry.place_forget()
        self.password_entry.place_forget()
        self.login_button.place_forget()
        # Tạo nhãn "Password" và đặt ở tọa độ (92,443)
        self.confirm_password_label = ctk.CTkLabel(self.frame, text="Password", font=("default", 20, "bold"))
        self.confirm_password_label.place(x=92, y=443)

        # Tạo hộp nhập liệu thứ nhất và đặt ở tọa độ (92,370)
        self.username_entry = ctk.CTkEntry(self.frame, width=343, height=54, fg_color="white", border_width=2, border_color="black", corner_radius=20, font=("default", 20))
        self.username_entry.place(x=92, y=370)
        pass

def check_gmail_in_string(s):
    return "@gmail.com" in s
def send_verification_code(receiver_email):
    # Tạo mã xác minh ngẫu nhiên
    code = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(6))

    # Tạo nội dung email
    subject = "Your verification code confirm the email to login/signup into Animal RaceTrack"
    body = f"""Hello {receiver_email}.
    We have sent a verificaion code to verify your login or registration.
    Your verification code is: {code}
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

# Tạo một đối tượng LoginMenu và vẽ nó
login_menu = LoginMenu()
login_menu.draw()
