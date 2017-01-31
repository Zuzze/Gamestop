from django import forms

UserType = (('1', 'Developer'), ('2', 'Player'))

class RegistrationForm(forms.Form):
    def __init__(self, *args, **kwargs):
        self.label_class = 'sr-only'
    #    self.form_class = 'form-control'
        super(RegistrationForm, self).__init__(*args, **kwargs)

    name = forms.CharField(label='Name', max_length=256,
        widget=forms.TextInput(attrs={'class': 'form-control',
                                      'placeholder': 'Full Name'}))
    username = forms.CharField(label='Username', max_length=256,
        widget=forms.PasswordInput(attrs={'class': 'form-control',
                                          'placeholder': 'Username'}))
    password = forms.CharField(label='Password',
        widget=forms.PasswordInput(attrs={'class': 'form-control',
                                          'placeholder': 'Password'}))
    user_type = forms.ChoiceField(choices=UserType,
        widget=forms.RadioSelect(attrs={'class':'form-control'}))

class LoginForm(forms.Form):
    def __init__(self, *args, **kwargs):
        self.label_class = 'sr-only'
        super(LoginForm, self).__init__(*args, **kwargs)

    username = forms.CharField(label='Username', max_length=256,
        widget=forms.PasswordInput(attrs={'class': 'form-control',
                                          'placeholder': 'Username'}))
    password = forms.CharField(label='Password',
        widget=forms.PasswordInput(attrs={'class': 'form-control',
                                          'placeholder': 'Password'}))
