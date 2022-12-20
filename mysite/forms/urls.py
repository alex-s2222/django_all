from django.urls import path
from . import views
from forms.views import UserFormView, UserEditFormView

urlpatterns = [
	path('register', UserFormView.as_view()),
	path('<int:profile_id>/edit/', UserEditFormView.as_view())
]