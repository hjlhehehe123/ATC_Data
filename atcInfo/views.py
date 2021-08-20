import json
import os
from datetime import datetime

from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse, StreamingHttpResponse
from django.shortcuts import render
from django.utils.encoding import escape_uri_path

from atcInfo.models import info, info_01, info_02, info_03, info_04, info_05, info_06, info_07, info_08, info_09, \
    info_10, info_11, info_12, info_13, info_14, info_15, info_16, info_17, info_18
# Create your views here.
from trainningcompletion.models import trainningstatusdetail


def getinfo(request):
    name = ""
    if request.session.get('status'):
        name = request.session.get('name')

    context = {}
    if request.POST.get('人员'):
        选的人员 = request.POST.get('人员')
        context['选的人员'] = 选的人员
        name = 选的人员
    if request.GET.get('人员'):
        选的人员 = request.GET.get('人员')
        context['选的人员'] = 选的人员
        name = 选的人员

    人员 = 获取所有的登陆人()
    context['人员'] = 人员
    print('人员')
    print(人员)

    try:
        if info_01.objects.filter(data_01=name):
            print("已经有人员信息")
            print(name)
        else:
            info_01.objects.create(data_01=name, )
            info_02.objects.create(data_01=name, )
            info_03.objects.create(data_01=name, )
            info_04.objects.create(data_01=name, )
            info_05.objects.create(data_01=name, )
            info_06.objects.create(data_01=name, )
            info_07.objects.create(data_01=name, )
            info_08.objects.create(data_01=name, )
            info_09.objects.create(data_01=name, )
            info_10.objects.create(data_01=name, )
            info_11.objects.create(data_01=name, )
            info_12.objects.create(data_01=name, )
            info_13.objects.create(data_01=name, )
            info_14.objects.create(data_01=name, )
            info_15.objects.create(data_01=name, )
            info_16.objects.create(data_01=name, )
            info_17.objects.create(data_01=name, )
            info_18.objects.create(data_01=name, )

    except ObjectDoesNotExist:
        print('没查到')

    # getatcinfo = info.objects.get(id=1)
    # context['atcName'] = getatcinfo.atcName
    # context['atcOld'] = getatcinfo.atcOld
    try:
        getatcinfo01 = info_01.objects.get(data_01=name)
        # getatcinfo02 = info_02.objects.get(data_01=name)
        # getatcinfo03 = info_03.objects.get(data_01=name)
        # getatcinfo04 = info_04.objects.get(data_01=name)
        # getatcinfo05 = info_05.objects.get(data_01=name)
        # getatcinfo06 = info_06.objects.get(data_01=name)
        # getatcinfo07 = info_07.objects.get(data_01=name)
        # getatcinfo08 = info_08.objects.get(data_01=name)
        # getatcinfo09 = info_09.objects.get(data_01=name)
        # getatcinfo10 = info_10.objects.get(data_01=name)
        # getatcinfo11 = info_11.objects.get(data_01=name)
        # getatcinfo12 = info_12.objects.filter(data_01=name)
        # getatcinfo13 = info_13.objects.get(data_01=name)
        # getatcinfo14 = info_14.objects.get(data_01=name)
        # getatcinfo15 = info_15.objects.get(data_01=name)
        # getatcinfo16 = info_16.objects.get(data_01=name)
        # getatcinfo17 = info_17.objects.get(data_01=name)
        # getatcinfo18 = info_18.objects.get(data_01=name)
    except getatcinfo01.DoesNotExist:
        getatcinfo01 = None

    data_00_12 = info_12.objects.filter(data_01=name).values_list("id", "data_02", "data_03", "data_04", "data_05", )
    data_00_12 = list(data_00_12)
    a12 = []
    for i in data_00_12:
        a12.append(i)
    a12 = json.dumps(a12, ensure_ascii=False)
    context['data_00_12'] = a12
    print("data_00_12")
    print(data_00_12)

    a03 = []
    a04 = []
    a05 = []
    a06 = []
    a07 = []
    a08 = []
    a09 = []
    a10 = []
    a11 = []
    a12 = []
    a13 = []
    a14 = []
    a15 = []
    a16 = []
    a17 = []
    a18 = []
    for i in list(
            info_03.objects.filter(data_01=name).values_list("id", "data_02", "data_03", "data_04", "data_05",
                                                             "data_06",
                                                             "data_07", "data_08", )): a03.append(i)
    for i in list(
            info_04.objects.filter(data_01=name).values_list("id", "data_02", "data_03", "data_04", "data_05",
                                                             "data_06",
                                                             "data_07", )): a04.append(i)
    for i in list(
            info_05.objects.filter(data_01=name).values_list("id", "data_02", "data_03", "data_04", "data_05",
                                                             "data_06", )): a05.append(i)
    for i in list(
            info_06.objects.filter(data_01=name).values_list("id", "data_02", "data_03", "data_04", "data_05",
                                                             "data_06",
                                                             "data_07", )): a06.append(i)
    for i in list(
            info_07.objects.filter(data_01=name).values_list("id", "data_02", "data_03", "data_04", "data_05",
                                                             "data_06",
                                                             "data_07", "data_08", )): a07.append(i)
    for i in list(
            info_08.objects.filter(data_01=name).values_list("id", "data_02", "data_03", "data_04", "data_05",
                                                             "data_06",
                                                             "data_07", "data_08",
                                                             "data_09", "data_10", "data_11", "data_12", "data_13",
                                                             "data_14", "data_15",
                                                             "data_16", "data_17", "data_18", "data_19", "data_20",
                                                             "data_21", "data_22",
                                                             )): a08.append(i)
    for i in list(
            info_09.objects.filter(data_01=name).values_list("id", "data_02", "data_03", "data_04", "data_05",
                                                             "data_06", )): a09.append(i)
    for i in list(
            info_10.objects.filter(data_01=name).values_list("id", "data_02", "data_03", "data_04", "data_05",
                                                             "data_06",
                                                             "data_07", "data_08", "data_09", )): a10.append(i)
    for i in list(
            info_11.objects.filter(data_01=name).values_list("id", "data_02", "data_03", "data_04", )): a11.append(i)
    for i in list(
            info_12.objects.filter(data_01=name).values_list("id", "data_02", "data_03", "data_04",
                                                             "data_05", )): a12.append(
        i)
    for i in list(
            info_13.objects.filter(data_01=name).values_list("id", "data_02", "data_03", "data_04", "data_05",
                                                             "data_06", )): a13.append(i)
    for i in list(
            info_14.objects.filter(data_01=name).values_list("id", "data_02", "data_03", "data_04", "data_05",
                                                             "data_06", )): a14.append(i)
    for i in list(
            info_15.objects.filter(data_01=name).values_list("id", "data_02", "data_03", "data_04",
                                                             "data_05", )): a15.append(
        i)
    for i in list(
            info_16.objects.filter(data_01=name).values_list("id", "data_02", "data_03", "data_04", )): a16.append(i)
    for i in list(
            info_17.objects.filter(data_01=name).values_list("id", "data_02", "data_03", "data_04", "data_05",
                                                             "data_06",
                                                             "data_07", "data_08", )): a17.append(i)
    for i in list(
            info_18.objects.filter(data_01=name).values_list("id", "data_02", "data_03", "data_04", "data_05",
                                                             "data_06", )): a18.append(i)

    context['data_00_03'] = json.dumps(a03, ensure_ascii=False)
    context['data_00_04'] = json.dumps(a04, ensure_ascii=False)
    context['data_00_05'] = json.dumps(a05, ensure_ascii=False)
    context['data_00_06'] = json.dumps(a06, ensure_ascii=False)
    context['data_00_07'] = json.dumps(a07, ensure_ascii=False)

    context['data_00_09'] = json.dumps(a09, ensure_ascii=False)
    context['data_00_10'] = json.dumps(a10, ensure_ascii=False)
    context['data_00_11'] = json.dumps(a11, ensure_ascii=False)
    context['data_00_12'] = json.dumps(a12, ensure_ascii=False)
    context['data_00_13'] = json.dumps(a13, ensure_ascii=False)
    context['data_00_14'] = json.dumps(a14, ensure_ascii=False)
    context['data_00_15'] = json.dumps(a15, ensure_ascii=False)
    context['data_00_16'] = json.dumps(a16, ensure_ascii=False)
    context['data_00_17'] = json.dumps(a17, ensure_ascii=False)
    context['data_00_18'] = json.dumps(a18, ensure_ascii=False)

    context['data_00_01'] = getatcinfo01.id
    context['data_01_01'] = getatcinfo01.data_01
    context['data_02_01'] = getatcinfo01.data_02
    context['data_03_01'] = getatcinfo01.data_03
    context['data_04_01'] = getatcinfo01.data_04
    context['data_05_01'] = getatcinfo01.data_05
    context['data_06_01'] = getatcinfo01.data_06
    context['data_07_01'] = getatcinfo01.data_07
    context['data_08_01'] = getatcinfo01.data_08
    context['data_09_01'] = getatcinfo01.data_09
    context['data_10_01'] = getatcinfo01.data_10
    context['data_11_01'] = getatcinfo01.data_11
    context['data_12_01'] = getatcinfo01.data_12
    context['data_13_01'] = getatcinfo01.data_13
    context['data_14_01'] = getatcinfo01.data_14
    context['data_15_01'] = getatcinfo01.data_15
    context['data_16_01'] = getatcinfo01.data_16
    context['data_17_01'] = getatcinfo01.data_17
    context['data_18_01'] = getatcinfo01.data_18
    context['data_19_01'] = getatcinfo01.data_19
    context['data_20_01'] = getatcinfo01.data_20

    ff1 = info_03.objects \
        .filter().values_list().all()
    aa1 = ""
    for k in ff1:
        m = list(k)
        aa1 = aa1 + str(m[4]) + " "

    data = []
    培训类别 = ["上岗前培训", "资格培训", "复习培训", "附加培训", "追加培训", "补习培训"
        , "设备培训", "熟练培训", "专项培训", ]
    本人 = []
    本人.append(name)
    for xy in 本人:
        for lb in 培训类别:
            ii = []
            ff = trainningstatusdetail.objects \
                .filter().values_list().all()

            ggid1 = 1
            for k in ff:
                m = list(k)
                ee = []

                if xy in m[8].split():
                    # print(
                    #     " nf" + '*********' + '  ' )
                    # print( nf == datetime.strptime(m[13].split()[0], '%Y-%m-%d').year)

                    if lb == m[2]:
                        if m[11] != "0":
                            ee.append(ggid1)
                            ggid1 += 1
                            ee.append(str(datetime.strptime(m[13].split()[0], '%Y-%m-%d').year) + "年" + lb)
                            ee.append('管制运行部')
                            ee.append(m[6])
                            ee.append(lb)
                            ee.append(m[5])
                            ee.append(aa1)
                            ee.append('')
                            ee.append(m[13].split()[0] + "-" + m[13].split()[1])  # 开始时间
                            ee.append(m[13].split()[0] + "-" + m[13].split()[2])
                            ee.append('')
                            ee.append(float(m[11]) / float(m[10]))
                            ee.append('')

                            ee.append('')
                            ee.append('')
                            ee.append('')

                            ee.append(m[7])  # 培训教员
                            ee.append('')
                            ee.append('')
                            ee.append('')
                            ee.append('')
                            ee.append('')

                            data.append(ee)

    context['data_00_08'] = json.dumps(data, ensure_ascii=False)
    print('data_00_08')
    print()

    # context['data_01_02'] = getatcinfo02.data_01
    # context['data_02_02'] = getatcinfo02.data_02
    # context['data_03_02'] = getatcinfo02.data_03
    # context['data_04_02'] = getatcinfo02.data_04
    # context['data_05_02'] = getatcinfo02.data_05
    # context['data_06_02'] = getatcinfo02.data_06
    # context['data_07_02'] = getatcinfo02.data_07
    # context['data_08_02'] = getatcinfo02.data_08
    # context['data_09_02'] = getatcinfo02.data_09
    # context['data_10_02'] = getatcinfo02.data_10
    # context['data_11_02'] = getatcinfo02.data_11
    # context['data_12_02'] = getatcinfo02.data_12
    # context['data_13_02'] = getatcinfo02.data_13
    # context['data_14_02'] = getatcinfo02.data_14
    # context['data_15_02'] = getatcinfo02.data_15
    # context['data_16_02'] = getatcinfo02.data_16
    # context['data_17_02'] = getatcinfo02.data_17
    # context['data_18_02'] = getatcinfo02.data_18
    # context['data_19_02'] = getatcinfo02.data_19
    # context['data_20_02'] = getatcinfo02.data_20
    #
    # context['data_01_03'] = getatcinfo03.data_01
    # context['data_02_03'] = getatcinfo03.data_02
    # context['data_03_03'] = getatcinfo03.data_03
    # context['data_04_03'] = getatcinfo03.data_04
    # context['data_05_03'] = getatcinfo03.data_05
    # context['data_06_03'] = getatcinfo03.data_06
    # context['data_07_03'] = getatcinfo03.data_07
    # context['data_08_03'] = getatcinfo03.data_08
    # context['data_09_03'] = getatcinfo03.data_09
    # context['data_10_03'] = getatcinfo03.data_10
    # context['data_11_03'] = getatcinfo03.data_11
    # context['data_12_03'] = getatcinfo03.data_12
    # context['data_13_03'] = getatcinfo03.data_13
    # context['data_14_03'] = getatcinfo03.data_14
    # context['data_15_03'] = getatcinfo03.data_15
    # context['data_16_03'] = getatcinfo03.data_16
    # context['data_17_03'] = getatcinfo03.data_17
    # context['data_18_03'] = getatcinfo03.data_18
    # context['data_19_03'] = getatcinfo03.data_19
    # context['data_20_03'] = getatcinfo03.data_20
    #
    # context['data_01_04'] = getatcinfo04.data_01
    # context['data_02_04'] = getatcinfo04.data_02
    # context['data_03_04'] = getatcinfo04.data_03
    # context['data_04_04'] = getatcinfo04.data_04
    # context['data_05_04'] = getatcinfo04.data_05
    # context['data_06_04'] = getatcinfo04.data_06
    # context['data_07_04'] = getatcinfo04.data_07
    # context['data_08_04'] = getatcinfo04.data_08
    # context['data_09_04'] = getatcinfo04.data_09
    # context['data_10_04'] = getatcinfo04.data_10
    # context['data_11_04'] = getatcinfo04.data_11
    # context['data_12_04'] = getatcinfo04.data_12
    # context['data_13_04'] = getatcinfo04.data_13
    # context['data_14_04'] = getatcinfo04.data_14
    # context['data_15_04'] = getatcinfo04.data_15
    # context['data_16_04'] = getatcinfo04.data_16
    # context['data_17_04'] = getatcinfo04.data_17
    # context['data_18_04'] = getatcinfo04.data_18
    # context['data_19_04'] = getatcinfo04.data_19
    # context['data_20_04'] = getatcinfo04.data_20
    #
    # context['data_01_05'] = getatcinfo05.data_01
    # context['data_02_05'] = getatcinfo05.data_02
    # context['data_03_05'] = getatcinfo05.data_03
    # context['data_04_05'] = getatcinfo05.data_04
    # context['data_05_05'] = getatcinfo05.data_05
    # context['data_06_05'] = getatcinfo05.data_06
    # context['data_07_05'] = getatcinfo05.data_07
    # context['data_08_05'] = getatcinfo05.data_08
    # context['data_09_05'] = getatcinfo05.data_09
    # context['data_10_05'] = getatcinfo05.data_10
    # context['data_11_05'] = getatcinfo05.data_11
    # context['data_12_05'] = getatcinfo05.data_12
    # context['data_13_05'] = getatcinfo05.data_13
    # context['data_14_05'] = getatcinfo05.data_14
    # context['data_15_05'] = getatcinfo05.data_15
    # context['data_16_05'] = getatcinfo05.data_16
    # context['data_17_05'] = getatcinfo05.data_17
    # context['data_18_05'] = getatcinfo05.data_18
    # context['data_19_05'] = getatcinfo05.data_19
    # context['data_20_05'] = getatcinfo05.data_20
    #
    # context['data_01_06'] = getatcinfo06.data_01
    # context['data_02_06'] = getatcinfo06.data_02
    # context['data_03_06'] = getatcinfo06.data_03
    # context['data_04_06'] = getatcinfo06.data_04
    # context['data_05_06'] = getatcinfo06.data_05
    # context['data_06_06'] = getatcinfo06.data_06
    # context['data_07_06'] = getatcinfo06.data_07
    # context['data_08_06'] = getatcinfo06.data_08
    # context['data_09_06'] = getatcinfo06.data_09
    # context['data_10_06'] = getatcinfo06.data_10
    # context['data_11_06'] = getatcinfo06.data_11
    # context['data_12_06'] = getatcinfo06.data_12
    # context['data_13_06'] = getatcinfo06.data_13
    # context['data_14_06'] = getatcinfo06.data_14
    # context['data_15_06'] = getatcinfo06.data_15
    # context['data_16_06'] = getatcinfo06.data_16
    # context['data_17_06'] = getatcinfo06.data_17
    # context['data_18_06'] = getatcinfo06.data_18
    # context['data_19_06'] = getatcinfo06.data_19
    # context['data_20_06'] = getatcinfo06.data_20
    #
    # context['data_01_07'] = getatcinfo07.data_01
    # context['data_02_07'] = getatcinfo07.data_02
    # context['data_03_07'] = getatcinfo07.data_03
    # context['data_04_07'] = getatcinfo07.data_04
    # context['data_05_07'] = getatcinfo07.data_05
    # context['data_06_07'] = getatcinfo07.data_06
    # context['data_07_07'] = getatcinfo07.data_07
    # context['data_08_07'] = getatcinfo07.data_08
    # context['data_09_07'] = getatcinfo07.data_09
    # context['data_10_07'] = getatcinfo07.data_10
    # context['data_11_07'] = getatcinfo07.data_11
    # context['data_12_07'] = getatcinfo07.data_12
    # context['data_13_07'] = getatcinfo07.data_13
    # context['data_14_07'] = getatcinfo07.data_14
    # context['data_15_07'] = getatcinfo07.data_15
    # context['data_16_07'] = getatcinfo07.data_16
    # context['data_17_07'] = getatcinfo07.data_17
    # context['data_18_07'] = getatcinfo07.data_18
    # context['data_19_07'] = getatcinfo07.data_19
    # context['data_20_07'] = getatcinfo07.data_20
    #
    # context['data_01_08'] = getatcinfo08.data_01
    # context['data_02_08'] = getatcinfo08.data_02
    # context['data_03_08'] = getatcinfo08.data_03
    # context['data_04_08'] = getatcinfo08.data_04
    # context['data_05_08'] = getatcinfo08.data_05
    # context['data_06_08'] = getatcinfo08.data_06
    # context['data_07_08'] = getatcinfo08.data_07
    # context['data_08_08'] = getatcinfo08.data_08
    # context['data_09_08'] = getatcinfo08.data_09
    # context['data_10_08'] = getatcinfo08.data_10
    # context['data_11_08'] = getatcinfo08.data_11
    # context['data_12_08'] = getatcinfo08.data_12
    # context['data_13_08'] = getatcinfo08.data_13
    # context['data_14_08'] = getatcinfo08.data_14
    # context['data_15_08'] = getatcinfo08.data_15
    # context['data_16_08'] = getatcinfo08.data_16
    # context['data_17_08'] = getatcinfo08.data_17
    # context['data_18_08'] = getatcinfo08.data_18
    # context['data_19_08'] = getatcinfo08.data_19
    # context['data_20_08'] = getatcinfo08.data_20
    # context['data_21_08'] = getatcinfo08.data_21
    # context['data_22_08'] = getatcinfo08.data_22
    # context['data_23_08'] = getatcinfo08.data_23
    # context['data_24_08'] = getatcinfo08.data_24
    # context['data_25_08'] = getatcinfo08.data_25
    # context['data_26_08'] = getatcinfo08.data_26
    # context['data_27_08'] = getatcinfo08.data_27
    # context['data_28_08'] = getatcinfo08.data_28
    # context['data_29_08'] = getatcinfo08.data_29
    # context['data_30_08'] = getatcinfo08.data_30
    #
    # context['data_01_09'] = getatcinfo09.data_01
    # context['data_02_09'] = getatcinfo09.data_02
    # context['data_03_09'] = getatcinfo09.data_03
    # context['data_04_09'] = getatcinfo09.data_04
    # context['data_05_09'] = getatcinfo09.data_05
    # context['data_06_09'] = getatcinfo09.data_06
    # context['data_07_09'] = getatcinfo09.data_07
    # context['data_08_09'] = getatcinfo09.data_08
    # context['data_09_09'] = getatcinfo09.data_09
    # context['data_10_09'] = getatcinfo09.data_10
    # context['data_11_09'] = getatcinfo09.data_11
    # context['data_12_09'] = getatcinfo09.data_12
    # context['data_13_09'] = getatcinfo09.data_13
    # context['data_14_09'] = getatcinfo09.data_14
    # context['data_15_09'] = getatcinfo09.data_15
    # context['data_16_09'] = getatcinfo09.data_16
    # context['data_17_09'] = getatcinfo09.data_17
    # context['data_18_09'] = getatcinfo09.data_18
    # context['data_19_09'] = getatcinfo09.data_19
    # context['data_20_09'] = getatcinfo09.data_20
    #
    # context['data_01_10'] = getatcinfo10.data_01
    # context['data_02_10'] = getatcinfo10.data_02
    # context['data_03_10'] = getatcinfo10.data_03
    # context['data_04_10'] = getatcinfo10.data_04
    # context['data_05_10'] = getatcinfo10.data_05
    # context['data_06_10'] = getatcinfo10.data_06
    # context['data_07_10'] = getatcinfo10.data_07
    # context['data_08_10'] = getatcinfo10.data_08
    # context['data_09_10'] = getatcinfo10.data_09
    # context['data_10_10'] = getatcinfo10.data_10
    # context['data_11_10'] = getatcinfo10.data_11
    # context['data_12_10'] = getatcinfo10.data_12
    # context['data_13_10'] = getatcinfo10.data_13
    # context['data_14_10'] = getatcinfo10.data_14
    # context['data_15_10'] = getatcinfo10.data_15
    # context['data_16_10'] = getatcinfo10.data_16
    # context['data_17_10'] = getatcinfo10.data_17
    # context['data_18_10'] = getatcinfo10.data_18
    # context['data_19_10'] = getatcinfo10.data_19
    # context['data_20_10'] = getatcinfo10.data_20
    #
    # context['data_01_11'] = getatcinfo11.data_01
    # context['data_02_11'] = getatcinfo11.data_02
    # context['data_03_11'] = getatcinfo11.data_03
    # context['data_04_11'] = getatcinfo11.data_04
    # context['data_05_11'] = getatcinfo11.data_05
    # context['data_06_11'] = getatcinfo11.data_06
    # context['data_07_11'] = getatcinfo11.data_07
    # context['data_08_11'] = getatcinfo11.data_08
    # context['data_09_11'] = getatcinfo11.data_09
    # context['data_10_11'] = getatcinfo11.data_10
    # context['data_11_11'] = getatcinfo11.data_11
    # context['data_12_11'] = getatcinfo11.data_12
    # context['data_13_11'] = getatcinfo11.data_13
    # context['data_14_11'] = getatcinfo11.data_14
    # context['data_15_11'] = getatcinfo11.data_15
    # context['data_16_11'] = getatcinfo11.data_16
    # context['data_17_11'] = getatcinfo11.data_17
    # context['data_18_11'] = getatcinfo11.data_18
    # context['data_19_11'] = getatcinfo11.data_19
    # context['data_20_11'] = getatcinfo11.data_20
    #
    # # context['data_01_12'] = getatcinfo12.data_01
    # # context['data_02_12'] = getatcinfo12.data_02
    # # context['data_03_12'] = getatcinfo12.data_03
    # # context['data_04_12'] = getatcinfo12.data_04
    # # context['data_05_12'] = getatcinfo12.data_05
    # # context['data_06_12'] = getatcinfo12.data_06
    # # context['data_07_12'] = getatcinfo12.data_07
    # # context['data_08_12'] = getatcinfo12.data_08
    # # context['data_09_12'] = getatcinfo12.data_09
    # # context['data_10_12'] = getatcinfo12.data_10
    # # context['data_11_12'] = getatcinfo12.data_11
    # # context['data_12_12'] = getatcinfo12.data_12
    # # context['data_13_12'] = getatcinfo12.data_13
    # # context['data_14_12'] = getatcinfo12.data_14
    # # context['data_15_12'] = getatcinfo12.data_15
    # # context['data_16_12'] = getatcinfo12.data_16
    # # context['data_17_12'] = getatcinfo12.data_17
    # # context['data_18_12'] = getatcinfo12.data_18
    # # context['data_19_12'] = getatcinfo12.data_19
    # # context['data_20_12'] = getatcinfo12.data_20
    #
    # context['data_01_13'] = getatcinfo13.data_01
    # context['data_02_13'] = getatcinfo13.data_02
    # context['data_03_13'] = getatcinfo13.data_03
    # context['data_04_13'] = getatcinfo13.data_04
    # context['data_05_13'] = getatcinfo13.data_05
    # context['data_06_13'] = getatcinfo13.data_06
    # context['data_07_13'] = getatcinfo13.data_07
    # context['data_08_13'] = getatcinfo13.data_08
    # context['data_09_13'] = getatcinfo13.data_09
    # context['data_10_13'] = getatcinfo13.data_10
    # context['data_11_13'] = getatcinfo13.data_11
    # context['data_12_13'] = getatcinfo13.data_12
    # context['data_13_13'] = getatcinfo13.data_13
    # context['data_14_13'] = getatcinfo13.data_14
    # context['data_15_13'] = getatcinfo13.data_15
    # context['data_16_13'] = getatcinfo13.data_16
    # context['data_17_13'] = getatcinfo13.data_17
    # context['data_18_13'] = getatcinfo13.data_18
    # context['data_19_13'] = getatcinfo13.data_19
    # context['data_20_13'] = getatcinfo13.data_20
    #
    # context['data_01_14'] = getatcinfo14.data_01
    # context['data_02_14'] = getatcinfo14.data_02
    # context['data_03_14'] = getatcinfo14.data_03
    # context['data_04_14'] = getatcinfo14.data_04
    # context['data_05_14'] = getatcinfo14.data_05
    # context['data_06_14'] = getatcinfo14.data_06
    # context['data_07_14'] = getatcinfo14.data_07
    # context['data_08_14'] = getatcinfo14.data_08
    # context['data_09_14'] = getatcinfo14.data_09
    # context['data_10_14'] = getatcinfo14.data_10
    # context['data_11_14'] = getatcinfo14.data_11
    # context['data_12_14'] = getatcinfo14.data_12
    # context['data_13_14'] = getatcinfo14.data_13
    # context['data_14_14'] = getatcinfo14.data_14
    # context['data_15_14'] = getatcinfo14.data_15
    # context['data_16_14'] = getatcinfo14.data_16
    # context['data_17_14'] = getatcinfo14.data_17
    # context['data_18_14'] = getatcinfo14.data_18
    # context['data_19_14'] = getatcinfo14.data_19
    # context['data_20_14'] = getatcinfo14.data_20
    #
    # context['data_01_15'] = getatcinfo15.data_01
    # context['data_02_15'] = getatcinfo15.data_02
    # context['data_03_15'] = getatcinfo15.data_03
    # context['data_04_15'] = getatcinfo15.data_04
    # context['data_05_15'] = getatcinfo15.data_05
    # context['data_06_15'] = getatcinfo15.data_06
    # context['data_07_15'] = getatcinfo15.data_07
    # context['data_08_15'] = getatcinfo15.data_08
    # context['data_09_15'] = getatcinfo15.data_09
    # context['data_10_15'] = getatcinfo15.data_10
    # context['data_11_15'] = getatcinfo15.data_11
    # context['data_12_15'] = getatcinfo15.data_12
    # context['data_13_15'] = getatcinfo15.data_13
    # context['data_14_15'] = getatcinfo15.data_14
    # context['data_15_15'] = getatcinfo15.data_15
    # context['data_16_15'] = getatcinfo15.data_16
    # context['data_17_15'] = getatcinfo15.data_17
    # context['data_18_15'] = getatcinfo15.data_18
    # context['data_19_15'] = getatcinfo15.data_19
    # context['data_20_15'] = getatcinfo15.data_20
    #
    # context['data_01_16'] = getatcinfo16.data_01
    # context['data_02_16'] = getatcinfo16.data_02
    # context['data_03_16'] = getatcinfo16.data_03
    # context['data_04_16'] = getatcinfo16.data_04
    # context['data_05_16'] = getatcinfo16.data_05
    # context['data_06_16'] = getatcinfo16.data_06
    # context['data_07_16'] = getatcinfo16.data_07
    # context['data_08_16'] = getatcinfo16.data_08
    # context['data_09_16'] = getatcinfo16.data_09
    # context['data_10_16'] = getatcinfo16.data_10
    # context['data_11_16'] = getatcinfo16.data_11
    # context['data_12_16'] = getatcinfo16.data_12
    # context['data_13_16'] = getatcinfo16.data_13
    # context['data_14_16'] = getatcinfo16.data_14
    # context['data_15_16'] = getatcinfo16.data_15
    # context['data_16_16'] = getatcinfo16.data_16
    # context['data_17_16'] = getatcinfo16.data_17
    # context['data_18_16'] = getatcinfo16.data_18
    # context['data_19_16'] = getatcinfo16.data_19
    # context['data_20_16'] = getatcinfo16.data_20
    #
    # context['data_01_17'] = getatcinfo17.data_01
    # context['data_02_17'] = getatcinfo17.data_02
    # context['data_03_17'] = getatcinfo17.data_03
    # context['data_04_17'] = getatcinfo17.data_04
    # context['data_05_17'] = getatcinfo17.data_05
    # context['data_06_17'] = getatcinfo17.data_06
    # context['data_07_17'] = getatcinfo17.data_07
    # context['data_08_17'] = getatcinfo17.data_08
    # context['data_09_17'] = getatcinfo17.data_09
    # context['data_10_17'] = getatcinfo17.data_10
    # context['data_11_17'] = getatcinfo17.data_11
    # context['data_12_17'] = getatcinfo17.data_12
    # context['data_13_17'] = getatcinfo17.data_13
    # context['data_14_17'] = getatcinfo17.data_14
    # context['data_15_17'] = getatcinfo17.data_15
    # context['data_16_17'] = getatcinfo17.data_16
    # context['data_17_17'] = getatcinfo17.data_17
    # context['data_18_17'] = getatcinfo17.data_18
    # context['data_19_17'] = getatcinfo17.data_19
    # context['data_20_17'] = getatcinfo17.data_20
    #
    # context['data_01_18'] = getatcinfo18.data_01
    # context['data_02_18'] = getatcinfo18.data_02
    # context['data_03_18'] = getatcinfo18.data_03
    # context['data_04_18'] = getatcinfo18.data_04
    # context['data_05_18'] = getatcinfo18.data_05
    # context['data_06_18'] = getatcinfo18.data_06
    # context['data_07_18'] = getatcinfo18.data_07
    # context['data_08_18'] = getatcinfo18.data_08
    # context['data_09_18'] = getatcinfo18.data_09
    # context['data_10_18'] = getatcinfo18.data_10
    # context['data_11_18'] = getatcinfo18.data_11
    # context['data_12_18'] = getatcinfo18.data_12
    # context['data_13_18'] = getatcinfo18.data_13
    # context['data_14_18'] = getatcinfo18.data_14
    # context['data_15_18'] = getatcinfo18.data_15
    # context['data_16_18'] = getatcinfo18.data_16
    # context['data_17_18'] = getatcinfo18.data_17
    # context['data_18_18'] = getatcinfo18.data_18
    # context['data_19_18'] = getatcinfo18.data_19
    # context['data_20_18'] = getatcinfo18.data_20
    #

    import numpy as np
    import matplotlib.pyplot as plt
    plt.rcParams['font.sans-serif'] = 'SimHei'
    plt.rcParams['axes.unicode_minus'] = False
    plt.style.use('ggplot')
    values = [90, 89, 95, 98, 100, 92, 96]

    feature = np.array(['通话用语', '通话用语', '其他', '特情处置', '管制程序', '通报协调', '间隔效率', '雷达监控'])  # 标签
    angles = np.linspace(0, 2 * np.pi, len(values), endpoint=False)
    values = np.concatenate((values, [values[0]]))
    angles = np.concatenate((angles, [angles[0]]))
    fig = plt.figure()
    ax = fig.add_subplot(111, polar=True)
    ax.fill(angles, values, 'o-', linewidth=2, alpha=0.2)
    ax.fill(angles, values, alpha=0.1)
    ax.set_thetagrids(angles * 180 / np.pi, feature)  # 添加标签
    ax.set_ylim(0, 100)
    plt.title('关键指标雷达图')
    ax.grid(True)
    plt.savefig('E:/pythonproject/ATC_data/static/' + context['data_01_01'] + '_01.jpg')
    # plt.show()
    # E: / demo / project1 / img / test.jpg
    return render(request, 'personinfo.html', context)


