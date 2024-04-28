import opencage, open_meteo

def get_location_data(query):
    """
    query (string) - a phrase used for getting coordinates and other location data for a place through the Opencage API
    """

    return opencage.LocationData(query)
    
    """
    Use (with example instance class location):

    location.coordinates -  string for coordinates

    location.name - string for proper location name

    location.is_night - boolean representing time of day (day or night)

    Example Usage
    location = get_location_data('Fargo')
    print(location)

    """

def get_weather_data(coordinates):
    """
    coordinates (string) - coordinates to be used for Open-Meteo API
    """
    return open_meteo.WeatherData(coordinates)
    """
    list of class attributes one can access         (using example instance class weather)

    weather.current.temperature
    weather.current.temperature_apparent            (for wind chill or what it feels like outside)
    weather.current.temperature_min
    weather.current.temperature_max
    weather.current.weather_classification          (string)
    weather.current.wind_speed
    weather.current.wind_direction                  (string)

    weather.forecasts[day].date                     (day is a integer, 0 is current day, 6 is seventh day)
    weather.forecasts[day].temperature_min
    weather.forecasts[day].temperature_max
    weather.forecasts[day].weather_classification   (string)
    weather.forecasts[day].precipitation_chance

    """
