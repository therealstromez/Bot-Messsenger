import json
from src import bot
import os

USER = os.getenv("USER")
PASSWORD = os.getenv("PASSWORD")

user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.5 Safari/605.1.15'

def main():
    # Load session đăng nhập từ trước nếu có
    with open('session.json') as f:
        session_cookies = json.load(f)

    client = bot.moifb(USER, PASSWORD, session_cookies=session_cookies)

    # Lấy session và lưu vào file để lần sau dùng cho đăng nhập
    session_cookies_new = client.getSession()
    with open('session.json', 'w') as outfile:
        json.dump(session_cookies_new, outfile)

    # Lắng nghe phản hồi từ messager
    client.listen()


if __name__ == '__main__':
    main()
