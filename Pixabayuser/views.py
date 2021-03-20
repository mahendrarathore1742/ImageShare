from django.shortcuts import render,redirect,get_object_or_404,get_list_or_404
from django.contrib import messages
from .userforms import updatedata,Imagepost,Userform
from .models import ImagePost
from django.views.generic.edit import UpdateView
from django.contrib.auth.models import User
from django.views.generic.edit import FormView
from django.views.generic.detail import DetailView
from django.views.generic import ListView
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Userdata
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Following;
import json
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.views.generic.base import RedirectView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.db.models import Count
from taggit.models import Tag
from django.template.defaultfilters import slugify
from functools import reduce
import operator 
from django.db.models import Q
from django.contrib.auth import logout
from hitcount.models import HitCount
from hitcount.views import HitCountMixin

@login_required
def following(request):
	user=Following.objects.get(user=request.user);
	followed_user=[i for i in user.followed.all()];
	followed_user.append(request.user);
	posts=ImagePost.objects.filter(user__in=followed_user).order_by("-id");
	return render(request,'myaccountdata/following.html',{"posts":posts})

@login_required
def myimages(request):
	user = request.user
	data = ImagePost.objects.filter(user=user).order_by("-id")
	return render(request,'myaccountdata/myimage.html',{"data":data})
 
@login_required
def settings(request):
	if request.method=="POST":
		form=updatedata(request.POST or None,request.FILES or None, instance=request.user.userprofile or None);
		form1=Userform(request.POST or None,instance=request.user or None);
		if form.is_valid() and form1.is_valid():
			form.save();
			form1.save(commit=False);
			return redirect('/user/account/settings/');
		else:
			messages.error(request,form.errors)
			messages.error(request,form1.errors)
			return redirect('/user/account/settings/');
	else: 
		form=updatedata( instance=request.user.userprofile);
		form1=Userform(instance=request.user);
		return render(request,'myaccountdata/settings.html',{"form":form,"form1":form1});
	return render(request,'myaccountdata/settings.html')

@login_required
def upload(request):
	user=request.user;
	alltags=ImagePost.tags.most_common();
	if request.method=="POST":
		user=request.user
		form=Imagepost(request.POST or None,request.FILES or None);
		common_tags = ImagePost.tags.most_common()[:4]
		if form.is_valid():
			obj = form.save(commit=False) 
			obj.user = request.user; 
			obj.save()
			form.save_m2m()
			return redirect('/user/account/myimages/');
		else:
			messages.error(request,form.errors)
			return redirect('/user/account/upload/');
	else: 
		form=Imagepost();
		return render(request,'myaccountdata/upload.html',{"form":form,'alltags':alltags});
	return render(request,'myaccountdata/upload.html',{'alltags':alltags})
 
@login_required
def Myprofile(request):
	user = request.user
	Imagecount = ImagePost.objects.filter(user=user).count()
	queryset=ImagePost.objects.filter(user=user).aggregate(total_likes=Count('like'))['total_likes'] or 0
	data = ImagePost.objects.filter(user=user).order_by('-id')
	following_obj=Following.objects.get(user__username=user).follower.count();
	return render(request,'myaccountdata/Myprofile.html',{"Imagecount":Imagecount,"data":data,"following_obj":following_obj,'queryset':queryset})


class Displayimages(DetailView):
	template_name="myaccountdata/photo.html";
	queryset=ImagePost.objects.all();

def DiplayImages(request,username,slug):
	try:
		user=User.objects.filter(username=username);
		Data=None;
		if user and request.user.is_authenticated:
			user=user[0]
			Data=Following.objects.filter(user=request.user,followed=user);
		usernamedata=User.objects.get(username=username)
		queryset=ImagePost.objects.get(slug=slug);
		hit_count = HitCount.objects.get_for_object(queryset)
		hit_count_response = HitCountMixin.hit_count(request, hit_count)
		data = ImagePost.objects.filter(user__username=username).order_by("-id")[:6];
		return render(request,"myaccountdata/photo.html",{"queryset":queryset,
														'data':data,
														'usernamedata':usernamedata,
														'Data':Data,
														})
		 
	except Exception as e:
		return HttpResponse("404 not Found")
	
	

