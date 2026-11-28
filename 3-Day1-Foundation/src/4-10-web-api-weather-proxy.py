#
# file : 4-10-web-api-weather-proxy.py
# 機能： WebAPI　OpenWeatherProxyを経由して、OpenWeatherが提供する天気予報を取得する
#
import urequests
BASE_URL='https://287vqq2f1a.execute-api.ap-northeast-1.amazonAAA.com/default/OpenWeatherProxy'

LOCATION=(35.7388919, 139.4607429)
API_KEY='0123aabbbccc'

lat, lon = LOCATION
request_url = f"{BASE_URL}?lat={lat}&lon={lon}&api_key={API_KEY}"
response = urequests.get(request_url)

if response.status_code == 200:
    data = response.json()
    print("city:", data.get("name"))
    print("weather:", data["weather"][0]["description"])
    print("temp:", data["main"]["temp"], "C")
    print("hum:", data["main"]["humidity"], "%")
    print("wind:", data["wind"]["speed"], "m/s")
else:
    print("error:", data)
