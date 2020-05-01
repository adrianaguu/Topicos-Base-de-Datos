from django import forms

class PhraseForm(forms.Form):
    vec1 = forms.CharField(label='vec1', widget=forms.Textarea)
    vec2 = forms.CharField(label='vec2', widget=forms.Textarea)
    vec3 = forms.CharField(label='vec3', widget=forms.Textarea)
    vec4 = forms.CharField(label='vec4', widget=forms.Textarea)
    vec5 = forms.CharField(label='vec5', widget=forms.Textarea)
    result = forms.CharField(label='result', widget=forms.Textarea, required=False)
