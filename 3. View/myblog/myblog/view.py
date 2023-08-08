from django.http import HttpResponse  # yang ditambahkan


def tentang(request):  # yang ditambahkan
    return HttpResponse('Halaman Tentang')  # yang ditambahkan


def index(request):  # yang ditambahkan
    return HttpResponse('hallo')  # yang ditambahkan
