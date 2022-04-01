from django import forms
from django.contrib.auth.models import User

class LoginForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput)

class UserRegistrationForm(forms.ModelForm):
    phoneno=forms.IntegerField(label='Phone Number')
    address1=forms.CharField(label='Address1',max_length=1024)
    address2=forms.CharField(label='Address2',max_length=1024)
    city=forms.CharField(label='City',max_length=50)
    state=forms.CharField(label='State',max_length=50)
    country=forms.CharField(label='Country',max_length=50)
    pincode=forms.IntegerField(label='Pincode')
    password=forms.CharField(label='Password',widget=forms.PasswordInput)
    password2=forms.CharField(label='Repeat Password',widget=forms.PasswordInput)
    Signup_as_service_personnel=forms.BooleanField()
    Signup_as_Employeed=forms.BooleanField()


    class Meta:
        model=User
        fields = ('username','first_name','last_name','email')

    def clean_password2(self):
        cd=self.cleaned_data
        if cd['password']!=cd['password2']:
            raise forms.ValidationError('Passwords don\'t Match')
        return cd['password2']

class add_new_items(forms.Form):
    item_name = forms.CharField(label='Item Name', max_length=50)
    price = forms.FloatField(label='Price')
    brand = forms.CharField(label='Model',max_length=50)
    type = forms.CharField(label='Type', max_length=50)
    date = forms.DateField(label='Date')
    invoice_image = forms.ImageField(label='Invoice Image')
    Warranty = forms.BooleanField()
    Insurance = forms.BooleanField()


