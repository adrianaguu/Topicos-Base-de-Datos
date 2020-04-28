from django import forms

class PhraseForm(forms.Form):
    phrase = forms.CharField(label='Ingrese la frase', widget=forms.Textarea)
    convertedphrase = forms.CharField(label='Frase procesada', widget=forms.Textarea, required=False)
