from django import forms

class AddGameForm(forms.Form):
    game_title = forms.CharField(label='Game Title', max_length=127)
    game_url = forms.URLField(label='Game URL', max_length=256)
    game_price = forms.DecimalField(label='Game Price', max_digits=8)
    game_description = forms.CharField(label='Game Description', max_length=1024,
        required=False)
    game_icon = forms.URLField(label='Game Icon', max_length=256, required=False)
