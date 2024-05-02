import opencage_key, json, requests, os 
KEY = opencage_key.get_key()

class LocationData:
    def __init__(self, query):
        data = get_json(query)
        if valid_data(data) == False:
            self.coordinates = "N/A,N/A"
            self.name = ""
            self.is_night = False
        else:
            self.coordinates = self.get_coordinates(data)
            self.name = self.get_name(data)
            self.is_night = self.get_time(data)

    def __str__(self):
        return ("Coordinates: " + self.coordinates + " \n"
                "Name: " + self.name + " \n"
                "Is Night: " + str(self.is_night) + " \n")
        
    def get_coordinates(self,data):
        coordinate_str = str(data['results'][0]['geometry']['lat']) + "," + str(data['results'][0]['geometry']['lng'])
        return coordinate_str

    def get_name(self,data):
        return data['results'][0]['formatted']

    def get_time(self, data):
        UNIX_LENGTH_OF_DAY = 86400
        current_time = self.get_timestamp(data)
        sunrise = self.get_sunrise(data)
        sunset = self.get_sunset(data)
        if sunrise > sunset: # when API reponse for sunrise is bugged (e.g. see Fargo)
            day_length = (UNIX_LENGTH_OF_DAY - ( sunrise - self.get_sunset(data) ))
            if sunrise > current_time:
                sunrise = sunset - day_length
            else:         
                sunset = sunrise + day_length
        
        if sunrise <= current_time <= sunset:
            return False
        else:
            return True

    def get_timestamp(self, data):
        return data['timestamp']['created_unix']

    def get_sunrise(self,data):
        return data['results'][0]['annotations']['sun']['rise']['civil']

    def get_sunset(self,data):
        return data['results'][0]['annotations']['sun']['set']['civil']


def format_query(query):
    return query.replace(" ", "+")

def valid_data(data):
    if  data['total_results'] > 0:
        return True
    return False

def get_json(query):
    query = format_query(query)
    web_address = 'https://api.opencagedata.com/geocode/v1/json?q=' + query + '&key=' + KEY + '&language=en&pretty=1'
    r = requests.get(web_address)
    data = r.json()
    return data

