from django.urls import path  # yang ditambahkan
from . import view  # yang ditambahkan
# yang ditambahkan
urlpatterns = [  # yang ditambahkan
    path('', view.index, name='index'),  # yang ditambahkan
]
