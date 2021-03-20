from django.shortcuts import render,redirect
from django.contrib import messages
from .form import signup 
from django.contrib.auth import authenticate,login,logout;
from django.contrib.auth.models import User
from django.contrib import messages,auth

def signupuser(request):
	if not request.user.is_authenticated:
		if request.method=="POST":
			form=signup(request.POST or None) 
			if form.is_valid():
				form.save();
				return redirect('/user/account/settings/')
			else:
				messages.error(request,form.errors)
				return redirect('/user/account');
		else:
			form=signup();
			return render(request,"account.html",{"form":form})
		return render(request,'account.html')
	else:
		return redirect("/user/account/settings/");

def loginuser(request):
	if not request.user.is_authenticated:
		if request.method=="POST":
			if request.POST['email'].strip() and  request.POST['password']:
				try:
					user=User.objects.get(email=request.POST['email'])
					auth.login(request,user)
					if request.POST["next"] !="":
						return redirect(request.POST.get('next'));
					else:
						return redirect("/user/account/settings/");        
					return redirect("/user/account/settings/");
				except User.DoesNotExist:
					messages.error(request,"User Does't Exist");
					return render(request,"login.html");
			else:
				messages.error(request,"Empty field");
				return render(request,"login.html")
		else:
			return render(request,'login.html')
	else:
		return redirect("/user/account/settings/");

