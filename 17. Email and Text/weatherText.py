#! python

import os, requests
from pprint import pprint

API_TOKEN=os.environ['PUSHOVER_API_KEY']
USER_KEY=os.environ['PUSHOVER_USER_KEY']
EMAIL=os.environ['EMAIL']


url = 'https://api.weather.gov/'
headers = {'user-agent': EMAIL}

#health-check
res = requests.get(url, headers=headers)
res.raise_for_status()

lat_lon = ','.join(['40.726260', '-73.944310'])


#station information
points_url = url + '/points/' + lat_lon
res = requests.get(points_url, headers=headers)
response_data = res.json()

#retrieve forecast information
forecast_url = response_data['properties']['forecast']

res = requests.get(forecast_url, headers=headers)
response_data = res.json()
forecast = response_data['properties']['periods'][0]['shortForecast']

def sendPushNotification(message):
    push_params = {
        'token': API_TOKEN,
        'user': USER_KEY,
        'message': message,
        'device': 'iphone'
    }
    res = requests.post(push_url, params=push_params)
    

push_url = 'https://api.pushover.net/1/messages.json'

if 'Showers' in forecast:
    message = "Bring an umbrella"
    sendPushNotification(message)
    






