


#def hello(request):
#    return HttpResponse("Hello world ! ")


from django.http import HttpResponse
from django.shortcuts import render





def login(request):
   # context = {}
    #context['hello'] = 'Hello World!'
    return render(request, 'index.html')

def banzu(request):
    return render(request, 'banzu.html')

def instruction(request):
    return render(request, 'instruction.html')

def simulator(request):
    return render(request, 'simulator.html')

def closedtrainning(request):
    return render(request, 'closedtrainnig.html')

def ontrainning(request):
    return render(request, 'ontrainning.html')

def sheet(request):
    return render(request, 'sheet.html')