def getinfo_save(request):
    name = ""
    if request.session.get('status'):
        name = request.session.get('name')

    context = {}
    if request.POST.get('人员'):
        选的人员 = request.POST.get('人员')
        context['选的人员'] = 选的人员
        name = 选的人员
    人员 = 获取所有的登陆人()

    context['人员'] = 人员
    print('人员')
    print(人员)

    info_01.objects.filter(data_01=request.POST.get('data_01_01')).update(data_02=request.POST.get('data_02_01'))
    info_01.objects.filter(data_01=request.POST.get('data_01_01')).update(data_03=request.POST.get('data_03_01'))
    info_01.objects.filter(data_01=request.POST.get('data_01_01')).update(data_04=request.POST.get('data_04_01'))
    info_01.objects.filter(data_01=request.POST.get('data_01_01')).update(data_05=request.POST.get('data_05_01'))
    info_01.objects.filter(data_01=request.POST.get('data_01_01')).update(data_06=request.POST.get('data_06_01'))
    info_01.objects.filter(data_01=request.POST.get('data_01_01')).update(data_07=request.POST.get('data_07_01'))
    info_01.objects.filter(data_01=request.POST.get('data_01_01')).update(data_08=request.POST.get('data_08_01'))
    info_01.objects.filter(data_01=request.POST.get('data_01_01')).update(data_09=request.POST.get('data_09_01'))
    info_01.objects.filter(data_01=request.POST.get('data_01_01')).update(data_10=request.POST.get('data_10_01'))
    info_01.objects.filter(data_01=request.POST.get('data_01_01')).update(data_11=request.POST.get('data_11_01'))
    info_01.objects.filter(data_01=request.POST.get('data_01_01')).update(data_12=request.POST.get('data_12_01'))
    info_01.objects.filter(data_01=request.POST.get('data_01_01')).update(data_13=request.POST.get('data_13_01'))
    info_01.objects.filter(data_01=request.POST.get('data_01_01')).update(data_14=request.POST.get('data_14_01'))
    info_01.objects.filter(data_01=request.POST.get('data_01_01')).update(data_15=request.POST.get('data_15_01'))
    info_01.objects.filter(data_01=request.POST.get('data_01_01')).update(data_16=request.POST.get('data_16_01'))
    info_01.objects.filter(data_01=request.POST.get('data_01_01')).update(data_17=request.POST.get('data_17_01'))
    info_01.objects.filter(data_01=request.POST.get('data_01_01')).update(data_18=request.POST.get('data_18_01'))
    info_01.objects.filter(data_01=request.POST.get('data_01_01')).update(data_19=request.POST.get('data_19_01'))
    info_01.objects.filter(data_01=request.POST.get('data_01_01')).update(data_20=request.POST.get('data_20_01'))

    info_02.objects.filter(data_01=request.POST.get('data_01_01')).update(data_02=request.POST.get('data_02_02'))
    info_02.objects.filter(data_01=request.POST.get('data_01_01')).update(data_03=request.POST.get('data_03_02'))
    info_02.objects.filter(data_01=request.POST.get('data_01_01')).update(data_04=request.POST.get('data_04_02'))
    info_02.objects.filter(data_01=request.POST.get('data_01_01')).update(data_05=request.POST.get('data_05_02'))
    info_02.objects.filter(data_01=request.POST.get('data_01_01')).update(data_06=request.POST.get('data_06_02'))
    info_02.objects.filter(data_01=request.POST.get('data_01_01')).update(data_07=request.POST.get('data_07_02'))
    info_02.objects.filter(data_01=request.POST.get('data_01_01')).update(data_08=request.POST.get('data_08_02'))
    info_02.objects.filter(data_01=request.POST.get('data_01_01')).update(data_09=request.POST.get('data_09_02'))
    info_02.objects.filter(data_01=request.POST.get('data_01_01')).update(data_10=request.POST.get('data_10_02'))
    info_02.objects.filter(data_01=request.POST.get('data_01_01')).update(data_11=request.POST.get('data_11_02'))
    info_02.objects.filter(data_01=request.POST.get('data_01_01')).update(data_12=request.POST.get('data_12_02'))
    info_02.objects.filter(data_01=request.POST.get('data_01_01')).update(data_13=request.POST.get('data_13_02'))
    info_02.objects.filter(data_01=request.POST.get('data_01_01')).update(data_14=request.POST.get('data_14_02'))
    info_02.objects.filter(data_01=request.POST.get('data_01_01')).update(data_15=request.POST.get('data_15_02'))
    info_02.objects.filter(data_01=request.POST.get('data_01_01')).update(data_16=request.POST.get('data_16_02'))
    info_02.objects.filter(data_01=request.POST.get('data_01_01')).update(data_17=request.POST.get('data_17_02'))
    info_02.objects.filter(data_01=request.POST.get('data_01_01')).update(data_18=request.POST.get('data_18_02'))
    info_02.objects.filter(data_01=request.POST.get('data_01_01')).update(data_19=request.POST.get('data_19_02'))
    info_02.objects.filter(data_01=request.POST.get('data_01_01')).update(data_20=request.POST.get('data_20_02'))

    # info_03.objects.filter(data_01=request.POST.get('data_01_01')).update(data_02=request.POST.get('data_02_03'))
    # info_03.objects.filter(data_01=request.POST.get('data_01_01')).update(data_03=request.POST.get('data_03_03'))
    # info_03.objects.filter(data_01=request.POST.get('data_01_01')).update(data_04=request.POST.get('data_04_03'))
    # info_03.objects.filter(data_01=request.POST.get('data_01_01')).update(data_05=request.POST.get('data_05_03'))
    # info_03.objects.filter(data_01=request.POST.get('data_01_01')).update(data_06=request.POST.get('data_06_03'))
    # info_03.objects.filter(data_01=request.POST.get('data_01_01')).update(data_07=request.POST.get('data_07_03'))
    # info_03.objects.filter(data_01=request.POST.get('data_01_01')).update(data_08=request.POST.get('data_08_03'))
    # info_03.objects.filter(data_01=request.POST.get('data_01_01')).update(data_09=request.POST.get('data_09_03'))
    # info_03.objects.filter(data_01=request.POST.get('data_01_01')).update(data_10=request.POST.get('data_10_03'))
    # info_03.objects.filter(data_01=request.POST.get('data_01_01')).update(data_11=request.POST.get('data_11_03'))
    # info_03.objects.filter(data_01=request.POST.get('data_01_01')).update(data_12=request.POST.get('data_12_03'))
    # info_03.objects.filter(data_01=request.POST.get('data_01_01')).update(data_13=request.POST.get('data_13_03'))
    # info_03.objects.filter(data_01=request.POST.get('data_01_01')).update(data_14=request.POST.get('data_14_03'))
    # info_03.objects.filter(data_01=request.POST.get('data_01_01')).update(data_15=request.POST.get('data_15_03'))
    # info_03.objects.filter(data_01=request.POST.get('data_01_01')).update(data_16=request.POST.get('data_16_03'))
    # info_03.objects.filter(data_01=request.POST.get('data_01_01')).update(data_17=request.POST.get('data_17_03'))
    # info_03.objects.filter(data_01=request.POST.get('data_01_01')).update(data_18=request.POST.get('data_18_03'))
    # info_03.objects.filter(data_01=request.POST.get('data_01_01')).update(data_19=request.POST.get('data_19_03'))
    # info_03.objects.filter(data_01=request.POST.get('data_01_01')).update(data_20=request.POST.get('data_20_03'))
    #
    # info_04.objects.filter(data_01=request.POST.get('data_01_01')).update(data_02=request.POST.get('data_02_04'))
    # info_04.objects.filter(data_01=request.POST.get('data_01_01')).update(data_03=request.POST.get('data_03_04'))
    # info_04.objects.filter(data_01=request.POST.get('data_01_01')).update(data_04=request.POST.get('data_04_04'))
    # info_04.objects.filter(data_01=request.POST.get('data_01_01')).update(data_05=request.POST.get('data_05_04'))
    # info_04.objects.filter(data_01=request.POST.get('data_01_01')).update(data_06=request.POST.get('data_06_04'))
    # info_04.objects.filter(data_01=request.POST.get('data_01_01')).update(data_07=request.POST.get('data_07_04'))
    # info_04.objects.filter(data_01=request.POST.get('data_01_01')).update(data_08=request.POST.get('data_08_04'))
    # info_04.objects.filter(data_01=request.POST.get('data_01_01')).update(data_09=request.POST.get('data_09_04'))
    # info_04.objects.filter(data_01=request.POST.get('data_01_01')).update(data_10=request.POST.get('data_10_04'))
    # info_04.objects.filter(data_01=request.POST.get('data_01_01')).update(data_11=request.POST.get('data_11_04'))
    # info_04.objects.filter(data_01=request.POST.get('data_01_01')).update(data_12=request.POST.get('data_12_04'))
    # info_04.objects.filter(data_01=request.POST.get('data_01_01')).update(data_13=request.POST.get('data_13_04'))
    # info_04.objects.filter(data_01=request.POST.get('data_01_01')).update(data_14=request.POST.get('data_14_04'))
    # info_04.objects.filter(data_01=request.POST.get('data_01_01')).update(data_15=request.POST.get('data_15_04'))
    # info_04.objects.filter(data_01=request.POST.get('data_01_01')).update(data_16=request.POST.get('data_16_04'))
    # info_04.objects.filter(data_01=request.POST.get('data_01_01')).update(data_17=request.POST.get('data_17_04'))
    # info_04.objects.filter(data_01=request.POST.get('data_01_01')).update(data_18=request.POST.get('data_18_04'))
    # info_04.objects.filter(data_01=request.POST.get('data_01_01')).update(data_19=request.POST.get('data_19_04'))
    # info_04.objects.filter(data_01=request.POST.get('data_01_01')).update(data_20=request.POST.get('data_20_04'))
    #
    # info_05.objects.filter(data_01=request.POST.get('data_01_01')).update(data_02=request.POST.get('data_02_05'))
    # info_05.objects.filter(data_01=request.POST.get('data_01_01')).update(data_03=request.POST.get('data_03_05'))
    # info_05.objects.filter(data_01=request.POST.get('data_01_01')).update(data_04=request.POST.get('data_04_05'))
    # info_05.objects.filter(data_01=request.POST.get('data_01_01')).update(data_05=request.POST.get('data_05_05'))
    # info_05.objects.filter(data_01=request.POST.get('data_01_01')).update(data_06=request.POST.get('data_06_05'))
    # info_05.objects.filter(data_01=request.POST.get('data_01_01')).update(data_07=request.POST.get('data_07_05'))
    # info_05.objects.filter(data_01=request.POST.get('data_01_01')).update(data_08=request.POST.get('data_08_05'))
    # info_05.objects.filter(data_01=request.POST.get('data_01_01')).update(data_09=request.POST.get('data_09_05'))
    # info_05.objects.filter(data_01=request.POST.get('data_01_01')).update(data_10=request.POST.get('data_10_05'))
    # info_05.objects.filter(data_01=request.POST.get('data_01_01')).update(data_11=request.POST.get('data_11_05'))
    # info_05.objects.filter(data_01=request.POST.get('data_01_01')).update(data_12=request.POST.get('data_12_05'))
    # info_05.objects.filter(data_01=request.POST.get('data_01_01')).update(data_13=request.POST.get('data_13_05'))
    # info_05.objects.filter(data_01=request.POST.get('data_01_01')).update(data_14=request.POST.get('data_14_05'))
    # info_05.objects.filter(data_01=request.POST.get('data_01_01')).update(data_15=request.POST.get('data_15_05'))
    # info_05.objects.filter(data_01=request.POST.get('data_01_01')).update(data_16=request.POST.get('data_16_05'))
    # info_05.objects.filter(data_01=request.POST.get('data_01_01')).update(data_17=request.POST.get('data_17_05'))
    # info_05.objects.filter(data_01=request.POST.get('data_01_01')).update(data_18=request.POST.get('data_18_05'))
    # info_05.objects.filter(data_01=request.POST.get('data_01_01')).update(data_19=request.POST.get('data_19_05'))
    # info_05.objects.filter(data_01=request.POST.get('data_01_01')).update(data_20=request.POST.get('data_20_05'))
    #
    # info_06.objects.filter(data_01=request.POST.get('data_01_01')).update(data_02=request.POST.get('data_02_06'))
    # info_06.objects.filter(data_01=request.POST.get('data_01_01')).update(data_03=request.POST.get('data_03_06'))
    # info_06.objects.filter(data_01=request.POST.get('data_01_01')).update(data_04=request.POST.get('data_04_06'))
    # info_06.objects.filter(data_01=request.POST.get('data_01_01')).update(data_05=request.POST.get('data_05_06'))
    # info_06.objects.filter(data_01=request.POST.get('data_01_01')).update(data_06=request.POST.get('data_06_06'))
    # info_06.objects.filter(data_01=request.POST.get('data_01_01')).update(data_07=request.POST.get('data_07_06'))
    # info_06.objects.filter(data_01=request.POST.get('data_01_01')).update(data_08=request.POST.get('data_08_06'))
    # info_06.objects.filter(data_01=request.POST.get('data_01_01')).update(data_09=request.POST.get('data_09_06'))
    # info_06.objects.filter(data_01=request.POST.get('data_01_01')).update(data_10=request.POST.get('data_10_06'))
    # info_06.objects.filter(data_01=request.POST.get('data_01_01')).update(data_11=request.POST.get('data_11_06'))
    # info_06.objects.filter(data_01=request.POST.get('data_01_01')).update(data_12=request.POST.get('data_12_06'))
    # info_06.objects.filter(data_01=request.POST.get('data_01_01')).update(data_13=request.POST.get('data_13_06'))
    # info_06.objects.filter(data_01=request.POST.get('data_01_01')).update(data_14=request.POST.get('data_14_06'))
    # info_06.objects.filter(data_01=request.POST.get('data_01_01')).update(data_15=request.POST.get('data_15_06'))
    # info_06.objects.filter(data_01=request.POST.get('data_01_01')).update(data_16=request.POST.get('data_16_06'))
    # info_06.objects.filter(data_01=request.POST.get('data_01_01')).update(data_17=request.POST.get('data_17_06'))
    # info_06.objects.filter(data_01=request.POST.get('data_01_01')).update(data_18=request.POST.get('data_18_06'))
    # info_06.objects.filter(data_01=request.POST.get('data_01_01')).update(data_19=request.POST.get('data_19_06'))
    # info_06.objects.filter(data_01=request.POST.get('data_01_01')).update(data_20=request.POST.get('data_20_06'))
    #
    # info_07.objects.filter(data_01=request.POST.get('data_01_01')).update(data_02=request.POST.get('data_02_07'))
    # info_07.objects.filter(data_01=request.POST.get('data_01_01')).update(data_03=request.POST.get('data_03_07'))
    # info_07.objects.filter(data_01=request.POST.get('data_01_01')).update(data_04=request.POST.get('data_04_07'))
    # info_07.objects.filter(data_01=request.POST.get('data_01_01')).update(data_05=request.POST.get('data_05_07'))
    # info_07.objects.filter(data_01=request.POST.get('data_01_01')).update(data_06=request.POST.get('data_06_07'))
    # info_07.objects.filter(data_01=request.POST.get('data_01_01')).update(data_07=request.POST.get('data_07_07'))
    # info_07.objects.filter(data_01=request.POST.get('data_01_01')).update(data_08=request.POST.get('data_08_07'))
    # info_07.objects.filter(data_01=request.POST.get('data_01_01')).update(data_09=request.POST.get('data_09_07'))
    # info_07.objects.filter(data_01=request.POST.get('data_01_01')).update(data_10=request.POST.get('data_10_07'))
    # info_07.objects.filter(data_01=request.POST.get('data_01_01')).update(data_11=request.POST.get('data_11_07'))
    # info_07.objects.filter(data_01=request.POST.get('data_01_01')).update(data_12=request.POST.get('data_12_07'))
    # info_07.objects.filter(data_01=request.POST.get('data_01_01')).update(data_13=request.POST.get('data_13_07'))
    # info_07.objects.filter(data_01=request.POST.get('data_01_01')).update(data_14=request.POST.get('data_14_07'))
    # info_07.objects.filter(data_01=request.POST.get('data_01_01')).update(data_15=request.POST.get('data_15_07'))
    # info_07.objects.filter(data_01=request.POST.get('data_01_01')).update(data_16=request.POST.get('data_16_07'))
    # info_07.objects.filter(data_01=request.POST.get('data_01_01')).update(data_17=request.POST.get('data_17_07'))
    # info_07.objects.filter(data_01=request.POST.get('data_01_01')).update(data_18=request.POST.get('data_18_07'))
    # info_07.objects.filter(data_01=request.POST.get('data_01_01')).update(data_19=request.POST.get('data_19_07'))
    # info_07.objects.filter(data_01=request.POST.get('data_01_01')).update(data_20=request.POST.get('data_20_07'))
    #
    # info_08.objects.filter(data_01=request.POST.get('data_01_01')).update(data_02=request.POST.get('data_02_08'))
    # info_08.objects.filter(data_01=request.POST.get('data_01_01')).update(data_03=request.POST.get('data_03_08'))
    # info_08.objects.filter(data_01=request.POST.get('data_01_01')).update(data_04=request.POST.get('data_04_08'))
    # info_08.objects.filter(data_01=request.POST.get('data_01_01')).update(data_05=request.POST.get('data_05_08'))
    # info_08.objects.filter(data_01=request.POST.get('data_01_01')).update(data_06=request.POST.get('data_06_08'))
    # info_08.objects.filter(data_01=request.POST.get('data_01_01')).update(data_07=request.POST.get('data_07_08'))
    # info_08.objects.filter(data_01=request.POST.get('data_01_01')).update(data_08=request.POST.get('data_08_08'))
    # info_08.objects.filter(data_01=request.POST.get('data_01_01')).update(data_09=request.POST.get('data_09_08'))
    # info_08.objects.filter(data_01=request.POST.get('data_01_01')).update(data_10=request.POST.get('data_10_08'))
    # info_08.objects.filter(data_01=request.POST.get('data_01_01')).update(data_11=request.POST.get('data_11_08'))
    # info_08.objects.filter(data_01=request.POST.get('data_01_01')).update(data_12=request.POST.get('data_12_08'))
    # info_08.objects.filter(data_01=request.POST.get('data_01_01')).update(data_13=request.POST.get('data_13_08'))
    # info_08.objects.filter(data_01=request.POST.get('data_01_01')).update(data_14=request.POST.get('data_14_08'))
    # info_08.objects.filter(data_01=request.POST.get('data_01_01')).update(data_15=request.POST.get('data_15_08'))
    # info_08.objects.filter(data_01=request.POST.get('data_01_01')).update(data_16=request.POST.get('data_16_08'))
    # info_08.objects.filter(data_01=request.POST.get('data_01_01')).update(data_17=request.POST.get('data_17_08'))
    # info_08.objects.filter(data_01=request.POST.get('data_01_01')).update(data_18=request.POST.get('data_18_08'))
    # info_08.objects.filter(data_01=request.POST.get('data_01_01')).update(data_19=request.POST.get('data_19_08'))
    # info_08.objects.filter(data_01=request.POST.get('data_01_01')).update(data_20=request.POST.get('data_20_08'))
    # info_08.objects.filter(data_01=request.POST.get('data_01_01')).update(data_21=request.POST.get('data_21_08'))
    # info_08.objects.filter(data_01=request.POST.get('data_01_01')).update(data_22=request.POST.get('data_22_08'))
    # info_08.objects.filter(data_01=request.POST.get('data_01_01')).update(data_23=request.POST.get('data_23_08'))
    # info_08.objects.filter(data_01=request.POST.get('data_01_01')).update(data_24=request.POST.get('data_24_08'))
    # info_08.objects.filter(data_01=request.POST.get('data_01_01')).update(data_25=request.POST.get('data_25_08'))
    # info_08.objects.filter(data_01=request.POST.get('data_01_01')).update(data_26=request.POST.get('data_26_08'))
    # info_08.objects.filter(data_01=request.POST.get('data_01_01')).update(data_27=request.POST.get('data_27_08'))
    # info_08.objects.filter(data_01=request.POST.get('data_01_01')).update(data_28=request.POST.get('data_28_08'))
    # info_08.objects.filter(data_01=request.POST.get('data_01_01')).update(data_29=request.POST.get('data_29_08'))
    # info_08.objects.filter(data_01=request.POST.get('data_01_01')).update(data_30=request.POST.get('data_30_08'))
    #
    # info_09.objects.filter(data_01=request.POST.get('data_01_01')).update(data_02=request.POST.get('data_02_09'))
    # info_09.objects.filter(data_01=request.POST.get('data_01_01')).update(data_03=request.POST.get('data_03_09'))
    # info_09.objects.filter(data_01=request.POST.get('data_01_01')).update(data_04=request.POST.get('data_04_09'))
    # info_09.objects.filter(data_01=request.POST.get('data_01_01')).update(data_05=request.POST.get('data_05_09'))
    # info_09.objects.filter(data_01=request.POST.get('data_01_01')).update(data_06=request.POST.get('data_06_09'))
    # info_09.objects.filter(data_01=request.POST.get('data_01_01')).update(data_07=request.POST.get('data_07_09'))
    # info_09.objects.filter(data_01=request.POST.get('data_01_01')).update(data_08=request.POST.get('data_08_09'))
    # info_09.objects.filter(data_01=request.POST.get('data_01_01')).update(data_09=request.POST.get('data_09_09'))
    # info_09.objects.filter(data_01=request.POST.get('data_01_01')).update(data_10=request.POST.get('data_10_09'))
    # info_09.objects.filter(data_01=request.POST.get('data_01_01')).update(data_11=request.POST.get('data_11_09'))
    # info_09.objects.filter(data_01=request.POST.get('data_01_01')).update(data_12=request.POST.get('data_12_09'))
    # info_09.objects.filter(data_01=request.POST.get('data_01_01')).update(data_13=request.POST.get('data_13_09'))
    # info_09.objects.filter(data_01=request.POST.get('data_01_01')).update(data_14=request.POST.get('data_14_09'))
    # info_09.objects.filter(data_01=request.POST.get('data_01_01')).update(data_15=request.POST.get('data_15_09'))
    # info_09.objects.filter(data_01=request.POST.get('data_01_01')).update(data_16=request.POST.get('data_16_09'))
    # info_09.objects.filter(data_01=request.POST.get('data_01_01')).update(data_17=request.POST.get('data_17_09'))
    # info_09.objects.filter(data_01=request.POST.get('data_01_01')).update(data_18=request.POST.get('data_18_09'))
    # info_09.objects.filter(data_01=request.POST.get('data_01_01')).update(data_19=request.POST.get('data_19_09'))
    # info_09.objects.filter(data_01=request.POST.get('data_01_01')).update(data_20=request.POST.get('data_20_09'))
    #
    # info_10.objects.filter(data_01=request.POST.get('data_01_01')).update(data_02=request.POST.get('data_02_10'))
    # info_10.objects.filter(data_01=request.POST.get('data_01_01')).update(data_03=request.POST.get('data_03_10'))
    # info_10.objects.filter(data_01=request.POST.get('data_01_01')).update(data_04=request.POST.get('data_04_10'))
    # info_10.objects.filter(data_01=request.POST.get('data_01_01')).update(data_05=request.POST.get('data_05_10'))
    # info_10.objects.filter(data_01=request.POST.get('data_01_01')).update(data_06=request.POST.get('data_06_10'))
    # info_10.objects.filter(data_01=request.POST.get('data_01_01')).update(data_07=request.POST.get('data_07_10'))
    # info_10.objects.filter(data_01=request.POST.get('data_01_01')).update(data_08=request.POST.get('data_08_10'))
    # info_10.objects.filter(data_01=request.POST.get('data_01_01')).update(data_09=request.POST.get('data_09_10'))
    # info_10.objects.filter(data_01=request.POST.get('data_01_01')).update(data_10=request.POST.get('data_10_10'))
    # info_10.objects.filter(data_01=request.POST.get('data_01_01')).update(data_11=request.POST.get('data_11_10'))
    # info_10.objects.filter(data_01=request.POST.get('data_01_01')).update(data_12=request.POST.get('data_12_10'))
    # info_10.objects.filter(data_01=request.POST.get('data_01_01')).update(data_13=request.POST.get('data_13_10'))
    # info_10.objects.filter(data_01=request.POST.get('data_01_01')).update(data_14=request.POST.get('data_14_10'))
    # info_10.objects.filter(data_01=request.POST.get('data_01_01')).update(data_15=request.POST.get('data_15_10'))
    # info_10.objects.filter(data_01=request.POST.get('data_01_01')).update(data_16=request.POST.get('data_16_10'))
    # info_10.objects.filter(data_01=request.POST.get('data_01_01')).update(data_17=request.POST.get('data_17_10'))
    # info_10.objects.filter(data_01=request.POST.get('data_01_01')).update(data_18=request.POST.get('data_18_10'))
    # info_10.objects.filter(data_01=request.POST.get('data_01_01')).update(data_19=request.POST.get('data_19_10'))
    # info_10.objects.filter(data_01=request.POST.get('data_01_01')).update(data_20=request.POST.get('data_20_10'))
    #
    # info_11.objects.filter(data_01=request.POST.get('data_01_01')).update(data_02=request.POST.get('data_02_11'))
    # info_11.objects.filter(data_01=request.POST.get('data_01_01')).update(data_03=request.POST.get('data_03_11'))
    # info_11.objects.filter(data_01=request.POST.get('data_01_01')).update(data_04=request.POST.get('data_04_11'))
    # info_11.objects.filter(data_01=request.POST.get('data_01_01')).update(data_05=request.POST.get('data_05_11'))
    # info_11.objects.filter(data_01=request.POST.get('data_01_01')).update(data_06=request.POST.get('data_06_11'))
    # info_11.objects.filter(data_01=request.POST.get('data_01_01')).update(data_07=request.POST.get('data_07_11'))
    # info_11.objects.filter(data_01=request.POST.get('data_01_01')).update(data_08=request.POST.get('data_08_11'))
    # info_11.objects.filter(data_01=request.POST.get('data_01_01')).update(data_09=request.POST.get('data_09_11'))
    # info_11.objects.filter(data_01=request.POST.get('data_01_01')).update(data_10=request.POST.get('data_10_11'))
    # info_11.objects.filter(data_01=request.POST.get('data_01_01')).update(data_11=request.POST.get('data_11_11'))
    # info_11.objects.filter(data_01=request.POST.get('data_01_01')).update(data_12=request.POST.get('data_12_11'))
    # info_11.objects.filter(data_01=request.POST.get('data_01_01')).update(data_13=request.POST.get('data_13_11'))
    # info_11.objects.filter(data_01=request.POST.get('data_01_01')).update(data_14=request.POST.get('data_14_11'))
    # info_11.objects.filter(data_01=request.POST.get('data_01_01')).update(data_15=request.POST.get('data_15_11'))
    # info_11.objects.filter(data_01=request.POST.get('data_01_01')).update(data_16=request.POST.get('data_16_11'))
    # info_11.objects.filter(data_01=request.POST.get('data_01_01')).update(data_17=request.POST.get('data_17_11'))
    # info_11.objects.filter(data_01=request.POST.get('data_01_01')).update(data_18=request.POST.get('data_18_11'))
    # info_11.objects.filter(data_01=request.POST.get('data_01_01')).update(data_19=request.POST.get('data_19_11'))
    # info_11.objects.filter(data_01=request.POST.get('data_01_01')).update(data_20=request.POST.get('data_20_11'))
    #
    # info_12.objects.filter(data_01=request.POST.get('data_01_01')).update(data_02=request.POST.get('data_02_12'))
    # info_12.objects.filter(data_01=request.POST.get('data_01_01')).update(data_03=request.POST.get('data_03_12'))
    # info_12.objects.filter(data_01=request.POST.get('data_01_01')).update(data_04=request.POST.get('data_04_12'))
    # info_12.objects.filter(data_01=request.POST.get('data_01_01')).update(data_05=request.POST.get('data_05_12'))
    # info_12.objects.filter(data_01=request.POST.get('data_01_01')).update(data_06=request.POST.get('data_06_12'))
    # info_12.objects.filter(data_01=request.POST.get('data_01_01')).update(data_07=request.POST.get('data_07_12'))
    # info_12.objects.filter(data_01=request.POST.get('data_01_01')).update(data_08=request.POST.get('data_08_12'))
    # info_12.objects.filter(data_01=request.POST.get('data_01_01')).update(data_09=request.POST.get('data_09_12'))
    # info_12.objects.filter(data_01=request.POST.get('data_01_01')).update(data_10=request.POST.get('data_10_12'))
    # info_12.objects.filter(data_01=request.POST.get('data_01_01')).update(data_11=request.POST.get('data_11_12'))
    # info_12.objects.filter(data_01=request.POST.get('data_01_01')).update(data_12=request.POST.get('data_12_12'))
    # info_12.objects.filter(data_01=request.POST.get('data_01_01')).update(data_13=request.POST.get('data_13_12'))
    # info_12.objects.filter(data_01=request.POST.get('data_01_01')).update(data_14=request.POST.get('data_14_12'))
    # info_12.objects.filter(data_01=request.POST.get('data_01_01')).update(data_15=request.POST.get('data_15_12'))
    # info_12.objects.filter(data_01=request.POST.get('data_01_01')).update(data_16=request.POST.get('data_16_12'))
    # info_12.objects.filter(data_01=request.POST.get('data_01_01')).update(data_17=request.POST.get('data_17_12'))
    # info_12.objects.filter(data_01=request.POST.get('data_01_01')).update(data_18=request.POST.get('data_18_12'))
    # info_12.objects.filter(data_01=request.POST.get('data_01_01')).update(data_19=request.POST.get('data_19_12'))
    # info_12.objects.filter(data_01=request.POST.get('data_01_01')).update(data_20=request.POST.get('data_20_12'))
    #
    # info_13.objects.filter(data_01=request.POST.get('data_01_01')).update(data_02=request.POST.get('data_02_13'))
    # info_13.objects.filter(data_01=request.POST.get('data_01_01')).update(data_03=request.POST.get('data_03_13'))
    # info_13.objects.filter(data_01=request.POST.get('data_01_01')).update(data_04=request.POST.get('data_04_13'))
    # info_13.objects.filter(data_01=request.POST.get('data_01_01')).update(data_05=request.POST.get('data_05_13'))
    # info_13.objects.filter(data_01=request.POST.get('data_01_01')).update(data_06=request.POST.get('data_06_13'))
    # info_13.objects.filter(data_01=request.POST.get('data_01_01')).update(data_07=request.POST.get('data_07_13'))
    # info_13.objects.filter(data_01=request.POST.get('data_01_01')).update(data_08=request.POST.get('data_08_13'))
    # info_13.objects.filter(data_01=request.POST.get('data_01_01')).update(data_09=request.POST.get('data_09_13'))
    # info_13.objects.filter(data_01=request.POST.get('data_01_01')).update(data_10=request.POST.get('data_10_13'))
    # info_13.objects.filter(data_01=request.POST.get('data_01_01')).update(data_11=request.POST.get('data_11_13'))
    # info_13.objects.filter(data_01=request.POST.get('data_01_01')).update(data_12=request.POST.get('data_12_13'))
    # info_13.objects.filter(data_01=request.POST.get('data_01_01')).update(data_13=request.POST.get('data_13_13'))
    # info_13.objects.filter(data_01=request.POST.get('data_01_01')).update(data_14=request.POST.get('data_14_13'))
    # info_13.objects.filter(data_01=request.POST.get('data_01_01')).update(data_15=request.POST.get('data_15_13'))
    # info_13.objects.filter(data_01=request.POST.get('data_01_01')).update(data_16=request.POST.get('data_16_13'))
    # info_13.objects.filter(data_01=request.POST.get('data_01_01')).update(data_17=request.POST.get('data_17_13'))
    # info_13.objects.filter(data_01=request.POST.get('data_01_01')).update(data_18=request.POST.get('data_18_13'))
    # info_13.objects.filter(data_01=request.POST.get('data_01_01')).update(data_19=request.POST.get('data_19_13'))
    # info_13.objects.filter(data_01=request.POST.get('data_01_01')).update(data_20=request.POST.get('data_20_13'))
    #
    # info_14.objects.filter(data_01=request.POST.get('data_01_01')).update(data_02=request.POST.get('data_02_14'))
    # info_14.objects.filter(data_01=request.POST.get('data_01_01')).update(data_03=request.POST.get('data_03_14'))
    # info_14.objects.filter(data_01=request.POST.get('data_01_01')).update(data_04=request.POST.get('data_04_14'))
    # info_14.objects.filter(data_01=request.POST.get('data_01_01')).update(data_05=request.POST.get('data_05_14'))
    # info_14.objects.filter(data_01=request.POST.get('data_01_01')).update(data_06=request.POST.get('data_06_14'))
    # info_14.objects.filter(data_01=request.POST.get('data_01_01')).update(data_07=request.POST.get('data_07_14'))
    # info_14.objects.filter(data_01=request.POST.get('data_01_01')).update(data_08=request.POST.get('data_08_14'))
    # info_14.objects.filter(data_01=request.POST.get('data_01_01')).update(data_09=request.POST.get('data_09_14'))
    # info_14.objects.filter(data_01=request.POST.get('data_01_01')).update(data_10=request.POST.get('data_10_14'))
    # info_14.objects.filter(data_01=request.POST.get('data_01_01')).update(data_11=request.POST.get('data_11_14'))
    # info_14.objects.filter(data_01=request.POST.get('data_01_01')).update(data_12=request.POST.get('data_12_14'))
    # info_14.objects.filter(data_01=request.POST.get('data_01_01')).update(data_13=request.POST.get('data_13_14'))
    # info_14.objects.filter(data_01=request.POST.get('data_01_01')).update(data_14=request.POST.get('data_14_14'))
    # info_14.objects.filter(data_01=request.POST.get('data_01_01')).update(data_15=request.POST.get('data_15_14'))
    # info_14.objects.filter(data_01=request.POST.get('data_01_01')).update(data_16=request.POST.get('data_16_14'))
    # info_14.objects.filter(data_01=request.POST.get('data_01_01')).update(data_17=request.POST.get('data_17_14'))
    # info_14.objects.filter(data_01=request.POST.get('data_01_01')).update(data_18=request.POST.get('data_18_14'))
    # info_14.objects.filter(data_01=request.POST.get('data_01_01')).update(data_19=request.POST.get('data_19_14'))
    # info_14.objects.filter(data_01=request.POST.get('data_01_01')).update(data_20=request.POST.get('data_20_14'))
    #
    # info_15.objects.filter(data_01=request.POST.get('data_01_01')).update(data_02=request.POST.get('data_02_15'))
    # info_15.objects.filter(data_01=request.POST.get('data_01_01')).update(data_03=request.POST.get('data_03_15'))
    # info_15.objects.filter(data_01=request.POST.get('data_01_01')).update(data_04=request.POST.get('data_04_15'))
    # info_15.objects.filter(data_01=request.POST.get('data_01_01')).update(data_05=request.POST.get('data_05_15'))
    # info_15.objects.filter(data_01=request.POST.get('data_01_01')).update(data_06=request.POST.get('data_06_15'))
    # info_15.objects.filter(data_01=request.POST.get('data_01_01')).update(data_07=request.POST.get('data_07_15'))
    # info_15.objects.filter(data_01=request.POST.get('data_01_01')).update(data_08=request.POST.get('data_08_15'))
    # info_15.objects.filter(data_01=request.POST.get('data_01_01')).update(data_09=request.POST.get('data_09_15'))
    # info_15.objects.filter(data_01=request.POST.get('data_01_01')).update(data_10=request.POST.get('data_10_15'))
    # info_15.objects.filter(data_01=request.POST.get('data_01_01')).update(data_11=request.POST.get('data_11_15'))
    # info_15.objects.filter(data_01=request.POST.get('data_01_01')).update(data_12=request.POST.get('data_12_15'))
    # info_15.objects.filter(data_01=request.POST.get('data_01_01')).update(data_13=request.POST.get('data_13_15'))
    # info_15.objects.filter(data_01=request.POST.get('data_01_01')).update(data_14=request.POST.get('data_14_15'))
    # info_15.objects.filter(data_01=request.POST.get('data_01_01')).update(data_15=request.POST.get('data_15_15'))
    # info_15.objects.filter(data_01=request.POST.get('data_01_01')).update(data_16=request.POST.get('data_16_15'))
    # info_15.objects.filter(data_01=request.POST.get('data_01_01')).update(data_17=request.POST.get('data_17_15'))
    # info_15.objects.filter(data_01=request.POST.get('data_01_01')).update(data_18=request.POST.get('data_18_15'))
    # info_15.objects.filter(data_01=request.POST.get('data_01_01')).update(data_19=request.POST.get('data_19_15'))
    # info_15.objects.filter(data_01=request.POST.get('data_01_01')).update(data_20=request.POST.get('data_20_15'))
    #
    # info_16.objects.filter(data_01=request.POST.get('data_01_01')).update(data_02=request.POST.get('data_02_16'))
    # info_16.objects.filter(data_01=request.POST.get('data_01_01')).update(data_03=request.POST.get('data_03_16'))
    # info_16.objects.filter(data_01=request.POST.get('data_01_01')).update(data_04=request.POST.get('data_04_16'))
    # info_16.objects.filter(data_01=request.POST.get('data_01_01')).update(data_05=request.POST.get('data_05_16'))
    # info_16.objects.filter(data_01=request.POST.get('data_01_01')).update(data_06=request.POST.get('data_06_16'))
    # info_16.objects.filter(data_01=request.POST.get('data_01_01')).update(data_07=request.POST.get('data_07_16'))
    # info_16.objects.filter(data_01=request.POST.get('data_01_01')).update(data_08=request.POST.get('data_08_16'))
    # info_16.objects.filter(data_01=request.POST.get('data_01_01')).update(data_09=request.POST.get('data_09_16'))
    # info_16.objects.filter(data_01=request.POST.get('data_01_01')).update(data_10=request.POST.get('data_10_16'))
    # info_16.objects.filter(data_01=request.POST.get('data_01_01')).update(data_11=request.POST.get('data_11_16'))
    # info_16.objects.filter(data_01=request.POST.get('data_01_01')).update(data_12=request.POST.get('data_12_16'))
    # info_16.objects.filter(data_01=request.POST.get('data_01_01')).update(data_13=request.POST.get('data_13_16'))
    # info_16.objects.filter(data_01=request.POST.get('data_01_01')).update(data_14=request.POST.get('data_14_16'))
    # info_16.objects.filter(data_01=request.POST.get('data_01_01')).update(data_15=request.POST.get('data_15_16'))
    # info_16.objects.filter(data_01=request.POST.get('data_01_01')).update(data_16=request.POST.get('data_16_16'))
    # info_16.objects.filter(data_01=request.POST.get('data_01_01')).update(data_17=request.POST.get('data_17_16'))
    # info_16.objects.filter(data_01=request.POST.get('data_01_01')).update(data_18=request.POST.get('data_18_16'))
    # info_16.objects.filter(data_01=request.POST.get('data_01_01')).update(data_19=request.POST.get('data_19_16'))
    # info_16.objects.filter(data_01=request.POST.get('data_01_01')).update(data_20=request.POST.get('data_20_16'))
    #
    # info_17.objects.filter(data_01=request.POST.get('data_01_01')).update(data_02=request.POST.get('data_02_17'))
    # info_17.objects.filter(data_01=request.POST.get('data_01_01')).update(data_03=request.POST.get('data_03_17'))
    # info_17.objects.filter(data_01=request.POST.get('data_01_01')).update(data_04=request.POST.get('data_04_17'))
    # info_17.objects.filter(data_01=request.POST.get('data_01_01')).update(data_05=request.POST.get('data_05_17'))
    # info_17.objects.filter(data_01=request.POST.get('data_01_01')).update(data_06=request.POST.get('data_06_17'))
    # info_17.objects.filter(data_01=request.POST.get('data_01_01')).update(data_07=request.POST.get('data_07_17'))
    # info_17.objects.filter(data_01=request.POST.get('data_01_01')).update(data_08=request.POST.get('data_08_17'))
    # info_17.objects.filter(data_01=request.POST.get('data_01_01')).update(data_09=request.POST.get('data_09_17'))
    # info_17.objects.filter(data_01=request.POST.get('data_01_01')).update(data_10=request.POST.get('data_10_17'))
    # info_17.objects.filter(data_01=request.POST.get('data_01_01')).update(data_11=request.POST.get('data_11_17'))
    # info_17.objects.filter(data_01=request.POST.get('data_01_01')).update(data_12=request.POST.get('data_12_17'))
    # info_17.objects.filter(data_01=request.POST.get('data_01_01')).update(data_13=request.POST.get('data_13_17'))
    # info_17.objects.filter(data_01=request.POST.get('data_01_01')).update(data_14=request.POST.get('data_14_17'))
    # info_17.objects.filter(data_01=request.POST.get('data_01_01')).update(data_15=request.POST.get('data_15_17'))
    # info_17.objects.filter(data_01=request.POST.get('data_01_01')).update(data_16=request.POST.get('data_16_17'))
    # info_17.objects.filter(data_01=request.POST.get('data_01_01')).update(data_17=request.POST.get('data_17_17'))
    # info_17.objects.filter(data_01=request.POST.get('data_01_01')).update(data_18=request.POST.get('data_18_17'))
    # info_17.objects.filter(data_01=request.POST.get('data_01_01')).update(data_19=request.POST.get('data_19_17'))
    # info_17.objects.filter(data_01=request.POST.get('data_01_01')).update(data_20=request.POST.get('data_20_17'))
    #
    # info_18.objects.filter(data_01=request.POST.get('data_01_01')).update(data_02=request.POST.get('data_02_18'))
    # info_18.objects.filter(data_01=request.POST.get('data_01_01')).update(data_03=request.POST.get('data_03_18'))
    # info_18.objects.filter(data_01=request.POST.get('data_01_01')).update(data_04=request.POST.get('data_04_18'))
    # info_18.objects.filter(data_01=request.POST.get('data_01_01')).update(data_05=request.POST.get('data_05_18'))
    # info_18.objects.filter(data_01=request.POST.get('data_01_01')).update(data_06=request.POST.get('data_06_18'))
    # info_18.objects.filter(data_01=request.POST.get('data_01_01')).update(data_07=request.POST.get('data_07_18'))
    # info_18.objects.filter(data_01=request.POST.get('data_01_01')).update(data_08=request.POST.get('data_08_18'))
    # info_18.objects.filter(data_01=request.POST.get('data_01_01')).update(data_09=request.POST.get('data_09_18'))
    # info_18.objects.filter(data_01=request.POST.get('data_01_01')).update(data_10=request.POST.get('data_10_18'))
    # info_18.objects.filter(data_01=request.POST.get('data_01_01')).update(data_11=request.POST.get('data_11_18'))
    # info_18.objects.filter(data_01=request.POST.get('data_01_01')).update(data_12=request.POST.get('data_12_18'))
    # info_18.objects.filter(data_01=request.POST.get('data_01_01')).update(data_13=request.POST.get('data_13_18'))
    # info_18.objects.filter(data_01=request.POST.get('data_01_01')).update(data_14=request.POST.get('data_14_18'))
    # info_18.objects.filter(data_01=request.POST.get('data_01_01')).update(data_15=request.POST.get('data_15_18'))
    # info_18.objects.filter(data_01=request.POST.get('data_01_01')).update(data_16=request.POST.get('data_16_18'))
    # info_18.objects.filter(data_01=request.POST.get('data_01_01')).update(data_17=request.POST.get('data_17_18'))
    # info_18.objects.filter(data_01=request.POST.get('data_01_01')).update(data_18=request.POST.get('data_18_18'))
    # info_18.objects.filter(data_01=request.POST.get('data_01_01')).update(data_19=request.POST.get('data_19_18'))
    # info_18.objects.filter(data_01=request.POST.get('data_01_01')).update(data_20=request.POST.get('data_20_18'))
    #

    try:
        getatcinfo01 = info_01.objects.get(data_01=request.POST.get('data_01_01'))

    except getatcinfo01.DoesNotExist:
        getatcinfo01 = None

    context['data_01_01'] = getatcinfo01.data_01
    context['data_02_01'] = getatcinfo01.data_02
    context['data_03_01'] = getatcinfo01.data_03
    context['data_04_01'] = getatcinfo01.data_04
    context['data_05_01'] = getatcinfo01.data_05
    context['data_06_01'] = getatcinfo01.data_06
    context['data_07_01'] = getatcinfo01.data_07
    context['data_08_01'] = getatcinfo01.data_08
    context['data_09_01'] = getatcinfo01.data_09
    context['data_10_01'] = getatcinfo01.data_10
    context['data_11_01'] = getatcinfo01.data_11
    context['data_12_01'] = getatcinfo01.data_12
    context['data_13_01'] = getatcinfo01.data_13
    context['data_14_01'] = getatcinfo01.data_14
    context['data_15_01'] = getatcinfo01.data_15
    context['data_16_01'] = getatcinfo01.data_16
    context['data_17_01'] = getatcinfo01.data_17
    context['data_18_01'] = getatcinfo01.data_18
    context['data_19_01'] = getatcinfo01.data_19
    context['data_20_01'] = getatcinfo01.data_20

    data_00_12 = info_12.objects.filter(data_01=name).values_list("id", "data_02", "data_03", "data_04", "data_05", )
    data_00_12 = list(data_00_12)
    a12 = []
    for i in data_00_12:
        a12.append(i)
    a12 = json.dumps(a12, ensure_ascii=False)
    context['data_00_12'] = a12
    print("data_00_12")
    print(data_00_12)

    a03 = []
    a04 = []
    a05 = []
    a06 = []
    a07 = []
    a08 = []
    a09 = []
    a10 = []
    a11 = []
    a12 = []
    a13 = []
    a14 = []
    a15 = []
    a16 = []
    a17 = []
    a18 = []
    for i in list(
            info_03.objects.filter(data_01=name).values_list("id", "data_02", "data_03", "data_04", "data_05",
                                                             "data_06",
                                                             "data_07", "data_08", )): a03.append(i)
    for i in list(
            info_04.objects.filter(data_01=name).values_list("id", "data_02", "data_03", "data_04", "data_05",
                                                             "data_06",
                                                             "data_07", )): a04.append(i)
    for i in list(
            info_05.objects.filter(data_01=name).values_list("id", "data_02", "data_03", "data_04", "data_05",
                                                             "data_06", )): a05.append(i)
    for i in list(
            info_06.objects.filter(data_01=name).values_list("id", "data_02", "data_03", "data_04", "data_05",
                                                             "data_06",
                                                             "data_07", )): a06.append(i)
    for i in list(
            info_07.objects.filter(data_01=name).values_list("id", "data_02", "data_03", "data_04", "data_05",
                                                             "data_06",
                                                             "data_07", "data_08", )): a07.append(i)
    for i in list(
            info_08.objects.filter(data_01=name).values_list("id", "data_02", "data_03", "data_04", "data_05",
                                                             "data_06",
                                                             "data_07", "data_08",
                                                             "data_09", "data_10", "data_11", "data_12", "data_13",
                                                             "data_14", "data_15",
                                                             "data_16", "data_17", "data_18", "data_19", "data_20",
                                                             "data_21", "data_22",
                                                             )): a08.append(i)
    for i in list(
            info_09.objects.filter(data_01=name).values_list("id", "data_02", "data_03", "data_04", "data_05",
                                                             "data_06", )): a09.append(i)
    for i in list(
            info_10.objects.filter(data_01=name).values_list("id", "data_02", "data_03", "data_04", "data_05",
                                                             "data_06",
                                                             "data_07", "data_08", "data_09", )): a10.append(i)
    for i in list(
            info_11.objects.filter(data_01=name).values_list("id", "data_02", "data_03", "data_04", )): a11.append(i)
    for i in list(
            info_12.objects.filter(data_01=name).values_list("id", "data_02", "data_03", "data_04",
                                                             "data_05", )): a12.append(
        i)
    for i in list(
            info_13.objects.filter(data_01=name).values_list("id", "data_02", "data_03", "data_04", "data_05",
                                                             "data_06", )): a13.append(i)
    for i in list(
            info_14.objects.filter(data_01=name).values_list("id", "data_02", "data_03", "data_04", "data_05",
                                                             "data_06", )): a14.append(i)
    for i in list(
            info_15.objects.filter(data_01=name).values_list("id", "data_02", "data_03", "data_04",
                                                             "data_05", )): a15.append(
        i)
    for i in list(
            info_16.objects.filter(data_01=name).values_list("id", "data_02", "data_03", "data_04", )): a16.append(i)
    for i in list(
            info_17.objects.filter(data_01=name).values_list("id", "data_02", "data_03", "data_04", "data_05",
                                                             "data_06",
                                                             "data_07", "data_08", )): a17.append(i)
    for i in list(
            info_18.objects.filter(data_01=name).values_list("id", "data_02", "data_03", "data_04", "data_05",
                                                             "data_06", )): a18.append(i)

    context['data_00_03'] = json.dumps(a03, ensure_ascii=False)
    context['data_00_04'] = json.dumps(a04, ensure_ascii=False)
    context['data_00_05'] = json.dumps(a05, ensure_ascii=False)
    context['data_00_06'] = json.dumps(a06, ensure_ascii=False)
    context['data_00_07'] = json.dumps(a07, ensure_ascii=False)

    context['data_00_09'] = json.dumps(a09, ensure_ascii=False)
    context['data_00_10'] = json.dumps(a10, ensure_ascii=False)
    context['data_00_11'] = json.dumps(a11, ensure_ascii=False)
    context['data_00_12'] = json.dumps(a12, ensure_ascii=False)
    context['data_00_13'] = json.dumps(a13, ensure_ascii=False)
    context['data_00_14'] = json.dumps(a14, ensure_ascii=False)
    context['data_00_15'] = json.dumps(a15, ensure_ascii=False)
    context['data_00_16'] = json.dumps(a16, ensure_ascii=False)
    context['data_00_17'] = json.dumps(a17, ensure_ascii=False)
    context['data_00_18'] = json.dumps(a18, ensure_ascii=False)

    ff1 = info_03.objects \
        .filter().values_list().all()
    aa1 = ""
    for k in ff1:
        m = list(k)
        aa1 = aa1 + str(m[4]) + " "

    data = []
    培训类别 = ["上岗前培训", "资格培训", "复习培训", "附加培训", "追加培训", "补习培训"
        , "设备培训", "熟练培训", "专项培训", ]
    本人 = []
    本人.append(name)
    for xy in 本人:
        for lb in 培训类别:
            ii = []
            ff = trainningstatusdetail.objects \
                .filter().values_list().all()
            ggid1 = 1
            for k in ff:
                m = list(k)
                ee = []

                if xy in m[8].split():
                    # print(
                    #     " nf" + '*********' + '  ' )
                    # print( nf == datetime.strptime(m[13].split()[0], '%Y-%m-%d').year)

                    if lb == m[2]:
                        if m[11] != "0":
                            ee.append(ggid1)
                            ggid1 += 1
                            ee.append(str(datetime.strptime(m[13].split()[0], '%Y-%m-%d').year) + "年" + lb)
                            ee.append('管制运行部')
                            ee.append(m[6])
                            ee.append(lb)
                            ee.append(m[5])
                            ee.append(aa1)
                            ee.append('')
                            ee.append(m[13].split()[0] + "-" + m[13].split()[1])  # 开始时间
                            ee.append(m[13].split()[0] + "-" + m[13].split()[2])
                            ee.append('')
                            ee.append(float(m[11]) / float(m[10]))
                            ee.append('')

                            ee.append('')
                            ee.append('')
                            ee.append('')

                            ee.append(m[7])  # 培训教员
                            ee.append('')
                            ee.append('')
                            ee.append('')
                            ee.append('')
                            ee.append('')

                            data.append(ee)

    context['data_00_08'] = json.dumps(data, ensure_ascii=False)
    print('data_00_08')
    print()

    file_list1 = []
    for root, dirs, files in os.walk('E:/pythonproject/ATC_data/static/files'):
        print(root)  # 当前目录路径
        print(dirs)  # 当前路径下所有子目录
        print(files)  # 当前路径下所有非目录子文件   只循环一次
        file_list1.append(files)
        print(file_list1)
        i2 = []
        for i1 in files:
            # if i1.split('_')[2] == username.split('_')[2]:
            i2.append(i1)

        context['file'] = json.dumps(i2, ensure_ascii=False)

    return render(request, 'personinfo.html', context)


