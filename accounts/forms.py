from django import forms
from .models import User, Profile
from django.contrib.auth.forms import UserCreationForm


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')


class ProfileForm1(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('image', 'bio', 'location', 'birth_date')


class ProfileForm(UserCreationForm):
    first_name = forms.CharField(label='Primeiro nome',max_length=100, required=True)
    last_name = forms.CharField(label='Sobrenome',max_length=100)
    email = forms.EmailField(label='E-mail',max_length=150, required=True)

    first_name.widget.attrs['class'] = 'form-control'
    last_name.widget.attrs['class'] = 'form-control'
    email.widget.attrs['class'] = 'form-control'

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2',)