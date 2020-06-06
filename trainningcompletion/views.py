import json
from datetime import datetime

from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

import TestModel
from atcInfo.models import info
from trainningcompletion import models
from TestModel.views import name1


# Create your views here.
def ajax(request):  # 学习用的，没实际用处
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


def global_params(request):  # 学习用的，没实际用处
    name = info.objects.all().only("name")

    return {"name": name}


# 以下是模拟机培训相关的
def trainningstatusdetail(request):  # 获取模拟机培训记录页面
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


def addtrainningrecord(request):  # 获取增加模拟机培训记录的页面
    data = info.objects.all()
    data = list(data)
    plan = models.monthplan.objects.values_list().all()
    plan = list(plan)
    fileuri = []
    # 先从库表中获取到与该应用相关的全部配置文件路径与文件信息，即fileuri
    for i in plan:
        fileuri.append(i)
    # 此时fileuri是一个python list类型，无法在页面js脚本中作为数组类型使用，需要转为json字符串
    plan = json.dumps(fileuri, ensure_ascii=False)
    print(plan)
    print("@@@@@@@@@@@@@@")
    return render(request, 'addtrainningrecord.html', {'data': data, 'plan': plan})


def dateDiffInHours(t1, t2):  # 时间计算，两个时间相差的小时数
    td = t2 - t1
    return td.days * 24 + td.seconds / 3600 + 1


def addtrainningrecord1(request):  # 获取增加模拟机培训记录的数据并保存
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

    now_time = datetime.now()
    month = datetime.strftime(now_time, "%m")
    data03 = month + "月"

    data05 = request.POST.get('data05')
    data06 = request.POST.get('data06')
    if data06 == '0':
        data06 = '塔台模拟机房'
    if data06 == '1':
        data06 = '雷达模拟机房'
    global data08
    data081 = request.POST.get('data081').strip()
    data082 = request.POST.get('data082').strip()
    data083 = request.POST.get('data083').strip()
    data084 = request.POST.get('data084').strip()
    data08 = data081 + ' ' + data082 + ' ' + data083 + ' ' + data084
    data08 = data08.rstrip()
    a = 1
    for i in data08:

        if ord(i) == 32:
            a = a + 1

    print('人数' + '*********' + str(a))

    global data09
    data091 = request.POST.get('data091').strip()
    data092 = request.POST.get('data092').strip()
    data09 = data091 + ' ' + data092
    data09 = data09.rstrip()

    data10 = a
    data11 = ''
    data12 = ''

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

    data15 = data15 + " " + t2.strftime('%H:%M')

    # data15 = data15 + datetime.strptime(data15, '%Y-%m-%d %H:%M').strftime('%H:%M')
    # print(datetime.strptime(data14, '%Y-%m-%d %H:%M').strftime('%Y-%m-%d %Z %H:%M:%S %A %x %X 星期 %w'))
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
    a.frontdata15 = data15
    a.frontdata16 = data16

    a.is_active = 0
    a.save()

    return render(request, 'trainningstatusdetail.html')


data08 = []


def ajax_addtrainningrecord(request):  # 获取增加模拟机培训记录的数据中的data08（培训对象）并赋值给全局变量data08，
    # addtrainningrecord1用到了全局变量data08
    global data08
    data08 = json.loads(request.body.decode("utf-8"))

    print("培训对象")
    print(data08)
    post_data = {
        "name": "1"
    }

    return HttpResponse(json.dumps(post_data), content_type='application/json')


data09 = []


def ajax_addtrainningrecord2(request):  ##获取增加模拟机培训记录的数据中的data09（机长）并赋值给全局变量data08，
    # addtrainningrecord1用到了全局变量data09
    global data09
    data09 = json.loads(request.body.decode("utf-8"))

    print("机长")
    print(data09)
    post_data = {
        "name": "1"
    }

    return HttpResponse(json.dumps(post_data), content_type='application/json')


