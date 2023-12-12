import datetime
from io import StringIO 

file_path = 'test.txt'
userName = 'Thuan'
winOrLose = 'win'
moneyBet = 200 # can be 200, 500, 1000. Change to bet_money
moneyNow = 5000 # Change to user_money


def updateMoneyAndWriteHistory(file_path, userName, moneyBet, winOrLose):
    global moneyNow
    if winOrLose == 'win':
        moneyNow += moneyBet * 3 
        result = f"win +{moneyBet * 3}"
    else:
        moneyNow -= moneyBet
        result = f'lose -{moneyBet}'
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    result_to_write = f"{current_time}: {userName} {result}, balance: {moneyNow}"

    with open(file_path, 'a') as file:
        file.write('\n'+ result_to_write)

#updateMoneyAndWriteHistory(file_path, userName, moneyBet, winOrLose, moneyNow)

historyLine = StringIO() #một bộ đệm string để có thể dễ dàng replace lại nhiều lần, đỡ cho ông ấy
traceBackCount = 0

def readHistorLineFromFile(file_path, historyLine, traceBackCount):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        line_number = len(lines) - 1 - traceBackCount
        if line_number < len(lines) and line_number >= 2:
            historyLine.truncate(0) #cắt ngắn hết ký tự ở historyline
            historyLine.seek(0) #trỏ vào đầu chuỗi đấy
            historyLine.write(lines[line_number]) #viết mới vào

#readHistorLineFromFile(file_path, historyLine, traceBackCount)
def main():
    Input = int(input("Nhap: "))
    while (Input != 0):
        moneyBet = Input
        traceBackCount = int(input("TraceBackCount: "))
        updateMoneyAndWriteHistory(file_path, userName, moneyBet, winOrLose)
        readHistorLineFromFile(file_path, historyLine, traceBackCount)
        print(historyLine.getvalue())
        Input = int(input("Nhap: "))

main()

#print(historyLine.getvalue())

