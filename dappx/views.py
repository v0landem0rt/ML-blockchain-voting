from django.shortcuts import render, redirect
import json
import base64
from dappx.forms import UserForm,UserProfileInfoForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
import subprocess
import os

def index(request):
   return render(request,'dappx/index.html')

@login_required
def special(request):
    return HttpResponse("You are logged in !")
@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))
def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            if 'profile_pic' in request.FILES:
                print('found it')
                profile.profile_pic = request.FILES['profile_pic']
            profile.save()
            registered = True
        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()
    return render(request,'dappx/registration.html',
                          {'user_form':user_form,
                           'profile_form':profile_form,
                           'registered':registered})
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Your account was inactive.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            return HttpResponse("Invalid login details given")
    else:
        return render(request, 'dappx/login.html', {})


'''
@login_required
def verify(request):
   if request.method == 'GET':
     result = subprocess.run(['python3', '/home/lera/verification_person/sec.py'], stdout=subprocess.PIPE)
     if result.stdout.decode('utf-8').find('Authentication Successfull'):
       return HttpResponse("You are verifyed successfully!")
     else:
       return HttpResponse("You aren't verify!")
'''

@login_required
def verify(request):
   if request.method == 'GET':

     result = subprocess.run(['python3', '/home/lera/verification_person/verification_id.py'], stdout=subprocess.PIPE)
     if result.stdout.decode('utf-8').find('Authentication Successfull'):
       res_string = {'verify': 1}
       return HttpResponse(json.dumps(res_string), content_type="application/json")
     else:
       res_string = {'verify': 0}
       return HttpResponse(json.dumps(res_string), content_type="application/json")


@login_required
def register_voting(request):
   if request.method == 'POST':

     body_unicode = request.body.decode('utf-8') 
     file1 = open("/home/lera/base64.txt", "w")
     file1.writelines(str(body_unicode))
     file1.close() 
     result = subprocess.run(['python3', '/home/lera/verification_person/registration_id.py'], stdout=subprocess.PIPE)
     if result.stdout.decode('utf-8').find('registered successfully\n'):
        os.system('rm /home/lera/base64.txt')
        res_string = {'register': 1}
        return HttpResponse(json.dumps(res_string), content_type="application/json")
     else:
        res_string = {'verify': 0}
        return HttpResponse(json.dumps(res_string), content_type="application/json")
   else:
      res_string = {'verify': 0}
      return HttpResponse(json.dumps(res_string), content_type="application/json")
