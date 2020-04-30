from django.shortcuts import render

from atcInfo.models import info


# Create your views here.

def getinfo(request):
    getatcinfo=info.objects.get(id=123)
    context = {}
    context['atcName'] = getatcinfo.atcName
    context['atcOld'] = getatcinfo.atcOld
    return render(request, 'personnalinfo.html', context)


def gettrainningstatus(request):
    # getatcinfo=info.objects.get(id=123)
    # context = {}
    # context['atcName'] = getatcinfo.atcName
    # context['atcOld'] = getatcinfo.atcOld
    return render(request, 'trainningstatus.html'
                  # , context
                  )

def infosearch(request):
    return render(request,'infosearch.html')
