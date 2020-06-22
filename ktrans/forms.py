from django import forms
from .models import Students, Drivers,QuickEnquiry


class ContactForm(forms.ModelForm):
    name = forms.CharField(max_length=30,widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.CharField(max_length=245,widget=forms.TextInput(attrs={'class':'form-control'}))
    phone = forms.CharField(max_length=20,widget=forms.TextInput(attrs={'class':'form-control'}))
    message = forms.CharField(max_length=200,widget=forms.Textarea(attrs={'class':'form-control','cols': 10, 'rows': 10}))

    class Meta:
        model = QuickEnquiry
        fields = ['name','email','phone','message']
