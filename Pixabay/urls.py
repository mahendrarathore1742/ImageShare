from django.urls import path;

from . import views
urlpatterns=[

	path('',views.home,name='home'),
	path('PopularHashtags/',views.most_popular_hashtags,name='most_popular_hashtags'),
	path('Trending/',views.Trending,name='Trending'),
	path('Mostlikephoto/',views.mostlikephoto,name='Mostlikephoto'),
	path('Usernotfound/',views.usernot_found,name='usernotfound'),
	path('photo/',views.photo,name='photo')

]