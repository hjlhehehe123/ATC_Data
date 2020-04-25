from django.shortcuts import render

from atcInfo.models import info


# Create your views here.

def getinfo(request):
    getatcinfo = info.objects.get(id=1)
    context = {}
    context['atcName'] = getatcinfo.atcName
    context['atcOld'] = getatcinfo.atcOld
    return render(request, 'infosearch.html', context)
    # return render(request, 'mainfo.html', context)


def gettrainningstatus(request):
    getatcinfo = info.objects.get(id=1)
    context = {}
    context['atcName'] = getatcinfo.atcName
    context['atcOld'] = getatcinfo.atcOld
    return render(request, 'trainningstatus.html', context)
    # return render(request, 'mainfo.html', context)


def gettrainningplan(request):
    getatcinfo = info.objects.get(id=1)
    context = {}
    context['atcName'] = getatcinfo.atcName
    context['atcOld'] = getatcinfo.atcOld
    return render(request, 'trainningplan.html', context)
    # return render(request, 'mainfo.html', context)
