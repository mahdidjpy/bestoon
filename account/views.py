from django.shortcuts import render
from django.views.generic import UpdateView, ListView, CreateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from bestoon.models import Income, Expense
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import User
from .forms import ProfileForm, IncomeForm, ExpenseForm, Signup
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.core.mail import EmailMessage
from django.contrib.auth.views import PasswordChangeView


class Home(LoginRequiredMixin, ListView):
	template_name = 'registration/home.html'
	model = Income

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		user = self.request.user 
		context['income'] =  Income.objects.filter(user=user)
		context['expense'] = Expense.objects.filter(user=user)
		return context



class Profile(LoginRequiredMixin, UpdateView):
	model = User
	template_name = 'registration/profile.html'
	success_url = reverse_lazy('account:profile')
	form_class = ProfileForm 
	

	def get_object(self):
		return User.objects.get(pk=self.request.user.pk)


	def get_form_kwargs(self):
		kwargs = super().get_form_kwargs()
		kwargs.update(
			{'user':self.request.user})	
		return kwargs


class UpdateIncome(LoginRequiredMixin, UpdateView):
	model = Income 
	form_class = IncomeForm
	template_name = 'registration/update.html'
	

	def get_initial(self):
		return {'user' : self.request.user}



	def get_form_kwargs(self):
		kwargs = super().get_form_kwargs()
		kwargs.update(
			{'user':self.request.user})	
		return kwargs
	

class UpdateExpense(LoginRequiredMixin, UpdateView):
	model = Expense 
	form_class = ExpenseForm
	template_name = 'registration/update.html'
	

	def get_initial(self):
		return {'user' : self.request.user}


	def get_form_kwargs(self):
		kwargs = super().get_form_kwargs()
		kwargs.update(
			{'user':self.request.user})	
		return kwargs


class Login(LoginView):
	template_name = 'registration/login.html'


class IncumSubmit(LoginRequiredMixin, CreateView):
	model = Income
	form_class = IncomeForm
	template_name = 'registration/create.html'


	def get_initial(self):
		return {'user' : self.request.user}


	def get_form_kwargs(self):
		kwargs = super().get_form_kwargs()
		kwargs.update(
			{'user':self.request.user})	
		return kwargs



class ExpenseSubmit(LoginRequiredMixin, CreateView):
	model = Expense
	form_class = ExpenseForm
	template_name = 'registration/create.html'
	


	def get_initial(self):
		return {'user' : self.request.user}


	def get_form_kwargs(self):
		kwargs = super().get_form_kwargs()
		kwargs.update(
			{'user':self.request.user})	
		return kwargs


class DeleteIncome(LoginRequiredMixin ,DeleteView):
	model = Income
	template_name = 'registration/delete.html'
	success_url = reverse_lazy('account:home')



class DeleteExpense(LoginRequiredMixin ,DeleteView):
	model = Expense
	template_name = 'registration/delete.html'
	success_url = reverse_lazy('account:home')	




class Registration(SuccessMessageMixin, CreateView):
	model = User
	template_name = 'registration/Signup.html'
	form_class = Signup
	success_url = reverse_lazy('account:profile')
	success_message = 'حساب کاربری با موفقیت ایجاد شد '


	def form_valid(self, form):
		super().form_valid(form)
		user = authenticate(self.request,
		 username=form.cleaned_data['username'],
		 password=form.cleaned_data['password1'])
		if user:
			user = form.save(commit=False)
			user.is_active = False
			user.save()
			current_site = get_current_site(self.request)
			mail_subject = 'فعال سازی حساب کاربری'
			message = render_to_string('registration/acc_active_email.html', {
			'user': user,
			'domain': current_site.domain,
			'uid': urlsafe_base64_encode(force_bytes(user.pk)),
			'token': account_activation_token.make_token(user),
			})
			to_email = form.cleaned_data.get('email')
			email = EmailMessage(
				mail_subject, message, to=[to_email]
			)
			email.send()
			return HttpResponse('.لطفا ایمیل خود را برای تکمیل فعال سازی حساب چک کنید ')
		else:
			return self.render_to_response(self.get_context_data(form=form))	



def activate(request, uidb64, token):
	try:
		uid = force_text(urlsafe_base64_decode(uidb64))
		user = User.objects.get(pk=uid)
	except (TypeError, ValueError, OverflowError, User.DoesNotExist):
		user = None
	if user is not None and account_activation_token.check_token(user, token):
		user.is_active = True
		user.save()
		return HttpResponse(' . حساب شما با موفقیت فعال شد <a href="../../login" > برای ورود کلیک کنید ')
	else:
		return HttpResponse('لینک نامعتر است')


class ChangePassword(PasswordChangeView):
    success_url = reverse_lazy('account:password_change_done')