def getinfo_save_ajax(request):
    post_data = {
        "name": "1"
    }
    data = json.loads(request.body.decode("utf-8"))
    print("getinfo_save_ajax")
    print(data)

    for aa in info_03.objects.filter(data_01=request.POST.get('data_01_01')):
        aa.update(data_02=data[0][0])
        aa.update(data_03=data[0][1])

    return HttpResponse(json.dumps(post_data
                                   ), content_type='application/json')


zz1 = [info_01,
       info_03,
       info_04,
       info_05,
       info_06,
       info_07,
       info_08,
       info_09,
       info_10,
       info_11,
       info_12,
       info_13,
       info_14,
       info_15,
       info_16,
       info_17,
       info_18]


def getinfo_savetable(request):
    post_data = {
        "name": "1"
    }
    aa3 = json.loads(request.body.decode("utf-8"))
    print("getinfo_savetable aa3 ")
    print(aa3)

    for i in aa3[1:]:
        print("i")
        print(i)

    zz3 = 0
    for zz2 in zz1:
        xx1 = 0

        for yy1 in aa3[zz3]:
            yy3 = {}
            xx2 = 1
            for yy2 in yy1[1:]:
                # dict['Age'] = 8  # 更新
                # dict['School'] = "RUNOOB"  # 添加
                if (xx2 + 1) < 10:
                    yy3["data_0" + str(xx2 + 1)] = (yy2)
                else:
                    yy3["data_" + str(xx2 + 1)] = (yy2)

                xx2 += 1
            print("biao hang lie")
            print(zz3)
            print(xx1)
            print(xx2)
            print("yy3")
            print(yy3)
            print("id")
            print(aa3[zz3][xx1][0])

            #  通常我们再变量前加一个星号(*)表示这个变量是元组/列表，加两个星号表示这个参数是字典
            zz2.objects.filter(id=aa3[zz3][xx1][0]).update(**yy3)
            xx1 += 1
        zz3 += 1

    # xx3 = []
    # for xx4 in list(info_03.objects.filter(id=aa3[0][0][0])):
    #     xx3.append(xx4)
    # for xx2 in xx3:

    # print("j")
    # print(j)
    # xx2.update(data_02=aa3[0][0][0])
    # xx1 += 1

    return HttpResponse(json.dumps(post_data
                                   ), content_type='application/json')


