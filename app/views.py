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
        print(nm)
        au=request.POST['au']
        da=request.POST['da']
        W=Webpage.objects.get(name=nm)
        AR=Accessrecord.objects.get_or_create(name=W,author=au,date=da)[0]
        AR.save()
        return HttpResponse('accessrecord data will be inserted')
    return render(request,'accessrec.html',d)
