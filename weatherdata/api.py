import json
from django.http import JsonResponse, response
import requests


class ManageWeatherData:

    def __init__(self):
        pass

    def getWeatherDataDetail(self,paramObj):
        
            response = requests.get('https://www.metoffice.gov.uk/pub/data/weather/uk/climate/datasets/'+paramObj["order"]+'/'+paramObj["param"]+'/'+paramObj["region"]+'.txt')
            
            #here I would perform some tasks on the data recieved from the API.
            
            return (response)

