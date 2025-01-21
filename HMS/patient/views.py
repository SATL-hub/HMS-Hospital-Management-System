from django.shortcuts import render
from .models import *
# Create your views here.
# def home(request):
#     return render(request,'home.html',{'activetab':'home'})


def about(request):
    a=Abouthms.objects.all().first()
    content=a.content
    images=a.images.split(",")
    print("content",content)
    print("images",len(images))
    return render(request,'home.html',{'activetab':'about','content':content,'images':images,'t_c':len(images)})