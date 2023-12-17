from twilio.rest import Client

# Thông tin tài khoản Twilio của bạn
account_sid = 'your_account_sid'
auth_token = 'your_auth_token'

client = Client(account_sid, auth_token)

message = client.messages.create(
    body="Đây là tin nhắn của bạn",
    from_="số điện thoại Twilio của bạn",
    to="số điện thoại nhận"
)