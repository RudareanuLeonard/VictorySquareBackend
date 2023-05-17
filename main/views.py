from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Currency
import requests
import json
import xmltodict
from xml.etree import ElementTree
# Create your views here.


def index(response):
    # ls = ToDoList.objects.get(id=id)
    return render(response, "main/base.html")

def home(response):
        # ls = ToDoList.objects.all()
        return render(response, "main/home.html")

def api_data_view(request):
    url = 'https://www.bnr.ro/nbrfxrates.xml'
    response = requests.get(url)
    data = response.content.decode('utf-8')
    # xml_data = xmltodict.parse(data)
    
    # return JsonResponse(xml_data, safe=False)

    root = ElementTree.fromstring(data)

    currencies = {}

    Currency.objects.all().delete()
    #  Save currency rates to the database
    for cube in root.iter('{http://www.bnr.ro/xsd}Rate'):
        currency = cube.attrib.get('currency')
        rate = cube.text
        
        current_currency = Currency(currency=currency, rate=rate)
        current_currency.save()

    # Retrieve currency items from the database
    currencies = Currency.objects.values('currency', 'rate')

    return JsonResponse(list(currencies), safe=False)
