from django.http import HttpResponse  # yang ditambahkan


def index(request):  # yang ditambahkan
    return HttpResponse("<h1>Tes, web tes</h1>")  # yang ditambahkan
