from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from HelloModel.models import Person, IDcard


def hello(request):
    return HttpResponse('hello')


def addperson(request):
    username = request.GET.get('username')
    person = Person()
    person.p_name = username
    person.save()

    return HttpResponse('人创建成功%d' % person.id)


def addidcard(request):
    id_num = request.GET.get('id_num')
    idcard = IDcard()
    idcard.id_num = id_num
    idcard.save()

    return HttpResponse('IDcard创建成功%d' % idcard.id)


def bindcard(request):
    person = Person.objects.last()
    idcard = IDcard.objects.last()

    idcard.id_person = person.id
    idcard.save()
    return HttpResponse('绑定成功')


def removeperson(request):
    person = Person.objects.last()
    person.delete()

    return HttpResponse('删除人员成功')


def removeidcard(request):
    idcard = IDcard.objects.last()
    idcard.delete()
    return HttpResponse('身份证删除成功')


def getpersonbycard(request):
    idcard = IDcard.objects.last()
    person = idcard.id_person
    print(person)
    return HttpResponse(person.p_name)


def getidcardbyperson(request):
    person = Person.objects.last()

    idcard = person.idcard

    return HttpResponse(idcard.id_num)