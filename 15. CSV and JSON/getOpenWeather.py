#! python3
# getOpenWeather.py - Prints the weather for a location from the command line.

import os, json, requests, sys

APPID = os.environ['OPEN_WEATHER_APP_ID']


# Compute location from command line arguments.

if len(sys.argv) < 2:
    print('Usage: getOpenWeather.py city_name, 2-letter_country_code')
    sys.exit()
location = ' '.join(sys.argv[1:])

lat = 40.727090
lon = -73.946730

# Download the JSON data from OpenWeatherMap.org's API
url = 'https://api.openweathermap.org/data/2.5/weather?lat=%s&lon=%s&appid=%s' \
       % (lat, lon, APPID)
       
response = requests.get(url)
response.raise_for_status()

#http://api.openweathermap.org/geo/1.0/direct?q={city name},{state code},{country code}&limit={limit}&appid={API key}

# Uncomment to see the raw JSON text:
#print(response.text)

# Load JSON data into a Python variable.
weatherData = json.loads(response.text)

# Print weather descriptions.
w = weatherData
print(w)
import pprint
pprint.pprint(w)
# print('Current weather is in %s:' % (location))
# print(w[0]['weather'][0]['main'], '-', w[0]['weather'][0]['description'])
# print()
# print('Tomorrow:')
# print(w[1]['weather'][0]['main'], '-', w[1]['weather'][0]['description'])
# print()
# print('Day after tomorrow:')
# print(w[2]['weather'][0]['main'], '-', w[2]['weather'][0]['description'])

