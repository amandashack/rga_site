from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField(label='E-Mail')
    date = forms.DateField()

class TrackerForm(forms.Form):
    mass_number = forms.FloatField(label='Mass #')
    body = forms.CharField(widget=forms.Textarea)
