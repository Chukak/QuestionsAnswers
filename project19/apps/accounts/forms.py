from django import forms
from django.forms import ModelForm
from django.forms.widgets import ClearableFileInput
from .models import User
from django.utils.translation import gettext_lazy as _


# custom image field widget
class CustomImageFieldWidget(ClearableFileInput):
    # set template for fileinput widget
    template_name = 'specials/clearable_file_input.html'


# Update user form
class UserUpdateForm(ModelForm):
    # password
    password = forms.CharField(max_length=32, help_text=_('32 character or fewer.'),
                               required=True, label=_('Password'),
                               widget=forms.PasswordInput(attrs={'class': 'form-control-inline'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'avatar')
        # set widgets with attrs
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control form-control-inline'}),
            'email': forms.TextInput(attrs={'class': 'form-control form-control-inline'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control form-control-inline'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control form-control-inline'}),
            'avatar': CustomImageFieldWidget(),
        }

    # override clean method for check password
    def clean_password(self):
        password = self.cleaned_data.get('password', '')
        if not self.instance.check_password(password):
            raise forms.ValidationError(_('Invalid password'))
        return password


