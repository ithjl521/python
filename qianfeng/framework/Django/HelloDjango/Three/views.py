from django.db.models import Max, F, Q
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
# Create your views here.
from Three.models import User, Order, Grade, Customer, Company, Animal


def index(request):

    three_index = loader.get_template('three_index.html')
    result = three_index.render()
    print(result)
    return HttpResponse(result)


def get_user(request):
    username = 'bug'
    password = 'abcdefg'

    users = User.objects.filter(u_name=username)
    if users.count():
        user = users.first()

        if user.u_password == password:
            print('获取用户信息成功')
        else:
            print('密码错误')
    else:
        print('用户不存在')

    return HttpResponse('获取成功')


def get_users(request):
    users = User.objects.all()[1:3]
    context = {
        'users': users
    }
    return render(request, 'user_list.html', context=context)


def get_orders(request):
    # orders = Order.objects.filter(o_time__year=2018)
    orders = Order.objects.filter(o_time__month=9)

    for order in orders:
        print(order.o_num)

    return HttpResponse('获取订单成功')


def getgrades(request):
    grades = Grade.objects.filter(student__s_name='hjl')
    for grade in grades:
        print(grade.g_name)
    return HttpResponse('获取成功')


def getcustomer(request):
    result = Customer.objects.aggregate(Max('c_cost'))
    print(result)
    return HttpResponse('获取花费成功')


def getcompany(request):
    # F对象可以获取属性的值，可以实现一个模型的不同属性的运算操作，还可以支持算术运算
    # companies = Company.objects.filter(c_boy_num__lt=F('c_girl_num'))
    # companies = Company.objects.filter(c_boy_num__lt=F('c_girl_num')-5)

    # Q对象可以对既有查询条件进行封装，封装之后，可以支持逻辑运算
    # companies = Company.objects.filter(c_boy_num__gt=1).filter(c_girl_num__gt=5)
    companies = Company.objects.filter(Q(c_boy_num__gt=1) & Q(c_girl_num__gt=5))

    for company in companies:
        print(company.c_name)
    return HttpResponse('获取公司成功')


def getanimals(request):
    animals = Animal.objects.all()

    for animal in animals:
        print(animal.a_name)

    return HttpResponse('动物获取成功')