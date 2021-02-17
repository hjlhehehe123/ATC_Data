from django.shortcuts import render
from docx import Document
import re

from xunliankaohe import models


# Create your views here.

def jichangfxkhb(request):
    return render(request, 'jichangfxkhb.html')




def addjichangfxkhb(request):  # 获取增加机场复训考核表记录的数据并保存

    textlist = []
    listnum=[11,1,1,1,1,1,1,2,1,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]

    datan = request.POST.get('data01')
    datas = request.POST.get('data02')

    for i in range(1,8):
        name = 'data0' + str(i)
        a=request.POST.get(name)
        textlist.append(a)

    data08 = request.POST.get('data08')
    if data08 == '0':
        data08 = '初级'
    if data08 == '1':
        data08 = '中级'
    if data08 == '2':
        data08 = '高级'
    textlist.append(data08)
    data09 = request.POST.get('data09')
    textlist.append(data09)

    for i in range(10,40):
        name = 'data' + str(i)
        a=request.POST.get(name)
        b=int(a)
        if i < 39:
           c = b * listnum[i-10]
        else:
            c=b*1
        b=str(b)
        c=str(c)
        textlist.append(b)
        textlist.append(c)

    data40 = request.POST.get('jgcs')
    data41 = request.POST.get('jgkf')
    data42 = request.POST.get('datajgz')
    data43 = request.POST.get('xtcs')
    data44 = request.POST.get('xtkf')
    data45 = request.POST.get('dataxtz')
    data46 = request.POST.get('yscs')
    data47 = request.POST.get('yskf')
    data48 = request.POST.get('dataysz')
    data49 = request.POST.get('lkcs')
    data50 = request.POST.get('lkkf')
    data51 = request.POST.get('datalkz')
    data52 = request.POST.get('tqcs')
    data53 = request.POST.get('tqkf')
    data54 = request.POST.get('datatqz')
    data55 = request.POST.get('ldcs')
    data56 = request.POST.get('ldkf')
    data57 = request.POST.get('dataldz')
    data58 = request.POST.get('qtkf')
    data59 = request.POST.get('data41')
    if data59=='':
       data59="无"

    textlist.append(data59)
    dataqtkf = request.POST.get('data40')
    textlist.append(dataqtkf)

    data61 = request.POST.get('qkjl')
    textlist.append(data61)
    data62 = request.POST.get('zwpj')
    textlist.append(data62)
    data63 = request.POST.get('jypy')
    textlist.append(data63)
    data64 = request.POST.get('jg')
    if data64 == '0':
        data64 = '通过'
    if data64 == '1':
        data64 = '不通过'
    if data64 == '2':
        data64 = '待定'
    data65 = request.POST.get('zf')
    textlist.append(data65)
    textlist.append(data64)
    data66 = request.POST.get('qm1')
    textlist.append(data66)
    data67 = request.POST.get('qm2')
    textlist.append(data67)
    data68 = request.POST.get('qm3')
    textlist.append(data68)

    a = models.jichangfxkhb()
    a.frontdata1 = datan
    a.frontdata2 = data40
    a.frontdata3 = data41
    a.frontdata4 = data42
    a.frontdata5 = data43
    a.frontdata6 = data44
    a.frontdata7 = data45
    a.frontdata8 = data46
    a.frontdata9 = data47
    a.frontdata10 = data48
    a.frontdata11 = data49
    a.frontdata12 = data50
    a.frontdata13 = data51
    a.frontdata14 = data52
    a.frontdata15 = data53
    a.frontdata16 = data54
    a.frontdata17 = data55
    a.frontdata18 = data56
    a.frontdata19 = data57
    a.frontdata20 = data58
    a.frontdata21 = data59
    a.frontdata22 = data64
    a.frontdata23 = data65


    a.is_active = 0
    a.save()

    doc = Document("E:\pythonproject\ATC_Data\考核表\复训考核表\机场复训考核表\机场复训考核表样表.docx")

    count = 0

    for n in range(0, 20):
        table = doc.tables[n]
        for row in table.rows:
            for cell in row.cells:
                if 'XXXX' in cell.text:
                    cell.text = cell.text.replace("XXXX", textlist[count])
                    count += 1
        n += 1

    doc.save('E:\pythonproject\ATC_Data\考核表\复训考核表\机场复训考核表\%s机场复训考核表.docx' %datan)
    return render(request, 'ok.html')
