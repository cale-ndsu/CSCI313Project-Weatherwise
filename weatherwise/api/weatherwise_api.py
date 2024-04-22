import opencage

def get_location_data(query):
    """
    query (string) - a phrase used for getting coordinates and other location data for a place through the OpenCage API
    """
    return opencage.LocationData(query)
    """
    Use (with example variable location):

    location.coordinates -  string for coordinates

    location.name - string for proper location name

    location.is_night - boolean representing time of day (day or night)

    Example Usage
    location = get_location_data('Fargo')
    print(location)

    """