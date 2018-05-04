from django.shortcuts import render
from django.http import HttpResponse
from feedback.forms import feedback_form
from maintainer.views import index

# Create your views here.
def feedback(request):
    form = feedback_form()

    if request.method =="POST":
        form = feedback_form(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print("Form validation Failed")

    return render(request,'feedback.html',{'form':form})
