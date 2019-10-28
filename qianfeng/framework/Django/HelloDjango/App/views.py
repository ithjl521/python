import random

from django.http import HttpResponse

# Create your views here.
from django.shortcuts import render

from App.models import Student, Person


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


def add_persons(request):
    for i in range(15):
        person = Person()
        flag = random.randrange(100)
        person.p_name = "tom%d" % i
        person.p_age = flag
        person.p_sex = flag % 2
        person.save()
    return HttpResponse('批量插入成功')


def get_persons(request):
    persons = Person.objects.filter(p_age__gt=18).filter(p_age__lt=80)

    persons_two = Person.filter(p_age__gt=50)
    context = {
        'persons':persons
    }
    return render(request, 'person_list.html', context=context)


def add_person(request):
    # person = Person.objects.create(p_name='sunck', p_age=16, p_sex=True)

    person = Person.create(p_name='jack')
    person.save()

    return HttpResponse('加入一个用户成功')