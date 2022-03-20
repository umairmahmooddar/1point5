from http.client import responses
import json
from django.http import HttpRequest, JsonResponse
from django.shortcuts import render
from django.http import HttpResponse
import requests

from common.responseClass import ResponseClass

from .api import ManageWeatherData


# Create your views here.

def get_data(request):

    requestData = {}
    requestData['meta'] = request.META
    requestData['body'] = request.body.decode('utf-8')
    resultResponse = ResponseClass()
    receivedRequest = '[]'

    
    try:
        #response = requests.get('https://www.metoffice.gov.uk/pub/data/weather/uk/climate/datasets/Tmax/date/East_Anglia.txt')
        
        receivedRequest = request.body.decode('utf-8')
        jsonObj = json.dumps(receivedRequest)

        #I am assuming that these values are coming from the frontend while calling the api to get specifc results
        #forexample: Sending the type of order, Region and Param.
    
        order = jsonObj['orderId']
        region = jsonObj['region']
        param = jsonObj['param']

        paramObj = {}
        paramObj["order"] = order
        paramObj["region"] = region
        paramObj["param"] = param

        weatherdata = ManageWeatherData()
        weatherDataDetails = weatherdata.getWeatherDataDetail(paramObj)


        objResult = dict()
        objResult["weatherDataDetails"] = weatherDataDetails
        return JsonResponse(objResult.toJson())
    
    except Exception as ex:
            resultResponse.set_display_message("error message")
            resultResponse.set_display_message_code("error code")
            return JsonResponse(resultResponse.toJson())