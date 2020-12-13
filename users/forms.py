from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
from bloging.models import post

"""
we need to add an email filed ,but usercreationform by deffult doesnot have that ,so we need to create a form that 
have that and also inhearte the usercreationform so it have the prev input filed and the new email one 
"""

class UserRegisterForm(UserCreationForm):
    #defult is reqired is true
    email=forms.EmailField(required=True)

    class Meta():
        """
        model that will get effected is the user model(user table in the database) when we do form.save() it will save it
        to the user model.
        note:this class is in UserCreationForm by diffult but since we add another form class to mutate the old one 
        we have to do this implicilty
        """
        model=User
        #fields that in out form and the order of the apperance
        fields=["username","email","password1","password2"]


#allow us to update user name and email ,and the other allow us to update our image
class UserUpdateForm(forms.ModelForm):
    email=forms.EmailField()

    class Meta():
        model=User
        #exclude =["password1","password2"]
        fields =["username","email"]

class ProfileUpdateForm(forms.ModelForm):
    class Meta():
        model=Profile
        fields =["image"]

