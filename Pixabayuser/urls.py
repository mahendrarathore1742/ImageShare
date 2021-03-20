from django.urls import path;
from . import views
from .views import (Displayimages,PostRedirectView,PostAPIRedirectView,SaveAPIRedirectView)

urlpatterns =[
	path('user/account/myimages/',views.myimages,name="myimages"),
	path('user/account/settings/',views.settings,name="settings"),
	path('user/account/following/',views.following,name="following"),
	path('user/account/upload/',views.upload,name="upload"),
	path('user/account/Myprofile/',views.Myprofile,name='Myprofile'),
	path('user/account/save/',views.saveImg,name='saveImg'),
	#path('Photo/<slug:username>/<slug:slug>/',Displayimages.as_view()),
	path('<slug:username>/',views.userdata,name='userdata'),
	path('user/follow/<slug:username>',views.follow,name="follow"),
	path('Photo/<slug:username>/<slug:slug>/',views.DiplayImages,name='DiplayImages'),
	path('Photo/<slug:username>/<slug:slug>/like',PostRedirectView.as_view(),name='like'),
	path('Photo/<slug:username>/<slug:slug>/like/api',PostAPIRedirectView.as_view(),name='like_api'),
	path('Photo/<slug:username>/<slug:slug>/save/api',SaveAPIRedirectView.as_view(),name='save_api'),
	path('Tags/<slug:slug>',views.detail_view,name="detail_view"),
	path('Search/data/',views.Search,name='Search'),
	path('user/account/logout/',views.logout_view,name='logout_view'),
	
]