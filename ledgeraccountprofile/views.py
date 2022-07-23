from django.forms import EmailField
from django.http import HttpResponse
from django.shortcuts import render
from ledgeraccountprofile.database import Connection
from django.contrib import messages
# Create your views here.

# web gunicorn Dairy.wsgi:application --log-file -
def index(request):
    db=Connection()
    x,y=db.checkUser()
    arr=[]
    for i in y:
        arr.append([i[2],i[3]])
    context={'abc':arr} 
    if 'add' in request.POST:
        code = int(request.POST.get('code'))
        accounttype = request.POST.get('accounttype')
        ledgertype = request.POST.get('ledgertype')
        subtedger = request.POST.get('subtedger')
        party = request.POST.get('party')
        dept = request.POST.get('dept')
        subdept = request.POST.get('subdept')
        grp = request.POST.get('grp')
        subgrp = request.POST.get('subgrp')
        db=Connection()
        x,y=db.storeUser(code,accounttype,ledgertype,subtedger,party,dept,subdept,grp,subgrp)
        arr=[]
        for i in y:
            arr.append([i[2],i[3]])
        context={'abc':arr}
        if(x==True): 
            return render(request,'ledgeraccountpage.html',context)
        else:
            return HttpResponse('Try Again')
    elif 'modify' in request.POST:
        code = int(request.POST.get('code'))
        accounttype = request.POST.get('accounttype')
        ledgertype = request.POST.get('ledgertype')
        subtedger = request.POST.get('subtedger')
        party = request.POST.get('party')
        dept = request.POST.get('dept')
        subdept = request.POST.get('subdept')
        grp = request.POST.get('grp')
        subgrp = request.POST.get('subgrp')
        db=Connection()
        y=db.updateUser(code,accounttype,ledgertype,subtedger,party,dept,subdept,grp,subgrp)
        arr=[]
        for i in y:
            arr.append([i[2],i[3]])
        context={'abc':arr}    
        return render(request,'ledgeraccountpage.html',context)
    elif 'delete' in request.POST:
        code = request.POST.get('code')
        db=Connection()
        x,y=db.deleteUser(code)
        if(x==True):
            arr=[]
            for i in y:
                arr.append([i[2],i[3]])
            context={'abc':arr} 
            return render(request,'ledgeraccountpage.html',context)
        else:
            return HttpResponse("User Not Found")
        
        
    elif 'print' in request.POST:
        db=Connection()
        # db.printData()
        x,y=db.checkUser()
        arr=[]
        for i in y:
            arr.append([i[2],i[3]])
        context={'abc':arr} 
        return render(request,'ledgeraccountpage.html',context)

    elif 'bata' in request.POST:
        l=[]
        m=[]
        code = int(request.POST.get('code'))
        accounttype = request.POST.get('accounttype')
        ledgertype = request.POST.get('ledgertype')
        subtedger = request.POST.get('subtedger')
        party = request.POST.get('party')
        dept = request.POST.get('dept')
        subdept = request.POST.get('subdept')
        grp = request.POST.get('grp')
        subgrp = request.POST.get('subgrp')
        # context={'c1':check1,'c2':check2,'c3':check3}
        # if(None in check1):
        #     print("Shivam")
        l=[code,accounttype,ledgertype,subtedger,party,dept,subdept,grp,subgrp]
        for i in l:
            if i is not None:
                m.append(i)
        db=Connection()
        db.displayData(m)
        return render(request,'ledgeraccountpage.html')
    return render(request,'ledgeraccountpage.html',context)