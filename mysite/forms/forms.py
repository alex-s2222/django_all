from django import forms
from django.core.exceptions import ValidationError
import datetime
from forms.models import User


	# тестовый способ оставил на память 
# class UserForm(forms.Form):
	# username = forms.CharField()
	# password = forms.CharField(min_length=5)
	# first_name = forms.CharField()
	# second_name = forms.CharField()
	# last_name = forms.CharField()
	# email = forms.EmailField()
	# birthday = forms.DateField()

	# def clean_birthday(self):
	# 	data = self.cleaned_birthday['birthday']
	# 	today = datetime.time.today()
	# 	year_delta = (today - data).days / 365
	# 	if year_delta < 18: 
	# 		raise ValidationError('Регистрироваться могут только лица старше 18 лет')
	# 	return data

	# def clean(self):
	# 	cleaned_data = super(UserForm, self).clean()
	# 	first_name = cleaned_data.get('first_name')
	# 	last_name = cleaned_data.get('last_name')
	# 	if first_name == 'Ivan' and last_name == 'Ivanov':
	# 		msg = 'error Ivan not cant registrations' 
	# 		self.add_error('first_name', msg)
	# 		self.add_error('last_name', msg)\

class UserForm(forms.ModelForm):

	class Meta:
		model = User
		fields = '__all__'