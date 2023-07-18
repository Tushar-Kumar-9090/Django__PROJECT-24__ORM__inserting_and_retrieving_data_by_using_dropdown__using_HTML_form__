from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from app.models import *


## Inserting Data into TOPIC table:---
#*------------------------------------------------
def insert_topic(request):
    if request.method=='POST':
        topic=request.POST['topic']

        TO=Topic.objects.get_or_create(topic_name=topic)[0]
        TO.save()
        return HttpResponse('<center><h1>Insertion of Topic is Done</h1></center>')

    return render(request,'insert_topic.html')



## Inserting Data into WEBPAGE table:---
#*------------------------------------------------
def insert_webpage(request):
    LTO=Topic.objects.all()
    d={'LTO':LTO}       ## for dropdown 

    if request.method=='POST':
        topic=request.POST['topic']
        name=request.POST.get('name') ## get() is the dictionary method
        url=request.POST['url']

        TO=Topic.objects.get(topic_name=topic)
        WO=Webpage.objects.get_or_create(topic_name=TO, name=name, url=url)[0]
        WO.save()
        return HttpResponse('<center><h1>Insertion of Webpage is Done</h1></center>')

    return render(request,'insert_webpage.html',d)



## Inserting Data into ACCESS_RECORD table:---
#*------------------------------------------------
def insert_access_record(request):
    LWO=Webpage.objects.all()
    d={'LWO':LWO}

    if request.method=='POST':
        name=request.POST['name']
        date=request.POST.get('date') ## get() is the dictionary method
        author=request.POST['author']

        WO=Webpage.objects.get(name=name)
        ACO=AccessRecord.objects.get_or_create(name=WO, date=date, author=author)[0]
        ACO.save()
        return HttpResponse('<center><h1>Insertion of Access_Record is Done</h1></center>')

    return render(request,'insert_access_record.html',d)




## Retrieving multiple topic_name details which is present in TOPIC:---
#*------------------------------------------------
def retrieving_webpage(request):
    LTO=Topic.objects.all()
    d={'LTO':LTO}

    if request.method=='POST':
        MSTS = request.POST.getlist('topic')

        WOS = Webpage.objects.none()

        for i in MSTS:
            WOS = WOS|Webpage.objects.filter(topic_name=i)  ## '|--> parallel pipe--> it will combine'

        d1 = {'WOS':WOS}
        return render(request,'display_webpage.html', d1)

    return render(request,'retrieving_webpage.html',d)




## Retrieving multiple names details which is present in WEBPAGE:---
#*------------------------------------------------
def retrieving_access_record(request):
    LWO=Webpage.objects.all()
    d={'LWO':LWO}

    if request.method=='POST':
        MSTS = request.POST.getlist('webpage')

        AOS = AccessRecord.objects.none()

        for i in MSTS:
            AOS = AOS|AccessRecord.objects.filter(name=i)

        d1 = {'AOS':AOS}
        return render(request,'display_access_record.html', d1)

    return render(request,'retrieving_access_record.html',d)




## By using check box and using action attribute
def checkbox(request):
    LTO=Topic.objects.all()
    d={'LTO':LTO}


    return render(request,'checkbox.html',d)







