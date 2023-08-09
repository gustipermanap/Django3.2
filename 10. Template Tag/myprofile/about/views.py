from django.shortcuts import render


def index(request):
    context = {
        'judul': 'about',
        'nama': 'Gusti Permana',
    }
    return render(request, 'about/index.html', context)
# Create your views here.
