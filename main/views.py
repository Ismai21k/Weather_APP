from django.shortcuts import render
from django.http import HttpResponse
# I add json file to load data to a python dictionary
import json

import urllib.request as urllib


def home(request):
    if request.method == 'POST':
        city = request.POST['city']
        # open weather api
        
        # source contain json data from api

        source = urllib.urlopen(
            'http://api.openweathermap.org/data/2.5/weather?q='
                    + city + '&appid= Use Yor API Here').read()
        
        # converting JSON data to a dictionary
        list_of_data = json.loads(source)
        
        # data for variable list_of_data
        data = {
           "country_code": str(list_of_data['sys']['country']), 
            "coordinate": str(list_of_data['coord']['lon'])  + '  '
                        + str(list_of_data['coord']['lat']), 
            "temp": str(list_of_data['main']['temp']) , 
            "pressure": str(list_of_data['main']['pressure'])  , 
            "humidity": str(list_of_data['main']['humidity'])  , 
        
        }
        print(data)


        return render(request, 'main/index.html', data)
    
    else:
        data = {}
        return render(request, "main/index.html", data)
        
  