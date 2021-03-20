from django.contrib.auth.models import User
from .models import  Userdata;
from django import forms
from django.contrib.auth.forms import UserCreationForm,UserChangeForm

from django import forms;
from .models import ImagePost


class  updatedata(UserChangeForm):
	class Meta:
		model=Userdata;
		fields=("Profileimage",'GENDER','FirstName','LastName','City','Country','Aboutme')

		
class Userform(UserChangeForm):
	class Meta:
		model=User;
		fields=("username",'email')
       
class Imagepost(forms.ModelForm):
	class Meta:
		model=ImagePost;
		fields=("Images","Title",'tags')






