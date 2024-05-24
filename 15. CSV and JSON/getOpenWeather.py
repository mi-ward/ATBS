#! python3
# getOpenWeather.py - Prints the weather for a location from the command line.

import os, json, requests, sys

APPID = os.environ['OPEN_WEATHER_APP_ID']

# Compute location from command line arguments.

if len(sys.argv) < 2:
    print('Usage: getOpenWeather.py city_name, 2-letter_state_code, 2-letter_country_code')
    sys.exit()
    
location = ','.join(sys.argv[1:])

# Retrieve lat and lon from API``
location_url = 'http://api.openweathermap.org/geo/1.0/direct?' \
                'q=%s&appid=%s' \
                % (location, APPID)
                
location_res = requests.get(location_url)
location_res.raise_for_status()
location = location_res.json()
lat = location[0]['lat']
lon = location[0]['lon']


# Download the JSON data from OpenWeatherMap.org's API
url = 'https://api.openweathermap.org/data/2.5/forecast?lat=%s&lon=%s&appid=%s' \
       % (lat, lon, APPID)
       
response = requests.get(url)
response.raise_for_status()

# Uncomment to see the raw JSON text:
#print(response.text)

# Load JSON data into a Python variable.
weatherData = json.loads(response.text)

# Print weather descriptions.
w = weatherData['list']

print('Current weather is in %s, %s:' % (location[0]['name'], location[0]['state']))
print(w[0]['weather'][0]['main'], '-', w[0]['weather'][0]['description'])
print()
print('Tomorrow:')
print(w[1]['weather'][0]['main'], '-', w[1]['weather'][0]['description'])
print()
print('Day after tomorrow:')
print(w[2]['weather'][0]['main'], '-', w[2]['weather'][0]['description'])

