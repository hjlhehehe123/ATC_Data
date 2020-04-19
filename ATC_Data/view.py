


#def hello(request):
#    return HttpResponse("Hello world ! ")


from django.http import HttpResponse
from django.shortcuts import render





def login(request):
   # context = {}
    #context['hello'] = 'Hello World!'
    return render(request, 'index.html')

