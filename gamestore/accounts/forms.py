from django import forms

UserType = (('1', 'Developer'), ('2', 'Player'))

class RegistrationForm(forms.Form):
    name = forms.CharField(label='Name', max_length=256)
    username = forms.CharField(label='Username', max_length=256)
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    user_type = forms.ChoiceField(widget=forms.RadioSelect, choices=UserType)

class LoginForm(forms.Form):
    username = forms.CharField(label='Username', max_length=256)
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
