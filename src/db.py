import json

# Lưu giá trị của a và b vào tập tin
data = {"status": False, "b": False}
with open("data.json", "w") as f:
    json.dump(data, f)

# Đọc giá trị của a và b từ tập tin
with open("data.json", "r") as f:
    data = json.load(f)
a = data["a"]
b = data["b"]

def store(key, data):
    with open('db.json', 'r') as f:
        tempdata = json.load(f)
    tempdata[key] = data
    with open('db.json', 'w') as f:
        json.dump(tempdata, f)