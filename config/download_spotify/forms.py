from django import forms


class GetLinkForm(forms.Form):
    title = forms.CharField(max_length=255, widget=forms.TextInput(
        attrs={'class': 'input-title'}
        ))

