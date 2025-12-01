# WebAPIを呼び出す

### Internet上のWebService

Internet上にはいろんなWebAPIが存在し、いろんなサービスを提供しています。無料で使えるサービスや、有料のサービスもあります。マイコンによるWebAPI活用の事例として、生活に役立つ情報を提供しているWebAPIを呼び出し、情報を提示したり、得られた情報に基づいて家電機器を制御することが考えられます。

### openweather

WebAPIの一例として世界の気象情報を取得できるOpenWeatherというサービスを紹介します。サイトのURLは以下です

https://openweathermap.org/

OpenWeatherでは、地点を指定してAPIを呼び出すことで地点の気象情報を得ることができます。気象情報を取得する以外に、＃＃、＃＃、＃＃等の情報が取得できます。使い方は、まずOpenWeatherのサイトにアカウントを登録し、APIを利用するための鍵を発行します。生成されたAPI鍵を用いて目的に応じたAPIにアクセスします。例えば、地点（緯度、経度）を指定して天気を取得する場合は以下となります。ここでAPI鍵は仮に12345678abcdefg とします
```
https://api.openweathermap.org/data/2.5/weather?lat=35.7388919&lon=139.4607429&appid=12345678abcdefg
```
lat=35.7388919&lon=139.4607429とは、職業大様の正門の位置です

例えば、CURLコマンドを使ってアクセスすると以下の情報が得られます。（鍵は置換しています）

```
$ curl  'https://api.openweathermap.org/data/2.5/weather?lat=35.7388919&lon=139.4607429&appid=12345678abcdefg' | jq

{
  "coord": {
    "lon": 139.4607,
    "lat": 35.7389
  },
  "weather": [
    {
      "id": 800,
      "main": "Clear",
      "description": "clear sky",
      "icon": "01n"
    }
  ],
  "base": "stations",
  "main": {
    "temp": 285.76,
    "feels_like": 284.54,
    "temp_min": 285.13,
    "temp_max": 288.9,
    "pressure": 1015,
    "humidity": 56,
    "sea_level": 1015,
    "grnd_level": 1006
  },
  "visibility": 10000,
  "wind": {
    "speed": 2.06,
    "deg": 340
  },
  "clouds": {
    "all": 0
  },
  "dt": 1764589970,
  "sys": {
    "type": 2,
    "id": 2009679,
    "country": "JP",
    "sunrise": 1764538409,
    "sunset": 1764574144
  },
  "timezone": 32400,
  "id": 7279570,
  "name": "Higashimurayama",
  "cod": 200
}
```
上記応答文字列中の、weather/main, weather/descriptionが現在の天候です
C-Pythonで書くと以下となります。
```
import requests
BASE_URL='https://api.openweathermap.org/data/2.5/weather'

LOCATION=(35.7388919, 139.4607429)
API_KEY='12345678abcdefg'            # <<<環境変数から取得すべき

# リクエスト送信
lat, lon = LOCATION
request_url = f"{BASE_URL}?lat={lat}&lon={lon}&appid={API_KEY}&units=metric&lang=ja"
response = requests.get(request_url)

# 結果を表示
if response.status_code == 200:
    # レスポンスをJSON形式で取得
    data = response.json()
    print("都市名:", data.get("name"))
    print("天気:", data["weather"][0]["description"])
    print("気温:", data["main"]["temp"], "C")
    print("湿度:", data["main"]["humidity"], "%")
    print("風速:", data["wind"]["speed"], "m/s")
else:
    print("エラー:", data)

```
上記コードを実行すると以下となります。(見出しの漢字を英語に換えています)
```
$ python3 weathertest.py
city: 東村山市
weather: 晴天
temp: 13 C
hum: 55 %
wind: 3.09 m/s
```
MicroPythonでも同様にrequestsモジュールが提供されており、ほぼ同じようなソースコードでAPIを呼び出すことができます。
MicroPython版天気情報取得プログラム
```
import urequests
BASE_URL='https://api.openweathermap.org/data/2.5/weather'

LOCATION=(35.7388919, 139.4607429)
API_KEY='12345678abcdefg'


lat, lon = LOCATION
request_url = f"{BASE_URL}?lat={lat}&lon={lon}&appid={API_KEY}&units=metric&lang=ja"
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
```
実行結果は以下です
```
city: Kodaira
weather: 晴天
temp: 13.15 C
hum: 53 %
wind: 3.09 m/s
```
APIの呼び出し時、lang=jaと設定しているので晴天と漢字で返却されています。APIキーは共用できないので、皆さんがWeatherAPIを呼び出す際は、各自でAPIキーを取得してAPIを呼び出してください。

なお、今回研修用にAWS上でWeatherAPI Proxyを構築しております。WeatherAPIを利用するためのキーの取得が困難な場合は、研修用のWeatherAPI Proxyをご利用ください。
研修用Weather APIのURLと呼び出し方は以下の通りです
```
https://287vqq2f1a.execute-api.ap-northeast-1.amazonAAA.com/default/OpenWeatherProxy?lat=<lat>&lon=<lon>&api_key=<api_key>
```
api_keyは研修の際にお伝えします。応答JSONはWeatherAPIの仕様と同じです。マイコンからの利用を想定して応答文字コードはen(English)を指定しています
MicroPythonからの呼び出し例は以下です
```
import urequests
BASE_URL='https://287vqq2f1a.execute-api.ap-northeast-1.amazonAAA.com/default/OpenWeatherProxy'

LOCATION=(35.7388919, 139.4607429)
API_KEY='12345678abcdefg'

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
```
RP2で実行した結果は以下です
```
city: Higashimurayama
weather: clear sky
temp: 12.88 C
hum: 54 %
wind: 3.09 m/s
```
