from django.shortcuts import render


def index(request):
    context = {
        'judul': 'Pendidikan',
        'nama': 'Gusti  Pendidikan',
        'nav': [
            ['/', 'Home'],
            ['/pendidikan', 'Pendidikan'],
            ['/about', 'About'],
            ['/context', 'context'],
        ]
    }  # jangan lupa tutup dengan return #yang di tambahkan
    return render(request, 'index.html', context)