def userdata(request,username):
	try:
		user=User.objects.filter(username=username);
		Data=None;
		if user and  request.user.is_authenticated:
			user=user[0]
			Data=Following.objects.filter(user=request.user,followed=user);
		Imagecount = ImagePost.objects.filter(user__username=username).count()
		queryset=ImagePost.objects.filter(user__username=username).aggregate(total_likes=Count('like'))['total_likes'] or 0
		print(queryset)
		data = ImagePost.objects.filter(user__username=username).order_by("-id")
		Userdata=User.objects.get(username=username)
		following_obj=Following.objects.get(user__username=username).follower.count();
		return render(request,'myaccountdata/user.html',{'Userdata':Userdata,
														'data':data,
														"Imagecount":Imagecount,
														"following_obj":following_obj,
														'Data':Data,
														"queryset":queryset
														})
	except Exception as e:
		return HttpResponse("404 Not Found")
	
	

@login_required
def follow(request,username):
	main_user=request.user;
	to_follow=User.objects.get(username=username);
	# if already following user
	following=Following.objects.filter(user=main_user,followed=to_follow);
	is_following=True if following else False;

	if is_following:
		Following.unfollow(main_user,to_follow);
		is_following=False
	else:
		Following.follow(main_user,to_follow)
		is_following=True;

	resp={
	"following":is_following
	}
	response=json.dumps(resp);
	print(response)
	return HttpResponse(response)


class PostRedirectView(RedirectView):
	def get_redirect_url(self,*args,**kwargs):
		slug=self.kwargs.get('slug');
		print(slug)
		obj=get_object_or_404(ImagePost,slug=slug);
		usr_=obj.get_detail_url()
		user=self.request.user;
		if user.is_authenticated:
			if user in obj.like.all():
				obj.like.remove(user);
			else:
				obj.like.add(user)
		return usr_

class PostAPIRedirectView(APIView):
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request,slug=None, username=None, format=None):
    	#slug=self.kwargs.get('slug');
    	
    	obj=get_object_or_404(ImagePost,slug=slug);
    	usr_=obj.get_api_like_url()
    	user=self.request.user;
    	updated=False;
    	liked=False
    	if user.is_authenticated:
    		if user in obj.like.all():
    			liked=False;
    			obj.like.remove(user);
    		else:
    			liked=True
    			obj.like.add(user);
    		updated=True
    		counts=obj.like.count()
    	data={"updated":updated,'liked':liked,"likescount": counts}
    	return Response(data)


class SaveAPIRedirectView(APIView):
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request,slug=None, username=None, format=None):
    	#slug=self.kwargs.get('slug');
    	obj=get_object_or_404(ImagePost,slug=slug);
    	usr_=obj.get_api_save_url()
    	user=self.request.user;
    	updated=False;
    	saved=False;
    	if user.is_authenticated:
    		if user in obj.save_post.all():
    			saved=False;
    			obj.save_post.remove(user);
    		else:
    			saved=True
    			obj.save_post.add(user);
    		updated=True
    		
    	datasave={"updated":updated,'saved':saved}
    	return Response(datasave)

@login_required
def saveImg(request):
	user=request.user;
	queryset = ImagePost.objects.filter(save_post=request.user).distinct().order_by('-id')
	print(queryset)
	return render(request,'myaccountdata/save.html',{'queryset':queryset}) 

def detail_view(request, slug):
    alltagsdata = get_object_or_404(Tag, slug=slug)
    posts = ImagePost.objects.filter(tags=alltagsdata).order_by('-id')
    return render(request, 'myaccountdata/alltagdata.html', {'alltagsdata':posts})


def Search(request):
	q=request.GET['query']
	if len(q)>78:
		allpost=ImagePost.objects.none();
	else:
		allpostTitle=ImagePost.objects.filter(tags__name__icontains=q)
		print(allpostTitle)
		allpostcontent=ImagePost.objects.filter(Title__icontains=q);
		allpost=allpostTitle.union(allpostcontent)
	if allpost.count()==0:
		 messages.error(request, 'No search Result Found try again')
	if q=="":
		messages.error(request, 'Enter the value what you want!')
		allpost=ImagePost.objects.none();
	data={'allpost':allpost,'query':q}
	return render(request,'myaccountdata/Search.html',data)

def logout_view(request):
    logout(request)
    return redirect('/user/account/login')





