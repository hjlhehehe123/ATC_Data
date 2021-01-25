# def hello(request):
#    return HttpResponse("Hello world ! ")

from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render

from atcInfo import models


def login(request):
    # context = {}
    # context['hello'] = 'Hello World!'
    return render(request, 'index.html')


def test(request):
    # context = {}
    # context['hello'] = 'Hello World!'
    return render(request, 'ACkhbgb.html')


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
    data = list(data)

    data1 = data
    selLocation1 = request.POST.get('selLocation1')
    selLocation2 = request.POST.get('selLocation2')
    selLocation3 = request.POST.get('selLocation3')
    print(selLocation3)

    if selLocation1 == 1 and selLocation2 == 1:
        return render(request, 'jichangfxkhb.html'
                      , {'data': data
                          , 'data1': data1
                          , 'data2': data
                          , 'data3': data
                          , 'data4': data
                          , 'data5': data
                          , 'data6': data
                         }

                      )
    else:
        return render(request, 'jichangfxkhb.html', {'data': data})


def saveevaluationresult(request):
    score = request.POST.get('score')
    训练情况 = request.POST.get('训练情况')
    教员评语 = request.POST.get('教员评语')
    studentname = request.POST.get('studentname')
    teachername = request.POST.get('teachername')
    selLocation11 = request.POST.get('selLocation11')
    a = models.saveevaluationresult()
    a.score = request.POST.get('score')
    a.训练情况 = request.POST.get('训练情况')
    a.教员评语 = request.POST.get('教员评语')
    a.studentname = request.POST.get('studentname')
    a.teachername = request.POST.get('teachername')
    a.selLocation11 = request.POST.get('selLocation11')

    a.is_active = 0

    a.save()

    print(score)
    print(训练情况)
    print(教员评语)
    print(studentname)
    print(teachername)
    print(selLocation11)
    return render(request, 'trainningstatus.html')


def getinfo(request):
    getatcinfo = models.info.objects.get(id=1)
    name = request.POST.get('name')
    context = {}
    if name is not None:
        try:

            getatcinfo = models.info.objects.get(atcName=name)

        except ObjectDoesNotExist:
            context['status'] = 0
            return render(request, 'personnalinfo.html', context)

    context['atcName'] = getatcinfo.atcName
    context['atcOld'] = getatcinfo.atcOld
    context['基本信息'] = getatcinfo.基本信息
    context['管制员等级信息'] = getatcinfo.管制员等级信息
    context['执照信息'] = getatcinfo.执照信息
    context['英语等级信息'] = getatcinfo.英语等级信息
    context['非管制学历信息'] = getatcinfo.非管制学历信息
    context['管制学历信息'] = getatcinfo.管制学历信息
    context['管制工作经历信息'] = getatcinfo.管制工作经历信息
    context['体检信息'] = getatcinfo.体检信息
    context['奖励信息'] = getatcinfo.奖励信息
    context['惩罚信息'] = getatcinfo.惩罚信息
    context['管制教员信息'] = getatcinfo.管制教员信息
    context['检查员信息'] = getatcinfo.检查员信息
    context['检查员考核信息'] = getatcinfo.检查员考核信息
    context['赴外培训信息'] = getatcinfo.赴外培训信息
    context['岗位培训信息'] = getatcinfo.岗位培训信息
    context['放单考核信息'] = getatcinfo.放单考核信息
    context['执照检查信息'] = getatcinfo.执照检查信息
    context['爱岗敬业信息'] = getatcinfo.爱岗敬业信息
    context['职称信息'] = getatcinfo.职称信息
    context['特殊技能信息'] = getatcinfo.特殊技能信息
    context['科室信息'] = getatcinfo.科室信息

    return render(request, 'personnalinfo.html', context)


