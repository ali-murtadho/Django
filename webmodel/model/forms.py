from django import forms
from .models import padi
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
class PadiForm(forms.ModelForm):
    class Meta:
        model = padi
        fields = ['varietas', 'warna', 'rasa', 'teknik', 'musim', 'penyakit', 'ph', 'b']

class UserRegistrationForm(UserCreationForm):
    username = forms.CharField()

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

