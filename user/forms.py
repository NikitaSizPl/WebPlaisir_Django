from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from user.models import User
from django import forms

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput)
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ('username', 'password')


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput)
    # instagram = forms.CharField(widget=forms.TextInput)
    # phone = forms.CharField(widget=forms.TextInput)
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ('username',  'password1', 'password2')


class UserProfilerForm(UserChangeForm):
    username = forms.CharField(widget=forms.TextInput)
    instagram = forms.CharField(widget=forms.TextInput)
    phone = forms.CharField(widget=forms.TextInput)
    class Meta:
        model = User
        fields = ('username', 'instagram', 'phone')