from django.shortcuts import render

from django.http import HttpResponseRedirect
from .forms import FirstForm,SecondForm,ThirdForm,FourForm
title="هوي يا زول"
message="أهلا بك في تطبيق تتبع الهواتف في حالة السرقة "
def First(request):
    if request.method == 'POST': # If the form has been submitted...
        form = FirstForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            # Process the data in form.cleaned_data
            # ...
            return HttpResponseRedirect('/second/') # Redirect after POST
    else:
        form = FirstForm() # An unbound form

    return render(request, 'first.html', { 'form': form,"title":title,"message":message})



def Second(request):
    if request.method == 'POST': # If the form has been submitted...
        form = SecondForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            # Process the data in form.cleaned_data
            # ...
            return HttpResponseRedirect('/third/') # Redirect after POST
    else:
        form = SecondForm() # An unbound form

    return render(request, 'second.html', { 'form': form,"title":title,"message":message})
def third(request):
    
    if request.method == 'POST': # If the form has been submitted...
        form = ThirdForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            # Process the data in form.cleaned_data
            # ...
            return HttpResponseRedirect('/fourth/') # Redirect after POST
    else:
        message="في حالة تعزر إسترجاع حسابك نحتاج الي كلمة أمان لإسترجاع ومتابعة هاتفك"
        form = ThirdForm() # An unbound form

    return render(request, 'third.html', { 'form': form,"title":title,"message":message})
def fourth(request):
    
    if request.method == 'POST': # If the form has been submitted...
        form = FourForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            # Process the data in form.cleaned_data
            # ...
            return HttpResponseRedirect('/markers/map/') # Redirect after POST
    else:
        message=""
        form = FourForm() # An unbound form

    return render(request, 'fourth.html', { 'form': form,"title":title,"message":message})
# Create your views here.
def Welcome(request):
    return render(request,"welcom.html",{"title":title,"message":message})