def change_trainning_record(request):  # 获取增加模拟机培训记录的页面
    if request.session.get('status'):  # 在判断网页请求的状态时，直接调用request.session从djang_session表中读取数据验证
        name2 = request.session.get('name')
        print(name2 + '*********' + 'session登陆人')
    data = models.trainningstatusdetail.objects.filter(frontdata7=name2).values_list().all()

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

    return render(request, 'change_trainning_record.html', {'data': data})


def change_trainning_record_save(request):  # 保存更改的模拟机培训记录页面的数据
    data = json.loads(request.body.decode("utf-8"))
    print(data)
    post_data = {
        "name": "1"
    }

    fileuri = []
    for i in data:
        fileuri.append(i)
    print(data)
    print(fileuri)
    print("每一行")

    for i in data:
        # print(i)
        print(i[0])
        print(i[1])
        models.trainningstatusdetail.objects.filter(frontdata1=i[1]).update(frontdata2=i[2])
        models.trainningstatusdetail.objects.filter(frontdata1=i[1]).update(frontdata3=i[3])
        models.trainningstatusdetail.objects.filter(frontdata1=i[1]).update(frontdata4=i[4])
        models.trainningstatusdetail.objects.filter(frontdata1=i[1]).update(frontdata5=i[5])
        models.trainningstatusdetail.objects.filter(frontdata1=i[1]).update(frontdata6=i[6])
        models.trainningstatusdetail.objects.filter(frontdata1=i[1]).update(frontdata7=i[7])
        models.trainningstatusdetail.objects.filter(frontdata1=i[1]).update(frontdata8=i[8])
        models.trainningstatusdetail.objects.filter(frontdata1=i[1]).update(frontdata9=i[9])
        models.trainningstatusdetail.objects.filter(frontdata1=i[1]).update(frontdata10=i[10])
        models.trainningstatusdetail.objects.filter(frontdata1=i[1]).update(frontdata11=i[11])
        models.trainningstatusdetail.objects.filter(frontdata1=i[1]).update(frontdata12=i[12])
        # models.trainningstatusdetail.objects.filter(frontdata1=i[1]).update(frontdata13=i[13])
        # models.trainningstatusdetail.objects.filter(frontdata1=i[1]).update(frontdata14=i[14])
        models.trainningstatusdetail.objects.filter(frontdata1=i[1]).update(frontdata15=i[13])
        models.trainningstatusdetail.objects.filter(frontdata1=i[1]).update(frontdata16=i[14])

        # for j in i:
        # print(j)

    return HttpResponse(json.dumps(post_data
                                   ), content_type='application/json')


# 以下是其他培训的
def trainningstatusdetailother(request):  # 获取其他培训记录页面
    data = models.trainningstatusdetailother.objects.values_list().all()

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

    return render(request, 'trainningstatusdetailother.html', {'data': data})


def ajax_addother(request):  # 保存其他培训记录页面的数据，暂时不用
    data = json.loads(request.body.decode("utf-8"))
    print(data)
    post_data = {
        "name": "1"
    }

    fileuri = []
    for i in data:
        fileuri.append(i)
    print(data)
    print(fileuri)
    print("每一行")

    for i in data:
        # print(i)
        print(i[0])
        print(i[1])
        a = models.trainningstatusdetailother()
        a.frontdata1 = i[1]
        a.frontdata2 = i[2]
        a.frontdata3 = i[3]
        a.frontdata4 = i[4]
        a.frontdata5 = i[5]
        a.frontdata6 = i[6]
        a.frontdata7 = i[7]
        a.frontdata8 = i[8]
        # a.frontdata9 = i[9]
        # a.frontdata10 = i[10]
        # a.frontdata11 = i[11]
        # a.frontdata12 = i[12]
        # a.frontdata13 = i[13]
        # a.frontdata14 = i[14]
        # a.frontdata15 = i[15]
        # a.frontdata16 = i[16]

        a.frontdata10 = i[9]
        a.frontdata11 = i[10]
        a.frontdata12 = i[11]
        a.frontdata13 = i[12]
        a.frontdata14 = i[13]
        a.frontdata15 = i[14]
        a.frontdata16 = i[15]
        a.is_active = 0
        a.save()

        # for j in i:
        # print(j)

    return HttpResponse(json.dumps(post_data
                                   ), content_type='application/json')


