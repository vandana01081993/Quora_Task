from django import forms
from .models import Question, Answer
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'})
    )

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['post_question']

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['content']

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
