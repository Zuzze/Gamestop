from django import forms

class AddGameForm(forms.Form):
    def __init__(self, *args, **kwargs):
        self.label_class = 'sr-only'
        super(AddGameForm, self).__init__(*args, **kwargs)

    game_title = forms.CharField(label='Game Title', max_length=127,
        widget=forms.TextInput(attrs={'class': 'form-control',
                                      'placeholder': 'Game Title'}))
    game_url = forms.URLField(label='Game URL', max_length=256,
        widget=forms.URLInput(attrs={'class': 'form-control',
                                     'placeholder': 'Game URL'}))
    game_price = forms.DecimalField(label='Game Price', max_digits=8,
        widget=forms.NumberInput(attrs={'class': 'form-control',
                                        'placeholder': 'Game Price'}))
    game_description = forms.CharField(label='Game Description', max_length=1024,
        required=False, widget=forms.NumberInput(attrs={'class': 'form-control',
                                            'placeholder': 'Game Description'}))
    game_icon = forms.URLField(label='Game Icon URL', max_length=256, required=False,
    widget=forms.URLInput(attrs={'class': 'form-control','placeholder': 'Game Icon URL'}))

    def clean(self):
        price_ = self.cleaned_data['game_price']
        if price_ < 0:
            raise forms.ValidationError("Game price cannot be less than zero.")
