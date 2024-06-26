import googlemaps
import pandas as pd

class GoogleMapSearch:
    def __init__(self, location, radius):
        self._gmaps = googlemaps.Client(key="AIzaSyCSelvx9eoEgQT8stZFa6mCfovKmPMVrN4")
        self._location = location
        self._radius = radius
        self.result = []
    
    def get_info(self):
        search_result = self._gmaps.places_nearby(self._location, self._radius, type="restaurant", language="zh-TW")
        for place in search_result['results']:
            self.result.append(place)
        self.result = pd.DataFrame.from_dict(self.result)