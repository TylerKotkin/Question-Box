from django import forms
from django.contrib.auth.models import User
from inquest.models import Question, Answer


class AnswerForm(forms.ModelForm):

    class Meta:
        model = Answer
        fields = ['text']


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'first_name', 'last_name']


class QuestionForm(forms.ModelForm):

    class Meta:
        model = Question
        fields = ['title', 'text']
