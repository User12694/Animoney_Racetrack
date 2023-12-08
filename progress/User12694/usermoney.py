#Import file này vào GameFunctions
import pygame, sys, os
from datetime import datetime

# Tạo các biến toàn cục cho tài khoản và số tiền:

username = 'nhat' #Khai báo trước, sau này có gì thế vô đây
user_id = username # Cái này tí nhập qua sau
money = 4800 #Cần thay đổi biến này thành biến cục bộ
reward = 100 #Ví dụ cho số tiền được thay đổi khi chơi minigame
#Thêm tí code ngăn người chơi ăn chặn tiền
if money > 0:
    money 
# Viết mảng chỉ kết quả
result = [('Lose'), ('Win')]
#Kết quả: Thắng hoặc thua, k có nhưng
result_index = 0
def update_money(username):
    #Đọc toàn bộ file: Dòng chỉ số 0 là mật khẩu, 1 là số tiền, 2 trở đi sẽ là dòng lịch sử đấu
    with open(f'./assets/player/{username}/{username}.txt','r') as f:
        lines = f.readlines()
    lines[1] = f"{money}\n" # Thay đổi dòng cần thiết. Ở đây thay thế money.
    with open(f'./assets/player/{username}/{username}.txt','w') as f:
        f.writelines(lines) # Ghi lại toàn bộ nội dung vào file
update_money(username=username)

#Hàm này nên được cập nhật khi kết thúc trận đấu. Lấy đối tượng thời gian khi nhấn Bắt đầu chơi
#Chỉ lấy ở phần chơi chính
now = datetime.now()
def update_timestamp(username, result): #Ta chỉ cần thay đổi kết quả các dòng timestamp thôi
    global now, reward#Lấy biến now toàn cục từ phần nhấn nút bắt đầu. 
    with open(f'./assets/player/{username}/{username}.txt', 'r') as f:
        lines = f.readlines() #Đọc tất cả các dòng và ghi nội dung của mỗi dòng vào một lines
    #Làm tròn thời gian đến phút
    rounded_now = now.replace(second= 0, microsecond=0)
    # Chuyển đổi ngày và giờ thành chuỗi
    datetime_string = rounded_now.strftime('%d/%m %H:%M')
    duel_recent = datetime_string + "," + result  # Lấy ra ngày giờ chơi và kết quả của lần chơi trước
    if result == 'Win':
        duel_recent = duel_recent + ',' + f'+{reward}' + '\n'
    else:
        duel_recent = duel_recent + ',' + f'-{reward}' + '\n'
    # Ghi lại nội dung vào file
    # Kiểm tra xem dòng cuối cùng có trống không, và kiểm tra xem s
    if len(lines) < 7:
        if lines[-1].strip() == '':
            # Nếu dòng cuối cùng trống, ghi nội dung mới lên dòng đó
            lines[-1] = duel_recent
        else:
        # Nếu dòng cuối cùng không trống, thêm nội dung mới vào cuối file
            lines.append(duel_recent)
    else:
        if lines[-1].strip() == '':
            # Nếu dòng cuối cùng trống, ghi nội dung mới lên dòng đó
            lines[-1] = duel_recent
        else:
            # Nếu dòng cuối cùng không trống, thêm nội dung mới vào cuối file
            lines.append(duel_recent)
        # Giữ lại dòng 0, 1 và các dòng có cùng cấu trúc từ 2 đến 7
        lines = lines[:2] + lines[-5:]
    # Ghi lại nội dung vào file
    with open(f'./assets/player/{username}/{username}.txt', 'w') as f:
        f.writelines(lines)
#Thực thi lệnh để test. Có thể bỏ nó đi
update_timestamp(username=user_id, result=result[result_index])
# Đặt giá trị kết quả mặc định là 0. Có thể thay đổi bằng cách thay chỉ số result_index