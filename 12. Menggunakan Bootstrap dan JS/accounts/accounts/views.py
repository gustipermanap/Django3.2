from django.shortcuts import render
from django.http import HttpResponse


def dashboard(request):
    return render(request, 'dashboard.html')


def products(request):
    return render(request, 'products.html')


def customer(request):
    return render(request, 'customer.html')


def navbar(request):
    return render(request, 'navbar.html')


def main(request):
    return render(request, 'main.html')


def status(request):
    return render(request, 'status.html')

# def home(request):
#     return HttpResponse('Halaman Home')


# def products(request):
#     return HttpResponse('Halaman Products')


# def customer(request):
#     return HttpResponse('Halaman Customer')
