from django import forms
from .models import Quiz1
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.contrib.auth.models import User




class QuizForm(forms.ModelForm):
    class Meta:
        model = Quiz1
        fields = ['title','question','option1','option2','option3','option4','correct_option']


class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

 