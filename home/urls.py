from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('home.urls')),
    path('home',include('home.urls')),
    path('about',include('about.urls')),
    path('services',include('services.urls')),
    path('booking',include('booking.urls')),
        path('buy',include('buy.urls')),

    path('sell',include('sell.urls')),
        path('reviews',include('reviews.urls')),



    path('contact',include('contact.urls')),
    path('driving',include('driving.urls')),
    path('electric',include('electric.urls')),
    path('petrol',include('petrol.urls')),
    path('warranty',include('warranty.urls')),
    path('olas1pro',include('olas1pro.urls')),
    path('maintenance',include('maintenance.urls')),
    path('olas1air',include('olas1air.urls')),
    path('olas1x',include('olas1x.urls')),
    path('ather450s',include('ather450s.urls')),
    path('ather450x',include('ather450x.urls')),
    path('ather450apex',include('ather450apex.urls')),
    path('tvsiqube',include('tvsiqube.urls')),
    path('tvsiqubes',include('tvsiqubes.urls')),
    path('tvsiqubest',include('tvsiqubest.urls')),
    path('vidav1plus',include('vidav1plus.urls')),
    path('vidav1pro',include('vidav1pro.urls')),
    path('hondapcselectric',include('hondapcselectric.urls')),
    path('hondaugo',include('hondaugo.urls')),
    path('bajajchetak',include('bajajchetak.urls')),
    path('riverindie',include('riverindie.urls')),
    path('tvsjupiter',include('tvsjupiter.urls')),
    path('tvsjupiter125',include('tvsjupiter125.urls')),
    path('tvsntorq',include('tvsntorq.urls')),
    path('tvszest',include('tvszest.urls')),
    path('suzukiaccess125',include('suzukiaccess125.urls')),
    path('suzukiavenis125',include('suzukiavenis125.urls')),
    path('suzukiburgman125',include('suzukiburgman125.urls')),
    path('heropleasureplus',include('heropleasureplus.urls')),
    path('herodestini125',include('herodestini125.urls')),
    path('heroxoom110',include('heroxoom110.urls')),
    path('yamaharayzr125',include('yamaharayzr125.urls')),
    path('yamahaaerox155',include('yamahaaerox155.urls')),
    path('yamahafascino125',include('yamahafascino125.urls')),
    path('hondaactiva6g',include('hondaactiva6g.urls')),
    path('hondaactiva125',include('hondaactiva125.urls')),
    path('hondadio',include('hondadio.urls')),
    path('tvswarranty',include('tvswarranty.urls')),
    path('suzukiwarranty',include('suzukiwarranty.urls')),
    path('herowarranty',include('herowarranty.urls')),
    path('hondawarranty',include('hondawarranty.urls')),
    path('yamahawarranty',include('yamahawarranty.urls')),
    path('atherwarranty',include('atherwarranty.urls')),
    path('viviprowarranty',include('viviprowarranty.urls')),
    path('olawarranty',include('olawarranty.urls')),
    path('bajajwarranty',include('bajajwarranty.urls')),
    path('riverindiewarranty',include('riverindiewarranty.urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)