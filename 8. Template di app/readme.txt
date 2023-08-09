
source ~/env/bin/activate

===================================================
Membuat Project baru
---------------------------------------------------
django-admin startproject pembayaran
cd pembayaran/
python manage.py startapp spp
mkdir templates
buat html index dan spp pada templates

setting.py DIRS 'templates' dan installed_APP 'spp',
buat lagi templates pada app spp
cd spp
mkdir templates
cd templates
mkdir spp

membuat views.py di folder pembayaran

membuat index.html di template base
nano ../../templates/index.html
membuat spp.html di template base
nano ../../templates/spp.html

modifikasi views.py diApp spp
membuat urls.py di App spp

membuat index.html di folder spp/template/spp

jadi base dan app masing masing mempunyai template dan mempunya index