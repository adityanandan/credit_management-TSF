from django.shortcuts import render
from django.views import generic
from home.models import User, Transaction
from . import models
from django.http import HttpResponse
from django.db.models import F
# Create your views here.
def index(request):
    Transactionlist=Transaction.objects.all().order_by('-id')
    para={'Transaction':Transactionlist}
    return render(request,'index.html',para)

def transfer(request):
    userList=User.objects.all()
    params={'users':userList}
    return render(request,'transfer.html',params)

class UserList(generic.ListView):
    model=models.User
    template_name='user_list.html'

def analyze(request):
    userList=User.objects.all()
    from_us=int(request.POST.get('from_user','default'))
    to_us=int(request.POST.get('to_user','default'))

    from_user=from_us-1
    to_user=to_us-1
    cred=int(request.POST.get('credit','0'))

    if cred>0 and userList[from_user].credit>cred and userList[from_user].user_id != userList[to_user].user_id:
        user = User.objects.get(name=userList[to_user].name)
        user.previous_credit=F('credit')
        user.credit = F('credit') + cred
        user.save()
        user1 = User.objects.get(name=userList[from_user].name)
        user1.previous_credit=F('credit')
        user1.credit = F('credit') - cred
        user1.save()

        temp="From "+""+userList[from_user].name+""+" To "+""+userList[to_user].name+" : "+str(cred)+" credit"
        t=Transaction(history=temp)
        t.save()

        Transactionlist=Transaction.objects.all().order_by('-id')
        params={'output':t.history,'Transaction':Transactionlist}

        return render(request,'analyze.html',params)
    else:
        return HttpResponse("invalid available credit-amount ")
