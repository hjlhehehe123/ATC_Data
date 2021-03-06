import json
from datetime import datetime

from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q
from django.shortcuts import render

import trainningcompletion
from atcInfo.models import info
from data_anaiysis import models

# Create your views here.
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
培训类别 = ["上岗前培训", "资格培训", "复习培训", "附加培训", "追加培训", "补习培训"
    , "设备培训", "熟练培训", "专项培训", ]


def 获取所有可能的年份(年份):
    a1 = []
    for k1 in trainningcompletion.models.trainningstatusdetail.objects.filter().values_list('frontdata15'):
        for k11 in k1:
            if k11 != "培训完成时间":
                # print("培训完成时间")

                t2 = datetime.strptime(k11.split()[0], '%Y-%m-%d')
                a1.append(t2.year)

    年份.append(a1[0])
    for a2 in a1:
        if a2 in 年份:
            print("年份存在" + str(a2))
        else:
            年份.append(a2)
    print(年份)


# 以下是# 模拟机培训学时（塔台）

def tower_trainning_total_time(request):  # 获取模拟机培训学时（塔台）
    # 创建数据模拟机培训学时()

    年份 = []
    获取所有可能的年份(年份)
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

    now_time = datetime.now()
    now_year = datetime.strftime(now_time, "%y")
    now_year = str(2000 + int(now_year))
    now_month = datetime.strftime(now_time, "%m")
    day1 = 1
    day2 = 31

    print("now_month" + "*****" + now_month)

    # print("year" + "*****" + now_year)
    data = models.tower_trainning_total_time.objects \
        .filter(Q(data03__contains='上岗前培训') | Q(data03__contains='学时') | Q(data01=now_year, )).values_list("data01",
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
    print("data" + '*********' + '  ' + data)

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

    return render(request, 'tower_trainning_total_time.html', {'data': data,
                                                               'year': 年份, 'month': 月份, 'post_year1': now_year,
                                                               'month1': "1", 'day1': day1,
                                                               'post_year2': now_year, 'month2': "12", 'day2': day2, })


def tower_trainning_total_time_post(request):
    post_year1 = int(request.POST.get('year1'))
    month1 = request.POST.get('month1')
    month1 = int(''.join(month1).split("月")[0])
    day1 = int(request.POST.get('day1'))

    post_year2 = int(request.POST.get('year2'))
    month2 = request.POST.get('month2')
    month2 = int(''.join(month2).split("月")[0])
    day2 = int(request.POST.get('day2'))
    塔进区 = request.POST.get('塔进区')
    # 机房=["塔台模拟机房","雷达模拟机房"]
    # 科室=["塔台管制室","区域管制室"]
    a1 = ""
    b1 = ""
    if 塔进区 == "0":
        a1 = "塔台模拟机房"
        b1 = "塔台管制室"

    if 塔进区 == "1":
        a1 = "雷达模拟机房"
        b1 = "塔台管制室"

    if 塔进区 == "2":
        a1 = "雷达模拟机房"
        b1 = "区域管制室"

    # 创建数据模拟机培训学时()
    年份 = []
    获取所有可能的年份(年份)

    # 查询最小到日
    temp1 = []
    # 表头
    hh = []
    hh.append("年份")
    hh.append("月份")
    hh.append("上岗前培训")
    hh.append("")
    hh.append("资格培训")
    hh.append("")
    hh.append("复习培训")
    hh.append("")
    hh.append("附加培训")
    hh.append("")
    hh.append("追加培训 ")
    hh.append("")
    hh.append("补习培训")
    hh.append("")
    hh.append("设备培训")
    hh.append("")
    hh.append("熟练培训")
    hh.append("")
    hh.append("专项培训 ")
    hh.append("")
    hh.append("合计 ")
    hh.append("")
    temp1.append(hh)

    gg = []
    gg.append("")
    gg.append("")
    gg.append("学时")
    gg.append("人次")
    gg.append("学时")
    gg.append("人次")
    gg.append("学时")
    gg.append("人次")
    gg.append("学时")
    gg.append("人次")
    gg.append("学时")
    gg.append("人次")
    gg.append("学时")
    gg.append("人次")
    gg.append("学时")
    gg.append("人次")
    gg.append("学时")
    gg.append("人次")
    gg.append("学时")
    gg.append("人次")
    gg.append("学时")
    gg.append("人次")
    temp1.append(gg)
    jj = trainningcompletion.models.trainningstatusdetail.objects \
        .filter().values_list().all()
    kk = list(jj)
    ll = []
    for gg in kk:
        ff = []
        for hh in gg:
            ff.append(hh)
        ll.append(ff)

    学时 = 0

    培训类别 = ["上岗前培训", "资格培训", "复习培训", "附加培训", "追加培训", "补习培训"
        , "设备培训", "熟练培训", "专项培训", ]

    print("range")
    print(31 in range(31, 31, 1))
    print(30 in range(30, 31, 1))  # 31是不会循环到的
    # if (a1==m[6]) & (b1==m[4]):一定要加括号

    if post_year1 == post_year2:
        for bbb in range(post_year1, post_year2 + 1, 1):
            for aaa in range(month1, month2 + 1, 1):
                学时0 = 0
                学时1 = 0
                学时2 = 0
                学时3 = 0
                学时4 = 0
                学时5 = 0
                学时6 = 0
                学时7 = 0
                学时8 = 0
                人次0 = 0
                人次1 = 0
                人次2 = 0
                人次3 = 0
                人次4 = 0
                人次5 = 0
                人次6 = 0
                人次7 = 0
                人次8 = 0
                print("month")
                print(aaa)
                for m in ll[1:]:
                    mm = datetime.strptime(m[13].split()[0], '%Y-%m-%d').year
                    oo = datetime.strptime(m[13].split()[0], '%Y-%m-%d').month
                    pp = datetime.strptime(m[13].split()[0], '%Y-%m-%d').day
                    # print(pp)
                    print(a1)
                    print(b1)
                    print(m[6])
                    print(m[4])
                    # print(m[10])
                    if (aaa == oo) & (bbb == mm):
                        if month1 == month2:
                            if pp in range(day1, day2 + 1, 1):
                                if 塔进区 == "3":
                                    if m[2] == 培训类别[0]:
                                        学时0 = 学时0 + float(m[11])
                                        人次0 = 人次0 + float(m[10])
                                    if m[2] == 培训类别[1]:
                                        学时1 = 学时1 + float(m[11])
                                        人次1 = 人次1 + float(m[10])
                                    if m[2] == 培训类别[2]:
                                        学时2 = 学时2 + float(m[11])
                                        人次2 = 人次2 + float(m[10])
                                    if m[2] == 培训类别[3]:
                                        学时3 = 学时3 + float(m[11])
                                        人次3 = 人次3 + float(m[10])
                                    if m[2] == 培训类别[4]:
                                        学时4 = 学时4 + float(m[11])
                                        人次4 = 人次4 + float(m[10])
                                    if m[2] == 培训类别[5]:
                                        学时5 = 学时6 + float(m[11])
                                        人次5 = 人次6 + float(m[10])
                                    if m[2] == 培训类别[6]:
                                        学时6 = 学时6 + float(m[11])
                                        人次6 = 人次6 + float(m[10])
                                    if m[2] == 培训类别[7]:
                                        学时7 = 学时7 + float(m[11])
                                        人次7 = 人次7 + float(m[10])
                                    if m[2] == 培训类别[8]:
                                        学时8 = 学时8 + float(m[11])
                                        人次8 = 人次8 + float(m[10])
                                else:
                                    if (a1 == m[6]) & (b1 == m[4]):
                                        # prfloat("")
                                        if m[2] == 培训类别[0]:
                                            学时0 = 学时0 + float(m[11])
                                            人次0 = 人次0 + float(m[10])
                                        if m[2] == 培训类别[1]:
                                            学时1 = 学时1 + float(m[11])
                                            人次1 = 人次1 + float(m[10])
                                        if m[2] == 培训类别[2]:
                                            学时2 = 学时2 + float(m[11])
                                            人次2 = 人次2 + float(m[10])
                                        if m[2] == 培训类别[3]:
                                            学时3 = 学时3 + float(m[11])
                                            人次3 = 人次3 + float(m[10])
                                        if m[2] == 培训类别[4]:
                                            学时4 = 学时4 + float(m[11])
                                            人次4 = 人次4 + float(m[10])
                                        if m[2] == 培训类别[5]:
                                            学时5 = 学时6 + float(m[11])
                                            人次5 = 人次6 + float(m[10])
                                        if m[2] == 培训类别[6]:
                                            学时6 = 学时6 + float(m[11])
                                            人次6 = 人次6 + float(m[10])
                                        if m[2] == 培训类别[7]:
                                            学时7 = 学时7 + float(m[11])
                                            人次7 = 人次7 + float(m[10])
                                        if m[2] == 培训类别[8]:
                                            学时8 = 学时8 + float(m[11])
                                            人次8 = 人次8 + float(m[10])

                        if month1 < month2:
                            if (pp in range(day1, 31 + 1, 1)) & (oo in range(month1, month1 + 1, 1)):
                                if 塔进区 == "3":
                                    if m[2] == 培训类别[0]:
                                        学时0 = 学时0 + float(m[11])
                                        人次0 = 人次0 + float(m[10])
                                    if m[2] == 培训类别[1]:
                                        学时1 = 学时1 + float(m[11])
                                        人次1 = 人次1 + float(m[10])
                                    if m[2] == 培训类别[2]:
                                        学时2 = 学时2 + float(m[11])
                                        人次2 = 人次2 + float(m[10])
                                    if m[2] == 培训类别[3]:
                                        学时3 = 学时3 + float(m[11])
                                        人次3 = 人次3 + float(m[10])
                                    if m[2] == 培训类别[4]:
                                        学时4 = 学时4 + float(m[11])
                                        人次4 = 人次4 + float(m[10])
                                    if m[2] == 培训类别[5]:
                                        学时5 = 学时6 + float(m[11])
                                        人次5 = 人次6 + float(m[10])
                                    if m[2] == 培训类别[6]:
                                        学时6 = 学时6 + float(m[11])
                                        人次6 = 人次6 + float(m[10])
                                    if m[2] == 培训类别[7]:
                                        学时7 = 学时7 + float(m[11])
                                        人次7 = 人次7 + float(m[10])
                                    if m[2] == 培训类别[8]:
                                        学时8 = 学时8 + float(m[11])
                                        人次8 = 人次8 + float(m[10])
                                else:
                                    if (a1 == m[6]) & (b1 == m[4]):
                                        # prfloat("")
                                        if m[2] == 培训类别[0]:
                                            学时0 = 学时0 + float(m[11])
                                            人次0 = 人次0 + float(m[10])
                                        if m[2] == 培训类别[1]:
                                            学时1 = 学时1 + float(m[11])
                                            人次1 = 人次1 + float(m[10])
                                        if m[2] == 培训类别[2]:
                                            学时2 = 学时2 + float(m[11])
                                            人次2 = 人次2 + float(m[10])
                                        if m[2] == 培训类别[3]:
                                            学时3 = 学时3 + float(m[11])
                                            人次3 = 人次3 + float(m[10])
                                        if m[2] == 培训类别[4]:
                                            学时4 = 学时4 + float(m[11])
                                            人次4 = 人次4 + float(m[10])
                                        if m[2] == 培训类别[5]:
                                            学时5 = 学时6 + float(m[11])
                                            人次5 = 人次6 + float(m[10])
                                        if m[2] == 培训类别[6]:
                                            学时6 = 学时6 + float(m[11])
                                            人次6 = 人次6 + float(m[10])
                                        if m[2] == 培训类别[7]:
                                            学时7 = 学时7 + float(m[11])
                                            人次7 = 人次7 + float(m[10])
                                        if m[2] == 培训类别[8]:
                                            学时8 = 学时8 + float(m[11])
                                            人次8 = 人次8 + float(m[10])
                            if (pp in range(1, 31 + 1, 1)) & (oo in range(month1 + 1, month2, 1)):
                                if 塔进区 == "3":
                                    if m[2] == 培训类别[0]:
                                        学时0 = 学时0 + float(m[11])
                                        人次0 = 人次0 + float(m[10])
                                    if m[2] == 培训类别[1]:
                                        学时1 = 学时1 + float(m[11])
                                        人次1 = 人次1 + float(m[10])
                                    if m[2] == 培训类别[2]:
                                        学时2 = 学时2 + float(m[11])
                                        人次2 = 人次2 + float(m[10])
                                    if m[2] == 培训类别[3]:
                                        学时3 = 学时3 + float(m[11])
                                        人次3 = 人次3 + float(m[10])
                                    if m[2] == 培训类别[4]:
                                        学时4 = 学时4 + float(m[11])
                                        人次4 = 人次4 + float(m[10])
                                    if m[2] == 培训类别[5]:
                                        学时5 = 学时6 + float(m[11])
                                        人次5 = 人次6 + float(m[10])
                                    if m[2] == 培训类别[6]:
                                        学时6 = 学时6 + float(m[11])
                                        人次6 = 人次6 + float(m[10])
                                    if m[2] == 培训类别[7]:
                                        学时7 = 学时7 + float(m[11])
                                        人次7 = 人次7 + float(m[10])
                                    if m[2] == 培训类别[8]:
                                        学时8 = 学时8 + float(m[11])
                                        人次8 = 人次8 + float(m[10])
                                else:
                                    if (a1 == m[6]) & (b1 == m[4]):
                                        # prfloat("")
                                        if m[2] == 培训类别[0]:
                                            学时0 = 学时0 + float(m[11])
                                            人次0 = 人次0 + float(m[10])
                                        if m[2] == 培训类别[1]:
                                            学时1 = 学时1 + float(m[11])
                                            人次1 = 人次1 + float(m[10])
                                        if m[2] == 培训类别[2]:
                                            学时2 = 学时2 + float(m[11])
                                            人次2 = 人次2 + float(m[10])
                                        if m[2] == 培训类别[3]:
                                            学时3 = 学时3 + float(m[11])
                                            人次3 = 人次3 + float(m[10])
                                        if m[2] == 培训类别[4]:
                                            学时4 = 学时4 + float(m[11])
                                            人次4 = 人次4 + float(m[10])
                                        if m[2] == 培训类别[5]:
                                            学时5 = 学时6 + float(m[11])
                                            人次5 = 人次6 + float(m[10])
                                        if m[2] == 培训类别[6]:
                                            学时6 = 学时6 + float(m[11])
                                            人次6 = 人次6 + float(m[10])
                                        if m[2] == 培训类别[7]:
                                            学时7 = 学时7 + float(m[11])
                                            人次7 = 人次7 + float(m[10])
                                        if m[2] == 培训类别[8]:
                                            学时8 = 学时8 + float(m[11])
                                            人次8 = 人次8 + float(m[10])
                            if (pp in range(1, day2 + 1, 1)) & (oo in range(month2, month2 + 1, 1)):
                                if 塔进区 == "3":
                                    if m[2] == 培训类别[0]:
                                        学时0 = 学时0 + float(m[11])
                                        人次0 = 人次0 + float(m[10])
                                    if m[2] == 培训类别[1]:
                                        学时1 = 学时1 + float(m[11])
                                        人次1 = 人次1 + float(m[10])
                                    if m[2] == 培训类别[2]:
                                        学时2 = 学时2 + float(m[11])
                                        人次2 = 人次2 + float(m[10])
                                    if m[2] == 培训类别[3]:
                                        学时3 = 学时3 + float(m[11])
                                        人次3 = 人次3 + float(m[10])
                                    if m[2] == 培训类别[4]:
                                        学时4 = 学时4 + float(m[11])
                                        人次4 = 人次4 + float(m[10])
                                    if m[2] == 培训类别[5]:
                                        学时5 = 学时6 + float(m[11])
                                        人次5 = 人次6 + float(m[10])
                                    if m[2] == 培训类别[6]:
                                        学时6 = 学时6 + float(m[11])
                                        人次6 = 人次6 + float(m[10])
                                    if m[2] == 培训类别[7]:
                                        学时7 = 学时7 + float(m[11])
                                        人次7 = 人次7 + float(m[10])
                                    if m[2] == 培训类别[8]:
                                        学时8 = 学时8 + float(m[11])
                                        人次8 = 人次8 + float(m[10])
                                else:
                                    if (a1 == m[6]) & (b1 == m[4]):
                                        # prfloat("")
                                        if m[2] == 培训类别[0]:
                                            学时0 = 学时0 + float(m[11])
                                            人次0 = 人次0 + float(m[10])
                                        if m[2] == 培训类别[1]:
                                            学时1 = 学时1 + float(m[11])
                                            人次1 = 人次1 + float(m[10])
                                        if m[2] == 培训类别[2]:
                                            学时2 = 学时2 + float(m[11])
                                            人次2 = 人次2 + float(m[10])
                                        if m[2] == 培训类别[3]:
                                            学时3 = 学时3 + float(m[11])
                                            人次3 = 人次3 + float(m[10])
                                        if m[2] == 培训类别[4]:
                                            学时4 = 学时4 + float(m[11])
                                            人次4 = 人次4 + float(m[10])
                                        if m[2] == 培训类别[5]:
                                            学时5 = 学时6 + float(m[11])
                                            人次5 = 人次6 + float(m[10])
                                        if m[2] == 培训类别[6]:
                                            学时6 = 学时6 + float(m[11])
                                            人次6 = 人次6 + float(m[10])
                                        if m[2] == 培训类别[7]:
                                            学时7 = 学时7 + float(m[11])
                                            人次7 = 人次7 + float(m[10])
                                        if m[2] == 培训类别[8]:
                                            学时8 = 学时8 + float(m[11])
                                            人次8 = 人次8 + float(m[10])
                ee = []
                ee.append(str(bbb) + "")
                ee.append(str(aaa) + "月")
                ee.append(学时0)
                ee.append(人次0)
                ee.append(学时1)
                ee.append(人次1)
                ee.append(学时2)
                ee.append(人次2)
                ee.append(学时3)
                ee.append(人次3)
                ee.append(学时4)
                ee.append(人次4)
                ee.append(学时5)
                ee.append(人次5)
                ee.append(学时6)
                ee.append(人次6)
                ee.append(学时7)
                ee.append(人次7)
                ee.append(学时8)
                ee.append(人次8)
                ee.append(学时0
                          + 学时1
                          + 学时2
                          + 学时3
                          + 学时4
                          + 学时5
                          + 学时6
                          + 学时7
                          + 学时8)
                ee.append(人次0
                          + 人次1
                          + 人次2
                          + 人次3
                          + 人次4
                          + 人次5
                          + 人次6
                          + 人次7
                          + 人次8)
                temp1.append(ee)
                print("temp1")
                print(temp1)
    if post_year1 < post_year2:
        for bbb in range(post_year1, post_year2 + 1, 1):
            for aaa in range(month1, month2 + 1, 1):
                学时0 = 0
                学时1 = 0
                学时2 = 0
                学时3 = 0
                学时4 = 0
                学时5 = 0
                学时6 = 0
                学时7 = 0
                学时8 = 0
                人次0 = 0
                人次1 = 0
                人次2 = 0
                人次3 = 0
                人次4 = 0
                人次5 = 0
                人次6 = 0
                人次7 = 0
                人次8 = 0
                print("month")
                print(aaa)
                for m in ll[1:]:
                    mm = datetime.strptime(m[13].split()[0], '%Y-%m-%d').year
                    oo = datetime.strptime(m[13].split()[0], '%Y-%m-%d').month
                    pp = datetime.strptime(m[13].split()[0], '%Y-%m-%d').day
                    # print(pp)
                    print(a1)
                    print(b1)
                    print(m[6])
                    print(m[4])
                    # print(m[10])
                    if (aaa == oo) & (bbb == mm):
                        if (pp in range(day1, 31 + 1, 1)) & (oo in range(month1, month1 + 1, 1)) \
                                & (mm in range(post_year1, post_year1 + 1, 1)):
                            if 塔进区 == "3":
                                if m[2] == 培训类别[0]:
                                    学时0 = 学时0 + float(m[11])
                                    人次0 = 人次0 + float(m[10])
                                if m[2] == 培训类别[1]:
                                    学时1 = 学时1 + float(m[11])
                                    人次1 = 人次1 + float(m[10])
                                if m[2] == 培训类别[2]:
                                    学时2 = 学时2 + float(m[11])
                                    人次2 = 人次2 + float(m[10])
                                if m[2] == 培训类别[3]:
                                    学时3 = 学时3 + float(m[11])
                                    人次3 = 人次3 + float(m[10])
                                if m[2] == 培训类别[4]:
                                    学时4 = 学时4 + float(m[11])
                                    人次4 = 人次4 + float(m[10])
                                if m[2] == 培训类别[5]:
                                    学时5 = 学时6 + float(m[11])
                                    人次5 = 人次6 + float(m[10])
                                if m[2] == 培训类别[6]:
                                    学时6 = 学时6 + float(m[11])
                                    人次6 = 人次6 + float(m[10])
                                if m[2] == 培训类别[7]:
                                    学时7 = 学时7 + float(m[11])
                                    人次7 = 人次7 + float(m[10])
                                if m[2] == 培训类别[8]:
                                    学时8 = 学时8 + float(m[11])
                                    人次8 = 人次8 + float(m[10])
                            else:
                                if (a1 == m[6]) & (b1 == m[4]):
                                    # prfloat("")
                                    if m[2] == 培训类别[0]:
                                        学时0 = 学时0 + float(m[11])
                                        人次0 = 人次0 + float(m[10])
                                    if m[2] == 培训类别[1]:
                                        学时1 = 学时1 + float(m[11])
                                        人次1 = 人次1 + float(m[10])
                                    if m[2] == 培训类别[2]:
                                        学时2 = 学时2 + float(m[11])
                                        人次2 = 人次2 + float(m[10])
                                    if m[2] == 培训类别[3]:
                                        学时3 = 学时3 + float(m[11])
                                        人次3 = 人次3 + float(m[10])
                                    if m[2] == 培训类别[4]:
                                        学时4 = 学时4 + float(m[11])
                                        人次4 = 人次4 + float(m[10])
                                    if m[2] == 培训类别[5]:
                                        学时5 = 学时6 + float(m[11])
                                        人次5 = 人次6 + float(m[10])
                                    if m[2] == 培训类别[6]:
                                        学时6 = 学时6 + float(m[11])
                                        人次6 = 人次6 + float(m[10])
                                    if m[2] == 培训类别[7]:
                                        学时7 = 学时7 + float(m[11])
                                        人次7 = 人次7 + float(m[10])
                                    if m[2] == 培训类别[8]:
                                        学时8 = 学时8 + float(m[11])
                                        人次8 = 人次8 + float(m[10])
                        if (pp in (range(1, 31 + 1, 1))) & (oo in range(month1 + 1, 12 + 1, 1)) \
                                & (mm in range(post_year1, post_year1 + 1, 1)):
                            if 塔进区 == "3":
                                if m[2] == 培训类别[0]:
                                    学时0 = 学时0 + float(m[11])
                                    人次0 = 人次0 + float(m[10])
                                if m[2] == 培训类别[1]:
                                    学时1 = 学时1 + float(m[11])
                                    人次1 = 人次1 + float(m[10])
                                if m[2] == 培训类别[2]:
                                    学时2 = 学时2 + float(m[11])
                                    人次2 = 人次2 + float(m[10])
                                if m[2] == 培训类别[3]:
                                    学时3 = 学时3 + float(m[11])
                                    人次3 = 人次3 + float(m[10])
                                if m[2] == 培训类别[4]:
                                    学时4 = 学时4 + float(m[11])
                                    人次4 = 人次4 + float(m[10])
                                if m[2] == 培训类别[5]:
                                    学时5 = 学时6 + float(m[11])
                                    人次5 = 人次6 + float(m[10])
                                if m[2] == 培训类别[6]:
                                    学时6 = 学时6 + float(m[11])
                                    人次6 = 人次6 + float(m[10])
                                if m[2] == 培训类别[7]:
                                    学时7 = 学时7 + float(m[11])
                                    人次7 = 人次7 + float(m[10])
                                if m[2] == 培训类别[8]:
                                    学时8 = 学时8 + float(m[11])
                                    人次8 = 人次8 + float(m[10])
                            else:
                                if (a1 == m[6]) & (b1 == m[4]):
                                    # prfloat("")
                                    if m[2] == 培训类别[0]:
                                        学时0 = 学时0 + float(m[11])
                                        人次0 = 人次0 + float(m[10])
                                    if m[2] == 培训类别[1]:
                                        学时1 = 学时1 + float(m[11])
                                        人次1 = 人次1 + float(m[10])
                                    if m[2] == 培训类别[2]:
                                        学时2 = 学时2 + float(m[11])
                                        人次2 = 人次2 + float(m[10])
                                    if m[2] == 培训类别[3]:
                                        学时3 = 学时3 + float(m[11])
                                        人次3 = 人次3 + float(m[10])
                                    if m[2] == 培训类别[4]:
                                        学时4 = 学时4 + float(m[11])
                                        人次4 = 人次4 + float(m[10])
                                    if m[2] == 培训类别[5]:
                                        学时5 = 学时6 + float(m[11])
                                        人次5 = 人次6 + float(m[10])
                                    if m[2] == 培训类别[6]:
                                        学时6 = 学时6 + float(m[11])
                                        人次6 = 人次6 + float(m[10])
                                    if m[2] == 培训类别[7]:
                                        学时7 = 学时7 + float(m[11])
                                        人次7 = 人次7 + float(m[10])
                                    if m[2] == 培训类别[8]:
                                        学时8 = 学时8 + float(m[11])
                                        人次8 = 人次8 + float(m[10])
                        if (pp in range(1, 31 + 1, 1)) & (oo in range(1, 12 + 1, 1)) \
                                & (mm in range(post_year1 + 1, post_year2 - 1 + 1, 1)):
                            if 塔进区 == "3":
                                if m[2] == 培训类别[0]:
                                    学时0 = 学时0 + float(m[11])
                                    人次0 = 人次0 + float(m[10])
                                if m[2] == 培训类别[1]:
                                    学时1 = 学时1 + float(m[11])
                                    人次1 = 人次1 + float(m[10])
                                if m[2] == 培训类别[2]:
                                    学时2 = 学时2 + float(m[11])
                                    人次2 = 人次2 + float(m[10])
                                if m[2] == 培训类别[3]:
                                    学时3 = 学时3 + float(m[11])
                                    人次3 = 人次3 + float(m[10])
                                if m[2] == 培训类别[4]:
                                    学时4 = 学时4 + float(m[11])
                                    人次4 = 人次4 + float(m[10])
                                if m[2] == 培训类别[5]:
                                    学时5 = 学时6 + float(m[11])
                                    人次5 = 人次6 + float(m[10])
                                if m[2] == 培训类别[6]:
                                    学时6 = 学时6 + float(m[11])
                                    人次6 = 人次6 + float(m[10])
                                if m[2] == 培训类别[7]:
                                    学时7 = 学时7 + float(m[11])
                                    人次7 = 人次7 + float(m[10])
                                if m[2] == 培训类别[8]:
                                    学时8 = 学时8 + float(m[11])
                                    人次8 = 人次8 + float(m[10])
                            else:
                                if (a1 == m[6]) & (b1 == m[4]):
                                    # prfloat("")
                                    if m[2] == 培训类别[0]:
                                        学时0 = 学时0 + float(m[11])
                                        人次0 = 人次0 + float(m[10])
                                    if m[2] == 培训类别[1]:
                                        学时1 = 学时1 + float(m[11])
                                        人次1 = 人次1 + float(m[10])
                                    if m[2] == 培训类别[2]:
                                        学时2 = 学时2 + float(m[11])
                                        人次2 = 人次2 + float(m[10])
                                    if m[2] == 培训类别[3]:
                                        学时3 = 学时3 + float(m[11])
                                        人次3 = 人次3 + float(m[10])
                                    if m[2] == 培训类别[4]:
                                        学时4 = 学时4 + float(m[11])
                                        人次4 = 人次4 + float(m[10])
                                    if m[2] == 培训类别[5]:
                                        学时5 = 学时6 + float(m[11])
                                        人次5 = 人次6 + float(m[10])
                                    if m[2] == 培训类别[6]:
                                        学时6 = 学时6 + float(m[11])
                                        人次6 = 人次6 + float(m[10])
                                    if m[2] == 培训类别[7]:
                                        学时7 = 学时7 + float(m[11])
                                        人次7 = 人次7 + float(m[10])
                                    if m[2] == 培训类别[8]:
                                        学时8 = 学时8 + float(m[11])
                                        人次8 = 人次8 + float(m[10])
                        if (pp in range(1, 31 + 1, 1)) & (oo in range(1, month2 - 1 + 1, 1)) \
                                & (mm in range(post_year2, post_year2 + 1, 1)):
                            if 塔进区 == "3":
                                if m[2] == 培训类别[0]:
                                    学时0 = 学时0 + float(m[11])
                                    人次0 = 人次0 + float(m[10])
                                if m[2] == 培训类别[1]:
                                    学时1 = 学时1 + float(m[11])
                                    人次1 = 人次1 + float(m[10])
                                if m[2] == 培训类别[2]:
                                    学时2 = 学时2 + float(m[11])
                                    人次2 = 人次2 + float(m[10])
                                if m[2] == 培训类别[3]:
                                    学时3 = 学时3 + float(m[11])
                                    人次3 = 人次3 + float(m[10])
                                if m[2] == 培训类别[4]:
                                    学时4 = 学时4 + float(m[11])
                                    人次4 = 人次4 + float(m[10])
                                if m[2] == 培训类别[5]:
                                    学时5 = 学时6 + float(m[11])
                                    人次5 = 人次6 + float(m[10])
                                if m[2] == 培训类别[6]:
                                    学时6 = 学时6 + float(m[11])
                                    人次6 = 人次6 + float(m[10])
                                if m[2] == 培训类别[7]:
                                    学时7 = 学时7 + float(m[11])
                                    人次7 = 人次7 + float(m[10])
                                if m[2] == 培训类别[8]:
                                    学时8 = 学时8 + float(m[11])
                                    人次8 = 人次8 + float(m[10])
                            else:
                                if (a1 == m[6]) & (b1 == m[4]):
                                    # prfloat("")
                                    if m[2] == 培训类别[0]:
                                        学时0 = 学时0 + float(m[11])
                                        人次0 = 人次0 + float(m[10])
                                    if m[2] == 培训类别[1]:
                                        学时1 = 学时1 + float(m[11])
                                        人次1 = 人次1 + float(m[10])
                                    if m[2] == 培训类别[2]:
                                        学时2 = 学时2 + float(m[11])
                                        人次2 = 人次2 + float(m[10])
                                    if m[2] == 培训类别[3]:
                                        学时3 = 学时3 + float(m[11])
                                        人次3 = 人次3 + float(m[10])
                                    if m[2] == 培训类别[4]:
                                        学时4 = 学时4 + float(m[11])
                                        人次4 = 人次4 + float(m[10])
                                    if m[2] == 培训类别[5]:
                                        学时5 = 学时6 + float(m[11])
                                        人次5 = 人次6 + float(m[10])
                                    if m[2] == 培训类别[6]:
                                        学时6 = 学时6 + float(m[11])
                                        人次6 = 人次6 + float(m[10])
                                    if m[2] == 培训类别[7]:
                                        学时7 = 学时7 + float(m[11])
                                        人次7 = 人次7 + float(m[10])
                                    if m[2] == 培训类别[8]:
                                        学时8 = 学时8 + float(m[11])
                                        人次8 = 人次8 + float(m[10])
                        if (pp in range(1, day2 + 1, 1)) & (oo in range(month2, month2 + 1, 1)) \
                                & (mm in range(post_year2, post_year2 + 1, 1)):
                            if 塔进区 == "3":
                                if m[2] == 培训类别[0]:
                                    学时0 = 学时0 + float(m[11])
                                    人次0 = 人次0 + float(m[10])
                                if m[2] == 培训类别[1]:
                                    学时1 = 学时1 + float(m[11])
                                    人次1 = 人次1 + float(m[10])
                                if m[2] == 培训类别[2]:
                                    学时2 = 学时2 + float(m[11])
                                    人次2 = 人次2 + float(m[10])
                                if m[2] == 培训类别[3]:
                                    学时3 = 学时3 + float(m[11])
                                    人次3 = 人次3 + float(m[10])
                                if m[2] == 培训类别[4]:
                                    学时4 = 学时4 + float(m[11])
                                    人次4 = 人次4 + float(m[10])
                                if m[2] == 培训类别[5]:
                                    学时5 = 学时6 + float(m[11])
                                    人次5 = 人次6 + float(m[10])
                                if m[2] == 培训类别[6]:
                                    学时6 = 学时6 + float(m[11])
                                    人次6 = 人次6 + float(m[10])
                                if m[2] == 培训类别[7]:
                                    学时7 = 学时7 + float(m[11])
                                    人次7 = 人次7 + float(m[10])
                                if m[2] == 培训类别[8]:
                                    学时8 = 学时8 + float(m[11])
                                    人次8 = 人次8 + float(m[10])
                            else:
                                if (a1 == m[6]) & (b1 == m[4]):
                                    # prfloat("")
                                    if m[2] == 培训类别[0]:
                                        学时0 = 学时0 + float(m[11])
                                        人次0 = 人次0 + float(m[10])
                                    if m[2] == 培训类别[1]:
                                        学时1 = 学时1 + float(m[11])
                                        人次1 = 人次1 + float(m[10])
                                    if m[2] == 培训类别[2]:
                                        学时2 = 学时2 + float(m[11])
                                        人次2 = 人次2 + float(m[10])
                                    if m[2] == 培训类别[3]:
                                        学时3 = 学时3 + float(m[11])
                                        人次3 = 人次3 + float(m[10])
                                    if m[2] == 培训类别[4]:
                                        学时4 = 学时4 + float(m[11])
                                        人次4 = 人次4 + float(m[10])
                                    if m[2] == 培训类别[5]:
                                        学时5 = 学时6 + float(m[11])
                                        人次5 = 人次6 + float(m[10])
                                    if m[2] == 培训类别[6]:
                                        学时6 = 学时6 + float(m[11])
                                        人次6 = 人次6 + float(m[10])
                                    if m[2] == 培训类别[7]:
                                        学时7 = 学时7 + float(m[11])
                                        人次7 = 人次7 + float(m[10])
                                    if m[2] == 培训类别[8]:
                                        学时8 = 学时8 + float(m[11])
                                        人次8 = 人次8 + float(m[10])
                ee = []
                ee.append(str(bbb) + "")
                ee.append(str(aaa) + "月")
                ee.append(学时0)
                ee.append(人次0)
                ee.append(学时1)
                ee.append(人次1)
                ee.append(学时2)
                ee.append(人次2)
                ee.append(学时3)
                ee.append(人次3)
                ee.append(学时4)
                ee.append(人次4)
                ee.append(学时5)
                ee.append(人次5)
                ee.append(学时6)
                ee.append(人次6)
                ee.append(学时7)
                ee.append(人次7)
                ee.append(学时8)
                ee.append(人次8)
                ee.append(学时0
                          + 学时1
                          + 学时2
                          + 学时3
                          + 学时4
                          + 学时5
                          + 学时6
                          + 学时7
                          + 学时8)
                ee.append(人次0
                          + 人次1
                          + 人次2
                          + 人次3
                          + 人次4
                          + 人次5
                          + 人次6
                          + 人次7
                          + 人次8)
                temp1.append(ee)
                print("temp1")
                print(temp1)

    # if post_year1 == post_year2:
    #     if int(mm) == post_year1:
    #         for mm1 in range(month1 - 1, month2, 1):
    #             if oo ==mm1+1:
    #                 if month1 == month2:
    #                     for nn1 in range(day1 - 1, day2, 1):
    #                         if pp == nn1:
    #                             ee = []
    #                             ee.append(mm)
    #                             ee.append(oo)

    # 查询最小到月
    temp = []
    # 表头
    aa1 = models.tower_trainning_total_time.objects \
        .filter(
        Q(data03__contains='上岗前培训') | Q(data03__contains='学时')).values_list(
        "data01",
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
    aa1 = list(aa1)
    for i in aa1:
        temp.append(i)

    if post_year1 > post_year2:
        print("年份选择错误")
    if post_year1 == post_year2:
        for mm1 in range(month1 - 1, month2, 1):
            aa = models.tower_trainning_total_time.objects \
                .filter(Q(data01=post_year1, data02=月份[mm1])).values_list(
                "data01",
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
            aa = list(aa)

            for i in aa:
                temp.append(i)

    if post_year1 < post_year2:
        # 相差的年数 = post_year2 - post_year1
        for mm1 in range(month1 - 1, 12, 1):
            aa = models.tower_trainning_total_time.objects \
                .filter(
                Q(data01=post_year1, data02=月份[mm1])).values_list(
                "data01",
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
            aa = list(aa)
            for i in aa:
                temp.append(i)

        for yy in range(post_year1 + 1, post_year2, 1):
            for mm2 in range(0, 12, 1):
                aa = models.tower_trainning_total_time.objects \
                    .filter(
                    Q(data01=yy,
                      data02=月份[mm2])).values_list(
                    "data01",
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
                aa = list(aa)
                for i in aa:
                    temp.append(i)

        for mm3 in range(0, month2, 1):
            aa = models.tower_trainning_total_time.objects \
                .filter(
                Q(data01=post_year2,
                  data02=月份[mm3])).values_list(
                "data01",
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
            aa = list(aa)
            for i in aa:
                temp.append(i)
    print("temp")
    print(temp)

    # 计算最后一行合计
    dd = ("", "合计")
    for j in range(2, len(temp[0]), 1):
        c = 0
        for i in range(2, len(temp), 1):
            c = c + float(temp[i][j])
        dd = dd + (c,)

    temp.append(dd)
    temp = json.dumps(temp, ensure_ascii=False)
    if request.session.get('status'):  # 在判断网页请求的状态时，直接调用request.session从djang_session表中读取数据验证
        name2 = request.session.get('name')
        print(name2 + '*********' + 'session登陆人')
        print(str(day1) + str(day2) + '*********' + 'day12')
    if day1 == 0 & day2 == 0:
        qq = temp

    else:
        qq = temp1
        print('*********' + 'day1 != 0')

    return render(request, 'tower_trainning_total_time.html', {'data': qq,
                                                               'year': 年份, 'month': 月份, 'post_year1': post_year1,
                                                               'month1': month1, 'day1': day1,
                                                               'post_year2': post_year2, 'month2': month2,
                                                               'day2': day2, })


def 创建数据模拟机培训学时():
    年份 = []
    获取所有可能的年份(年份)

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
        for j0 in 年份:
            for j1 in 月份:
                if models.tower_trainning_total_time.objects.filter(data01=j0, data02=j1, ):
                    print("已经有月份")
                else:
                    models.tower_trainning_total_time.objects.create(data01=j0, data02=j1, )
                    print("创建了:" + j1)

        for y in 年份:
            for i in 培训类别:
                for j in 月份:

                    # print(i)
                    # a = models.tower_trainning_total_time
                    学时 = 0
                    for k in trainningcompletion.models.trainningstatusdetail.objects.filter(frontdata3=j,
                                                                                             frontdata2=i,
                                                                                             frontdata4="塔台管制室", ).values_list(
                        'frontdata11', 'frontdata15', ):
                        # print("k" + "".join(k))
                        # for m in k:

                        m = list(k)
                        # print("m" + str(m))
                        # print("m" +str(m[0]) )
                        # print("m" + str(m[1]))
                        print(m[1].split()[0])
                        if datetime.strptime(m[1].split()[0], '%Y-%m-%d').year == y:
                            学时 = 学时 + float(m[0])
                    # print(学时)
                    人次 = 0
                    for k1 in trainningcompletion.models.trainningstatusdetail.objects.filter(frontdata3=j,
                                                                                              frontdata2=i,
                                                                                              frontdata4="塔台管制室", ).values_list(
                        'frontdata10', 'frontdata15', ):

                        m1 = list(k1)
                        if datetime.strptime(m1[1].split()[0], '%Y-%m-%d').year == y:
                            人次 = 人次 + float(m1[0])
                    # print(人次)
                    if i == "上岗前培训":
                        models.tower_trainning_total_time.objects.filter(data01=y, data02=j).update(data03=学时)
                        models.tower_trainning_total_time.objects.filter(data01=y, data02=j).update(data04=人次)
                    if i == "资格培训":
                        models.tower_trainning_total_time.objects.filter(data01=y, data02=j).update(data05=学时)
                        models.tower_trainning_total_time.objects.filter(data01=y, data02=j).update(data06=人次)
                    if i == "复习培训":
                        models.tower_trainning_total_time.objects.filter(data01=y, data02=j).update(data07=学时)
                        models.tower_trainning_total_time.objects.filter(data01=y, data02=j).update(data08=人次)
                    if i == "附加培训":
                        models.tower_trainning_total_time.objects.filter(data01=y, data02=j).update(data09=学时)
                        models.tower_trainning_total_time.objects.filter(data01=y, data02=j).update(data10=人次)
                    if i == "追加培训":
                        models.tower_trainning_total_time.objects.filter(data01=y, data02=j).update(data11=学时)
                        models.tower_trainning_total_time.objects.filter(data01=y, data02=j).update(data12=人次)
                    if i == "补习培训":
                        models.tower_trainning_total_time.objects.filter(data01=y, data02=j).update(data13=学时)
                        models.tower_trainning_total_time.objects.filter(data01=y, data02=j).update(data14=人次)
                    if i == "设备培训":
                        models.tower_trainning_total_time.objects.filter(data01=y, data02=j).update(data15=学时)
                        models.tower_trainning_total_time.objects.filter(data01=y, data02=j).update(data16=人次)
                    if i == "熟练培训":
                        models.tower_trainning_total_time.objects.filter(data01=y, data02=j).update(data17=学时)
                        models.tower_trainning_total_time.objects.filter(data01=y, data02=j).update(data18=人次)
                    if i == "专项培训":
                        models.tower_trainning_total_time.objects.filter(data01=y, data02=j).update(data19=学时)
                        models.tower_trainning_total_time.objects.filter(data01=y, data02=j).update(data20=人次)
            计算行的和(y)
            if models.tower_trainning_total_time.objects.filter(data01=y, data02="合计", ):
                print("已经有列合计")
            else:
                models.tower_trainning_total_time.objects.create(data01=y, data02="合计", )
            计算列的和(y)



    except ObjectDoesNotExist:
        print('没查到')


def 计算行的和(y):
    for i3 in 月份:

        data21 = 0  # 每行的学时和
        data22 = 0  # 每行的人次和
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
            for m in models.tower_trainning_total_time.objects.filter(data01=y, data02=i3).values_list(
                    'data' + str(k4), ):
                for k6 in m:
                    data21 = data21 + float(k6.strip())

            for n in models.tower_trainning_total_time.objects.filter(data01=y, data02=i3).values_list(
                    'data' + str(k5), ):
                for k7 in n:
                    data22 = data22 + float(k7.strip())
        models.tower_trainning_total_time.objects.filter(data01=y, data02=i3).update(
            data21=data21,
            data22=data22, )


def 计算列的和(y):
    aa = []

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

            for k in models.tower_trainning_total_time.objects.filter(data01=y, data02=i3).values_list(
                    'data' + str(k4)):
                for m in k:
                    列合计学时 = 列合计学时 + float(m.strip())  # 不可转换空字符串为整型

            for k1 in models.tower_trainning_total_time.objects.filter(data01=y, data02=i3).values_list(
                    'data' + str(k5)):
                for m1 in k1:
                    列合计人次 = 列合计人次 + float(m1.strip())

        aa.append(列合计学时)
        aa.append(列合计人次)
        # print(列合计人次)
        # print(列合计学时)
        # print(i)
        # names = locals()
        # for i in range(3, 22, 2):
        #     names['data0' + str(i)] = i

    models.tower_trainning_total_time.objects.filter(data01=y, data02="合计").update(
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


教员 = ["何升恒", "周星言", "林文", "廖海艺"]


# 以下是#•教员教学学时统计
def instructor_total_time(request):  # •教员教学学时统计

    年份 = []
    获取所有可能的年份(年份)

    now_time = datetime.now()
    year = datetime.strftime(now_time, "%y")
    year = str(2000 + float(year))

    print("year" + year)
    data = models.instructor_total_time.objects \
        .filter(Q(data01__contains='姓名') | Q(data03__contains='上岗前培训') | Q(data26=year, )).values_list(
        "data26", "data27", "data01",
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
        "data23",
        "data24",
        "data25",

    ).all()

    data = list(data)

    fileuri = []
    for i in data:
        fileuri.append(i)
    data = json.dumps(fileuri, ensure_ascii=False)
    if request.session.get('status'):  # 在判断网页请求的状态时，直接调用request.session从djang_session表中读取数据验证
        name2 = request.session.get('name')
        print(name2 + '*********' + 'session登陆人')
    return render(request, 'instructor_total_time.html', {'data': data, 'year': 年份, 'month': 月份, "人员": 教员})


def 创建教员教学总学时():
    年份 = []
    获取所有可能的年份(年份)

    培训类别 = ["上岗前培训", "资格培训", "复习培训", "附加培训", "追加培训", "补习培训"
        , "设备培训", "熟练培训", "专项培训", ]  # 指模拟机培训类别
    其他培训类别 = ["上岗前培训",
              "资格培训",
              "理论复训",
              "附加培训",
              "追加培训",
              "补习培训",
              "设备培训",
              "熟练培训",
              "专项培训",
              "案例分析",
              "安全教育",
              "空管大讲堂",
              ]

    教员 = ["何升恒", "周星言", "林文", "廖海艺"]
    科室 = ["塔台管制室",
          "区域管制室",
          ]

    try:
        if models.instructor_total_time.objects.filter(data01="姓名", data02="科室", ):
            print("已经有表头")
        else:

            models.instructor_total_time.objects.create(
                data26="年份",
                data27="月份",
                data01="姓名",
                data02="科室",
                data03="模拟机教学",
                data04="",
                data05="",
                data06="",
                data07="",
                data08="",
                data09="",
                data10="",
                data11="",
                data12="",
                data13="其他教学",
                data14="",
                data15="",
                data16="",
                data17="",
                data18="",
                data19="",
                data20="",
                data21="",
                data22="",
                data23="",
                data24="",
                data25="",

            )

            models.instructor_total_time.objects.create(
                data26="",
                data27="",
                data01="",
                data02="",
                data03="上岗前培训",
                data04="资格培训",
                data05="复习培训",
                data06="附加培训",
                data07="追加培训",
                data08="补习培训",
                data09="设备培训",
                data10="熟练培训",
                data11="专项培训",
                data12="合计",
                data13="上岗前培训",
                data14="资格培训",
                data15="理论复训",
                data16="附加培训",
                data17="追加培训",
                data18="补习培训",
                data19="设备培训",
                data20="熟练培训",
                data21="专项培训",
                data22="案例分析",
                data23="安全教育",
                data24="空管大讲堂",
                data25="合计",

            )
            print("创建了表头:")
        for j0 in 年份:
            for j1 in 月份:
                for j2 in 教员:
                    if models.instructor_total_time.objects.filter(data26=j0, data27=j1, data01=j2, ):
                        print("表2已经有年份(左侧表头)")
                    else:
                        models.instructor_total_time.objects.create(data26=j0, data27=j1, data01=j2, )
                        # print("创建了年份:" + float(j0))

        for y in 年份:
            for j in 月份:
                # 算模拟机培训
                for i in 培训类别:
                    for qq in 教员:

                        # print(i)

                        学时 = 0
                        for k in trainningcompletion.models.trainningstatusdetail.objects.filter(
                                frontdata3=j, frontdata2=i, frontdata7=qq,
                        ).values_list(
                            'frontdata11', 'frontdata15', ):
                            # print("k" + "".join(k))
                            # for m in k:

                            m = list(k)
                            # print("m" + str(m))
                            # print("m" +str(float(m[0])) )
                            # print("m" + str(m[1]))
                            print(m[1].split()[0])
                            if datetime.strptime(m[1].split()[0], '%Y-%m-%d').year == y:
                                学时 = 学时 + float(m[0])
                                # models.instructor_total_time.objects.filter(data26=y, data01=j, data02=i).update(data03=学时)

                        if i == "上岗前培训":
                            models.instructor_total_time.objects.filter(data26=y, data27=j, data01=qq, ).update(
                                data03=学时)
                        if i == "资格培训":
                            models.instructor_total_time.objects.filter(data26=y, data27=j, data01=qq).update(data04=学时)
                        if i == "复习培训":
                            models.instructor_total_time.objects.filter(data26=y, data27=j, data01=qq).update(data05=学时)
                        if i == "附加培训":
                            models.instructor_total_time.objects.filter(data26=y, data27=j, data01=qq).update(data06=学时)
                        if i == "追加培训":
                            models.instructor_total_time.objects.filter(data26=y, data27=j, data01=qq).update(data07=学时)
                        if i == "补习培训":
                            models.instructor_total_time.objects.filter(data26=y, data27=j, data01=qq).update(data08=学时)
                        if i == "设备培训":
                            models.instructor_total_time.objects.filter(data26=y, data27=j, data01=qq).update(data09=学时)
                        if i == "熟练培训":
                            models.instructor_total_time.objects.filter(data26=y, data27=j, data01=qq).update(data10=学时)
                        if i == "专项培训":
                            models.instructor_total_time.objects.filter(data26=y, data27=j, data01=qq).update(data11=学时)
                for i3 in 教员:

                    data12 = 0  # 每行的学时和

                    for k3 in range(3, 12, 1):
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
                        for m in models.instructor_total_time.objects.filter(data26=y, data27=j, data01=i3).values_list(
                                'data' + str(k4), ):
                            for k6 in m:
                                if k6 == "":
                                    k6 = "0"
                                data12 = data12 + float(k6.strip())
                    models.instructor_total_time.objects.filter(data26=y, data27=j, data01=i3).update(
                        data12=data12,
                    )

                # 算其他培训
                for i in 其他培训类别:
                    for qq in 教员:

                        # print(i)

                        学时 = 0
                        for k in trainningcompletion.models.trainningstatusdetailother.objects.filter(
                                frontdata3=j, frontdata2=i,
                                frontdata7=qq,
                        ).values_list(
                            'frontdata11', 'frontdata15', ):
                            # print("k" + "".join(k))
                            # for m in k:

                            m = list(k)
                            # print("m" + str(m))
                            # print("m" +str(float(m[0])) )
                            # print("m" + str(m[1]))
                            print(m[1].split()[0])
                            if datetime.strptime(m[1].split()[0], '%Y-%m-%d').year == y:
                                学时 = 学时 + float(m[0])
                                # models.instructor_total_time.objects.filter(data26=y, data27=j, data01=qq, data02=i).update(data03=学时)

                        if i == "上岗前培训":
                            models.instructor_total_time.objects.filter(data26=y, data27=j, data01=qq, ).update(
                                data13=学时)
                        if i == "资格培训":
                            models.instructor_total_time.objects.filter(data26=y, data27=j, data01=qq).update(data14=学时)
                        if i == "理论复训":
                            models.instructor_total_time.objects.filter(data26=y, data27=j, data01=qq).update(data15=学时)
                        if i == "附加培训":
                            models.instructor_total_time.objects.filter(data26=y, data27=j, data01=qq).update(data16=学时)
                        if i == "追加培训":
                            models.instructor_total_time.objects.filter(data26=y, data27=j, data01=qq).update(data17=学时)
                        if i == "补习培训":
                            models.instructor_total_time.objects.filter(data26=y, data27=j, data01=qq).update(data18=学时)
                        if i == "设备培训":
                            models.instructor_total_time.objects.filter(data26=y, data27=j, data01=qq).update(data19=学时)
                        if i == "熟练培训":
                            models.instructor_total_time.objects.filter(data26=y, data27=j, data01=qq).update(data20=学时)
                        if i == "专项培训":
                            models.instructor_total_time.objects.filter(data26=y, data27=j, data01=qq).update(data21=学时)
                        if i == "案例分析":
                            models.instructor_total_time.objects.filter(data26=y, data27=j, data01=qq).update(data22=学时)
                        if i == "安全教育":
                            models.instructor_total_time.objects.filter(data26=y, data27=j, data01=qq).update(data23=学时)
                        if i == "空管大讲堂":
                            models.instructor_total_time.objects.filter(data26=y, data27=j, data01=qq).update(data24=学时)
                for i3 in 教员:
                    data25 = 0  # 每行的学时和
                    for k3 in range(13, 25, 1):
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
                        for m in models.instructor_total_time.objects.filter(data26=y, data27=j, data01=i3).values_list(
                                'data' + str(k4), ):
                            for k6 in m:
                                if k6 == "":
                                    k6 = "0"  # 防止为空
                                data25 = data25 + float(k6.strip())
                    models.instructor_total_time.objects.filter(data26=y, data27=j, data01=i3).update(
                        data25=data25,
                    )











    except ObjectDoesNotExist:
        print('没查到')


def instructor_total_time_post(request):
    post_year1 = int(request.POST.get('year1'))
    month1 = request.POST.get('month1')
    month1 = int(''.join(month1).split("月")[0])

    post_year2 = int(request.POST.get('year2'))
    month2 = request.POST.get('month2')
    month2 = int(''.join(month2).split("月")[0])
    选的人员 = request.POST.get('人员')

    # 创建数据模拟机培训学时()
    年份 = []
    获取所有可能的年份(年份)

    temp = []
    # 表头
    aa1 = models.instructor_total_time.objects \
        .filter(
        Q(data01__contains='姓名') | Q(data03__contains='上岗前培训')).values_list(
        "data26",
        "data27",
        "data01",
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
        "data23",
        "data24",
        "data25",

    ).all()
    aa1 = list(aa1)
    for i in aa1:
        temp.append(i)

    if post_year1 > post_year2:
        print("年份选择错误")
    if post_year1 == post_year2:
        for mm1 in range(month1 - 1, month2, 1):
            aa = models.instructor_total_time.objects \
                .filter(Q(data26=post_year1, data27=月份[mm1], data01=选的人员)).values_list(
                "data26",
                "data27",
                "data01",
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
                "data23",
                "data24",
                "data25",

            ).all()
            aa = list(aa)

            for i in aa:
                temp.append(i)

    if post_year1 < post_year2:
        # 相差的年数 = post_year2 - post_year1
        for mm1 in range(month1 - 1, 12, 1):
            aa = models.instructor_total_time.objects \
                .filter(
                Q(data26=post_year1, data27=月份[mm1], data01=选的人员)).values_list(
                "data26",
                "data27",
                "data01",
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
                "data23",
                "data24",
                "data25",

            ).all()
            aa = list(aa)
            for i in aa:
                temp.append(i)

        for yy in range(post_year1 + 1, post_year2, 1):
            for mm2 in range(0, 12, 1):
                aa = models.instructor_total_time.objects \
                    .filter(
                    Q(data26=yy, data02=月份[mm2], data01=选的人员
                      )).values_list(
                    "data26",
                    "data27",
                    "data01",
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
                    "data23",
                    "data24",
                    "data25",

                ).all()
                aa = list(aa)
                for i in aa:
                    temp.append(i)
        for mm3 in range(0, month2, 1):
            aa = models.instructor_total_time.objects \
                .filter(
                Q(data26=post_year2, data27=月份[mm3], data01=选的人员
                  )).values_list(
                "data26",
                "data27",
                "data01",
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
                "data23",
                "data24",
                "data25",

            ).all()

    aa = list(aa)
    for i in aa:
        temp.append(i)
    print(temp)

    # # 计算最后一行合计
    # dd = ("", "合计")
    # for j in range(2, len(temp[0]), 1):
    #     c = 0
    #     for i in range(2, len(temp), 1):
    #         c = c + float(temp[i][j])
    #     dd = dd + (c,)
    #
    # temp.append(dd)

    data = json.dumps(temp, ensure_ascii=False)
    if request.session.get('status'):  # 在判断网页请求的状态时，直接调用request.session从djang_session表中读取数据验证
        name2 = request.session.get('name')
        print(name2 + '*********' + 'session登陆人')

    return render(request, 'instructor_total_time.html', {'data': data, 'year': 年份, 'month': 月份, "人员": 教员})


def test(request):  # 测试

    培训类别 = {"上岗前培训", "资格培训", "复习培训", "附加培训", "追加培训", "补习培训"
        , "设备培训", "熟练培训", "专项培训",
            }
    for i in 培训类别:
        print(i)
        print('data' + str({i}))

    return render(request, 'ok.html', )


# 先获取教员列表
def instructor_teach_record_instructorlist(request):  # •

    instructorlist = ["马朝兵", "何升恒"]
    return render(request, 'instructor_teach_record_instructorlist.html', {'instructorlist': instructorlist, })


# # 教员教学记录
def instructor_teach_record_instructorlist_post(request):
    instructorlist = ["马朝兵", "何升恒"]
    instructor = request.POST.get('instructor')

    学时 = 0
    data = []
    # 表头
    hh = []
    hh.append("年      ")
    hh.append("日期    ")
    hh.append("主办单位")
    hh.append("教学地点")
    hh.append("培训类别")
    hh.append("教学方式")
    hh.append("教学内容")
    hh.append("教学时段")
    hh.append("课时    ")
    hh.append("教学表现")
    hh.append("备注    ")
    data.append(hh)
    ff = trainningcompletion.models.trainningstatusdetail.objects \
        .filter(frontdata7=instructor, ).values_list().all()

    for k in ff:
        m = list(k)
        ee = []
        # zhuyi  frontdata13  14  meiyou   id 那一项也是数据
        print(" m" + '*********' + '  ' + str(m[:]))
        print("str((len(m)))" + '*********' + '  ' + str((len(m))))
        print("m[14].split()" + '*********' + '  ' + str(m[14].split()))
        print("m[14]" + '*********' + '  ' + str(m[14]))
        print("m[13]" + '*********' + '  ' + str(m[13]))

        ee.append(datetime.strptime(m[13].split()[0], '%Y-%m-%d').year)
        ee.append(m[13].split()[0])
        ee.append("技术业务室")
        ee.append(m[6])
        ee.append(m[2])
        ee.append("模拟机")
        ee.append(m[5])
        ee.append(m[13].split()[1] + "-" + m[13].split()[2])
        ee.append(m[10])
        ee.append("优")
        ee.append(m[14])
        data.append(ee)

    return render(request, 'instructor_teach_record.html',
                  {'data': data, 'instructorlist': instructorlist, 'instructor': instructor, })


def single_person_trainning_record(request):  #

    年份 = []
    获取所有可能的年份(年份)
    人员 = 获取所有的登陆人()
    if request.session.get('status'):
        name = request.session.get('name')
    本人 = []
    本人.append(name)

    data = 生成所有个人培训记录(年份, 本人)

    return render(request, 'single_person_trainning_record.html',
                  {'data': data, 'year': 年份, 'month': 月份,
                   '人员': 人员,
                   '选的人员': name,
                   '培训类别': 培训类别,
                   '选的培训类别': "所有",
                   'year1': "2020", 'month1': "1月",
                   'year2': "2020", 'month2': "12月",
                   })


def 生成所有个人培训记录(年份, 本人):
    data = []
    # 表头
    hh = []
    hh.append("年份    ")
    hh.append("月份    ")
    hh.append("培训类型")
    hh.append("开始时间")
    hh.append("结束时间")
    hh.append("训练科目")
    hh.append("学时")
    hh.append("责任教员")
    hh.append("成绩    ")
    hh.append("模拟机考核视频")
    hh.append("备注    ")
    data.append(hh)
    for xy in 本人:
        for nf in 年份:
            for yf in 月份:
                for lb in 培训类别:
                    # mm = []
                    #                     # mm.append(nf)
                    #                     # mm.append(yf)
                    #                     # mm.append(lb)
                    #                     # mm.append('')
                    #                     # mm.append('')
                    #                     # mm.append('')     kebaonou
                    #                     # mm.append('')
                    #                     # mm.append('')
                    #                     # data.append(mm)

                    ii = []
                    ff = trainningcompletion.models.trainningstatusdetail.objects \
                        .filter().values_list().all()
                    for k in ff:
                        m = list(k)
                        ee = []
                        # zhuyi  frontdata13  14  meiyou   id 那一项也是数据

                        # print(" xy in m[8].split()" + '*********' + '  ' )
                        # print(" xy in m[8].split()" + '*********' + '  ' + str(m[8].split()))
                        # # 字符串加布尔值一定为flase 坑
                        # print(" xy in m[8].split()" + '*********' + '  ' + str(xy) in m[8].split())
                        # print( str(xy) in m[8].split())

                        if xy in m[8].split():
                            # print(
                            #     " nf" + '*********' + '  ' )
                            # print( nf == datetime.strptime(m[13].split()[0], '%Y-%m-%d').year)
                            if nf == datetime.strptime(m[13].split()[0], '%Y-%m-%d').year:
                                # print(" yf == m[13]" + '*********' + '  ' + yf == m[13])

                                if yf == m[3]:
                                    if lb == m[2]:
                                        if m[11] != "0":
                                            ee.append(nf)
                                            ee.append(yf)
                                            ee.append(lb)
                                            ee.append(m[13].split()[0] + "-" + m[13].split()[1])
                                            ee.append(m[13].split()[0] + "-" + m[13].split()[2])
                                            ee.append(m[5])
                                            ee.append(m[11])
                                            ee.append(m[7])
                                            ee.append('')
                                            ee.append('')
                                            ee.append('')
                                            ii.append(ee)
                                            data.append(ee)

                    jj = []
                    jj.append(nf)
                    jj.append(yf)
                    jj.append(lb + '合计')
                    jj.append('')
                    jj.append('')
                    jj.append('')
                    ll = 0
                    # print(" str(ii)" + '*********' + '  ' + str(ii))
                    for kk in ii:
                        # if isinstance(kk[6], int):
                        # print(" str(kk[6])" + '*********' + '  ' + str(kk[6]))
                        ll = ll + float(kk[6])
                    jj.append(ll)
                    jj.append('')
                    jj.append('')
                    if ll != 0:
                        data.append(jj)

                    # pp = []
                    # pp.append('')
                    # pp.append('')
                    # pp.append('')
                    # pp.append('')
                    # pp.append('')
                    # pp.append('')
                    # pp.append('')
                    # pp.append('')
                    # data.append(pp)

    return data


def single_person_trainning_record_post(request):
    post_year1 = int(request.POST.get('year1'))
    month11 = request.POST.get('month1')
    month1 = int(''.join(month11).split("月")[0])

    post_year2 = int(request.POST.get('year2'))
    month21 = request.POST.get('month2')
    month2 = int(''.join(month21).split("月")[0])

    选的人员 = request.POST.get('人员')
    选的培训类别 = request.POST.get('培训类别')
    培训类别1 = ["所有", "上岗前培训", "资格培训", "复习培训", "附加培训", "追加培训", "补习培训"
        , "设备培训", "熟练培训", "专项培训", ]

    print('选的人员')
    print(选的人员)
    年份 = []
    获取所有可能的年份(年份)
    人员 = 获取所有的登陆人()

    本人 = []
    本人.append(选的人员)
    # 本人 = ["马朝兵"]
    data = 生成所有个人培训记录(年份, 本人)

    if post_year1 > post_year2:
        print("年份选择错误")
    # print(str(data))
    # 表头
    hh = []
    hh.append("年份    ")
    hh.append("月份    ")
    hh.append("培训类型")
    hh.append("开始时间")
    hh.append("结束时间")
    hh.append("训练科目")
    hh.append("学时")
    hh.append("责任教员")
    hh.append("成绩    ")
    hh.append("模拟机考核视频")
    hh.append("备注    ")
    oo = []
    oo.append(hh)
    # print("data[1:]")
    # print(data[1:])
    for nn in data[1:]:
        # print("nn")
        # print(nn)
        # print(str(nn))
        if 选的培训类别 == "所有":
            if nn[0] != "":
                if post_year1 == post_year2:
                    if int(nn[0]) == post_year1:
                        for mm1 in range(month1 - 1, month2, 1):
                            if (nn[1] == 月份[mm1]) & (int(nn[0]) == post_year1):
                                oo.append(nn)

                if post_year1 < post_year2:
                    if post_year2 >= int(nn[0]) >= post_year1:
                        for mm1 in range(month1 - 1, 12, 1):
                            if (nn[1] == 月份[mm1]) & (int(nn[0]) == post_year1):  # index是从0开始的
                                oo.append(nn)

                        for yy in range(post_year1 + 1, post_year2 - 1, 1):
                            for mm2 in range(0, 12, 1):
                                if (nn[1] == 月份[mm2]) & (int(nn[0]) == yy):
                                    oo.append(nn)

                        for mm3 in range(0, month2, 1):
                            if (nn[1] == 月份[mm3]) & (int(nn[0]) == post_year2):
                                oo.append(nn)
        else:
            if (nn[2] == 选的培训类别) or (nn[2] == 选的培训类别 + "合计"):
                if nn[0] != "":
                    if post_year1 == post_year2:
                        if int(nn[0]) == post_year1:
                            for mm1 in range(month1 - 1, month2, 1):
                                if (nn[1] == 月份[mm1]) & (int(nn[0]) == post_year1):
                                    oo.append(nn)

                    if post_year1 < post_year2:
                        if post_year2 >= int(nn[0]) >= post_year1:
                            for mm1 in range(month1 - 1, 12, 1):
                                if (nn[1] == 月份[mm1]) & (int(nn[0]) == post_year1):  # index是从0开始的
                                    oo.append(nn)

                            for yy in range(post_year1 + 1, post_year2 - 1, 1):
                                for mm2 in range(0, 12, 1):
                                    if (nn[1] == 月份[mm2]) & (int(nn[0]) == yy):
                                        oo.append(nn)

                            for mm3 in range(0, month2, 1):
                                if (nn[1] == 月份[mm3]) & (int(nn[0]) == post_year2):
                                    oo.append(nn)
    qq = []
    ll = 0
    for pp in oo[1:]:
        if (pp[2] == 选的培训类别 + "合计"):
            ll = ll + float(pp[6])
    qq.append('')
    qq.append('')
    qq.append('总合计')
    qq.append('')
    qq.append('')
    qq.append('')
    qq.append(ll)
    qq.append('')
    qq.append('')
    qq.append('')
    qq.append('')
    if 选的培训类别 != "所有":
        oo.append(qq)

    print(oo)
    return render(request, 'single_person_trainning_record.html',
                  {'data': oo, 'year': 年份, 'month': 月份,
                   '人员': 人员, '培训类别': 培训类别1,
                   '选的人员': 选的人员,
                   '选的培训类别': 选的培训类别,
                   'year1': post_year1, 'month1': month11,
                   'year2': post_year1, 'month2': month21, })


def 获取所有的登陆人():
    from TestModel.models import logins
    jj = logins.objects \
        .filter().values_list().all()
    kk = list(jj)
    ll = []
    for gg in kk:
        ll.append(gg[1])
    return ll


# 以下最新学时统计
def training_time(request):
    年份 = []
    获取所有可能的年份(年份)

    now_time = datetime.now()
    year = datetime.strftime(now_time, "%y")
    year = str(2000 + float(year))
    if request.session.get('status'):  # 在判断网页请求的状态时，直接调用request.session从djang_session表中读取数据验证
        name2 = request.session.get('name')
        print(name2 + '*********' + 'session登陆人')

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

    now_time = datetime.now()
    now_year = datetime.strftime(now_time, "%y")
    now_year = str(2000 + int(now_year))
    now_month = datetime.strftime(now_time, "%m")
    day1 = 1
    day2 = 31
    塔进区 = "3"
    放单情况 = "3"
    人员 = ""

    b1 = ""
    if 塔进区 == "0":
        b1 = "塔台管制室"
    if 塔进区 == "1":
        b1 = "塔台管制室"
    if 塔进区 == "2":
        b1 = "区域管制室"
    if 塔进区 == "4":
        b1 = "飞行服务室"

    a1 = ""
    if 放单情况 == "0":
        a1 = "放单"
    if 放单情况 == "1":
        a1 = "部分放单"
    if 放单情况 == "2":
        a1 = "未放单"
    print("xxxxxxxxxxxxxxxxxx")
    print(人员)
    print(a1)
    print(b1)

    年份 = []
    获取所有可能的年份(年份)
    temp1 = []
    ccc = []
    # 表头
    hh = []
    hh.append("姓名")
    hh.append("岗位")
    hh.append("模拟机培训")
    hh.append("")
    hh.append("")
    hh.append("")
    hh.append("")
    hh.append("")
    hh.append("")
    hh.append("")
    hh.append("")
    hh.append("模拟机培训合计")
    hh.append("理论培训")
    hh.append("")
    hh.append("")
    hh.append("")
    hh.append("")
    hh.append("")
    hh.append("")
    hh.append("")
    hh.append("")
    hh.append("")
    hh.append("")
    hh.append("")
    hh.append("理论培训合计")
    hh.append("总计")
    hh.append("放单情况")

    ccc.append(hh)

    gg = []
    gg.append("")
    gg.append("")
    gg.append("上岗前培训")
    gg.append("复习培训")
    gg.append("资格培训")
    gg.append("设备培训")
    gg.append("熟练培训")
    gg.append("补习培训")
    gg.append("追加培训")
    gg.append("附加培训")
    gg.append("专项培训")
    gg.append("")
    gg.append("上岗前培训")
    gg.append("理论复训")
    gg.append("资格培训")
    gg.append("设备培训")
    gg.append("熟练培训")
    gg.append("补习培训")
    gg.append("追加培训")
    gg.append("附加培训")
    gg.append("专项培训")
    gg.append("安全教育")
    gg.append("案例分析")
    gg.append("空管大讲堂")
    ccc.append(gg)

    jj = trainningcompletion.models.trainningstatusdetail.objects \
        .filter().values_list().all()
    kk = list(jj)
    ll = []
    for gg in kk:
        ff = []
        for hh in gg:
            ff.append(hh)
        ll.append(ff)

    jj1 = info.objects \
        .filter().values_list().all()
    kk1 = list(jj1)

    jj2 = trainningcompletion.models.trainningstatusdetailother.objects \
        .filter().values_list().all()
    kk2 = list(jj2)
    ll2 = []
    for gg2 in kk2:
        ff2 = []
        for hh2 in gg2:
            ff2.append(hh2)
        ll2.append(ff2)

    people = []

    for gg1 in kk1:
        print(gg1)
        print(gg1[23])
        print(gg1[2])

        if 人员 == "":
            print("zzzzzzzzzzzzzzzzz111")
            if b1 == "":
                print("zzzzzzzzzzzzzzzzz22222")
                if a1 == gg1[2]:
                    people.append(gg1[1])
                    print("zzzzzzzzzzzzzzzzz")
                    print("1")
                if a1 == "":
                    people.append(gg1[1])
                    print("zzzzzzzzzzzzzzzzz")
                    print("2")
            if b1 == gg1[23]:
                print("zzzzzzzzzzzzzzzzz3333")
                if a1 == gg1[2]:
                    people.append(gg1[1])
                    print("zzzzzzzzzzzzzzzzz")
                    print("3")
                if a1 == "":
                    people.append(gg1[1])
                    print("zzzzzzzzzzzzzzzzz")
                    print("4")
        else:
            if 人员 == gg1[1]:
                people.append(gg1[1])
                print("zzzzzzzzzzzzzzzzz")
                print("5")

    培训类别 = ["上岗前培训", "资格培训", "复习培训", "附加培训", "追加培训", "补习培训"
        , "设备培训", "熟练培训", "专项培训", ]
    其他培训类别 = ["上岗前培训",
              "理论复训",
              "资格培训",
              "设备培训",
              "熟练培训",
              "补习培训",
              "追加培训",
              "附加培训",
              "专项培训",
              "安全教育",
              "案例分析",
              "空管大讲堂",
              ]

    start_date = datetime.strptime(str(int(now_year) - 1) + "-" + now_month + "-" + str(day1), "%Y-%m-%d")
    end_date = datetime.strptime(str(int(now_year)) + "-" + now_month + "-" + str(day2), "%Y-%m-%d")
    x1 = start_date.year * 365 + start_date.month * 12 + start_date.day
    x2 = end_date.year * 365 + end_date.month * 12 + end_date.day
    print(name2 + '*********' + 'x1')
    print(x1)
    print(x2)
    print(people)

    for bbb in people:
        time_all1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, ]
        time_all2 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ]
        jjj = []
        aaa = 0
        for pp in 培训类别:
            for m in ll[1:]:
                print(m[8])
                print("m[8].split()")
                print(m[8].split(" "))
                mm = datetime.strptime(m[13].split()[0], '%Y-%m-%d')
                x3 = mm.year * 365 + mm.month * 12 + mm.day
                print(people)
                print(x1)
                print(x2)
                print(x3)
                if x3 in range(x1,
                               x2 + 1, 1):
                    if bbb in m[8].split(" "):

                        if pp == m[2]:
                            time_all1[aaa] = time_all1[aaa] + float(m[11])
            aaa = aaa + 1
        iii = 0
        for pp in 其他培训类别:
            for m in ll2[1:]:

                mm = datetime.strptime(m[12].split()[0], '%Y-%m-%d')
                x3 = mm.year * 365 + mm.month * 12 + mm.day
                # print(people)
                # print(x1)
                # print(x2)
                # print(x3)
                if x3 in range(x1,
                               x2 + 1, 1):
                    if bbb in m[8].split(" "):

                        if pp == m[2]:
                            time_all2[iii] = time_all2[iii] + float(m[11])
            iii = iii + 1

        jjj.append(bbb)
        for gg2 in kk1:
            if gg2[1] == bbb:
                jjj.append(gg2[23])
        ddd = 0
        hhh = 0
        for eee in time_all1:
            hhh = hhh + time_all1[ddd]
            jjj.append(time_all1[ddd])
            ddd = ddd + 1
        jjj.append(hhh)
        fff = 0
        iii = 0
        for ggg in time_all2:
            iii = iii + time_all2[fff]
            jjj.append(time_all2[fff])
            fff = fff + 1
        jjj.append(iii)
        jjj.append(hhh + iii)
        for gg2 in kk1:
            if gg2[1] == bbb:
                jjj.append(gg2[2])
        ccc.append(jjj)
    data = ccc
    print(name2 + '*********' + 'data')
    print(data)

    return render(request, 'training_time.html',
                  {'data': data, 'year': 年份, 'month': 月份, 'post_year1': str(int(now_year) - 1),
                   'month1': now_month, 'day1': day1,
                   'post_year2': now_year, 'month2': now_month, 'day2': day2, })


def training_time_post(request):
    post_year1 = int(request.POST.get('year1'))
    month1 = request.POST.get('month1')
    month1 = int(''.join(month1).split("月")[0])

    post_year2 = int(request.POST.get('year2'))
    month2 = request.POST.get('month2')
    month2 = int(''.join(month2).split("月")[0])

    塔进区 = request.POST.get('塔进区')
    放单情况 = request.POST.get('放单情况')

    人员 = request.POST.get('search-text1')
    if 人员:
        print("11111")
    else:
        人员 = ""

    年份 = []
    获取所有可能的年份(年份)

    now_time = datetime.now()
    year = datetime.strftime(now_time, "%y")
    year = str(2000 + float(year))
    if request.session.get('status'):  # 在判断网页请求的状态时，直接调用request.session从djang_session表中读取数据验证
        name2 = request.session.get('name')
        print(name2 + '*********' + 'session登陆人')

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

    now_time = datetime.now()
    now_year = datetime.strftime(now_time, "%y")
    now_year = str(2000 + int(now_year))
    now_month = datetime.strftime(now_time, "%m")
    day1 = 1
    day2 = 31

    b1 = ""
    if 塔进区 == "0":
        b1 = "塔台管制室"
    if 塔进区 == "1":
        b1 = "塔台管制室"
    if 塔进区 == "2":
        b1 = "区域管制室"
    if 塔进区 == "4":
        b1 = "飞行服务室"

    a1 = ""
    if 放单情况 == "0":
        a1 = "放单"
    if 放单情况 == "1":
        a1 = "部分放单"
    if 放单情况 == "2":
        a1 = "未放单"

    年份 = []
    获取所有可能的年份(年份)
    temp1 = []
    ccc = []
    # 表头
    hh = []
    hh.append("姓名")
    hh.append("岗位")
    hh.append("模拟机培训")
    hh.append("")
    hh.append("")
    hh.append("")
    hh.append("")
    hh.append("")
    hh.append("")
    hh.append("")
    hh.append("")
    hh.append("模拟机培训合计")
    hh.append("理论培训")
    hh.append("")
    hh.append("")
    hh.append("")
    hh.append("")
    hh.append("")
    hh.append("")
    hh.append("")
    hh.append("")
    hh.append("")
    hh.append("")
    hh.append("")
    hh.append("理论培训合计")
    hh.append("总计")
    hh.append("放单情况")

    ccc.append(hh)

    gg = []
    gg.append("")
    gg.append("")
    gg.append("上岗前培训")
    gg.append("复习培训")
    gg.append("资格培训")
    gg.append("设备培训")
    gg.append("熟练培训")
    gg.append("补习培训")
    gg.append("追加培训")
    gg.append("附加培训")
    gg.append("专项培训")
    gg.append("")
    gg.append("上岗前培训")
    gg.append("理论复训")
    gg.append("资格培训")
    gg.append("设备培训")
    gg.append("熟练培训")
    gg.append("补习培训")
    gg.append("追加培训")
    gg.append("附加培训")
    gg.append("专项培训")
    gg.append("安全教育")
    gg.append("案例分析")
    gg.append("空管大讲堂")
    ccc.append(gg)

    jj = trainningcompletion.models.trainningstatusdetail.objects \
        .filter().values_list().all()
    kk = list(jj)
    ll = []
    for gg in kk:
        ff = []
        for hh in gg:
            ff.append(hh)
        ll.append(ff)

    jj1 = info.objects \
        .filter().values_list().all()
    kk1 = list(jj1)

    jj2 = trainningcompletion.models.trainningstatusdetailother.objects \
        .filter().values_list().all()
    kk2 = list(jj2)
    ll2 = []
    for gg2 in kk2:
        ff2 = []
        for hh2 in gg2:
            ff2.append(hh2)
        ll2.append(ff2)

    people = []
    print(人员)
    print(a1)
    print(b1)

    for gg1 in kk1:
        print(gg1)
        print(gg1[23])
        print(gg1[2])

        if 人员 == "":
            print("zzzzzzzzzzzzzzzzz111")
            if b1 == "":
                print("zzzzzzzzzzzzzzzzz22222")
                if a1 == gg1[2]:
                    people.append(gg1[1])
                    print("zzzzzzzzzzzzzzzzz")
                    print("1")
                if a1 == "":
                    people.append(gg1[1])
                    print("zzzzzzzzzzzzzzzzz")
                    print("2")
            if b1 == gg1[23]:
                print("zzzzzzzzzzzzzzzzz3333")
                if a1 == gg1[2]:
                    people.append(gg1[1])
                    print("zzzzzzzzzzzzzzzzz")
                    print("3")
                if a1 == "":
                    people.append(gg1[1])
                    print("zzzzzzzzzzzzzzzzz")
                    print("4")
        else:
            if 人员 == gg1[1]:
                people.append(gg1[1])
                print("zzzzzzzzzzzzzzzzz")
                print("5")

    培训类别 = ["上岗前培训",
            "复习培训",
            "资格培训",
            "设备培训",
            "熟练培训",
            "补习培训",
            "追加培训",
            "附加培训",
            "专项培训",
            ]

    其他培训类别 = ["上岗前培训",
              "理论复训",
              "资格培训",
              "设备培训",
              "熟练培训",
              "补习培训",
              "追加培训",
              "附加培训",
              "专项培训",
              "安全教育",
              "案例分析",
              "空管大讲堂",
              ]

    start_date = datetime.strptime(str(post_year1) + "-" + str(month1) + "-" + str(day1), "%Y-%m-%d")
    end_date = datetime.strptime(str(post_year2) + "-" + str(month2) + "-" + str(day2), "%Y-%m-%d")
    x1 = start_date.year * 365 + start_date.month * 12 + start_date.day
    x2 = end_date.year * 365 + end_date.month * 12 + end_date.day
    # print(name2 + '*********' + 'x1')

    for bbb in people:
        time_all1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, ]
        time_all2 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ]
        jjj = []
        aaa = 0
        for pp in 培训类别:
            for m in ll[1:]:
                print(m[8])
                print("m[8].split()")
                print(m[8].split(" "))
                mm = datetime.strptime(m[13].split()[0], '%Y-%m-%d')
                x3 = mm.year * 365 + mm.month * 12 + mm.day
                print(people)
                print(x1)
                print(x2)
                print(x3)
                if x3 in range(x1,
                               x2 + 1, 1):
                    if bbb in m[8].split(" "):

                        if pp == m[2]:
                            time_all1[aaa] = time_all1[aaa] + float(m[11])
            aaa = aaa + 1
        iii = 0
        for pp in 其他培训类别:
            for m in ll2[1:]:

                mm = datetime.strptime(m[12].split()[0], '%Y-%m-%d')
                x3 = mm.year * 365 + mm.month * 12 + mm.day
                # print(people)
                # print(x1)
                # print(x2)
                # print(x3)
                if x3 in range(x1,
                               x2 + 1, 1):
                    if bbb in m[8].split(" "):

                        if pp == m[2]:
                            time_all2[iii] = time_all2[iii] + float(m[11])
            iii = iii + 1

        jjj.append(bbb)
        for gg2 in kk1:
            if gg2[1] == bbb:
                jjj.append(gg2[23])
        ddd = 0
        hhh = 0
        for eee in time_all1:
            hhh = hhh + time_all1[ddd]
            jjj.append(time_all1[ddd])
            ddd = ddd + 1
        jjj.append(hhh)
        fff = 0
        iii = 0
        for ggg in time_all2:
            iii = iii + time_all2[fff]
            jjj.append(time_all2[fff])
            fff = fff + 1
        jjj.append(iii)
        jjj.append(hhh + iii)
        for gg2 in kk1:
            if gg2[1] == bbb:
                jjj.append(gg2[2])
        ccc.append(jjj)
    data = ccc
    print(name2 + '*********' + 'data')
    print(data)

    return render(request, 'training_time.html', {'data': data, 'year': 年份, 'month': 月份, 'post_year1': post_year1,
                                                  'month1': month1, 'day1': day1,
                                                  'post_year2': post_year2, 'month2': month2, 'day2': day2, })
