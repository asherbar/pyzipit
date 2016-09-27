import io
import json
import os
import urllib.request

from zip_by_address.address import Address


class AddressByCoordinatesResolver:
    _GM__REVERSE_JSON_ADDRESS = 'https://maps.googleapis.com/maps/api/geocode/json?&latlng'

    def __init__(self, language='en', latitude=-1, longitude=-1):
        self.language = language
        self.latitude = latitude
        self.longitude = longitude

    def resolve_address(self):
        request_url = '{}={},{}&key={}&language={}'.format(
            self._GM__REVERSE_JSON_ADDRESS, self.latitude, self.longitude, os.environ['GOOGLE_MAPS_API_KEY'],
            self.language)
        with urllib.request.urlopen(request_url) as response, \
                io.TextIOWrapper(response, encoding=response.headers.get_content_charset('utf-8')) as f:
            result = json.load(f)
        if result['status'] != 'OK':
            raise RuntimeError('Unable to get address from coordinates ({}, {}). Request ended with status {}'.format(
                self.latitude, self.longitude, result['status'])
            )
        address_components = result['results'][0]['address_components']
        country, state, city, street, street_number = [''] * 5
        for component in address_components:
            if 'street_number' in component['types']:
                street_number = int(component['long_name'].split('-')[0])
            elif 'route' in component['types']:
                street = component['long_name']
            elif 'locality' in component['types']:
                city = component['long_name']
            elif 'administrative_area_level_1' in component['types']:
                state = component['long_name']
            elif 'country' in component['types']:
                country = component['long_name']
        return Address(country, state, city, street, street_number)
