


#def hello(request):
#    return HttpResponse("Hello world ! ")


from django.shortcuts import render

from atcInfo import models


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
    data = models.evalution1.objects.all()
    selLocation1 = request.POST.get('selLocation1')
    selLocation2 = request.POST.get('selLocation2')
    selLocation3 = request.POST.get('selLocation3')
    print(selLocation3)

    if selLocation1 == 1 and selLocation2 == 1:
        return render(request, 'sheet048.html', {'data': data})
    else:
        return render(request, 'sheet048.html', {'data': data})


def saveevaluationresult(request):
    训练情况 = request.POST.get('训练情况')
    教员评语 = request.POST.get('教员评语')

    studentname = request.POST.get('studentname')
    teachername = request.POST.get('teachername')

    print(训练情况)
    print(教员评语)

    return render(request, 'trainningstatus.html')
