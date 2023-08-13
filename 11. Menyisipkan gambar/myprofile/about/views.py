from django.shortcuts import render


def index(request):
    context = {
        'judul': 'About',
        'nama': 'Gusti Permana',
                'nav': [
                    ['/', 'Home'],
                    ['/pendidikan', 'Pendidikan'],
                    ['/about', 'about'],
                    ['/context', 'Context'],
                ]
    }
    return render(request, 'index.html', context)
# Create your views here.
