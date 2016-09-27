import requests


class AddressByCoordinatesResolver:
    def __init__(self):
        self.latitude = -1
        self.longitude = -1

    def resolve_address(self):
        _GM__REVERSE_JSON_ADDRESS = 'https://maps.googleapis.com/maps/api/geocode/json?latlng'
        requests.get(
            '%s=32.1091841,34.8354139&key=AIzaSyCds4p3MBAOso2f1cJ-yRo3t-S3nUQNRIM&result_type=street_address&language=he' % _GM__REVERSE_JSON_ADDRESS)
