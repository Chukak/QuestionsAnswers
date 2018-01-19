from django import forms
from django.forms import ModelForm
from ..accounts.models import User
from django.utils.translation import gettext_lazy as _


class UserCreationForm(ModelForm):
    password = forms.CharField(max_length=32, help_text=_('Required. 32 character or fewer.'),
                               required=True, label=_('Password'),
                               widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'avatar')

    def clean_password(self):
        password = self.cleaned_data.get('password', '')
        if not password:
            raise forms.ValidationError('Not is password')
        return password


class UserLoginForm(forms.Form):
    username = forms.CharField(max_length=150, required=True, label=_('Username'),
                               validators=[],
                               error_messages={
                                   'invalid': _('No such user.'),
                               },
                               widget=forms.TextInput())
    password = forms.CharField(max_length=32, required=True, label=_('Password'),
                               validators=[],
                               error_messages={
                                   'invalid': _('Invalid password.'),
                               },
                               widget=forms.PasswordInput())


