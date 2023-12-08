import pygame, sys, os
from datetime import datetime
from collection import deque

# Tạo các biến toàn cục cho tài khoản và số tiền:
username = 'phuoc' #Khai báo trước, sau này có gì thế vô đây
user_id = username # Cái này tí nhập qua sau
#Lấy thời gian hiện tại
now = datetime.now()
#Làm tròn thời gian đến phút
money = 4800
rounded_now = now.replace(second= 0, microsecond=0)
date_string = rounded_now.strftime('%d/%m')
time_string = rounded_now.strftime('%H:%M')
# Viết mảng chỉ kết quả
result = ['Lose', 'Win']
doesWin = 0
timestamp = date_string + ' ' + time_string + "," + result[doesWin]
def update_money():
    #Đọc toàn bộ file: Dòng chỉ số 0 là mật khẩu, 1 là số tiền, 2 trở đi sẽ là dòng lịch sử đấu
    with open(f'./assets/player/{username}/{username}.txt','r') as f:
        lines = f.readlines()
    lines[1] = f"{money}\n" # Thay đổi dòng cần thiết. Ở đây thay thế money.
    with open(f'./assets/player/{username}/{username}.txt','w') as f:
        f.writelines(lines) # Ghi lại toàn bộ nội dung vào file
update_money()
def update_timestamp(): #Ta chỉ cần thay đổi kết quả các dòng timestamp thôi
    with open(f'./assets/player/{username}/{username}.txt', 'r') as f:
        lines = f.readlines()

    # Giữ lại dòng 0 và 1, và tạo một deque với các dòng từ 2 đến 7
    lines = lines[:2] + list(deque(lines[2:8], maxlen=6))

    # Ghi lại nội dung vào file
    with open(f'./assets/player/{username}/{username}.txt', 'w') as f:
        f.writelines(lines)
update_timestamp()    