from django.shortcuts import render
from Pixabayuser.models import ImagePost
from Pixabayuser.models import Userdata
from django.db.models import Count
from taggit.models import Tag
from collections import Counter

def home(request):
	Alldata=ImagePost.objects.all().order_by("-id");
	return render(request,'home.html',{"Alldata":Alldata});

def photo(request):
	Alldata=ImagePost.objects.all().order_by('-id');
	return render(request,'photo.html',{"Alldata":Alldata});

def most_popular_hashtags(request):
	tophastag=ImagePost.tags.most_common()[:10];
	return render(request,'PopularHashtags.html',{'tophastag':tophastag})

def Trending(request):
	Trending_image=ImagePost.objects.order_by('hit')[:8] 

	return render(request,'Trending.html',{'Trending_image':Trending_image})

def mostlikephoto(request):
	Most_likes=ImagePost.objects.annotate(like_count=Count('like')).order_by('-like_count')[:20] 
	return render(request,'Mostlikephoto.html',{'Most_likes':Most_likes})

def usernot_found(request):
	return render(request,'usernot_found.html')




