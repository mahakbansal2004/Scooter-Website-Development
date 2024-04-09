from django.shortcuts import render,HttpResponse
from datetime import datetime
from home.models import Contact
from home.models import Maintenance
from home.models import Driving
from home.models import Tvswarranty
# from home.models import Herowarranty
# from home.models import Suzukiwarranty
# from home.models import Hondawarranty
# from home.models import Yamahawarranty
# from home.models import Atherwarranty
# from home.models import Viviprowarranty
# from home.models import Olawarranty
# from home.models import Bajajwarranty
# from home.models import Riverindiewarranty
from home.models import Olas1pro

# Create your views here.

def home(request):
    return render(request,'home.html')
    #return HttpResponse("this is a about page")


def index(request):
    context={
        'variable':"mahak is great"
    }
    return render(request,'index.html',context)

def about(request):
    return render(request,'about.html')
    #return HttpResponse("this is a about page")

def services(request):
    return render(request,'services.html')
    #return HttpResponse("this is a services page")

def contact(request):
     if request.method=="POST":
         name=request.POST.get('name')
         phone=request.POST.get('phone')
         email=request.POST.get('email')
         desc=request.POST.get('desc')
         contact= Contact(name=name,phone=phone,email=email,desc=desc,date=datetime.today())
         contact.save()
     return render(request,'contact.html')
     #return HttpResponse("this is a contact page")


def electric(request):
    return render(request,'electric.html')
    #return HttpResponse("this is a services page")

def petrol(request):
    return render(request,'petrol.html')
    #return HttpResponse("this is a services page")

def warranty(request):
    return render(request,'warranty.html')
    #return HttpResponse("this is a services page")

def maintenance(request):
    if request.method=="POST":
         name=request.POST.get('name')
         phone=request.POST.get('phone')
         email=request.POST.get('email')
         maintenance= Maintenance(name=name,phone=phone,email=email,date=datetime.today())
         maintenance.save()
    return render(request,'maintenance.html')
    #return HttpResponse("this is a services page")

def driving(request):
        name=request.POST.get('name')
        dob=request.POST.get('dob')
        address=request.POST.get('address')
        model=request.POST.get('model')
        type=request.POST.get('type')
        pic=request.FILES.get('pic')
        if not name:
            return render(request, 'driving.html', {'error': 'Name cannot be empty'})
        dob = datetime.strptime(dob, '%Y-%m-%d').date() if dob else None

        driving= Driving(name=name,dob=dob,address=address,model=model,type=type,pic=pic,date=datetime.today())
        driving.save()
        return render(request,'driving.html')
    #return HttpResponse("this is a services page")




def olas1pro(request):
    if request.method=="POST":
         name=request.POST.get('name')
         brandname=request.POST.get('brandname')
         address=request.POST.get('address')
         
         email=request.POST.get('email')
         olas1pro= Olas1pro(name=name,brandname=brandname,address=address,email=email,date=datetime.today())
         olas1pro.save()
         return render(request,'home.html')



    return render(request,'olas1pro.html')

    #return HttpResponse("this is a services page")

def olas1air(request):
    return render(request,'olas1air.html')

def olas1x(request):
    return render(request,'olas1x.html')

def ather450s(request):
    return render(request,'ather450s.html')

def ather450x(request):
    return render(request,'ather450x.html')

def ather450apex(request):
    return render(request,'ather450apex.html')

def tvsiqube(request):
    return render(request,'tvsiqube.html')

def tvsiqubes(request):
    return render(request,'tvsiqubes.html')

def tvsiqubest(request):
    return render(request,'tvsiqubest.html')

def vidav1plus(request):
    return render(request,'vidav1plus.html')

def vidav1pro(request):
    return render(request,'vidav1pro.html')

def hondapcxelectric(request):
    return render(request,'hondapcxelectric.html')

def hondaugo(request):
    return render(request,'hondaugo.html')

def bajajchetak(request):
    return render(request,'bajajchetak.html')

def riverindie(request):
    return render(request,'riverindie.html')

def tvsjupiter(request):
    return render(request,'tvsjupiter.html')

def tvsjupiter125(request):
    return render(request,'tvsjupiter125.html')

def tvsntorq(request):
    return render(request,'tvsntorq.html')

def tvszest(request):
    return render(request,'tvszest.html')

def suzukiaccess125(request):
    return render(request,'suzukiaccess125.html')

def suzukiavenis125(request):
    return render(request,'suzukiavenis125.html')

