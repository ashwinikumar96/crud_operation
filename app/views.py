from django.shortcuts import render
from app.models import *
from django.db.models.functions import Length
from django.db.models import Q
# Create your views here.

def insert_topic(request):
    tn = input('Enter topic_name : ')
    to = Topic.objects.get_or_create(topic_name=tn)[0]
    to.save()
    qsto = Topic.objects.all()
    return render(request,'display_topic.html',{'qsto':qsto})
def insert_webpage(request):
    tn = input('Enter topic_name : ')
    to = Topic.objects.get(topic_name=tn)
    to.save()
    n = input('Enter name : ')
    u = input('Enter url : ')
    wo = Webpage.objects.get_or_create(topic_name=to,name=n,url=u)[0]
    wo.save()
    qswo = Webpage.objects.all()
    return render(request,'display_webpage.html',{'qswo':qswo})
def insert_accessrecord(request):
    tn = input('Enter topic_name : ')
    to = Topic.objects.get(topic_name=tn)
    to.save()
    n = input('Enter name : ')
    u = input('Enter url : ')
    wo = Webpage.objects.get(topic_name=to,name=n,url=u)
    wo.save()
    d = input('Enter Date(yyyy-mm-dd) : ')
    a = input('Enter author : ')
    e = input('Enter email : ')
    ao = AccessRecord.objects.get_or_create(name=wo,date=d,author=a,email=e)[0]
    ao.save()
    qsao = AccessRecord.objects.all()
    return render(request,'display_accessrecord.html',{'qsao':qsao})

def display_topic(request):
    qsto = Topic.objects.all()
    qsto = Topic.objects.all().exclude(pk='Cricket')
    qsto = Topic.objects.all().order_by('topic_name')
    qsto = Topic.objects.all().order_by('-topic_name')
    qsto = Topic.objects.all().order_by(Length('topic_name'))
    qsto = Topic.objects.all().order_by(Length('topic_name').desc())
    return render(request,'display_topic.html',{'qsto':qsto})
def display_webpage(request):
    qswo = Webpage.objects.all()
    qswo = Webpage.objects.all().exclude(topic_name = 'Cricket')
    qswo = Webpage.objects.all().order_by('name')
    qswo = Webpage.objects.all().order_by('-name')
    qswo = Webpage.objects.all().order_by(Length('name'))
    qswo = Webpage.objects.all().order_by(Length('name').desc())
    qswo = Webpage.objects.filter(name__startswith = 'h')
    qswo = Webpage.objects.filter(url__endswith = 'in')
    qswo = Webpage.objects.filter(name__contains = 'i')
    qswo = Webpage.objects.filter(topic_name__in= ('Cricket', 'FootBall'))
    qswo = Webpage.objects.filter(Q(topic_name= 'Cricket') & Q(url__endswith = 'in'))
    qswo = Webpage.objects.filter(Q(topic_name= 'Cricket') | Q(topic_name__in = ('Cricket', 'FootBall')))

    return render(request,'display_webpage.html',{'qswo':qswo})
def display_accessrecord(request):
    qsao = AccessRecord.objects.all()
    qsao = AccessRecord.objects.all().exclude(author = 'bunty')
    qsao = AccessRecord.objects.all().order_by('author')
    qsao = AccessRecord.objects.all().order_by('-author')
    qsao = AccessRecord.objects.all().order_by(Length('author'))
    qsao = AccessRecord.objects.all().order_by(Length('author').desc())
    qsao = AccessRecord.objects.filter(author__startswith = 'b')
    qsao = AccessRecord.objects.filter(author__endswith = 'i')
    qsao = AccessRecord.objects.filter(email__contains = '@')
    qsao = AccessRecord.objects.filter(date__gt = '2000-11-11')
    qsao = AccessRecord.objects.filter(date__gte = '2000-11-11')
    qsao = AccessRecord.objects.filter(date__lt = '2023-8-11')
    qsao = AccessRecord.objects.filter(date__lte = '2023-8-11')
    qsao = AccessRecord.objects.filter(date__year = '2023')
    qsao = AccessRecord.objects.filter(date__month = '8')
    qsao = AccessRecord.objects.filter(date__day = '11')
    qsao = AccessRecord.objects.filter(date__year__lt = '2023')
    qsao = AccessRecord.objects.filter(date__year__gt = '2000')
    qsao = AccessRecord.objects.filter(email__regex = '^a\w+')
    qsao = AccessRecord.objects.filter(author__regex = '^R\w+')
    qsao = AccessRecord.objects.filter(Q(author__contains = 'i') & Q(date__year = '2000'))
    qsao = AccessRecord.objects.filter(Q(author__contains = 'i') | Q(date__year = '2000'))

    return render(request,'display_accessrecord.html',{'qsao':qsao})

def update_webpage(request):
    Webpage.objects.filter(topic_name = 'VollyBall').update(name = 'Nauymur')
    Webpage.objects.filter(topic_name = 'Cricket').update(url = 'https://bcci.in')
    Webpage.objects.filter(topic_name = 'BasketBall').update(url = 'https://bcci.in')
    Webpage.objects.filter(name = 'Dhoni').update(topic_name = 'FootBall')
    Webpage.objects.update_or_create(topic_name = 'VollyBall',defaults={'url':'https://volly.com'})
    BO = Topic.objects.get(topic_name = 'Basket Ball') 
    Webpage.objects.update_or_create(topic_name = BO,defaults={'name':'Jordan'})
    Webpage.objects.update_or_create(name = 'XYZ',defaults={'topic_name':BO,'url':'https://xyz.com'})
    FBO = Topic.objects.get(topic_name = 'FootBall')
    Webpage.objects.update_or_create(name = 'XYZ',defaults={'topic_name':FBO})
    # Webpage.objects.update_or_create(url = 'https://bcci.in',defaults={'topic_name':FBO})
    qswo = Webpage.objects.all()
    return render(request,'display_webpage.html',{'qswo':qswo})

def delete_webpage(request):
    Webpage.objects.filter(topic_name = 'Basket Ball').delete()
    Webpage.objects.all().delete()
    qswo = Webpage.objects.all()
    return render(request,'display_webpage.html',{'qswo':qswo})