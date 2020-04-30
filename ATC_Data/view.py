


#def hello(request):
#    return HttpResponse("Hello world ! ")


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


def analysis(request):
    return render(request, 'analysis.html')


def makeplan(request):
    return render(request, 'makeplan.html')


def getsheet(request):
    selLocation1 = request.POST.get('selLocation1')
    selLocation2 = request.POST.get('selLocation2')
    selLocation3 = request.POST.get('selLocation3')
    print(selLocation3)

    if selLocation1 == 1 and selLocation2 == 1:
        return render(request, 'sheet048.html')
    else:
        return render(request, 'sheet048.html')
