from django.shortcuts import render


def index(request):
    context = {
        # variable yang di tambahkan
        'judul': 'My Profile',
        'nama': 'Gusti Permana Putra',
        # tag yang ditambahkan
        'nav': [
            ['/', 'Home'],
            ['/pendidikan', 'Pendidikan'],
            ['/about', 'About'],
            ['/context', 'Context'],
        ]
    }
    return render(request, 'index.html', context)
# yang ditambahkan
