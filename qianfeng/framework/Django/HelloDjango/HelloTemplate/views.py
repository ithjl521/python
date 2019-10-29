from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from HelloTemplate.models import Student


def hello(request):
    return HttpResponse('hello')


def get_students(request):
    students = Student.objects.all()

    context = {
        'students': students,
        'code': '<h2>code</h2>'
    }
    return render(request, 'students.html', context=context)


def home(request):
    return render(request, 'tmp_home.html',context={'title': 'home'})


def home_mine(request):
    return render(request, 'home_mine.html')