def addtrainningrecordother(request):  # 获取增加其他培训记录的页面

    now_time = datetime.now()
    month = datetime.strftime(now_time, "%m")
    print("month" + str(int(month)))
    data = info.objects.all()
    data = list(data)

    plan = models.monthplan.objects.filter(month=str(int(month))).values_list().all()
    plan = list(plan)
    banzu = models.banzu.objects.values_list().all()
    banzu = list(banzu)
    fileuri = []
    # 先从库表中获取到与该应用相关的全部配置文件路径与文件信息，即fileuri
    for i in plan:
        fileuri.append(i)
    # 此时fileuri是一个python list类型，无法在页面js脚本中作为数组类型使用，需要转为json字符串
    plan = json.dumps(fileuri, ensure_ascii=False)
    print(plan)
    print("@@@@@@@@@@@@@@")

    fileuri2 = []
    for i in banzu:
        fileuri2.append(i)
    banzu = json.dumps(fileuri2, ensure_ascii=False)
    print(banzu)
    print("@@@@@@@@@@@@@@")
    return render(request, 'addtrainningrecordother.html', {'data': data, 'plan': plan, 'banzu': banzu})


def dateDiffInHours(t1, t2):  ##时间计算，两个时间相差的小时数
    td = t2 - t1
    return td.days * 24 + td.seconds / 3600


def addtrainningrecordother1(request):  ##获取增加其他培训记录的数据并保存
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
    now_time = datetime.now()
    month = datetime.strftime(now_time, "%m")
    data03 = month + "月"

    data05 = request.POST.get('data05')
    data06 = request.POST.get('data06')
    data08 = request.POST.get('data08').strip()

    a = 1
    for i in data08:

        if ord(i) == 32:
            a = a + 1
    data10 = str(a)
    data11 = ''
    data12 = ''

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
    data15 = data15 + " " + t2.strftime('%H:%M')

    # data15 = data15 + datetime.strptime(data15, '%Y-%m-%d %H:%M').strftime('%H:%M')
    # print(datetime.strptime(data14, '%Y-%m-%d %H:%M').strftime('%Y-%m-%d %Z %H:%M:%S %A %x %X 星期 %w'))
    print(data15)

    a = models.trainningstatusdetailother()
    a.frontdata1 = models.trainningstatusdetailother.objects.all().count() + 1
    a.frontdata2 = data02
    a.frontdata3 = data03
    a.frontdata4 = data04
    a.frontdata5 = data05
    a.frontdata6 = data06
    a.frontdata7 = data07
    a.frontdata8 = data08
    # a.frontdata9 = data09
    a.frontdata10 = data10
    a.frontdata11 = data11
    a.frontdata12 = data12

    a.frontdata15 = data15
    a.frontdata16 = data16

    a.is_active = 0
    a.save()

    return render(request, 'trainningstatusdetailother.html')


data08 = []


def ajax_addtrainningrecordother(request):  ##获取增加其他培训记录的数据中的data08（培训对象）并赋值给全局变量data08，
    # addtrainningrecord1用到了全局变量data08
    global data08
    data08 = json.loads(request.body.decode("utf-8"))

    print("培训对象")
    print(data08)
    post_data = {
        "name": "1"
    }

    return HttpResponse(json.dumps(post_data), content_type='application/json')


def change_trainning_record_other(request):  # 获取增加其他培训记录的页面
    if request.session.get('status'):  # 在判断网页请求的状态时，直接调用request.session从djang_session表中读取数据验证
        name2 = request.session.get('name')
        print(name2 + '*********' + 'session登陆人')
    data = models.trainningstatusdetailother.objects.filter(frontdata7=name2).values_list().all()

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

    return render(request, 'change_trainning_record_other.html', {'data': data})


