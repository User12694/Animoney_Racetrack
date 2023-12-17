import requests

def send_code_via_phone_number(phone_number):

    # Thông tin API của bạn
    api_key = "7B4282572D4722BFB72196D84479DF"
    secret_key = "622B62DD57A5F7928E4707F1B3CC45"

    # Số điện thoại người nhận
    phone_number = "0898855732"

    # Nội dung tin nhắn
    message = "Hello. "

    # URL của API
    url = "https://api.esms.vn/MainService.svc/json/SendMultipleMessage_V4_get"

    # Thông tin cần gửi
    data = {
        "Phone": phone_number,
        "Content": message,
        "ApiKey": api_key,
        "SecretKey": secret_key,
        "IsUnicode": False,
        "SmsType": 2,
        "Brandname": "",
        "BrandnameCode": "",
        "RequestId": "",
        "IsAd": False
    }

    # Gửi yêu cầu GET đến API
    response = requests.get(url, params=data)

    # In ra kết quả
    print(response.json())
