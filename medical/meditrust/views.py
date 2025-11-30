from django.shortcuts import render, redirect
from .models import register
from .models import operat
from .models import medicin
from .models import Transaction
import datetime
oid=None
mida=None
def Register(req):
    cid=req.POST.get('cid')

    cn=req.POST.get('cn')
    g=req.POST.get('g')
    dob=req.POST.get('dob')
    pn=req.POST.get('pn')
    email=req.POST.get('email')
    state=req.POST.get('state')
    city=req.POST.get('city')
    r1=register(id=cid,Customername=cn,Gender=g,DateOfBirth=dob,Phonenumber=pn,Email=email,State=state,City=city)
    r1.save()
    return render(req,'register.html',)
def login(req):
    return render(req,'login.html')
def aboutus(req):
    return render(req,'aboutus.html')
def contact(req):
    return render(req,'contactus.html')
def admin12(req):
    return render(req,'admin12.html')
def home(req):
    return render(req,'home.html')
def totalsales(req):
    return render(req,'totalsales.html')
def alogin(req):
    if req.method=='POST':
        a=req.POST.get('un')
        b=req.POST.get('p')
        try:
            c=operat.objects.get(OUsername=a)
        except:
            return render(req, 'adminlogin.html', {'msg': 'Invalid Username/Password '})
        if c!=None and b==c.Password:
            return render(req,'operator.html')
        else:
            return render(req, 'adminlogin.html',{'msg':'Invalid Username/Password '})
    else:
         return render(req,'adminlogin.html')
def datewise (req):
    if req.method=='POST':
        a=req.POST.get('sd')
        b=req.POST.get('ed')
        print(a)
        do= Transaction.objects.filter(Date__range=[a,b])
        if do.exists():
            return render(req,'datewise.html',{'msg':do})
        else:
                return render(req, 'datewise.html',{'msg1':'no Data Found'})
    else:
        return render(req,'datewise.html')
def singledate(req):
        if req.method == 'POST':
            a = req.POST.get('sd')
            data= Transaction.objects.filter(Date=a)
            if data.exists():
                return render(req, 'singledate.html', {'msg': data})
            else:
                return render(req, 'singledate.html', {'msg1': 'No Data Found'})
        else:
            return render(req, 'singledate.html')
def operatorwise(req):
    if req.method=='POST':
        a=req.POST.get('oid')
        b=req.POST.get('d')
        do = Transaction.objects.filter(OperatorID__exact=a,Date__exact=b)
        print(do)
        if do:
            return render(req,'operatorwise.html',{'msg':do})
        else:
            return render(req, 'operatorwise.html',{'msg1':'no Data Found'})
    else:
        return render(req,'operatorwise.html')
def addoper(req):
    if req.method=='POST':
        b=req.POST.get('on')
        c=req.POST.get('ou')
        d=req.POST.get('p')
        e=req.POST.get('g')
        f=req.POST.get('ph')
        add=operat(OName=b,OUsername=c,Password=d,Gender=e,Phone=f)
        add.save()
        return render(req, 'addoper.html',{'msg':'New Operator Entered'})
    else:
        return render(req,'addoper.html')
def deleteoper(req):
    if req.method=='POST':
        a=int(req.POST.get('oid'))
        d=operat.objects.get(OID=a)
        d.delete()
        return render(req, 'delete.html',{'msg':'Operator Data Deleted'})
    else:
        return render(req,'delete.html')
def main(req):
    if req.method=='POST':
        a=req.POST.get('un')
        b=req.POST.get('p')
        try:
            c=operat.objects.get(OUsername=a)
            global oid
            oid = c.OID
        except:
            return render(req, 'login.html', {'msg': 'Invalid Username/Password '})
        if c!=None and b==c.Password:
            return render(req,'operator.html')

        else:
            return render(req, 'login.html',{'msg':'Invalid Username/Password '})
    else:
         return render(req,'login.html')
def addm(req):
    if  req.method=='POST':
        a=int(req.POST.get('mid'))
        b=req.POST.get('mn')
        c=req.POST.get('ed')
        d=int(req.POST.get('pc'))
        e=int(req.POST.get('sc'))
        f=int(req.POST.get('avy'))
        g=req.FILES.get('img')
        ad=medicin(MedicineName=b, EXPDate=c ,ProductCost=d, SeellingCost=e ,Availability=f ,Image=g)
        ad.save()
        return render(req,'midadd.html',{'msg':'Medicine Inserted'})
    else:
        return render(req, 'add.html',{'data':mida})