def change_trainning_record_other_save(request):  # 保存更改的其他培训记录页面的数据
    data = json.loads(request.body.decode("utf-8"))
    print(data)
    post_data = {
        "name": "1"
    }

    fileuri = []
    for i in data:
        fileuri.append(i)
    print(data)
    print(fileuri)
    print("每一行")

    for i in data:
        # print(i)
        print(i[0])
        print(i[1])
        models.trainningstatusdetailother.objects.filter(frontdata1=i[1]).update(frontdata2=i[2])
        models.trainningstatusdetailother.objects.filter(frontdata1=i[1]).update(frontdata3=i[3])
        models.trainningstatusdetailother.objects.filter(frontdata1=i[1]).update(frontdata4=i[4])
        models.trainningstatusdetailother.objects.filter(frontdata1=i[1]).update(frontdata5=i[5])
        models.trainningstatusdetailother.objects.filter(frontdata1=i[1]).update(frontdata6=i[6])
        models.trainningstatusdetailother.objects.filter(frontdata1=i[1]).update(frontdata7=i[7])
        models.trainningstatusdetailother.objects.filter(frontdata1=i[1]).update(frontdata8=i[8])
        # models.trainningstatusdetailother.objects.filter(frontdata1=i[1]).update(frontdata9=i[])
        models.trainningstatusdetailother.objects.filter(frontdata1=i[1]).update(frontdata10=i[9])
        models.trainningstatusdetailother.objects.filter(frontdata1=i[1]).update(frontdata11=i[10])
        models.trainningstatusdetailother.objects.filter(frontdata1=i[1]).update(frontdata12=i[11])
        # models.trainningstatusdetailother.objects.filter(frontdata1=i[1]).update(frontdata13=i[13])
        # models.trainningstatusdetailother.objects.filter(frontdata1=i[1]).update(frontdata14=i[14])
        models.trainningstatusdetailother.objects.filter(frontdata1=i[1]).update(frontdata15=i[12])
        models.trainningstatusdetailother.objects.filter(frontdata1=i[1]).update(frontdata16=i[13])

        # for j in i:
        # print(j)

    return HttpResponse(json.dumps(post_data
                                   ), content_type='application/json')


