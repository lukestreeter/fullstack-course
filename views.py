from django.shorcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("<em>My Second Project</em>")


def help(request):
helpdict = {'help_insert':'HELP PAGE'}
return render(request, 'first_app/index.html',context=helpdict)