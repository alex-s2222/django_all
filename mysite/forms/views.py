from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from django.shortcuts import render
from forms.forms import UserForm
from forms.models import User
# Create your views here.

class UserFormView(View):

	def get(self, request):
		user_form = UserForm()
		return render(request, 'forms/register.html', context={'user_form': user_form})

	def post(self, request):
		user_form = UserForm() 

		if user_form.is_valid():
			# совершаем какую бизнес логику
			# к примеру заносим в базу данных 
			User.objects.create(**user_form.cleaned_data)
			return HttpResponseRedirect('/')
		return render(request, 'forms/register.html', context={'user_form': user_form})


class UserEditFormView(View):
	 
	def get(self, request, profile_id):
		user = User.objects.get(id=profile_id)
		user_form = UserForm(instance=user)
		return render(request, 'forms/edit.html', context={'user_form': user_form, 'profile_id': profile_id})

	def post(self, request, profile_id):
		user = User.objects.get(id=profile_id)
		user_form = UserForm(request.POST, instance=user)

		if user_form.is_valid():
			user.save()
		return render(request, 'forms/edit.html', context={'user_form': user_form, 'profile_id': profile_id})