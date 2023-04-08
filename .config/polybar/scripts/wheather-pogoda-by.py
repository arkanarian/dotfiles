#!/home/imaksus/.config/polybar/scripts/venv/bin/python
import requests
import json
import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument('--temp', action="store_true")
parser.add_argument('--wind', action="store_true")
parser.add_argument('--sunset', action="store_true")
parser.add_argument('--get_icon_temp', action="store_true")
args = parser.parse_args()

try:
    # 26851 - Минск-Независимости
    # 26850 - Минск-Уручье
    response = requests.get('https://pogoda.by/api/v2/weather-fact?station=26850')
    content = json.loads(response.content.decode())
    if args.temp:
        temperature = str(content['t'])
        print(temperature + " °C")
    if args.wind:
        speedWind = str(content['speedWind'])
        print(speedWind + " m/s")
    if args.sunset:
        response = requests.get('https://api.sunrise-sunset.org/json?lat=53.93&lng=27.64&date=today')
        content = json.loads(response.content)
        results = content['results']
        sunrise = results['sunrise'].split(':')
        sunset = results['sunset'].split(':')
        sunrise_str = f"{int(sunrise[0])+3}:{sunrise[1]}"
        sunset_str = f"{int(sunset[0])+15}:{sunset[1]}"
        print(sunrise_str + "-" + sunset_str)
    if args.get_icon_temp:
        import re

        from test_weather import content
        #content = 'https://pogoda.by/assets/icons-weather/wi_day_2.png'
        #name = re.match(r'[/].*[\.]png$', content)
        name = re.search(r'/wi.*\.', content).group()
        time = re.search(r'_.*_', name).group()[1:-1]
        from datetime import datetime
        if datetime.now().strftime("%H") in ["00", "01", "02"]:
            time = "night"
        type = re.search(r'_\d*\.', name).group()[1:-1]
        if time == "day":
            if type == "1":
                print("")
            elif type == "2":
                print("")
            elif type == "3" or type == "14" or type == "17":
                print("")
            else:
                print("")
        else:
            if type == "1":
                print("")
            elif type == "2":
                print("")
            elif type == "3":
                print("")
            elif type == "5":
                print("")
            else:
                print("")
        print(type)
        print(time)


        #from datetime import datetime
        #now = datetime.now()
        #current_hours = int(now.strftime("%H"))
        #current_minutes = int(now.strftime("%m"))
        #response = requests.get('https://api.sunrise-sunset.org/json?lat=53.93&lng=27.64&date=today')
        #content = json.loads(response.content)
        #sunset_hour = int(content['results']['sunset'].split(':')[0]) + 15
        #sunset_minute = int(content['results']['sunset'].split(':')[1])
        #if current_hours < sunset_hour:
        #    print("")
        #else:
        #    print("")
except Exception as e:
    print("-")
    print(e)
    exit(0)
