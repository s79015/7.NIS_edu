from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# Create your forms here.

LANGUAGE_CHOICES= [
    ('ru', 'Руский'),
    ('kz', 'Казахский'),
    ]

class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)
	language = forms.CharField(label='Оқу тілін таңдаңыз/Выберите язык обучения', widget=forms.Select(choices=LANGUAGE_CHOICES))

	class Meta:
		model = User
		fields = ("username", "language", "email", "password1", "password2")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		user.language = self.cleaned_data['language']
		if commit:
			user.save()
		return user