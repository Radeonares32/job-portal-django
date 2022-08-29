projeyi başlatmadan ilk once postgresql indirmeniz gerekiyor
indirdikten sonra job adında bir database oluşturmanız gerekiyor isme dikkat buyuk kuçuk harf
duyarlıdır


çalıştırmak için şu adımları izleyin
not:manage.py dosyası ile aynı dizinde olmanız gerekli


1.python manage.py makemigrations
2.python manage.py migrate --run-syncdb
3.python manage.py createsuperuser

bu adımlardan sonra sizden bir  username isteyecek admin panel girmek için
bir de email ve şifre isteyecek bu adımları yaptıktan sonra çalışmaya hazır

çalıştırmak için

python manage.py runserver


Not:3 revizyon hakkınız bulunmakta eğer revizyon hakkınızı kullanmak isterseniz lütfen mümkün
oldugunca ayrıntılı bilgi veriniz 3 hakkınızdan sonra ücrete tabidir