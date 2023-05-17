from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import ToDoList, Item
import requests
import json
import xmltodict
from xml.etree import ElementTree
# Create your views here.


def index(response, id):
    ls = ToDoList.objects.get(id=id)
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

    # Find the desired currency rates
    for cube in root.iter('{http://www.bnr.ro/xsd}Rate'):
        currency = cube.attrib.get('currency')
        rate = cube.text
        currencies[currency] = rate


    
    return JsonResponse(currencies, safe=False)
