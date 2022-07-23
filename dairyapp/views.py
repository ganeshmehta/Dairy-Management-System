from django.forms import EmailField
from django.http import HttpResponse
from django.shortcuts import render
from dairyapp.database import Connection
from django.contrib import messages
# Create your views here.

# web gunicorn Dairy.wsgi:application --log-file -
def index(request):
    db=Connection()
    x,y=db.checkUser()
    context={'abc':y}
    if 'add' in request.POST:
        email = request.POST.get('email')
        inv = request.POST.get('inv')
        vehicle = request.POST.get('vehicle')
        invno = int(request.POST.get('invno'))
        deliveryemail = request.POST.get('deliveryemail')
        invby = request.POST.get('invby')
        refno = request.POST.get('refno')
        vatac = request.POST.get('vatac')
        db=Connection()
        x,y=db.storeUser(email,inv,vehicle,invno,deliveryemail,invby,refno,vatac)
        context={'abc':y}
        if(x==True): 
            return render(request, 'index.html',context)
        else:
            return HttpResponse('Try Again')
    elif 'modify' in request.POST:
        email = request.POST.get('email')
        inv = request.POST.get('inv')
        vehicle = request.POST.get('vehicle')
        invno = int(request.POST.get('invno'))
        deliveryemail = request.POST.get('deliveryemail')
        invby = request.POST.get('invby')
        refno = request.POST.get('refno')
        vatac = request.POST.get('vatac')
        db=Connection()
        y=db.updateUser(email,inv,vehicle,invno,deliveryemail,invby,refno,vatac)
        context={'abc':y}     
        return render(request, 'index.html',context)
    elif 'delete' in request.POST:
        email = request.POST.get('email')
        db=Connection()
        x,y=db.deleteUser(email)
        if(x==True):
            context={'abc':y}
            return render(request, 'index.html',context)
        else:
            return HttpResponse("User Not Found")
        
        
    elif 'print' in request.POST:
        db=Connection()
        # db.printData()
        x,y=db.checkUser()
        context={'abc':y}
        return render(request, 'base.html',context)

    elif 'bata' in request.POST:
        l=[]
        m=[]
        email=request.POST.get('email')
        inv=request.POST.get('inv')
        vehicle=request.POST.get('vehicle')
        invno = request.POST.get('invno')
        deliveryemail = request.POST.get('deliveryemail')
        invby = request.POST.get('invby')
        refno = request.POST.get('refno')
        vatac = request.POST.get('vatac')
        # context={'c1':check1,'c2':check2,'c3':check3}
        # if(None in check1):
        #     print("Shivam")
        l=[email,inv,vehicle,invno,deliveryemail,invby,refno,vatac]
        for i in l:
            if i is not None:
                m.append(i)
        db=Connection()
        db.displayData(m)
        return render(request, 'index.html')
    return render(request, 'index.html',context)


    