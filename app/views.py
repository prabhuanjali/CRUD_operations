from django.shortcuts import render

# Create your views here.
from app.models import *

def display_topics(request):
    QSTO= Topic.objects.all()

    d={'QSTO':QSTO}

    return render(request,'display_topics.html',d)

def display_webpages(request):
    QSWO=WebPage.objects.all()
    d={'QSWO':QSWO}

    return render(request,'display_webpages.html',d)


def display_Access(request):
    QSAO=Access_Record.objects.all()

    d={'QSAO':QSAO}

    return render(request,'display_Access.html',d)



def insert_topic(request):
    tn=input('Enter the topic name: ')
    TO=Topic.objects.get_or_create(topic_name=tn)[0]
    TO.save()

    QSTO= Topic.objects.all()
    d={'QSTO':QSTO}
    return render(request,'display_topics.html',d)


def insert_webpage(request):
    tn=input('Enter the topic name: ')
    na=input('Enter the Name: ')
    url=input('Enter the url: ')
    TO=Topic.objects.get(topic_name=tn)
    WO=WebPage.objects.get_or_create(topic_name=TO, name=na,url=url)[0]
    WO.save()

    QSWO=WebPage.objects.all()
    d={'QSWO':QSWO}
    return render(request,'display_webpages.html',d)


def insert_AC(request):
    date=input('Enter the date: ')
    au=input('Enter the Author: ')
    eml=input('Enter the Email: ')
    pk = int(input('Enter the Primary Key: '))
    WO=WebPage.objects.get(pk=pk)
    AC=Access_Record.objects.get_or_create(name=WO, date=date,author=au, email=eml)[0]
    AC.save()

    QSAO=Access_Record.objects.all()
    d={'QSAO':QSAO}
    return render(request,'display_Access.html',d)




