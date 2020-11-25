from django import forms
from django.contrib.auth import (
    authenticate,
    get_user_model

)
from .models import User, Client
from django.forms import ModelForm

# User = get_user_model()

class UserLoginForm(forms.Form):
    email = forms.CharField(max_length=255)
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self, *args, **kwargs):
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')

        if email and password:
            user = authenticate(email=email,password=password)
            if not user:
                raise forms.ValidationError('Invalid email or password')
            if not user.check_password(password):
                raise forms.ValidationError('Invalid email or password')
            # if not email.is_active:
            #     raise forms.ValidationError('This user is not active')
        return super(UserLoginForm, self).clean(*args, **kwargs)

class UserRegisterForm(forms.ModelForm):
    first_name = forms.CharField(label="First Name")
    last_name = forms.CharField(label="Last Name")
    email = forms.EmailField(label='Email Address')
    email2 = forms.EmailField(label='Confirm Email Address')
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'email',
            'email2',
            'password'
        ]
    
    def clean(self, *args, **kwargs):
        first_name = self.cleaned_data.get('first_name')
        last_name = self.cleaned_data.get('last_name')
        email = self.cleaned_data.get('email')
        email2 = self.cleaned_data.get('email2')
        if email != email2:
            raise forms.ValidationError("Emails must match")
        # Check if email is already being used 
        email_qs = User.objects.filter(email=email)
        if email_qs.exists():
            raise forms.ValidationError(
                "This email is already being used"
        )
        return super(UserRegisterForm, self).clean(*args, **kwargs)


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['first_name', 'last_name', 'email', 'phone_num']
        first_name = forms.CharField(label="First Name")
        last_name = forms.CharField(label="Last Name")
        email = forms.EmailField(label='Email Address')
        phone_num = forms.CharField(label="Phone Number", max_length=10)
    
    def clean(self, *args, **kwargs):
        first_name = self.cleaned_data.get('first_name')
        last_name = self.cleaned_data.get('last_name')
        email = self.cleaned_data.get('email')
        phone_num = self.cleaned_data.get('phone_num')
        
        return super(ClientForm, self).clean(*args, **kwargs)