def getinfo_add_row(request):
    post_data = {
        "name": "1"
    }

    aab5 = json.loads(request.body.decode("utf-8"))
    print("getinfo_add_row aab5 ")
    print(aab5)

    zza1 = [info_01(),
            info_03(),
            info_04(),
            info_05(),
            info_06(),
            info_07(),
            info_08(),
            info_09(),
            info_10(),
            info_11(),
            info_12(),
            info_13(),
            info_14(),
            info_15(),
            info_16(),
            info_17(),
            info_18()]

    zza1[int(aab5[0]) - 2].data_01 = aab5[1]
    zza1[int(aab5[0]) - 2].data_02 = ""
    zza1[int(aab5[0]) - 2].data_03 = ""
    zza1[int(aab5[0]) - 2].data_04 = ""
    zza1[int(aab5[0]) - 2].data_05 = ""
    zza1[int(aab5[0]) - 2].data_06 = ""
    zza1[int(aab5[0]) - 2].data_07 = ""
    zza1[int(aab5[0]) - 2].data_08 = ""
    zza1[int(aab5[0]) - 2].data_09 = ""
    zza1[int(aab5[0]) - 2].data_10 = ""
    zza1[int(aab5[0]) - 2].data_11 = ""
    zza1[int(aab5[0]) - 2].data_12 = ""
    zza1[int(aab5[0]) - 2].data_13 = ""
    zza1[int(aab5[0]) - 2].data_14 = ""
    zza1[int(aab5[0]) - 2].data_15 = ""
    zza1[int(aab5[0]) - 2].data_16 = ""
    zza1[int(aab5[0]) - 2].data_17 = ""
    zza1[int(aab5[0]) - 2].data_18 = ""
    zza1[int(aab5[0]) - 2].data_19 = ""
    zza1[int(aab5[0]) - 2].data_20 = ""
    zza1[int(aab5[0]) - 2].is_active = 0
    zza1[int(aab5[0]) - 2].save()
    print("getinfo_add_row id ")
    print(zza1[int(aab5[0]) - 2].id)
    xxa3 = []
    xxa3.append(zza1[int(aab5[0]) - 2].id)

    return HttpResponse(json.dumps(xxa3
                                   ), content_type='application/json')


