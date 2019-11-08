from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView

from App.models import Book


class HelloView(View):

    def get(self, request):
        return render(request, 'hello.html')

    def post(self, request):
        data = {
            'status': 200,
        }

        return JsonResponse(data=data)


class HelloTemplateView(TemplateView):
    template_name = 'hello.html'


class HelloListView(ListView):
    template_name = 'book_list.html'
    model = Book


class HelloDetailView(DetailView):
    template_name = 'book.html'
    model = Book
