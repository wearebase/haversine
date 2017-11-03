from math import radians, cos, sin, asin, sqrt, atan2

AVG_EARTH_RADIUS = 6371  # in km


def haversine(point1, point2, miles=False, bearing=False):
    """ Calculate the great-circle distance between two points on the Earth surface.

    :input: two 2-tuples, containing the latitude and longitude of each point
    in decimal degrees.

    Example: haversine((45.7597, 4.8422), (48.8567, 2.3508))

    :output: Returns the distance between the two points.
    The default unit is kilometers. Miles can be returned
    if the ``miles`` parameter is set to True. Bearing can additionally
    be returned if the ``bearing`` parameter is set to True.

    """
    # unpack latitude/longitude
    lat1, lng1 = point1
    lat2, lng2 = point2

    # convert all latitudes/longitudes from decimal degrees to radians
    lat1, lng1, lat2, lng2 = map(radians, (lat1, lng1, lat2, lng2))

    # calculate haversine
    lat = lat2 - lat1
    lng = lng2 - lng1
    d = sin(lat * 0.5) ** 2 + cos(lat1) * cos(lat2) * sin(lng * 0.5) ** 2
    h = 2 * AVG_EARTH_RADIUS * asin(sqrt(d))  # in kilometers

    if miles:
        h = h * 0.621371  # in miles

    if bearing:
        y = sin(lng) * cos(lat2);
        x = cos(lat1) * sin(lat2) - sin(lat1) * cos(lat2) * cos(lng);
        bearing = atan2(y, x)  # in radians
        return h, bearing

    return h
