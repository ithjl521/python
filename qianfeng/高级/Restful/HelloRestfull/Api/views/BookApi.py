from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from Api.models import Book


# Create your views here.


@csrf_exempt
def books(request):
    if request.method == 'GET':
        book_list = Book.objects.all()
        book_list_json = []

        for book in book_list:
            book_list_json.append(book.to_dic())

        data = {
            'status': 200,
            'msg': 'ok',
            'data': book_list_json,
        }
        return JsonResponse(data=data)

    elif request.method == 'POST':
        b_name = request.POST.get('b_name')
        b_price = request.POST.get('b_price')

        book = Book()
        book.b_name = b_name
        book.b_price = b_price
        book.save()

        data = {
            'status': 201,
            'msg': 'crate success',
            'data': book.to_dic(),
        }

        return JsonResponse(data=data, status=201)

@csrf_exempt
def book(request, book_id):
    if request.method == 'GET':
        book_obj = Book.objects.get(pk=book_id)
        data = {
            'status': 200,
            'msg': 'get one success',
            'data': book_obj.to_dic(),
        }

        return JsonResponse(data=data)
    elif request.method == 'DELETE':
        book_obj = Book.objects.get(pk=book_id)
        book_obj.delete()
        data = {
            'status': 204,
            'msg': 'delete success',
            'data': {}
        }

        return JsonResponse(data=data)
