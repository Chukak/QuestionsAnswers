from django import forms
from .models import Answer


# create answer form
class CreateAnswerForm(forms.ModelForm):

    class Meta:
        model = Answer
        fields = ('text', )
        widgets = {}


# update answer form
class UpdateAnswerForm(forms.ModelForm):

    class Meta:
        model = Answer
        fields = ('text', )
        widgets = {}
