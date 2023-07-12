from django.contrib.auth.forms import UserCreationForm
from django.forms import ValidationError
from django.contrib.auth.models import User
from django import forms
class RegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=20,required=True)
    last_name = forms.CharField(max_length=20,required=True)
    email = forms.EmailField(max_length=50,required=True)

    class Meta:
        model = User
        fields = ["first_name","last_name",'username',"email","password1","password2"]

    def clean_email(self):
        email1 = self.cleaned_data['email']
        user = None
        try:
            user = User.objects.get(email = email1)
        except:
            return email1
        if(user is not None):
            raise ValidationError('User already exists')