import opencage, math, json, urllib.request

class WeatherData:

    def __init__(self,coordinates):
        data = get_json(parse_coordinates(coordinates))
        self.current = self.Current(data)
        self.forecasts = {}
        for forecast in range(7):
            self.forecasts[forecast] = self.Forecast(data,forecast)

    def __str__(self):
        return('' + str(self.current) + ' \n'
               '' + str(list((self.forecasts).values())) + ' \n')
        

    class Current:
        def __init__(self, data):
            self.temperature = get_temperature(data)
            self.temperature_apparent = get_temperature_apparent(data)
            self.temperature_min = get_temperature_min(data)
            self.temperature_max = get_temperature_max(data)
            self.weather_classification = get_weather_classification(data)
            self.wind_speed = get_wind_speed(data)
            self.wind_direction = get_wind_direction(data)
            self.precipitation_chance = get_precipitation_chance(data,0)

        def __str__(self):
            return ('Temperature: ' + str(self.temperature) + ' \n'
                    'Apparent Temperature: ' + str(self.temperature_apparent) + ' \n'
                    'Min Temperature: ' + str(self.temperature_min) + ' \n'
                    'Max Temperature: ' + str(self.temperature_max) + ' \n'
                    'Weather Classification: ' + self.weather_classification + ' \n'
                    'Wind Speed: ' + str(self.wind_speed) + ' \n'
                    'Wind Direction: ' + str(self.wind_direction) + ' \n'
                    'Precipitation Chance: ' + str(self.precipitation_chance) + ' \n')

    class Forecast:
        def __init__(self, data, day):
            self.date = get_date(data, day)
            self.temperature_min = get_temperature_min(data,day)
            self.temperature_max = get_temperature_max(data,day)
            self.weather_classification = get_weather_classification(data,False, day)
            self.precipitation_chance = get_precipitation_chance(data,day)

        def __repr__(self):
            return ('Date: ' + self.date + ' \n'
                    'Min Temperature: ' + str(self.temperature_min) + ' \n'
                    'Max Temperature: ' + str(self.temperature_max) + ' \n'
                    'Weather Classification: ' + self.weather_classification + ' \n'
                    'Precipitation Chance: ' + str(self.precipitation_chance) + ' \n')

def get_temperature(data):
    return data['current']['temperature_2m']

def get_temperature_apparent(data):
    return data['current']['apparent_temperature']

def get_temperature_min(data, day = 0):
    return data['daily']['temperature_2m_min'][day]

def get_temperature_max(data,day = 0):
    return data['daily']['temperature_2m_max'][day] 

def get_weather_classification(data, current = True, day = 0):
    code = None
    if current:
        code = str(data['current']['weather_code'])
    else:
        code = str(data['daily']['weather_code'][day])

    match code:
        case '0':
            return 'Clear'
        case '1':
            return 'Mostly Clear'
        case '2':
            return 'Partly Cloudy'
        case '3':
            return 'Overcast'
        case '45' | '48':
            return 'Fog'
        case '51' | '53' | '55':
            return 'Drizzle'
        case '56' | '57':
            return 'Freezing Drizzle'
        case '61' | '80':
            return 'Light Rain'
        case '63' | '81':
            return 'Rain'
        case '65' | '82':
            return 'Heavy Rain'
        case '66' | '67':
            return 'Freezing Rain'
        case '71' | '85':
            return 'Light Snow'
        case '73':
            return 'Snow'
        case '75' | '86':
            return 'Heavy Snow'
        case '77':
            return 'Snow Grains'
        case '95':
            return 'Thunderstorm'
        case '96' | '99':
            return 'Hailstorm'

    
def get_wind_speed(data):
    return data['current']['wind_speed_10m']

def get_wind_direction(data):
    wind_direction_num = data['current']['wind_direction_10m']
    angle = str(math.ceil(wind_direction_num / 30 ))

    match angle:
        case '1' | '12':
            return 'N'
        case '2':
            return 'NE'
        case '3' | '4':
            return 'E'
        case '5':
            return 'SE'
        case '6' | '7':
            return 'S'
        case '8':
            return 'SW'
        case '9' | '10':
            return 'W'
        case '11':
            return 'NW'
        case other:
            return 'N'

def get_date(data, day):
    return data['daily']['time'][day]

def get_precipitation_chance(data, day):
    return data['daily']['precipitation_probability_max'][day]

def parse_coordinates(coordinates):
    return coordinates.split(',')

def valid_data(data):
    if 'error' not in data:
        return True
    return False

def get_json(lat_and_lon):
    lat = lat_and_lon[0]
    lon = lat_and_lon[1]
    web_address = 'https://api.open-meteo.com/v1/forecast?latitude=' + lat + '&longitude=' + lon + '&current=temperature_2m,apparent_temperature,weather_code,wind_speed_10m,wind_direction_10m&daily=weather_code,temperature_2m_max,temperature_2m_min,precipitation_probability_max&temperature_unit=fahrenheit&wind_speed_unit=mph&precipitation_unit=inch&timezone=auto'
    with urllib.request.urlopen(web_address) as url:
        data = json.load(url)
        return data
