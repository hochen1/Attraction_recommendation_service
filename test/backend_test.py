import requests

def test_get_home():
    url = "http://127.0.0.1:5000/"
    response = requests.get(url)
    print("GET /")
    print("Status Code:", response.status_code)
    print("Response Body:", response.text)

def test_post_coordinates():
    url = "http://127.0.0.1:5000/api/coordinates"
    # 测试缺少数据的情况
    data = {}
    response = requests.post(url, json=data)
    print("\nPOST /api/coordinates with missing data")
    print("Status Code:", response.status_code)
    print("Response Body:", response.json())
    
    # 测试正常的数据传输
    data = {"latitude": 39.91, "longitude": 116.30}
    response = requests.post(url, json=data)
    print("\nPOST /api/coordinates with valid data")
    print("Status Code:", response.status_code)
    print("Response Body:", response.json())

if __name__ == "__main__":
    test_get_home()
    test_post_coordinates()
