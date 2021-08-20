import json
from django.shortcuts import render
from jianchabaogao import models
from atcInfo.models import info_02
import re
# Create your views here.

def showjianchabaogao(request):#获取检查报告记录页面
    data = models.jianchabaogao.objects.values_list().all()
    data = list(data)

    fileuri = []

    for i in data:
        fileuri.append(i)
    data = json.dumps(fileuri, ensure_ascii=False)

    print(data)
    return render(request, 'showjianchabaogao.html', {'data': data})

def indexjianchabaogao(request):
    return render(request, 'jianchabaogao.html')


def addjianchabaogao(request):  # 获取增加检查报告记录的数据并保存


    data01 = request.POST.get('keshi')
    if data01 == '0':
        data01 = '塔台'
    if data01 == '1':
        data01 = '区调'
    if data01 == '2':
        data01 = '飞服'

    data02 = request.POST.get('leixing')
    if data02 == '0':
        data02 = '日检查'
    if data02 == '1':
        data02 = '周检查'
    if data02 == '2':
        data02 = '月检查'

    data03 = request.POST.get('per')
    data04 = request.POST.get('data15')
    data05 = request.POST.get('data151')

    b = info_02.objects.get(data_01=data03)

    data06 = request.POST.get('zhibiao')
    data07 = request.POST.get('pingjia')
    if data06 == '0':
        data06 = '通话用语'
        if data07 != "表扬" and "正常":
           b.data_02 = int(b.data_02)-1
    if data06 == '1':
        data06 = '雷达监控'
        if data07 != "表扬" and "正常":
           b.data_03 = int(b.data_03) - 1
    if data06 == '2':
        data06 = '间隔效率'
        if data07 != "表扬" and "正常":
           b.data_04 = int(b.data_04) - 1
    if data06 == '3':
        data06 = '通报协调'
        if data07 != "表扬" and "正常":
           b.data_05 = int(b.data_05) - 1
    if data06 == '4':
        data06 = '管制程序'
        if data07 != "表扬" and "正常":
           b.data_06 =int(b.data_06) - 1
    if data06 == '5':
        data06 = '特情处置'
        if data07 != "表扬" and "正常":
           b.data_07 = int(b.data_07) - 1
    if data06 == '6':
        data06 = '其他情况'
        if data07 != "表扬" and "正常":
           b.data_08 = int(b.data_08) - 1

    if data07 == '0':
        data07 = '表扬'
    if data07 == '1':
        data07 = '正常'
    if data07 == '2':
        data07 = '技能缺陷'
    if data07 == '3':
        data07 = '现场纠违'
    if data07 == '4':
        data07 = '无后果违章'

    data08 = request.POST.get('miaoshu')

    a = models.jianchabaogao()
    a.frontdata1 = data01
    a.frontdata2 = data02
    a.frontdata3 = data03
    a.frontdata4 = data04
    a.frontdata5 = data05
    a.frontdata6 = data06
    a.frontdata7 = data07
    a.frontdata8 = data08

    a.is_active = 0
    a.save()
    b.is_active = 0
    b.save()

    return render(request, 'ok.html')

def find(request):
    data01 = request.POST.get('leixing')
    if data01 == '0':
        data01 = '日检查'
    if data01 == '1':
        data01 = '周检查'
    if data01 == '2':
        data01 = '月检查'
    if data01 == '3':
        data01 = '全部'
    data02 = request.POST.get('data15')
    data03 = request.POST.get('data151')
    if (data02!= '') and (data03!= ''):
         data02 = int(re.sub("\D", "", data02))
         data03 = int(re.sub("\D", "", data03))


    data = []

    if data01=='全部':
        dataq = models.jianchabaogao.objects.values_list().all()
        dataq = list(dataq)
        if (data02 or data03) == '':
            for i in dataq:
                data.append(i)
        else:
            for i in dataq:
                frontdata4 = int(re.sub("\D", "", i[4]))
                frontdata5 = int(re.sub("\D", "", i[5]))
                if (frontdata4 >= data02) and (frontdata5 <= data03):
                   data.append(i)
        data = json.dumps(data, ensure_ascii=False)

    elif data01 == '日检查':
        dataq = models.jianchabaogao.objects.filter(frontdata2 = data01)
        if (data02 or data03) == '':
            for i in dataq:
                fileuri = []
                fileuri.append(i.id)
                fileuri.append(i.frontdata1)
                fileuri.append(i.frontdata2)
                fileuri.append(i.frontdata3)
                fileuri.append(i.frontdata4)
                fileuri.append(i.frontdata5)
                fileuri.append(i.frontdata6)
                fileuri.append(i.frontdata7)
                fileuri.append(i.frontdata8)
                data.append(fileuri)
        else:
            for i in dataq:
                frontdata4 = int(re.sub("\D", "", i.frontdata4))
                frontdata5 = int(re.sub("\D", "", i.frontdata5))
                if (frontdata4 >= data02) and (frontdata5 <= data03):
                    fileuri = []
                    fileuri.append(i.id)
                    fileuri.append(i.frontdata1)
                    fileuri.append(i.frontdata2)
                    fileuri.append(i.frontdata3)
                    fileuri.append(i.frontdata4)
                    fileuri.append(i.frontdata5)
                    fileuri.append(i.frontdata6)
                    fileuri.append(i.frontdata7)
                    fileuri.append(i.frontdata8)
                    data.append(fileuri)

    else:
        dataq = models.jianchabaogao.objects.filter(frontdata2 = data01)
        if (data02 or data03) == '':
            for i in dataq:
                fileuri = []
                fileuri.append(i.id)
                fileuri.append(i.frontdata1)
                fileuri.append(i.frontdata2)
                fileuri.append(i.frontdata3)
                fileuri.append(i.frontdata4)
                fileuri.append(i.frontdata5)
                fileuri.append(i.frontdata6)
                fileuri.append(i.frontdata7)
                fileuri.append(i.frontdata8)
                data.append(fileuri)
        else:
            for i in dataq:
                frontdata4 = int(re.sub("\D", "", i.frontdata4))
                frontdata5 = int(re.sub("\D", "", i.frontdata5))
                if (frontdata4 >= data02) and (frontdata5 <= data03):
                    fileuri = []
                    fileuri.append(i.id)
                    fileuri.append(i.frontdata1)
                    fileuri.append(i.frontdata2)
                    fileuri.append(i.frontdata3)
                    fileuri.append(i.frontdata4)
                    fileuri.append(i.frontdata5)
                    fileuri.append(i.frontdata6)
                    fileuri.append(i.frontdata7)
                    fileuri.append(i.frontdata8)
                    data.append(fileuri)

    return render(request, 'showjianchabaogao.html', {'data': data})