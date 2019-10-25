import random

from django.http import HttpResponse

# Create your views here.
from django.shortcuts import render

from App.models import Student


def hello(request):
    return HttpResponse('hello django')


def tags(request):
    return HttpResponse('<h2>low</h2>')


def index(request):
    return render(request, 'index.html')


def home(request):
    return render(request, 'home.html')


def other_urls(request):
    return HttpResponse("other urls")


def add_student(request):
    student = Student()
    student.s_name = 'jerry %d' % random.randrange(100)
    student.s_age = 38
    student.save()

    return HttpResponse('Add success')


def get_students(request):
    students = Student.objects.all()

    for student in students:
        print(student.s_name)

    # return HttpResponse('students')
    context = {
        'hobby': 'play',
        'eat': 'meat',
        'students': students
    }
    return render(request, 'student_list.html', context=context)


def update_student(request):
    student = Student.objects.get(pk=2)
    student.s_name = 'Bug'
    student.save()

    return HttpResponse('update success')


def delete_student(request):
    student = Student.objects.get(pk=1)
    student.delete()

    return HttpResponse('delete success')