def updatemid(req):
    if req.method=='POST':
        q=int(req.POST.get('q'))
        res= medicin.objects.get(MedicineID=mida)
        res.Availability += q
        res.save()
        return render(req,'midadd.html',{'msg':'Medicine Updated'})
    else:
        return render(req,'updatemid.html',{'data':mida})
def midadd(req):
    if req.method=='POST':
        global mida
        mida=int(req.POST.get('mid'))
        try:
            tm = medicin.objects.get(MedicineID=mida)
            return redirect('un')
        except:
            return redirect('am')
    else:
        return render(req,'midadd.html')
def removem(req):
    if req.method == 'POST':
        a = int(req.POST.get('smi'))
        try:
            c = medicin.objects.get(MedicineID=a)
            c.delete()
            return render(req, 'removemid.html', {'m':'Medicine Deleted'})
        except:

            return render(req, 'removemid.html', {'m': 'Enter the Valid Medicine ID'})
    else:
        return render(req, 'removemid.html')
def searchm(req):
    if  req.method=='POST':
        a=int(req.POST.get('smi'))
        try:
            c =medicin.objects.get(MedicineID=a)
            return render(req,'search.html',{'m':c})
        except:

            return render(req,'search.html',{'msg':'enter the Valid Medicine ID'})
    else:
        return render(req, 'search.html')
def billingm(req):
    if req.method== 'POST':
        a=int(req.POST.get('mid'))
        b=int(req.POST.get('q'))
        cu=int(req.POST.get('cus'))
        c=req.POST.get('b')
        date = datetime.date.today()
        odate = date.isoformat()
        s=[]
        q=[]
        bill=[]
        try:
            med = medicin.objects.get(MedicineID=a)
            cost = med.SeellingCost
            print("hello")

            if b<=med.Availability:
                print("hi")
                s.append(a)
                q.append(b)
                bill.append(med.SeellingCost *b)
                print(med.SeellingCost)
                tra = Transaction.objects.all()
                tr=Transaction(Date=odate,Cusid=cu,MID=a,OperatorID=oid,Quantity=b,BillAmount=med.SeellingCost * b)
                tr.save()
                tm=medicin.objects.get(MedicineID=a)
                mod=medicin(MedicineID=a ,MedicineName=tm.MedicineName, EXPDate=tm.EXPDate ,ProductCost=tm.ProductCost, SeellingCost=tm.SeellingCost ,Availability=tm.Availability-b ,Image=tm.Image)
                mod.save()
                do= Transaction.objects.all( )
                for i in do:
                    pass
                print(i)
                # data1= {'TransactionID': data.TransactionID, 'Date': odate, 'Cusid': data.cu, 'MID':data. a, 'OperatorID': data.oid,
                #         'Quantity': b, 'BillAmount': med.SeellingCost * b, 'Total': sum(bill), }
                return render(req,'billing.html',{'msg':i})
            # else:
            #     if b<=med.Availability:
            #         s.append(a)
            #         q.append(b)
            #         bill.append(cost *b)
            #         print(bill)
            #
            #         tr=Transaction(Date=odate,Cusid=cu,MID=a,OperatorID=oid,Quantity=b,BillAmount=cost * b)
            #         tr.save()
            #         tra=Transaction.objects.all()
            #         data={'TransactionID':tra.TransactionID,'Date':odate,'Cusid':cu,'MID':a,'OperatorID':oid,'Quantity':b,'BillAmount':med.SeellingCost * b,'Total':sum(bill),}
            #         data1.append(data)
            #         return render(req, 'billing.html', {'msg':data1})
            else:
                return render(req,'billing.html',{'msg1':'Medicine quantity is not much more'})
        except Exception as e:
            print('bye')
            print(e)
            return render(req, 'billing.html',{'msg1':'Invalid Mid except'})


    else:
        return render(req, 'billing.html')
def checkm(req):
    if req.method=='POST':
        a=req.POST.get('d')
        try:
            do = Transaction.objects.filter(Date=a)
            if do:
                tot=0
                for i in do:
                    tot+=i.BillAmount
                return render(req,'checkamt.html',{'msg':do ,'t':tot,'date':a})

            else:
                return render(req, 'checkamt.html', {'msg1': 'Data Not Found'})
        except:
            return render(req, 'checkamt.html',{'msg1':'Data Not Found'})
    else:
        return render(req, 'checkamt.html')
def operator(req):
    return render(req,'operator.html')
