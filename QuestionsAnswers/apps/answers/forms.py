from django import forms
from .models import Answer


# create answer form
class CreateAnswerForm(forms.ModelForm):

    class Meta:
        model = Answer
        fields = ('text', )
        widgets = {
            'text': forms.Textarea(attrs={'class': 'question-text'}),
        }


# update answer form
class UpdateAnswerForm(forms.ModelForm):

    class Meta:
        model = Answer
        fields = ('text', )
        widgets = {
            'text': forms.Textarea(attrs={'class': 'question-text'}),
        }