def getinfo_delete_row(request):
    post_data = {
        "name": "1"
    }
    x3 = json.loads(request.body.decode("utf-8"))
    zz1[int(x3[1]) - 2].objects.filter(id=x3[0]).delete()

    return HttpResponse(json.dumps(post_data
                                   ), content_type='application/json')


def 获取所有的登陆人():
    from TestModel.models import logins
    jj = logins.objects \
        .filter().values_list().all()
    kk = list(jj)
    ll = []
    for gg in kk:
        ll.append(gg[1])
    return ll


def gettrainningstatus(request):
    # getatcinfo=info.objects.get(id=123)
    # context = {}
    # context['atcName'] = getatcinfo.atcName
    # context['atcOld'] = getatcinfo.atcOld
    return render(request, 'trainningstatus.html'
                  # , context
                  )


def infosearch(request):
    jj2 = info.objects \
        .filter().values_list().all()
    kk2 = list(jj2)
    ll2 = []
    for gg2 in kk2:
        ff2 = []
        for hh2 in gg2:
            ff2.append(hh2)
        ll2.append(ff2)
    context = {}
    mm3 = {}
    mm2 = []
    mm5 = []
    mm4 = 0
    for gg2 in ll2[0:]:
        ff2 = []
        ff2.append(gg2[1])
        ff2.append(gg2[3])
        ff2.append(gg2[23])

        ff2.append(gg2[4])
        ff2.append(gg2[5])
        ff2.append(gg2[6])
        ff2.append(gg2[7])
        ff2.append(gg2[8])
        ff2.append(gg2[2])
        ff2.append(gg2[9])
        ff2.append(gg2[0])
        mm2.append(ff2)
    mm5.append(mm2)

    #     mm3['a01'] = gg2[1]
    #     mm3['a02'] = gg2[3]
    #     mm3['a03'] = gg2[23]
    #     mm3['a04'] = gg2[4]
    #     mm3['a05'] = gg2[5]
    #     mm3['a06'] = gg2[6]
    #     mm3['a07'] = gg2[7]
    #     mm3['a08'] = gg2[8]
    #     mm3['a09'] = gg2[2]
    #     mm3['a10'] = gg2[9]
    #
    #     context['data'+"_"+str(mm4)] = mm3
    #     mm4=mm4+1
    # print(context)

    return render(request, 'infosearch.html', {"data": mm2, })


