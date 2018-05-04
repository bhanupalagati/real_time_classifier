from django.shortcuts import render
from gre import grefn
from gre.forms import gre_form
import numpy as np

# Create your views here.
grei = []
def gre(request):
    form = gre_form()
    del grei[:]

    if request.method =="POST":
        form = gre_form(request.POST)
        data = request.POST
        gre_score = data.__getitem__('gre_score')
        grei.append(gre_score)
        tofel_score = data.__getitem__('tofel_score')
        grei.append(tofel_score)
        university_rating = data.__getitem__('university_rating')
        grei.append(university_rating)
        sop = data.__getitem__('sop')
        grei.append(sop)
        lor = data.__getitem__('lor')
        grei.append(lor)
        cgpa = data.__getitem__('cgpa')
        grei.append(cgpa)
        research = data.__getitem__('research')
        grei.append(research)


        if form.is_valid():
            form.save(commit=True)
            return gre_predict(request)
        else:
            print("Form validation Failed")
    return render(request,"gre/gre_form.html",{'form':form})


def gre_predict(request):

    inp = grei
    inp = [float(i) for i in inp]
    X_test = np.array([inp])
    val = grefn.predict(inp)
    dictio = {'fin':val}
    return render(request,'gre/gre_predict.html',context=dictio)
