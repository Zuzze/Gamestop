from django import forms

class RegistrationForm(forms.ModelForm):
    username = forms.CharField(label='Username', max_length=256)
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    #user_type
    #class Meta:
    #    model = User

class LoginForm(forms.Form):
    username = forms.CharField(label='Username', max_length=256)
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
