""" Handle the geocoding logic with Google Maps Geocoding API """
import requests

from .constant import API_URL_GEOCODING


class GeocodingApi:
    """Request data from the geocoding api"""

    def __init__(self):
        self.payload = {"language": "fr", "address": request_location}
        self.r = requests.get(API_URL_GEOCODING, params=self.payload).json()

    def get_location_information(self):
        """Get the useful information for a given location

        Returns:
            str: Title of the request
        """
        city_name = self.r["results"][0]["address_components"][0]["long_name"]
        county = self.r["results"][0]["address_components"][2]["long_name"]
        lattitude = self.r["results"][0]["geometry"]["location"]["lat"]
        longitude = self.r["results"][0]["geometry"]["location"]["lng"]
        return city_name, county, lattitude, longitude


if __name__ == "__main__":
    pass
