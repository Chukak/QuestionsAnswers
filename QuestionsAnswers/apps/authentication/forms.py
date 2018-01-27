from django import forms
from django.forms import ModelForm
from ..accounts.models import User
from django.utils.translation import gettext_lazy as _


# Model form for User model
class UserCreationForm(ModelForm):
    # password field
    password = forms.CharField(max_length=32, help_text=_('Required. 32 character or fewer.'),
                               required=True, label=_('Password'),
                               widget=forms.PasswordInput(attrs={'class': 'form-control form-control-inline'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'avatar')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control form-control-inline'}),
            'email': forms.EmailInput(attrs={'class': 'form-control form-control-inline'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control form-control-inline'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control form-control-inline'}),
        }

    # clean method for password field
    def clean_password(self):
        password = self.cleaned_data.get('password', '')
        if not password:
            raise forms.ValidationError(_('Not is password'))
        return password


# User login form
class UserLoginForm(forms.Form):
    # username field
    username = forms.CharField(max_length=150, required=True, label=_('Username'),
                               validators=[],
                               widget=forms.TextInput(attrs={'class': 'form-control form-control-inline'}))
    # password field
    password = forms.CharField(max_length=32, required=True, label=_('Password'),
                               validators=[],
                               widget=forms.PasswordInput(attrs={'class': 'form-control form-control-inline'}))