def getinfo_input(request):
    name = ""
    if request.session.get('status'):
        name = request.session.get('name')

    context = {}
    if request.POST.get('人员'):
        选的人员 = request.POST.get('人员')
        context['选的人员'] = 选的人员
        name = 选的人员
    if request.GET.get('人员'):
        选的人员 = request.GET.get('人员')
        context['选的人员'] = 选的人员
        name = 选的人员

    人员 = 获取所有的登陆人()
    context['人员'] = 人员
    print('人员')
    print(人员)
    try:
        if info_01.objects.filter(data_01=name):
            print("已经有人员信息")
            print(name)
        else:
            info_01.objects.create(data_01=name, )
            info_02.objects.create(data_01=name, )
            info_03.objects.create(data_01=name, )
            info_04.objects.create(data_01=name, )
            info_05.objects.create(data_01=name, )
            info_06.objects.create(data_01=name, )
            info_07.objects.create(data_01=name, )
            info_08.objects.create(data_01=name, )
            info_09.objects.create(data_01=name, )
            info_10.objects.create(data_01=name, )
            info_11.objects.create(data_01=name, )
            info_12.objects.create(data_01=name, )
            info_13.objects.create(data_01=name, )
            info_14.objects.create(data_01=name, )
            info_15.objects.create(data_01=name, )
            info_16.objects.create(data_01=name, )
            info_17.objects.create(data_01=name, )
            info_18.objects.create(data_01=name, )

    except ObjectDoesNotExist:
        print('没查到')

        # getatcinfo = info.objects.get(id=1)
        # context['atcName'] = getatcinfo.atcName
        # context['atcOld'] = getatcinfo.atcOld
    try:
        getatcinfo01 = info_01.objects.get(data_01=name)
        getatcinfo02 = info_02.objects.get(data_01=name)
        # getatcinfo03 = info_03.objects.get(data_01=name)
        # getatcinfo04 = info_04.objects.get(data_01=name)
        # getatcinfo05 = info_05.objects.get(data_01=name)
        # getatcinfo06 = info_06.objects.get(data_01=name)
        # getatcinfo07 = info_07.objects.get(data_01=name)
        # getatcinfo08 = info_08.objects.get(data_01=name)
        # getatcinfo09 = info_09.objects.get(data_01=name)
        # getatcinfo10 = info_10.objects.get(data_01=name)
        # getatcinfo11 = info_11.objects.get(data_01=name)
        # getatcinfo12 = info_12.objects.filter(data_01=name)
        # getatcinfo13 = info_13.objects.get(data_01=name)
        # getatcinfo14 = info_14.objects.get(data_01=name)
        # getatcinfo15 = info_15.objects.get(data_01=name)
        # getatcinfo16 = info_16.objects.get(data_01=name)
        # getatcinfo17 = info_17.objects.get(data_01=name)
        # getatcinfo18 = info_18.objects.get(data_01=name)
    except getatcinfo01.DoesNotExist:
        getatcinfo01 = None

    data_00_12 = info_12.objects.filter(data_01=name).values_list("id", "data_02", "data_03", "data_04", "data_05", )
    data_00_12 = list(data_00_12)
    a12 = []
    for i in data_00_12:
        a12.append(i)
    a12 = json.dumps(a12, ensure_ascii=False)
    context['data_00_12'] = a12
    print("data_00_12")
    print(data_00_12)

    a03 = []
    a04 = []
    a05 = []
    a06 = []
    a07 = []
    a08 = []
    a09 = []
    a10 = []
    a11 = []
    a12 = []
    a13 = []
    a14 = []
    a15 = []
    a16 = []
    a17 = []
    a18 = []
    for i in list(
            info_03.objects.filter(data_01=name).values_list("id", "data_02", "data_03", "data_04", "data_05",
                                                             "data_06",
                                                             "data_07", "data_08", )):
        n = []
        for m in i:
            n.append(m)
        a03.append(n)
    for i in list(
            info_04.objects.filter(data_01=name).values_list("id", "data_02", "data_03", "data_04", "data_05",
                                                             "data_06",
                                                             "data_07", )):
        n = []
        for m in i:
            n.append(m)
        a04.append(n)
    for i in list(
            info_05.objects.filter(data_01=name).values_list("id", "data_02", "data_03", "data_04", "data_05",
                                                             "data_06", )):
        n = []
        for m in i:
            n.append(m)
        a05.append(n)
    for i in list(
            info_06.objects.filter(data_01=name).values_list("id", "data_02", "data_03", "data_04", "data_05",
                                                             "data_06",
                                                             "data_07", )):
        n = []
        for m in i:
            n.append(m)
        a06.append(n)

    for i in list(
            info_07.objects.filter(data_01=name).values_list("id", "data_02", "data_03", "data_04", "data_05",
                                                             "data_06",
                                                             "data_07", "data_08", )):
        n = []
        for m in i:
            n.append(m)
        a07.append(n)
    for i in list(
            info_08.objects.filter(data_01=name).values_list("id", "data_02", "data_03", "data_04", "data_05",
                                                             "data_06",
                                                             "data_07", "data_08",
                                                             "data_09", "data_10", "data_11", "data_12", "data_13",
                                                             "data_14", "data_15",
                                                             "data_16", "data_17", "data_18", "data_19", "data_20",
                                                             "data_21", "data_22",
                                                             )):
        n = []
        for m in i:
            n.append(m)
        a08.append(n)
    for i in list(
            info_09.objects.filter(data_01=name).values_list("id", "data_02", "data_03", "data_04", "data_05",
                                                             "data_06", )):
        n = []
        for m in i:
            n.append(m)
        a09.append(n)
    for i in list(
            info_10.objects.filter(data_01=name).values_list("id", "data_02", "data_03", "data_04", "data_05",
                                                             "data_06",
                                                             "data_07", "data_08", "data_09", )):
        n = []
        for m in i:
            n.append(m)
        a10.append(n)
    for i in list(
            info_11.objects.filter(data_01=name).values_list("id", "data_02", "data_03", "data_04", )):
        n = []
        for m in i:
            n.append(m)
        a11.append(n)
    for i in list(
            info_12.objects.filter(data_01=name).values_list("id", "data_02", "data_03", "data_04", "data_05", )):
        n = []
        for m in i:
            n.append(m)
        a12.append(n)
    for i in list(
            info_13.objects.filter(data_01=name).values_list("id", "data_02", "data_03", "data_04", "data_05",
                                                             "data_06", )):
        n = []
        for m in i:
            n.append(m)
        a13.append(n)
    for i in list(
            info_14.objects.filter(data_01=name).values_list("id", "data_02", "data_03", "data_04", "data_05",
                                                             "data_06", )):
        n = []
        for m in i:
            n.append(m)
        a14.append(n)
    for i in list(
            info_15.objects.filter(data_01=name).values_list("id", "data_02", "data_03", "data_04", )):
        n = []
        for m in i:
            n.append(m)
        a15.append(n)
    for i in list(
            info_16.objects.filter(data_01=name).values_list("id", "data_02", "data_03", "data_04", )):
        n = []
        for m in i:
            n.append(m)
        a16.append(n)
    for i in list(
            info_17.objects.filter(data_01=name).values_list("id", "data_02", "data_03", "data_04", "data_05",
                                                             "data_06",
                                                             "data_07", "data_08", )):
        n = []
        for m in i:
            n.append(m)
        a17.append(n)
    for i in list(
            info_18.objects.filter(data_01=name).values_list("id", "data_02", "data_03", "data_04", "data_05",
                                                             "data_06", )):
        n = []
        for m in i:
            n.append(m)
        a18.append(n)
    # 变成json，handsontable才能识别
    context['data_00_03'] = json.dumps(a03, ensure_ascii=False)
    context['data_00_04'] = json.dumps(a04, ensure_ascii=False)
    context['data_00_05'] = json.dumps(a05, ensure_ascii=False)
    context['data_00_06'] = json.dumps(a06, ensure_ascii=False)
    context['data_00_07'] = json.dumps(a07, ensure_ascii=False)

    context['data_00_09'] = json.dumps(a09, ensure_ascii=False)
    context['data_00_10'] = json.dumps(a10, ensure_ascii=False)
    context['data_00_11'] = json.dumps(a11, ensure_ascii=False)
    context['data_00_12'] = json.dumps(a12, ensure_ascii=False)
    context['data_00_13'] = json.dumps(a13, ensure_ascii=False)
    context['data_00_14'] = json.dumps(a14, ensure_ascii=False)
    context['data_00_15'] = json.dumps(a15, ensure_ascii=False)
    context['data_00_16'] = json.dumps(a16, ensure_ascii=False)
    context['data_00_17'] = json.dumps(a17, ensure_ascii=False)
    context['data_00_18'] = json.dumps(a18, ensure_ascii=False)

    context['a03'] = a03
    context['a04'] = a04
    context['a05'] = a05
    context['a06'] = a06
    context['a07'] = a07

    context['a09'] = a09
    context['a10'] = a10
    context['a11'] = a11
    context['a12'] = a12
    context['a13'] = a13
    context['a14'] = a14
    context['a15'] = a15
    context['a16'] = a16
    context['a17'] = a17
    context['a18'] = a18

    print('a06')
    print(a06)
    context['data_00_01'] = getatcinfo01.id
    context['data_01_01'] = getatcinfo01.data_01
    context['data_02_01'] = getatcinfo01.data_02
    context['data_03_01'] = getatcinfo01.data_03
    context['data_04_01'] = getatcinfo01.data_04
    context['data_05_01'] = getatcinfo01.data_05
    context['data_06_01'] = getatcinfo01.data_06
    context['data_07_01'] = getatcinfo01.data_07
    context['data_08_01'] = getatcinfo01.data_08
    context['data_09_01'] = getatcinfo01.data_09
    context['data_10_01'] = getatcinfo01.data_10
    context['data_11_01'] = getatcinfo01.data_11
    context['data_12_01'] = getatcinfo01.data_12
    context['data_13_01'] = getatcinfo01.data_13
    context['data_14_01'] = getatcinfo01.data_14
    context['data_15_01'] = getatcinfo01.data_15
    context['data_16_01'] = getatcinfo01.data_16
    context['data_17_01'] = getatcinfo01.data_17
    context['data_18_01'] = getatcinfo01.data_18
    context['data_19_01'] = getatcinfo01.data_19
    context['data_20_01'] = getatcinfo01.data_20

    context['data_01_02'] = getatcinfo02.data_01
    context['data_02_02'] = getatcinfo02.data_02
    context['data_03_02'] = getatcinfo02.data_03
    context['data_04_02'] = getatcinfo02.data_04
    context['data_05_02'] = getatcinfo02.data_05
    context['data_06_02'] = getatcinfo02.data_06
    context['data_07_02'] = getatcinfo02.data_07
    context['data_08_02'] = getatcinfo02.data_08
    context['data_09_02'] = getatcinfo02.data_09
    context['data_10_02'] = getatcinfo02.data_10
    context['data_11_02'] = getatcinfo02.data_11
    context['data_12_02'] = getatcinfo02.data_12
    context['data_13_02'] = getatcinfo02.data_13
    context['data_14_02'] = getatcinfo02.data_14
    context['data_15_02'] = getatcinfo02.data_15
    context['data_16_02'] = getatcinfo02.data_16
    context['data_17_02'] = getatcinfo02.data_17
    context['data_18_02'] = getatcinfo02.data_18
    context['data_19_02'] = getatcinfo02.data_19
    context['data_20_02'] = getatcinfo02.data_20

    ff1 = info_03.objects \
        .filter().values_list().all()
    aa1 = ""
    for k in ff1:
        m = list(k)
        aa1 = aa1 + str(m[4]) + " "

    data = []
    培训类别 = ["上岗前培训", "资格培训", "复习培训", "附加培训", "追加培训", "补习培训"
        , "设备培训", "熟练培训", "专项培训", ]
    本人 = []
    本人.append(name)
    for xy in 本人:
        for lb in 培训类别:
            ii = []
            ff = trainningstatusdetail.objects \
                .filter().values_list().all()
            ggid1 = 1
            for k in ff:
                m = list(k)
                ee = []

                if xy in m[8].split():
                    # print(
                    #     " nf" + '*********' + '  ' )
                    # print( nf == datetime.strptime(m[13].split()[0], '%Y-%m-%d').year)

                    if lb == m[2]:
                        if m[11] != "0":
                            ee.append(ggid1)
                            ggid1 += 1
                            ee.append(str(datetime.strptime(m[13].split()[0], '%Y-%m-%d').year) + "年" + lb)
                            ee.append('管制运行部')
                            ee.append(m[6])
                            ee.append(lb)
                            ee.append(m[5])
                            ee.append(aa1)
                            ee.append('')
                            ee.append(m[13].split()[0] + "-" + m[13].split()[1])  # 开始时间
                            ee.append(m[13].split()[0] + "-" + m[13].split()[2])
                            ee.append('')
                            ee.append(float(m[11]) / float(m[10]))
                            ee.append('')

                            ee.append('')
                            ee.append('')
                            ee.append('')

                            ee.append(m[7])  # 培训教员
                            ee.append('')
                            ee.append('')
                            ee.append('')
                            ee.append('')
                            ee.append('')

                            data.append(ee)

    context['data_00_08'] = json.dumps(data, ensure_ascii=False)
    print('data_00_08')
    print()

    import numpy as np
    import matplotlib.pyplot as plt
    plt.rcParams['font.sans-serif'] = 'SimHei'
    plt.rcParams['axes.unicode_minus'] = False
    plt.style.use('ggplot')
    values = [90, 89, 95, 98, 100, 92, 96]

    feature = np.array(['通话用语', '通话用语', '其他', '特情处置', '管制程序', '通报协调', '间隔效率', '雷达监控'])  # 标签
    angles = np.linspace(0, 2 * np.pi, len(values), endpoint=False)
    values = np.concatenate((values, [values[0]]))
    angles = np.concatenate((angles, [angles[0]]))
    fig = plt.figure()
    ax = fig.add_subplot(111, polar=True)
    ax.fill(angles, values, 'o-', linewidth=2, alpha=0.2)
    ax.fill(angles, values, alpha=0.1)
    ax.set_thetagrids(angles * 180 / np.pi, feature)  # 添加标签
    ax.set_ylim(0, 100)
    plt.title('关键指标雷达图')
    ax.grid(True)
    plt.savefig('E:/pythonproject/ATC_data/static/' + context['data_01_01'] + '_01.jpg')
    # plt.show()
    # E: / demo / project1 / img / test.jpg

    file_list1 = []
    for root, dirs, files in os.walk('E:/pythonproject/ATC_data/static/files'):
        print(root)  # 当前目录路径
        print(dirs)  # 当前路径下所有子目录
        print(files)  # 当前路径下所有非目录子文件   只循环一次
        file_list1.append(files)
        print(file_list1)
        i2 = []
        for i1 in files:
            # if i1.split('_')[2] == username.split('_')[2]:
            i2.append(i1)

        context['file'] = json.dumps(i2, ensure_ascii=False)

    return render(request, 'getinfo_input.html', context)


