from django.shortcuts import render
from django.http import HttpResponse
from maintainer.forms import titanic_form
from maintainer import pic


import numpy as np
# Create your views here.
#pid = 0,pclass=0,ag = 0,sib=0,par=0,mal=0,fem=0,ec=0,eq=0,es=0
fin = []

def index(request):
     mydict = {'var':"please go ahead and discover at /form guys"}
     return render(request,'index.html',context=mydict)

def aboutus(request):
     mydict = {'var':"please go ahead and discover at /form guys"}
     return render(request,'aboutus.html',context=mydict)

def titanic(request):
    del fin[:]
    form = titanic_form()

    if request.method =="POST":
        form = titanic_form(request.POST)
        data = request.POST
        passengerid = data.__getitem__('passengerid')
        fin.append(passengerid)
        passengerclass = data.__getitem__('passengerclass')
        fin.append(passengerclass)
        age = data.__getitem__('age')
        fin.append(age)
        siblings = data.__getitem__('siblings')
        fin.append(siblings)
        parents = data.__getitem__('parents')
        fin.append(parents)
        fare = data.__getitem__('fare')
        fin.append(fare)
        female = data.__getitem__('female')
        fin.append(female)
        male = data.__getitem__('male')
        fin.append(male)
        c = data.__getitem__('Cherbourg')
        fin.append(c)
        q = data.__getitem__('Queenstown')
        fin.append(q)
        s = data.__getitem__('Southampton')
        fin.append(s)
        if form.is_valid():
            form.save(commit=True)
            return titanic_predict(request)
        else:
            print("Form validation Failed")
    return render(request,"maintainer/titanic_form.html",{'form':form})

def titanic_predict(request):
    li = fin
    li = [float(i) for i in li]
    X_test = np.array([li])
    val = pic.prediction(li)
    dicti = {'fin':val}
    return render(request,'maintainer/titanic_predict.html',context=dicti)
