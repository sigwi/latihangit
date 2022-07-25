from django import forms

class HomeForm(forms.Form):
    nama_lengkap = forms.CharField(
        label ='Nama Lengkap',
        widget =forms.TextInput(attrs={'class':'form-control', 'placeholder':"Masukkan Nama Lengkap"})
    )
    category = forms.CharField(
        label = 'Category',
        widget = forms.TextInput(attrs={'class':'form-control'})
    )
