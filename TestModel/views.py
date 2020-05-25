
# Create your views here.

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse

from TestModel.models import logins

#加载登录页面
def login (request):
    return render(request, 'index.html')
name1 = '0'
# 验证登录
def do_login(request):
    account = request.POST.get('account')
    password = request.POST.get('password')

    ac = logins.objects.filter(atcAccount=account)

    if ac.exists() and password == logins.objects.get(atcAccount=account).atcPassword:
        global name1
        name1 = account
        context = {}
        context['atcName'] = ac.get(atcAccount=account).atcAccount
        request.session['status'] = True
        request.session['name'] = name1


        return render(request, 'main.html', context)
    else:
        return render(request, 'index.html')
def do_logout(request):
    request.session.flush()
    # return render(request, 'index.html')
    return redirect(reverse("login"))



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