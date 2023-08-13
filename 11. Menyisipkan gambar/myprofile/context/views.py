from django.shortcuts import render


def index(request):
    context = {
        'judul': 'context',
        'nama': 'Gusti  Context',
        'nav': [
            ['/', 'Home'],
            ['/pendidikan', 'PendiDIkan'],
            ['/about', 'About'],
            ['/context', 'context'],
        ]
    }

    return render(request, 'index.html', context)
# Create your views here.
