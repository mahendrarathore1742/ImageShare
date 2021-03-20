from django.contrib.auth.models import User
from django import forms

class signup(forms.ModelForm):
	class Meta:
		model=User;
		fields=("email",'username','password');
		

	def clean_email(self):
		email = self.cleaned_data['email'];

		if not email:
			raise forms.ValidationError('Enter the email!');
		elif User.objects.filter(email=email).first():
			raise forms.ValidationError('Email is already taken.')
		return email

	



