from django.shortcuts import render
from app.models import *
from django.http import HttpResponse

# Create your views here.
def insert_topic(request):
    if request.method=='POST':
        tn=request.POST['tn']
        TO=Topic.objects.get_or_create(topic_name=tn)[0]
        TO.save()
        return HttpResponse('data is inserted')
    return render(request,'insert_topic.html')
def insert_web(request):
    TOP=Topic.objects.all()
    d={'topics':TOP}
    if request.method=='POST':
        tn=request.POST['tn']
        nm=request.POST['nm']
        url=request.POST['url']
        eml=request.POST['eml']
        T=Topic.objects.get(topic_name=tn)
        WO=Webpage.objects.get_or_create(topic_name=T,name=nm,url=url,email=eml)[0]
        WO.save()
        return HttpResponse('data is inserted')
    return render(request,'insert_web.html',d)
def accessrec(request):
    ACR=Webpage.objects.all()
    d={'access':ACR}
    if request.method=='POST':
        nm=request.POST['nm']
        au=request.POST['au']
        da=request.POST['da']
        W=Webpage.objects.get(name=nm)
        AR=Accessrecord.objects.get_or_create(name=W,author=au,date=da)[0]
        AR.save()
        return HttpResponse('accessrecord data will be inserted')
    return render(request,'accessrec.html',d)
def retrive_data(request):
    LTO=Topic.objects.all()
    d={'topics':LTO}
    if request.method=='POST':
        td=request.POST.getlist('topic')
        webq=Webpage.objects.none()
        for i in td:
            webq=webq|Webpage.objects.filter(topic_name=i)
        d1={'webpages':webq}
        return render(request,'display_webpage.html',d1)

    return render(request,'retrive_data.html',d)
def checkbox(request):
    LTO=Topic.objects.all()
    d={'topics':LTO}
    return render(request,'checkbox.html',d)
