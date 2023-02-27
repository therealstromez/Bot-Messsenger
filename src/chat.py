import json
import requests

url = "https://api.simsimi.vn/v1/simtalk"


def response(message) -> str:
    payload = {
        "text": message,
        "lc": 'vn'
    }
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    if response.status_code == 200:
        data = json.loads(response.text)
        message = data.get("message")
        return message
    else:
        return "?"
