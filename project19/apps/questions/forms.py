from django import forms
from .models import Question


# create model form Question
class CreateQuestionForm(forms.ModelForm):

    class Meta:
        model = Question
        fields = ('title', 'text')
        widgets = {}


# update model form question
class UpdateQuestionForm(forms.ModelForm):

    class Meta:
        model = Question
        fields = ('title', 'text')
        widgets = {}
