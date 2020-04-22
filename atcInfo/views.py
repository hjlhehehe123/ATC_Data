from django.shortcuts import render
from atcInfo.models import info
# Create your views here.

def getinfo(request):
    getatcinfo=info.objects.get(id=123)
    context = {}
    context['atcName'] = getatcinfo.atcName
    context['atcOld'] = getatcinfo.atcOld
    return render(request, 'infosearch.html', context)
