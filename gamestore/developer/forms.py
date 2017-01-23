from django import forms

class AddGameForm(forms.Form):
    game_title = forms.CharField(label='Game Title', max_length=127)
    game_url = forms.URLField(label='Game URL', max_length=256)
