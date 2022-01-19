from django.http.response import HttpResponseRedirect
from django.shortcuts import render
import datetime
from django.db.models import Q
from bank.models import Transaction, Transfers

# Create your views here.

def twopage(request):
   
    andy=Transfers.objects.all()
    return render(request,'twopage.html',{'andy':andy})
        

def onepage(request):
    return render(request,'onepage.html')

def sendmoney(request):
    obj=Transfers.objects.all()
    return render(request,'sendmoney.html',{'obj':obj})

def fourpage(request):
    if request.method=="POST":
        lucha=request.POST.get('lucha')
        amount=request.POST.get('amount')
        kacha=request.POST.get('kacha')
        sender=Transfers.objects.get(name=kacha)
        reciever=Transfers.objects.get(name=lucha)
        sender.balance=sender.balance-int(amount)
        reciever.balance=reciever.balance+int(amount)
        Transfers.objects.filter(name=kacha).update(balance=sender.balance)
        Transfers.objects.filter(name=lucha).update(balance=reciever.balance)
        transaction=Transaction(
            fromName=sender.name,
            toName=reciever.name,
            amount=amount,
        )
        transaction.save()
        all=Transfers.objects.all()
    return render(request,'fourpage.html',{'andy':all})

def onendhalf(request):
    return render(request,'onendhalf.html')

def addmoney(request):
    obj=Transfers.objects.all()
    return render(request,'addmoney.html',{'obj':obj})

def added(request):
    if request.method=="POST":
        person=request.POST.get('lingam')
        amount=request.POST.get('amount')
        obj=Transfers.objects.get(name=person)
        obj.balance=obj.balance+int(amount)
        Transfers.objects.filter(name=person).update(balance=obj.balance)
        return HttpResponseRedirect("/twopage")
    
def history(request):
    history=Transaction.objects.all()
    return render(request,'history.html',{'history':history})

def passbook(request):
    history=Transfers.objects.all()
    return render(request,'passbook.html',{'history':history})    

def showpass(request):
    if request.method=="POST":
        kacha=request.POST.get('kacha')
        obj=Transaction.objects.filter(Q(fromName=kacha) | Q(toName=kacha))
        return render(request,'showpass.html',{'history':obj})
