from django import forms

class TeachersForm(forms.Form):
    name = forms.CharField( min_length=5, label='Your Name', label_suffix="",error_messages=
                           {'required':'Your name can not be emtpy','min_length':'Min length is 5','max_length':"max length should be 10"},
                           widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(required=False, help_text='Accept only gmail', label='Your Email', label_suffix="",
                           widget=forms.TextInput(attrs={'class':'form-control'}))
    phone_number = forms.IntegerField(label='Your Contact Number', label_suffix="",
                           widget=forms.TextInput(attrs={'class':'form-control'}))
    bio = forms.CharField(label='Bio',label_suffix="", widget=forms.Textarea(attrs={'placeholder':'Bio', 'cols':5,'class':'form-control'}))