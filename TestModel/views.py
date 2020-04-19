
# Create your views here.

from django.shortcuts import render
from django.http import HttpResponse
from TestModel.models import logins

#加载登录页面
def login (request):
    return render(request,'index.html')

# 验证登录
def do_login(request):
    account = request.POST.get('account')
    password = request.POST.get('password')

    ac = logins.objects.filter(atcAccount=account)
    if ac.exists() and password==logins.objects.get(atcAccount=account).atcPassword:
        return render(request, 'main.html')
    else:
        return render(request, 'index.html')



'''
    if account == '123' and password == '456':
        context = {}
        context['account2']=account
        return render(request, 'main.html',context)
    else:
        return render(request, 'index.html', {
            'account': account,
            'password': password
        })
'''