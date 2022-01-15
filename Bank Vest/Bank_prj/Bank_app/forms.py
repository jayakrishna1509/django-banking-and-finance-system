from django import forms
from .models import Register

class RegisterForm(forms.ModelForm):
    class Meta:
        fields = "__all__"

class LoginForm(forms.ModelForm):
    class Meta:
        fields = "__all__"
