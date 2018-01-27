from django import forms
from .models import Question


# create model form Question
class CreateQuestionForm(forms.ModelForm):

    class Meta:
        model = Question
        fields = ('title', 'text')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control form-width'}),
            'text': forms.Textarea(attrs={'class': 'question-text'}),
        }


# update model form question
class UpdateQuestionForm(forms.ModelForm):

    class Meta:
        model = Question
        fields = ('title', 'text')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control form-width'}),
            'text': forms.Textarea(attrs={'class': 'question-text'}),
        }