# 以下是# 模拟机培训学时（塔台）
def tower_trainning_total_time(request):  # 获取模拟机培训学时（塔台）

    # a = models.tower_trainning_total_time()
    # a.objects.get(data02="1月").data03 = models.trainningstatusdetail.objects.filter(frontdata3="1月",
    #                                                                              frontdata2="上岗前培训",
    #                                                                              frontdata4="塔台管制室", ).frontdata11.values_list().all()
    # print(models.trainningstatusdetail.objects.filter(frontdata3="3月",
    #                                                frontdata2="资格培训",
    #                                                frontdata4="区域管制室", ).values_list().all())
    培训类别 = ["上岗前培训", "资格培训", "复习培训", "附加培训", "追加培训", "补习培训"
        , "设备培训", "熟练培训", "专项培训", ]
    月份 = ["1月",
          "2月",
          "3月",
          "4月",
          "5月",
          "6月",
          "7月",
          "8月",
          "9月",
          "10月",
          "11月",
          "12月", ]
    try:
        if models.tower_trainning_total_time.objects.filter(data01="年份", data02="月份", ):
            print("已经有表头")
        else:

            models.tower_trainning_total_time.objects.create(
                data01="年份",
                data02="月份",
                data03="上岗前培训",
                data04="",
                data05="资格培训",
                data06="",
                data07="复习培训",
                data08="",
                data09="附加培训",
                data10="",
                data11="追加培训",
                data12="",
                data13="补习培训",
                data14="",
                data15="设备培训",
                data16="",
                data17="熟练培训",
                data18="",
                data19="专项培训",
                data20="",
                data21="合计",
                data22="", )

            models.tower_trainning_total_time.objects.create(
                data01="",
                data02="",
                data03="学时",
                data04="人次",
                data05="学时",
                data06="人次",
                data07="学时",
                data08="人次",
                data09="学时",
                data10="人次",
                data11="学时",
                data12="人次",
                data13="学时",
                data14="人次",
                data15="学时",
                data16="人次",
                data17="学时",
                data18="人次",
                data19="学时",
                data20="人次",
                data21="学时",
                data22="人次", )
            print("创建了表头:")

        for j1 in 月份:
            if models.tower_trainning_total_time.objects.filter(data01="2020", data02=j1, ):
                print("已经有月份")
            else:
                models.tower_trainning_total_time.objects.create(data01="2020", data02=j1, )
                print("创建了:" + j1)

        for i in 培训类别:
            for j in 月份:
                # print(i)
                # a = models.tower_trainning_total_time
                学时 = 0
                for k in models.trainningstatusdetail.objects.filter(frontdata3=j,
                                                                     frontdata2=i,
                                                                     frontdata4="塔台管制室", ).values_list('frontdata11'):
                    for m in k:
                        学时 = 学时 + int(m)
                print(学时)
                人次 = 0
                for k1 in models.trainningstatusdetail.objects.filter(frontdata3=j,
                                                                      frontdata2=i,
                                                                      frontdata4="塔台管制室", ).values_list('frontdata10'):
                    for m1 in k1:
                        人次 = 人次 + int(m1)
                print(人次)
                if i == "上岗前培训":
                    models.tower_trainning_total_time.objects.filter(data02=j).update(data03=学时)
                    models.tower_trainning_total_time.objects.filter(data02=j).update(data04=人次)
                if i == "资格培训":
                    models.tower_trainning_total_time.objects.filter(data02=j).update(data05=学时)
                    models.tower_trainning_total_time.objects.filter(data02=j).update(data06=人次)
                if i == "复习培训":
                    models.tower_trainning_total_time.objects.filter(data02=j).update(data07=学时)
                    models.tower_trainning_total_time.objects.filter(data02=j).update(data08=人次)
                if i == "附加培训":
                    models.tower_trainning_total_time.objects.filter(data02=j).update(data09=学时)
                    models.tower_trainning_total_time.objects.filter(data02=j).update(data10=人次)
                if i == "追加培训":
                    models.tower_trainning_total_time.objects.filter(data02=j).update(data11=学时)
                    models.tower_trainning_total_time.objects.filter(data02=j).update(data12=人次)
                if i == "补习培训":
                    models.tower_trainning_total_time.objects.filter(data02=j).update(data13=学时)
                    models.tower_trainning_total_time.objects.filter(data02=j).update(data14=人次)
                if i == "设备培训":
                    models.tower_trainning_total_time.objects.filter(data02=j).update(data15=学时)
                    models.tower_trainning_total_time.objects.filter(data02=j).update(data16=人次)
                if i == "熟练培训":
                    models.tower_trainning_total_time.objects.filter(data02=j).update(data17=学时)
                    models.tower_trainning_total_time.objects.filter(data02=j).update(data18=人次)
                if i == "专项培训":
                    models.tower_trainning_total_time.objects.filter(data02=j).update(data19=学时)
                    models.tower_trainning_total_time.objects.filter(data02=j).update(data20=人次)

        计算行的和()
        if models.tower_trainning_total_time.objects.filter(data01="", data02="合计",):
            print("已经有列合计")
        else:
            models.tower_trainning_total_time.objects.create(data01="", data02="合计", )
        计算列的和()


    except ObjectDoesNotExist:
        print('没查到')

    data = models.tower_trainning_total_time.objects.values_list("data01",
                                                                 "data02",
                                                                 "data03",
                                                                 "data04",
                                                                 "data05",
                                                                 "data06",
                                                                 "data07",
                                                                 "data08",
                                                                 "data09",
                                                                 "data10",
                                                                 "data11",
                                                                 "data12",
                                                                 "data13",
                                                                 "data14",
                                                                 "data15",
                                                                 "data16",
                                                                 "data17",
                                                                 "data18",
                                                                 "data19",
                                                                 "data20",
                                                                 "data21",
                                                                 "data22",

                                                                 ).all()

    data = list(data)
    # JsonResponse(ret_list, safe=False)
    # data = np.array(data)
    # data = json.dumps(data, safe=False)

    fileuri = []
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
    # print(data)
    if request.session.get('status'):  # 在判断网页请求的状态时，直接调用request.session从djang_session表中读取数据验证
        name2 = request.session.get('name')
        print(name2 + '*********' + 'session登陆人')

    return render(request, 'tower_trainning_total_time.html', {'data': data})


