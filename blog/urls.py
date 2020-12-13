"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from  users import views as user_views
#built in views(class based views)
#these views handle the logic ,but not the templates ,you need to write the template for them
#this auth_views also have the reset password views
from django.contrib.auth import  views as auth_views
#for static media (like pics)
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include("bloging.urls")),
    path('register/',user_views.register,name="register"),
    #note i change the directory inside the template from 1 to users, 
    path('login/',auth_views.LoginView.as_view(template_name='1/login.html'),name="login"),
    path('logout/',auth_views.LogoutView.as_view(template_name='1/logout.html'),name="logout"),

    path('reset-password/',auth_views.PasswordResetView.as_view(template_name='1/password_reset.html'),
    name="password_reset"),

    path('password-reset/done/',auth_views.PasswordResetDoneView.as_view
    (template_name='1/password_reset_done.html'),
    name="password_reset_done"),

    path('reset-password-confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view
    (template_name='1/password_reset_confirm.html'),
    name="password_reset_confirm"),
    
    path('reset-password-complete/',auth_views.PasswordResetCompleteView.as_view
    (template_name='1/password_reset_complete.html'),
    name="password_reset_complete"),

    path('password-change/',auth_views.PasswordChangeView.as_view
    (template_name='1/password_change.html'),
    name="password_change"),

    path('password-change-done/',auth_views.PasswordChangeDoneView.as_view
    (template_name='1/password_change_done.html'),
    name="password_change_done"),


    path('profile/',user_views.profile,name="profile"),
]   

#not good to use that in production ,so as long as we in the develploment we will use it 
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    