def upload(request):
    print("upload")
    username = request.POST.get('username')
    print(username)
    file_obj = request.FILES.get('file_obj')

    file_name = file_obj.name
    file_name = username + "_" + file_name

    path = os.path.join("E:/pythonproject/ATC_data/static/files", file_name)

    # 读取文件形式
    with open(path, 'wb') as f:
        for i in file_obj:
            f.write(i)
    # django 提供的chunks方法
    with open(path, 'wb') as f:
        for chunk in file_obj.chunks():
            f.write(chunk)

    file_list1 = []
    for root, dirs, files in os.walk('E:/pythonproject/ATC_data/static/files'):
        print(root)  # 当前目录路径
        print(dirs)  # 当前路径下所有子目录
        print(files)  # 当前路径下所有非目录子文件   只循环一次
        file_list1.append(files)
        print(file_list1)
        i2 = []
        for i1 in files:
            if i1.split('_')[2] == username.split('_')[2]:
                i2.append(i1)

        data = json.dumps(i2, ensure_ascii=False)

    # file_list = []
    # files = os.listdir('C:/project1/ATC_data/static/files')
    #
    # for i in files:
    #     file_list.append(i)
    # print(file_list)
    # data = json.dumps(file_list, ensure_ascii=False)
    return HttpResponse(data)


def download(request):
    print("download")
    filename = "hha"
    filename = request.GET.get('filename')
    print(str(filename))

    file = open('E:/pythonproject/ATC_data/static/files/' + filename, 'rb')
    response = StreamingHttpResponse(file)
    response['Content-Type'] = 'application/octet-stream'

    response['Content-Disposition'] = "attachment; filename*=utf-8''{}".format(escape_uri_path(filename))

    return response


def delete(request):
    file_name = json.loads(request.body.decode("utf-8"))

    path = "E:/pythonproject/ATC_data/static/files/" + file_name  # 文件路径
    if os.path.exists(path):  # 如果文件存在
        # 删除文件，可使用以下两种方法。
        os.remove(path)
        # os.unlink(path)
        print("delete ok    " + file_name)
    else:
        print('no such file')  # 则返回文件不存在

    print("delete")

    data = json.dumps("ok", ensure_ascii=False)
    return HttpResponse(data)