def 计算行的和():

    月份 = ["1月",
          "2月",
          "3月",
          "4月",
          "5月",
          "6月",
          "7月",
          "8月",
          "9月",
          "10月",
          "11月",
          "12月", ]
    for i3 in 月份:

        data21 = 0  # 每行的学时和
        data22 = 0 # 每行的人次和
        for k3 in range(3, 21, 2):
            # print(k3)
            k4 = ""
            k5 = ""
            if k3 < 10:
                k4 = "0" + str(k3)
            else:
                k4 = str(k3)
            if k3 < 9:
                k5 = "0" + str(k3 + 1)
            else:
                k5 = str(k3 + 1)
            for m in models.tower_trainning_total_time.objects.filter(data02=i3).values_list('data' + str(k4), ):
                for k6 in m:
                    data21 = data21 + int(k6.strip())

            for n in models.tower_trainning_total_time.objects.filter(data02=i3).values_list('data' + str(k5), ):
                for k7 in n:
                    data22 = data22 + int(k7.strip())
        models.tower_trainning_total_time.objects.filter(data02=i3).update(
            data21=data21,
            data22=data22, )


def 计算列的和():
    aa = []
    月份 = ["1月",
          "2月",
          "3月",
          "4月",
          "5月",
          "6月",
          "7月",
          "8月",
          "9月",
          "10月",
          "11月",
          "12月", ]

    for i in range(3, 22, 2):
        列合计学时 = 0
        列合计人次 = 0
        for i3 in 月份:
            k4 = ""
            k5 = ""
            if i < 10:
                k4 = "0" + str(i)
            else:
                k4 = str(i)
            if i < 9:
                k5 = "0" + str(i + 1)
            else:
                k5 = str(i + 1)

            # 计算列合计学时，人次

            for k in models.tower_trainning_total_time.objects.filter(data02=i3).values_list(
                    'data' + str(k4)):
                for m in k:
                    列合计学时 = 列合计学时 + int(m.strip())  # 不可转换空字符串为整型


            for k1 in models.tower_trainning_total_time.objects.filter(data02=i3).values_list(
                    'data' + str(k5)):
                for m1 in k1:
                    列合计人次 = 列合计人次 + int(m1.strip())


        aa.append(列合计学时)
        aa.append(列合计人次)
        # print(列合计人次)
        # print(列合计学时)
        # print(i)
        # names = locals()
        # for i in range(3, 22, 2):
        #     names['data0' + str(i)] = i


    models.tower_trainning_total_time.objects.filter(data02="合计").update(
        data03=aa[0],
        data04=aa[1],
        data05=aa[2],
        data06=aa[3],
        data07=aa[4],
        data08=aa[5],
        data09=aa[6],
        data10=aa[7],
        data11=aa[8],
        data12=aa[9],
        data13=aa[10],
        data14=aa[11],
        data15=aa[12],
        data16=aa[13],
        data17=aa[14],
        data18=aa[15],
        data19=aa[16],
        data20=aa[17],
        data21=aa[18],
        data22=aa[19],
    )


def test(request):  # 测试

    培训类别 = {"上岗前培训", "资格培训", "复习培训", "附加培训", "追加培训", "补习培训"
        , "设备培训", "熟练培训", "专项培训",
            }
    for i in 培训类别:
        print(i)
        print('data' + str({i}))

    return render(request, 'ok.html', )
