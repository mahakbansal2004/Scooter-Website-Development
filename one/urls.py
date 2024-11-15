"""
URL configuration for Hello project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from home import views


admin.site.site_header = "Skooty showroom Admin"
admin.site.site_title = "Skooty showroom Admin Portal"
admin.site.index_title = "Welcome to Skooty showroom Portal"

urlpatterns = [
    
    path('admin/', admin.site.urls),
    path("",views.home,name='home'),
    path("home",views.home,name='home'),
    path("about",views.about,name='about'),
    path("services",views.services,name='services'),
    path("booking",views.booking,name='booking'),
        path("buy",views.buy,name='buy'),

    path("sell",views.sell,name='sell'),
        path("reviews",views.reviews,name='reviews'),



    path("contact",views.contact,name='contact'),
    path("electric",views.electric,name='services'),
    path("petrol",views.petrol,name='petrol'),
    path("warranty",views.warranty,name='warranty'),
    path("maintenance",views.maintenance,name='maintenance'),
    path("driving",views.driving,name='driving'),
    path("olas1pro",views.olas1pro,name='olas1pro'),
    path("olas1air",views.olas1air,name='olas1air'),
    path("olas1x",views.olas1x,name='olas1x'),
    path("ather450s",views.ather450s,name='ather450s'),
    path("ather450x",views.ather450x,name='ather450x'),
    path("ather450apex",views.ather450apex,name='ather450apex'),
    path("tvsiqube",views.tvsiqube,name='tvsiqube'),
    path("tvsiqubes",views.tvsiqubes,name='tvsiqubes'),
    path("tvsiqubest",views.tvsiqubest,name='tvsiqubest'),
    path("vidav1plus",views.vidav1plus,name='vidav1plus'),
    path("vidav1pro",views.vidav1pro,name='vidav1pro'),
    path("hondapcxelectric",views.hondapcxelectric,name='hondapcxelectric'),
    path("hondaugo",views.hondaugo,name='hondaugo'),
    path("bajajchetak",views.bajajchetak,name='bajajchetak'),
    path("riverindie",views.riverindie,name='riverindie'),
    path("tvsjupiter",views.tvsjupiter,name='tvsjupiter'),
    path("tvsjupiter125",views.tvsjupiter125,name='tvsjupiter125'),
    path("tvsntorq",views.tvsntorq,name='tvsntorq'),
    path("tvszest",views.tvszest,name='tvszest'),
    path("suzukiaccess125",views.suzukiaccess125,name='suzukiaccess125'),
    path("suzukiavenis125",views.suzukiavenis125,name='suzukiavenis125'),
    path("suzukiburgman125",views.suzukiburgman125,name='suzukiburgman125'),
    path("heropleasureplus",views.heropleasureplus,name='heropleasureplus'),
    path("herodestini125",views.herodestini125,name='herodestini125'),
    path("heroxoom110",views.heroxoom110,name='heroxoom110'),
    path("yamaharayzr125",views.yamaharayzr125,name='yamaharayzr125'),
    path("yamahaaerox155",views.yamahaaerox155,name='yamahaaerox155'),
    path("yamahafascino125",views.yamahafascino125,name='yamahafascino125'),
    path("hondaactiva6g",views.hondaactiva6g,name='hondaactiva6g'),
    path("hondaactiva125",views.hondaactiva125,name='hondaactiva125'),
    path("hondadio",views.hondadio,name='hondadio'),
    path("tvswarranty",views.tvswarranty,name='tvswarranty'),
    path("suzukiwarranty",views.suzukiwarranty,name='suzukiwarranty'),
    path("herowarranty",views.herowarranty,name='herowarranty'),
    path("hondawarranty",views.hondawarranty,name='hondawarranty'),
    path("yamahawarranty",views.yamahawarranty,name='yamahawarranty'),
    path("atherwarranty",views.atherwarranty,name='atherwarranty'),
    path("viviprowarranty",views.viviprowarranty,name='viviprowarranty'),
    path("olawarranty",views.olawarranty,name='olawarranty'),
    path("bajajwarranty",views.bajajwarranty,name='bajajwarranty'),
    path("riverindiewarranty",views.riverindiewarranty,name='riverindiewarranty'),
   
   
    
]
