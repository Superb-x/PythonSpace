from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def home(request):
    string = u'我在自学Django框架，想用这个框架建设自己的网站'
    TutorialList = ['HTML', 'CSS', 'JavaScript', 'JQuery', 'Python', 'Django']
    info_dict = {'name': u'刘祥麟', 'home': u'湖南浏阳'}
    List = map(str, range(100))
    return render(request, 'home.html', {
        'TutorialList': TutorialList,
        'string': string,
        'info_dict': info_dict,
        'List': List,
    })