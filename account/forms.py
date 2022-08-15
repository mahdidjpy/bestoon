from django import forms
from .models import User
from bestoon.models import Income, Expense
from django.contrib.auth.forms import UserCreationForm


class ProfileForm(forms.ModelForm):


	def __init__(self, *args, **kwargs ):
		user = kwargs.pop('user')
		super().__init__(*args, **kwargs)
		if not user.is_superuser:
			self.fields['username'].disabled = True

	class Meta:

		model = User 
		fields = ['username', 'email', 'first_name', 'last_name']
		



class IncomeForm(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		user = kwargs.pop('user')

		super().__init__(*args, **kwargs)	

		if not user.is_superuser:
			self.fields['user'].disabled = True
			


	class Meta:
		model = Income
		fields = ['title', 'amount', 'user']



class ExpenseForm(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		user = kwargs.pop('user')
		super().__init__(*args, **kwargs)

		if not user.is_superuser:
			self.fields['user'].disabled = True
			


	class Meta:
		model = Expense
		fields = ['title', 'amount', 'user']




class Signup(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text='Required')
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

        