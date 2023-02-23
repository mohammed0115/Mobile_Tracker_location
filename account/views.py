from django.shortcuts import render

from django.http import HttpResponseRedirect
from .forms import FirstForm,SecondForm,ThirdForm,FourForm
from account.creator import createUser,createMarkers
from markers.models import Marker
from markers.location import get_location,get_ip

title="تطبيق تيم لننبع المواقع"
message="أهلا بك في تطبيق تتبع الهواتف في حالة السرقة "
def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def First(request):
    user={}
    if request.method == 'POST': # If the form has been submitted...
        form = FirstForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            # Process the data in form.cleaned_data
            # ...
            user={
                "full_name":request.POST.get('full_name'),
                "National_Id":request.POST.get('National_Id'),
                "phone":request.POST.get('phone'),
                }
            print(user)
            request.session['user']=user
            return HttpResponseRedirect('/second/') # Redirect after POST
    else:
        print("ip=",get_client_ip(request))
        user_ip=get_client_ip(request)
        form = FirstForm() # An unbound form

    return render(request, 'first.html', {'user': user,'form': form,"title":title,"message":message,"user_ip":user_ip})


def Second(request):
    if request.method == 'POST': # If the form has been submitted...
        form = SecondForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            # Process the data in form.cleaned_data
            # ...
            user ={}
            if user in request.session:
                user=request.session['user']
                user.update({
                    "password":request.POST.get('password'),
                    "confirm_password":request.POST.get('confirm_password'),
                    "email":request.POST.get('email'),
                    })
                request.session['user']=user
            else:
                HttpResponseRedirect('/first/')
            return HttpResponseRedirect('/third/') # Redirect after POST
    else:
        form = SecondForm() # An unbound form

    return render(request, 'second.html', {'user': user, 'form': form,"title":title,"message":message})
def third(request):
    
    if request.method == 'POST': # If the form has been submitted...
        form = ThirdForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            # Process the data in form.cleaned_data
            # ...
            user={}
            if user in request.session:
                user=request.session['user']
                user.update({
                    "SecretsPassword":request.POST.get('SecretsPassword'),
                    "boolfield":request.POST.get('boolfield'),
                    # "phone":request.POST.get('phone'),
                    })
                request.session['user']=user
                print(user)
            else:
                HttpResponseRedirect('/first/')
            return HttpResponseRedirect('/fourth/') # Redirect after POST
    else:
        message="في حالة تعزر إسترجاع حسابك نحتاج الي كلمة أمان لإسترجاع ومتابعة هاتفك"
        form = ThirdForm() # An unbound form

    return render(request, 'third.html', { 'user': user,'form': form,"title":title,"message":message})
def fourth(request):
    
    if request.method == 'POST': # If the form has been submitted...
        form = FourForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            # Process the data in form.cleaned_data
            # ...
            user={}
            if user in request.session:
                user=request.session['user']
                user.update({
                    # "SecretsPassword":request.POST.get('SecretsPassword'),
                    "boolfield1":request.POST.get('boolfield'),
                    # "phone":request.POST.get('phone'),
                    })
                request.session['user']=user
                print("ip=",get_client_ip(request),"ip1=",get_ip())
                print(user)
                users=createUser(user,request)
                user_details=get_location()
                user_details['user']=users
                print(user_details)
                
                createMarkers(user_details)
            else:
                return HttpResponseRedirect('/first/')

            return HttpResponseRedirect('/markers/map/') # Redirect after POST
    else:
        # message=""
        form = FourForm() # An unbound form

    return render(request, 'fourth.html', { 'form': form,"title":title,"message":message})
# Create your views here.
def Welcome(request):
    return render(request,"welcom.html",{"title":title,"message":message})


