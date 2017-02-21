from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

UserType = (('1', 'Developer'), ('2', 'Player'))

class RegistrationForm(forms.Form):
    def __init__(self, *args, **kwargs):
        self.label_class = 'sr-only'
        super(RegistrationForm, self).__init__(*args, **kwargs)

    name = forms.CharField(label='Name', max_length=256,
        widget=forms.TextInput(attrs={'class': 'form-control',
                                      'placeholder': 'Full Name'}))
    username = forms.CharField(label='Username', max_length=256,
        widget=forms.TextInput(attrs={'class': 'form-control',
                                          'placeholder': 'Username'}))
    password = forms.CharField(label='Password',
        widget=forms.PasswordInput(attrs={'class': 'form-control',
                                          'placeholder': 'Password'}))
    re_password = forms.CharField(label='Re-Password',
        widget=forms.PasswordInput(attrs={'class': 'form-control',
                                          'placeholder': 'Re-type Password'}))
    user_type = forms.ChoiceField(choices=UserType,
        widget=forms.RadioSelect(attrs={'class':'form-control'}))

    def clean(self):
        name_ = self.cleaned_data['name']
        username_ = self.cleaned_data['username']
        password_ = self.cleaned_data['password']
        re_password_ = self.cleaned_data['re_password']
        user_type_ = self.cleaned_data['user_type']

        if password_ != re_password_:
            raise forms.ValidationError("Passwords do not match.")

        try:
            user_exists = User.objects.get(username=username_)
        except User.DoesNotExist:
            print("User does not exist")
        else:
            print("User exist")
            raise forms.ValidationError("Username is taken!")

class LoginForm(forms.Form):
    def __init__(self, *args, **kwargs):
        self.label_class = 'sr-only'
        self.login_allowed = False
        super(LoginForm, self).__init__(*args, **kwargs)

    username = forms.CharField(label='Username', max_length=256,
        widget=forms.TextInput(attrs={'class': 'form-control',
                                          'placeholder': 'Username'}))
    password = forms.CharField(label='Password',
        widget=forms.PasswordInput(attrs={'class': 'form-control',
                                          'placeholder': 'Password'}))
    def clean(self):
        username_ = self.cleaned_data['username']
        password_ = self.cleaned_data['password']

        user = authenticate(username=username_, password=password_)
        if user is None:
            self.login_allowed = False
            raise forms.ValidationError("Username or password is wrong!")
        else:
            self.login_allowed = True
