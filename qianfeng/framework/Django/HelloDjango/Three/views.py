from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
# Create your views here.


def index(request):

    three_index = loader.get_template('three_index.html')
    result = three_index.render()
    print(result)
    return HttpResponse(result)
