# def hello(request):
#    return HttpResponse("Hello world ! ")
import json

from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

from atcInfo import models


def login(request):
    # context = {}
    # context['hello'] = 'Hello World!'
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
    data = list(data)

    data1 = data
    selLocation1 = request.POST.get('selLocation1')
    selLocation2 = request.POST.get('selLocation2')
    selLocation3 = request.POST.get('selLocation3')
    print(selLocation3)

    if selLocation1 == 1 and selLocation2 == 1:
        return render(request, 'sheet048.html'
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
        return render(request, 'sheet048.html', {'data': data})


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


def ajax(request):
    if request.method == "POST":
        name = request.POST.get('name')
        print("ok")
        print(name)
        post_data = {
            "name": "0",
        }
        if name == "1":
            post_data = {
                "name": "1""hh""ddd"
            }
            print("ok")
            print(name)
            status = 1
            result = "sucuss"
            return HttpResponse(json.dumps(post_data
                                           ), content_type='application/json')
            # return HttpResponse( status)


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

    return render(request, 'personnalinfo.html', context)


def trainningstatusdetail(request):
    data = models.trainningstatusdetail.objects.values_list().all()

    data = list(data)
    # JsonResponse(ret_list, safe=False)
    # data = np.array(data)
    # data = json.dumps(data, safe=False)

    fileuri = []
    # 先从库表中获取到与该应用相关的全部配置文件路径与文件信息，即fileuri
    for i in data:
        fileuri.append(i)
    # 此时fileuri是一个python list类型，无法在页面js脚本中作为数组类型使用，需要转为json字符串
    data = json.dumps(fileuri, ensure_ascii=False)

    # ls = []
    #
    # path_type = data.replace("'", "").strip("[]").strip().split(',')
    #
    # for i in range(len(path_type)):
    #     my_data = {path_type[i]}  # 组装成一个字典。
    #     ls.append(my_data)  # 把字典放进一个大的list中给后面程序使用。
    print(data)
    data1 = request.POST.get('data1')
    data2 = request.POST.get('data2')
    data3 = request.POST.get('data3')
    data4 = request.POST.get('data4')
    data5 = request.POST.get('data5')
    data6 = request.POST.get('data6')
    data7 = request.POST.get('data7')
    data8 = request.POST.get('data8')
    data9 = request.POST.get('data9')
    data10 = request.POST.get('data10')
    data11 = request.POST.get('data11')
    data12 = request.POST.get('data12')
    data13 = request.POST.get('data13')
    data14 = request.POST.get('data14')
    data15 = request.POST.get('data15')
    data16 = request.POST.get('data16')

    return render(request, 'trainningstatusdetail.html', {'data': data})





def ajax_add(request):
    data = json.loads(request.body.decode("utf-8"))
    print(data)
    post_data = {
        "name": "1"
    }

    fileuri = []
    # 先从库表中获取到与该应用相关的全部配置文件路径与文件信息，即fileuri
    for i in data:
        fileuri.append(i)
    print(data)
    print(fileuri)
    print("每一行")




    for i in data:
        # print(i)
        print(i[0])
        print(i[1])
        a = models.trainningstatusdetail()
        a.frontdata1 = i[1]
        a.frontdata2 = i[2]
        a.frontdata3 = i[3]
        a.frontdata4 = i[4]
        a.frontdata5 = i[5]
        a.frontdata6 = i[6]
        a.frontdata7 = i[7]
        a.frontdata8 = i[8]
        a.frontdata9 = i[9]
        a.frontdata10 = i[10]
        a.frontdata11 = i[11]
        a.frontdata12 = i[12]
        a.frontdata13 = i[13]
        a.frontdata14 = i[14]
        a.frontdata15 = i[15]
        a.frontdata16 = i[16]
        a.is_active = 0
        a.save()

        # for j in i:
            # print(j)

    return HttpResponse(json.dumps(post_data
                                   ), content_type='application/json')
def addtrainningrecord(request):

    return render(request, 'addtrainningrecord.html')
def addtrainningrecord1(request):
    data02 = request.POST.get('data02')
    data03 = request.POST.get('data03')
    data04 = request.POST.get('data04')
    data05 = request.POST.get('data05')
    data06 = request.POST.get('data06')
    data07 = request.POST.get('data07')
    data08 = request.POST.get('data08')
    data09 = request.POST.get('data09')
    data10 = request.POST.get('data10')
    data11 = request.POST.get('data11')
    data12 = request.POST.get('data12')
    data13 = request.POST.get('data13')
    data14 = request.POST.get('data14')
    data15 = request.POST.get('data15')
    data16 = request.POST.get('data16')
    a = models.trainningstatusdetail()

    a.frontdata1 = models.trainningstatusdetail.objects.all().count()+1
    a.frontdata2 = data02
    a.frontdata3 = data03
    a.frontdata4 = data04
    a.frontdata5 = data05
    a.frontdata6 = data06
    a.frontdata7 = data07
    a.frontdata8 = data08
    a.frontdata9 = data09
    a.frontdata10 = data10
    a.frontdata11 = data11
    a.frontdata12 = data12
    a.frontdata13 = data13
    a.frontdata14 = data14
    a.frontdata15 = data15
    a.frontdata16 = data16

    a.is_active = 0
    a.save()


    return render(request, 'ok.html')
