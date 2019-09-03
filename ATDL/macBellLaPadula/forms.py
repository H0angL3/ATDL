from django import forms


class WordProcessForm(forms.Form):
    content = forms.CharField(widget=forms.Textarea)

class Login(forms.Form):
    username = forms.CharField(max_length= 100, label="Tài khoản")
    password = forms.CharField(widget=forms.PasswordInput, label="Mật khẩu")

class NewDocument(forms.Form):
    title = forms.CharField(max_length=100, label='Title', widget=forms.TextInput(attrs={'placeholder': 'Your title'}))
    content = forms.CharField(
        label = 'Content',
        widget=forms.Textarea(attrs={
            'placeholder': 'Your content',
            'rows': 20,
            'cols': 100,
        }))
    categories = forms.ChoiceField(label="category")
    def __init__(self, categories, *args,**kwargs):
        super(NewDocument, self).__init__(*args, **kwargs)
        self.fields['categories'].choices = categories



