from django import forms

class BlogForm(forms.Form):
    judul = forms.CharField(
        label ='Judul',
        widget =forms.TextInput(attrs={'class':'form-control', 'placeholder':"Masukkan Judul"})
    )
    body = forms.CharField(
        label = 'Body',
        widget = forms.Textarea(attrs={'class':'form-control'})
    )
    category = forms.CharField(
        label = 'Category',
        widget = forms.TextInput(attrs={'class':'form-control'})
    )

    def clean_judul(self):
        judul_input = self.cleaned_data.get('judul')
        if judul_input == 'ucup':
            raise forms.ValidationError("Ucup tdk boleh diposting")
        return judul_input
