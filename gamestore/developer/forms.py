from django import forms
from gamedata.models import Game

GameCategory = (('A', 'Action'),
    ('RP', 'Role Playing'),
    ('FPS', 'FPS'),
    ('SM', 'Simulation'),
    ('SR', 'Strategy'),
    ('O', 'Other'))

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
        required=False, widget=forms.TextInput(attrs={'class': 'form-control',
                                            'placeholder': 'Game Description'}))

    game_icon = forms.URLField(label='Game Icon URL', max_length=256, required=False,
    widget=forms.URLInput(attrs={'class': 'form-control','placeholder': 'Game Icon URL'}))

    game_category = forms.ChoiceField(choices=GameCategory, initial='S', required=False,
        widget=forms.Select(attrs={'class':'form-control'}))

    def clean(self):
        price_ = self.cleaned_data['game_price']
        if price_ < 0:
            raise forms.ValidationError("Game price cannot be less than zero.")

        title_ = self.cleaned_data['game_title']
        g = Game.objects.filter(title=title_)
        if len(g):
            raise forms.ValidationError("Game title is already present.")


class ModifyGameForm(forms.Form):
    """
    def __init__(self, *args, **kwargs):
        self.label_class = 'sr-only'
        super(ModifyGameForm, self).__init__(*args, **kwargs)
    """

    game_title = forms.CharField(label='Game Title', max_length=127, required=False,
        widget=forms.TextInput(attrs={'class': 'form-control'}))

    game_url = forms.URLField(label='Game URL', max_length=256, required=False,
        widget=forms.URLInput(attrs={'class': 'form-control'}))

    game_price = forms.DecimalField(label='Game Price', max_digits=8, required=False,
        widget=forms.NumberInput(attrs={'class': 'form-control'}))

    game_description = forms.CharField(label='Game Description', max_length=1024, required=False,
        widget=forms.TextInput(attrs={'class': 'form-control'}))

    game_icon = forms.URLField(label='Game Icon URL', max_length=256, required=False,
        widget=forms.URLInput(attrs={'class': 'form-control'}))

    game_category = forms.ChoiceField(choices=GameCategory, initial='S', required=False,
        widget=forms.Select(attrs={'class':'form-control'}))
