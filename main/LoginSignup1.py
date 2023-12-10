from tkinter import * 
from tkinter import messagebox
import numpy as np
from tkinter import filedialog
from PIL import Image, ImageTk
import subprocess
import os

bg_color = '#2b95d1'

class RegisterMenu:
    def __init__(self, root):
        self.root = root
        self.root.title('Sign up')
        self.background = Frame(root, bg=bg_color)
        self.background.place(x=0, y=0, relwidth=1, relheight=1)
        self.root.geometry('925x500+300+200')
        self.root.configure(bg="#ffffff")
        self.root.resizable(False,False)
        self.login_lock = False

        self.img = PhotoImage(file='./assets/icon/banner1.png')
        Label(self.root,image=self.img, bg=bg_color).place(x=50,y=50)

        self.frame=Frame(self.root,width=350,height=390,bg=bg_color)
        self.frame.place(x=480,y=50)

        heading = Label(self.frame, text="Sign up",fg='ư',bg=bg_color,font=('./assets/font/SVN-Retron_2000.ttf',23,'bold'))
        heading.place(x=100,y=5)

        self.username_entry = self.create_entry(self.frame, 'Username', 30, 80)
        self.password_entry = self.create_entry(self.frame, 'Password', 30, 150)
        self.password_confirm_entry = self.create_entry(self.frame, 'Confirm Password', 30, 220)

        Button(self.frame,width=39,pady=7,text='Sign up',bg='#57a1f8',fg=bg_color,cursor='hand2',border=0,command=self.sign_up).place(x=35,y=280)
        label = Label(self.frame,text="Have an account?",fg='white',bg=bg_color,font=('./assets/font/SVN-Retron_2000.ttf',9))
        label.place(x=90,y=340)

        sign_in = Button(self.frame,width=5,text="Sign in",border=0,bg=bg_color,cursor='hand2',fg='#57a1f8',command=self.switch)
        sign_in.place(x=200,y=340)

        subprocess.run(['cmd', '/c', 'chcp', '65001'])

    def create_entry(self, frame, text, x, y):
        def on_enter(e):
            entry.delete(0,'end')
        def on_leave(e):
            name = entry.get()
            if name=='':
                entry.insert(0,text)

        entry = Entry(frame,width=25,fg='white',border=0,bg=bg_color,font=('./assets/font/SVN-Retron_2000.ttf',11))
        entry.place(x=x,y=y)
        entry.insert(0,text)
        entry.bind('<FocusIn>',on_enter)
        entry.bind('<FocusOut>',on_leave)

        Frame(frame,width=295,height=2,bg='white').place(x=25,y=y+27)
        return entry

    def sign_up(self):
        username = self.username_entry.get()  # Lấy tên người dùng từ trường nhập liệu
        password = self.password_entry.get()  # Lấy mật khẩu từ trường nhập liệu
        repeat_password = self.password_confirm_entry.get()  # Lấy mật khẩu nhập lại từ trường nhập liệu
        if username == "" or password == "" or repeat_password == "":
            messagebox.showerror("Have blank emulation!", "Have blank emulation!")
        else:
            if os.path.exists(f"assets/player/{username}/{username}.txt"):  # Kiểm tra xem tên người dùng có tồn tại không
                messagebox.showerror("Username existed!", "Username existed!")  # Hiển thị thông báo lỗi
            elif password == repeat_password:  # Kiểm tra xem mật khẩu và mật khẩu nhập lại có khớp không
                os.makedirs(f"assets/player/{username}",exist_ok=True)
                with open(f"assets/player/{username}/{username}.txt", "w") as file:  # Tạo một file mới với tên người dùng
                    file.write(password + "\n")  # Ghi mật khẩu vào dòng đầu tiên của file
                    file.write("500" + "\n")  # Ghi "500" vào dòng thứ hai của file
                messagebox.showinfo("Register successful!", "Register successful!")  # Hiển thị thông báo thành công
                self.switch()  # Chuyển về chế độ đăng nhập
            else:
                messagebox.showerror("Passwords do not match!", "Passwords do not match!")  # Hiển thị thông báo lỗi
    
    def switch(self):
        global app
        app = LoginMenu(root)
        return app

class LoginMenu:
    def __init__(self, root):
        self.root = root
        self.root.title('Login')
        self.background = Frame(root, bg=bg_color)
        self.background.place(x=0, y=0, relwidth=1, relheight=1)
        self.root.geometry('925x500+300+200')
        self.root.configure(bg="#ffffff")
        self.root.resizable(False,False)

        self.img = PhotoImage(file='./assets/icon/banner1.png')
        Label(self.root,image=self.img, bg=bg_color).place(x=50,y=50)

        self.frame=Frame(self.root,width=350,height=350,bg=bg_color)
        self.frame.place(x=480,y=70)

        heading = Label(self.frame, text="Sign in",fg='white',bg=bg_color,font=('./assets/font/SVN-Retron_2000.ttf',23,'bold'))
        heading.place(x=100,y=5)

        self.username_entry = self.create_entry(self.frame, 'Username', 30, 80)
        self.password_entry = self.create_entry(self.frame, 'Password', 30, 150)

        Button(self.frame,width=39,pady=7,text='Sign in',bg='#57a1f8',fg=bg_color,cursor='hand2',border=0,command=self.sign_in).place(x=35,y=204)
        label = Label(self.frame,text="Don't have an account?",fg='white',bg=bg_color,font=('./assets/font/SVN-Retron_2000.ttf',9))
        label.place(x=75,y=270)

        sign_up = Button(self.frame,width=6,text="Sign up",border=0,bg=bg_color,cursor='hand2',fg='#57a1f8',command=self.switch)
        sign_up.place(x=215,y=270)

    def create_entry(self, frame, text, x, y):
        def on_enter(e):
            entry.delete(0,'end')
        def on_leave(e):
            name = entry.get()
            if name=='':
                entry.insert(0,text)

        entry = Entry(frame,width=25,fg='white',border=0,bg=bg_color,font=('./assets/font/SVN-Retron_2000.ttf',11))
        entry.place(x=x,y=y)
        entry.insert(0,text)
        entry.bind('<FocusIn>',on_enter)
        entry.bind('<FocusOut>',on_leave)

        Frame(frame,width=295,height=2,bg='white').place(x=25,y=y+27)
        return entry

    def sign_in(self):
        username = self.username_entry.get()  # Lấy tên người dùng từ trường nhập liệu
        password = self.password_entry.get()  # Lấy mật khẩu từ trường nhập liệu
        if os.path.exists(f"assets/player/{username}/{username}.txt"):  # Kiểm tra xem tên người dùng có tồn tại không
            with open(f"assets/player/{username}/{username}.txt", "r") as file:  # Mở file tương ứng với tên người dùng
                if password == file.readline().strip():  # Kiểm tra xem mật khẩu có khớp không
                    messagebox.showinfo("Login successful!", "Login successful!")  # Hiển thị thông báo thành công
                    global login_lock
                    login_lock = True
                    self.root.quit()  # Thoát chương trình
                else:
                    messagebox.showerror("Invalid username or password!", "Invalid username or password!")  # Hiển thị thông báo lỗi
        else:
            messagebox.showerror("Invalid username or password!", "Invalid username or password!")  # Hiển thị thông báo lỗi
    def switch(self):
        global app
        app = RegisterMenu(root)
        return app

root = Tk()
app = LoginMenu(root)
root.mainloop()
