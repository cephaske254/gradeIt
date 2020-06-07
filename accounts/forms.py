from django import forms
from main.models import Profile

class UpdateUserForm(forms.Form):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    email = forms.EmailField(required=True)

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude=[]
