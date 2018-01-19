from django import forms
from django.forms import ModelForm
from .models import User
from django.utils.translation import gettext_lazy as _


# Update user form
class UserUpdateForm(ModelForm):
    # password
    password = forms.CharField(max_length=32, help_text=_('32 character or fewer.'),
                               required=True, label=_('Password'),
                               widget=forms.PasswordInput())
    # password repeat field
    password_repeat = forms.CharField(max_length=32, help_text=_('Repeat password.'),
                                      required=True, label=_('Repeat password'),
                                      widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'avatar')

    # override clean method for check password
    def clean(self):
        password = self.cleaned_data.get('password', '')
        repeat_password = self.cleaned_data.get('password_repeat', '')
        # if not password
        if not password or not repeat_password:
            raise forms.ValidationError(_('Enter a valid password.'))
        # if password and repeat password do not match
        if password != repeat_password:
            raise forms.ValidationError(_('Passwords do not match.'))
        return super().clean()
