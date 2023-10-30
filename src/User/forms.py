from django import forms
from django.forms import modelformset_factory, inlineformset_factory
from django.contrib.auth.models import User

input_css_class="inputs labels"

class SignInForm(forms.ModelForm):
    class Meta:
        model=User
        fields = ['email','password']
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.fields['name'].widget.attrs['placeholder'] = "Your name"
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = input_css_class

class SignUpForm(forms.ModelForm):
    class Meta:
        model=User
        fields = ['username','email','password'] 