def suzukiburgman125(request):
    return render(request,'suzukiburgman125.html')

def heropleasureplus(request):
    return render(request,'heropleasureplus.html')

def herodestini125(request):
    return render(request,'herodestini125.html')

def heroxoom110(request):
    return render(request,'heroxoom110.html')

def yamaharayzr125(request):
    return render(request,'yamaharayzr125.html')

def yamahaaerox155(request):
    return render(request,'yamahaaerox155.html')

def yamahafascino125(request):
    return render(request,'yamahafascino125.html')

def hondaactiva6g(request):
    return render(request,'hondaactiva6g.html')

def hondaactiva125(request):
    return render(request,'hondaactiva125.html')

def hondadio(request):
    return render(request,'hondadio.html')

   
def tvswarranty(request):
    if request.method=="POST":
         name=request.POST.get('name')
         phone=request.POST.get('phone')
         email=request.POST.get('email')
         brandname=request.POST.get('brandname')
         tvswarranty= Tvswarranty(name=name,brandname=brandname,phone=phone,email=email,date=datetime.today())
         tvswarranty.save()
         return render(request,'warranty.html')
    return render(request,'tvswarranty.html')

def suzukiwarranty(request):
    # if request.method=="POST":
    #      name=request.POST.get('name')
    #      phone=request.POST.get('phone')
    #      email=request.POST.get('email')
    #      suzukiwarranty= Suzukiwarranty(name=name,phone=phone,email=email,date=datetime.today())
    #      suzukiwarranty.save()
     return render(request,'suzukiwarranty.html')

def herowarranty(request):
    # if request.method=="POST":
    #      name=request.POST.get('name')
    #      phone=request.POST.get('phone')
    #      email=request.POST.get('email')
    #      herowarranty= Herowarranty(name=name,phone=phone,email=email,date=datetime.today())
    #      herowarranty.save()
    return render(request,'herowarranty.html')

def hondawarranty(request):
    # if request.method=="POST":
    #      name=request.POST.get('name')
    #      phone=request.POST.get('phone')
    #      email=request.POST.get('email')
    #      hondawarranty= Hondawarranty(name=name,phone=phone,email=email,date=datetime.today())
    #      hondawarranty.save()
    return render(request,'hondawarranty.html')

def yamahawarranty(request):
    # if request.method=="POST":
    #      name=request.POST.get('name')
    #      phone=request.POST.get('phone')
    #      email=request.POST.get('email')
    #      yamahawarranty= Yamahawarranty(name=name,phone=phone,email=email,date=datetime.today())
    #      yamahawarranty.save()
    return render(request,'yamahawarranty.html')

def atherwarranty(request):
    # if request.method=="POST":
    #      name=request.POST.get('name')
    #      phone=request.POST.get('phone')
    #      email=request.POST.get('email')
    #      atherwarranty= Atherwarranty(name=name,phone=phone,email=email,date=datetime.today())
    #      atherwarranty.save()
    return render(request,'atherwarranty.html')

def viviprowarranty(request):
    # if request.method=="POST":
    #      name=request.POST.get('name')
    #      phone=request.POST.get('phone')
    #      email=request.POST.get('email')
    #      viviprowarranty= Viviprowarranty(name=name,phone=phone,email=email,date=datetime.today())
    #      viviprowarranty.save()
    return render(request,'viviprowarranty.html')

def olawarranty(request):
    # if request.method=="POST":
    #      name=request.POST.get('name')
    #      phone=request.POST.get('phone')
    #      email=request.POST.get('email')
    #      olawarranty= Olawarranty(name=name,phone=phone,email=email,date=datetime.today())
    #      olawarranty.save()
    return render(request,'olawarranty.html')

def bajajwarranty(request):
    # if request.method=="POST":
    #      name=request.POST.get('name')
    #      phone=request.POST.get('phone')
    #      email=request.POST.get('email')
    #      bajajwarranty= Bajajwarranty(name=name,phone=phone,email=email,date=datetime.today())
    #      bajajwarranty.save()
    return render(request,'bajajwarranty.html')

def riverindiewarranty(request):
    # if request.method=="POST":
    #      name=request.POST.get('name')
    #      phone=request.POST.get('phone')
    #      email=request.POST.get('email')
    #      riverindiewarranty= Riverindiewarranty(name=name,phone=phone,email=email,date=datetime.today())
    #      riverindiewarranty.save()
    return render(request,'riverindiewarranty.html')