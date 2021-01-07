from django import forms
from App_Login.models import User, Profile

from django.contrib.auth.forms import UserCreationForm


# forms

class ProfileForm(forms.ModelForm):
    address_1 = forms.CharField(max_length=300,required=False, widget=forms.Textarea(attrs={'rows':2}))
    class Meta:
        model = Profile
        exclude = ('user',)

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('email', 'password1', 'password2')
