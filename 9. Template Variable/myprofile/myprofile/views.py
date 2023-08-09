from django.shortcuts import render


def index(request):
    context = {
        'judul': 'My Profile',
        'nama': 'Gusti Permana Putra'
    }
    return render(request, 'index.html', context)
# yang ditambahkan
