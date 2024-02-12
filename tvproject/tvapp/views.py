from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.
from . models import Place
from . models import Team
def demo(request):
    obj=Place.objects.all()
    return render(request,"index.html",{'result':obj})


def demo(request):
   obj=Team.objects.all()
   return render(request,"index.html", {'result': obj})

   #name="india"
   #return render(request,"home.html",{'obj':name})

#def addition(request):
   #x=int(request.GET['num1'])
  # y=int(request.GET['num2'])
   #res=x+y
  # return render(request,"about.html",{'result':res})
