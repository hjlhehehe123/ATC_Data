import json
from datetime import datetime

from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

import TestModel
from atcInfo.models import info
from trainningcompletion import models
from TestModel.views import name1


# Create your views here.
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


def global_params(request):
    name = info.objects.all().only("name")

    return {"name": name}


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


    if request.session.get('status'):  # 在判断网页请求的状态时，直接调用request.session从djang_session表中读取数据验证
        name2 = request.session.get('name')
        print(name2 + '*********' + 'session登陆人')

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
    data = info.objects.all()
    data = list(data)
    return render(request, 'addtrainningrecord.html', {'data': data})


def dateDiffInHours(t1, t2):
    td = t2 - t1
    return td.days * 24 + td.seconds / 3600 + 1


def addtrainningrecord1(request):
    # name1 = TestModel.views.name1
    #     # if name1 == '0':
    #     #     data04 = "未知"
    #     #     data07 = "未知"
    #     #     print(name1 + '*********' + '表示没有登陆')
    #     # else:
    #     #     try:
    #     #         print(name1 + '*********' + '登陆人')
    #     #         getatcinfo = info.objects.get(atcName=name1)
    #     #         print(getatcinfo.科室信息)
    #     #         data04 = getatcinfo.科室信息
    #     #         data07 = getatcinfo.atcName
    #     #     except ObjectDoesNotExist:
    #     #         print('没查到')
    if request.session.get('status'):  # 在判断网页请求的状态时，直接调用request.session从djang_session表中读取数据验证
        name2 = request.session.get('name')
        print(name2 + '*********' + 'session登陆人')
        if name2 == '0':
            data04 = "未知"
            data07 = "未知"
            print(name2 + '*********' + '表示没有登陆')
        else:
            try:
                print(name2 + '*********' + '登陆人')
                getatcinfo = info.objects.get(atcName=name2)
                print(getatcinfo.科室信息)
                data04 = getatcinfo.科室信息
                data07 = getatcinfo.atcName
            except ObjectDoesNotExist:
                print('没查到')

    data02 = request.POST.get('data02')
    if data02 == '0':
        data02 = '资格培训'
    if data02 == '1':
        data02 = '复习培训'
    if data02 == '2':
        data02 = '追加培训'
    data03 = request.POST.get('data03')

    data05 = request.POST.get('data05')
    data06 = request.POST.get('data06')
    global data08
    data08 = data08
    a = len(data08)
    print('人数' + '*********' + str(a))
    j = ''
    for i in data08:
        j = j + i + ' '
    print(data08)
    print(j)
    data08 = j

    global data09
    data09 = data09
    b = len(data09)
    print('人数' + '*********' + str(b))
    j = ''
    for i in data09:
        j = j + i + ' '
    print(data09)
    print(j)
    data09 = j

    data10 = str(a)
    data11 = ''
    data12 = ''
    data13 = request.POST.get('data13')
    data14 = request.POST.get('data14')
    data141 = request.POST.get('data141')
    data15 = request.POST.get('data15')
    data151 = request.POST.get('data151')
    data16 = request.POST.get('data16')
    t1 = datetime.strptime(data15, '%Y-%m-%d %H:%M')
    t2 = datetime.strptime(data151, '%Y-%m-%d %H:%M')

    print(dateDiffInHours(t1, t2))
    data11 = dateDiffInHours(t1, t2) * a
    data12 = 0.5
    if data11 < 6:
        data12 = 0.5
    if 8 > data11 > 6:
        data12 = 1
    if data11 > 8:
        data12 = 1.5

    print('--------------------------')
    # 获取日期对象并格式化输出
    t3 = datetime.strptime(data14, '%Y-%m-%d %H:%M')
    t4 = datetime.strptime(data141, '%Y-%m-%d %H:%M')
    data14 = data14 + " " + t4.strftime('%H:%M')
    data15 = data15 + " " + t2.strftime('%H:%M')

    # data15 = data15 + datetime.strptime(data15, '%Y-%m-%d %H:%M').strftime('%H:%M')
    # print(datetime.strptime(data14, '%Y-%m-%d %H:%M').strftime('%Y-%m-%d %Z %H:%M:%S %A %x %X 星期 %w'))
    print(data14)
    print(data15)

    a = models.trainningstatusdetail()
    a.frontdata1 = models.trainningstatusdetail.objects.all().count() + 1
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


data08 = []


def ajax_addtrainningrecord(request):
    global data08
    data08 = json.loads(request.body.decode("utf-8"))

    print("培训对象")
    print(data08)
    post_data = {
        "name": "1"
    }

    return HttpResponse(json.dumps(post_data), content_type='application/json')


data09 = []


def ajax_addtrainningrecord2(request):
    global data09
    data09 = json.loads(request.body.decode("utf-8"))

    print("培训对象")
    print(data09)
    post_data = {
        "name": "1"
    }

    return HttpResponse(json.dumps(post_data), content_type='application/json')


def test(request):
    return render(request, 'test.html', )
