from django.urls import path;

from . import views;
from django.contrib.auth import views as reset;

urlpatterns=[
	path('user/account/',views.signupuser,name='account'),
	path('user/account/login',views.loginuser,name="loginuser"),
	path('accounts/password/reset/',reset.PasswordResetView.as_view(template_name='PasswordReset/paswordreset.html'),name='password_reset'),
    path('accounts/password/reset/done',reset.PasswordResetDoneView.as_view(template_name='PasswordReset/Done.html'),name='password_reset_done'),
    path('accounts/password/reset/confirm/<uidb64>/<token>',reset.PasswordResetConfirmView.as_view(template_name='PasswordReset/confirm.html'),name='password_reset_confirm'),
    path('accounts/password/reset/complete',reset.PasswordResetCompleteView.as_view(template_name='PasswordReset/passwordresetcomplete.html'),name='password_reset_complete'),
] 





