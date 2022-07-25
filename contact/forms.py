from django import forms

class ContactForm(forms.Form):
    #data type
    integer   = forms.IntegerField()
    decimal   = forms.DecimalField()
    float     = forms.FloatField()
    boolean   = forms.BooleanField()
    character = forms.CharField(widget=forms.Textarea)
    #string type
    email   = forms.EmailField()
        # regex_field   = forms.RegexField()
    slug    = forms.SlugField()
    url     = forms.URLField()
        # ip      = forms.GenericIPAddressfield()
    #select input
    PILIHAN = (
        ('pilih1','nilai 1'),
        ('pilih2','nilai 2'),
        ('pilih3','nilai 3'),
    )
    choice = forms.ChoiceField(choices=PILIHAN)
    multiple_choice = forms.MultipleChoiceField(choices=PILIHAN)
    multi_type = forms.TypedMultipleChoiceField(choices=PILIHAN)
    #date time
    #file input
    file = forms.FileField()
    img = forms.ImageField()

    
