import requests
import os
from twilio.rest import Client
from dotenv import load_dotenv
load_dotenv()

MY_LAT = -36.8174267379405
MY_LONG = 174.59438583907396
api_key = os.environ.get('API_KEY')
account_sid = 'AC0e5a8aba827afacce0ad93f317763557'
auth_token = os.environ.get('AUTH_TOKEN')

parameters = {
    'lat': MY_LAT,
    'lon': MY_LONG,
    'appid': api_key,
}
response = requests.get('https://api.openweathermap.org/data/2.5/forecast', params=parameters)
response.raise_for_status()
data = response.json()
my_weather_list = (data['list'][3:7])
rain = False
for weather in my_weather_list:
    condition_code = (weather['weather'][0]['id'])
    if int(condition_code) < 700:
        rain = True
if rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body='Take an Umbrella ☔️',
        from_='+17622485658',
        to='+64223827851',
    )

    print(message.status)
    print('☔️')

else:
    print('☀️')
















