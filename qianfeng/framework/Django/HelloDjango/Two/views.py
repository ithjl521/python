import base64
import os
import random
from time import sleep

from django.core.cache import caches
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse
from django.views.decorators.cache import cache_page
from django.views.decorators.csrf import csrf_exempt

from Two.models import Student


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


def hello_response(request):
    response = HttpResponse()

    # response.status_code(404)
    # response.content = 'this is content'
    response.write('hello response')

    return response


def getticket(request):
    if random.randrange(10) > 5:
        url = reverse('two:response')
        print(url)
        # 重定向
        # return HttpResponseRedirect(url)  # 临时 302
        return redirect(url)

    return HttpResponse('未重定向')


def get_info(request):
    data = {
        'status': 200,
        'msg': 'success',
    }
    return JsonResponse(data=data)


def set_cookie(request):
    response = HttpResponse('设置cookie')
    # response.set_cookie('username', 'hjl', max_age=60)
    response.set_signed_cookie('content', 'this is content')

    return response


def get_cookie(request):
    # username = request.COOKIES.get('username')
    content = request.get_signed_cookie('content')
    return HttpResponse(content)


def set_session(request):
    # 默认过期时间14天
    request.session['username'] = 'session username'
    return HttpResponse('session设置成功')


def get_session(request):
    session_username = request.session.get('username')
    return HttpResponse(session_username)


def register(request):
    if request.method == 'GET':
        return render(request, 'student_register_two.html')
    elif request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            student = Student()
            student.s_name = username
            student.s_password = password

            student.save()
        except Exception as e:
            return redirect(reverse('two:register'))

        return HttpResponse('register success')


def login(request):
    if request.method == 'GET':
        return render(request, 'student_login_two.html')
    elif request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        students = Student.objects.filter(s_name=username).filter(s_password=password)
        if students.exists():
            token = base64.b32encode(os.urandom(20))  # 二进制

            student = students.first()
            student.s_token = token
            student.save()

            # response = HttpResponse('login success')
            # response.set_cookie('token', token)
            #
            # return response
            data = {
                'status': 200,
                'msg': 'ok',
                'token': str(token)
            }
            return JsonResponse(data=data)

        data = {
            'status': 600,
            'msg': 'error',
        }
        return JsonResponse(data=data)


def mine(request):
    token = request.COOKIES.get('token')

    try:
        student = Student.objects.get(s_token=token)
    except Exception as e:
        data = {
            'status': 600,
            'msg': 'error',
        }
        return JsonResponse(data=data)

    data = {
        'status': 200,
        'msg': 'ok',
        'data': {
            'username':student.s_name
        }
    }
    return JsonResponse(data=data)

# 豁免CSRF
@csrf_exempt
def upload_file(request):
    if request.method == 'GET':
        return render(request, 'upload.html')
    elif request.method == 'POST':
        icon = request.FILES.get('icon')

        with open(r'C:\Users\jiuzhou\Desktop\python\qianfeng\framework\Django\HelloDjango\static\img\icon.jpg', 'wb') as fp:
            for part in icon.chunks():
                fp.write(part)
                fp.flush()

        return HttpResponse('上传成功')


# @cache_page(timeout=30,cache='redis_backend')
@cache_page(timeout=30)
def news(request):
    # cache = caches['redis_backend']
    # result = cache.get('news')
    # if result:
    #     return HttpResponse(result)

    news_list = []

    for i in range(10):
        news_list.append('区块链火了%d' % i)

    sleep(3)

    data = {
        'news_list': news_list,
    }

    response = render(request, 'news.html', context=data)
    # try:
    # cache.set('news', response.content)
    # except Exception as e:
    #     return HttpResponse('error')

    return response
