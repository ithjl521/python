from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def students(request):
    return render(request, 'two_students.html')


def student(request, s_id):
    print(s_id)
    return HttpResponse('get student success')


def get_time(request, s, m, h):
    return HttpResponse('time%s:%s:%s' % (h, m, s))


def learn(request):
    return HttpResponse('namespace two')


def have_request(request):
    print(request.path)
    print(request.method)
    print(request.GET)
    print(request.POST)
    print(request.META)
    return HttpResponse('Request Success')