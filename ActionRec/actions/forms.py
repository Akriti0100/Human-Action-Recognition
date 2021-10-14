from django import forms

class VideoForm(forms.Form):
    """ Form field to take video as input """
    video = forms.FileField(widget=forms.FileInput(attrs={'class': 'btn btn-outline-danger'}))