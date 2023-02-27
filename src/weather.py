import requests
import json

# Khai báo URL API và thành phố bạn muốn dự báo thời tiết
url = 'http://api.weatherstack.com/current?access_key=ecd6363b0868b8e8765ecf164d3cae60&query=Quang%20Ninh'

# Gửi yêu cầu HTTP để lấy thông tin thời tiết
def get():
    response = requests.get(url)
    print(response)
    # Phân tích cú pháp JSON của phản hồi
    data = json.loads(response.text)

    # Lấy nhiệt độ và thông tin thời tiết hiện tại
    current_weather = data['current']
    temperature = current_weather['temperature']
    weather_descriptions = current_weather['weather_descriptions']

    # In thông tin lấy được
    return "Nhiệt độ hiện tại là: {} độ C\nThông tin thời tiết hiện tại là: {}".format(temperature, weather_descriptions[0])
