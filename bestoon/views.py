from django.views.generic import ListView
from .models import Expense, Income
from account.models import User
from django.db.models import Sum, Count
from django.http import JsonResponse


class HomePage(ListView):
	model = User
	template_name = 'bestoon/home.html'


	def get_context_data(self):
		context = super().get_context_data()
		user = self.request.user
		context['incomesum'] = Income.objects.filter(user=user).aggregate(Sum('amount'))
		context['incomecount'] = Income.objects.filter(user=user).aggregate(Count('title'))
		context['expensesum'] = Expense.objects.filter(user=user).aggregate(Sum('amount'))
		context['expensecount'] = Expense.objects.filter(user=user).aggregate(Count('title'))
		context['difference'] = Income.objects.filter(user=user).aggregate(
			Sum('amount'))['amount__sum'] - Expense.objects.filter(user=user).aggregate(
			Sum('amount'))['amount__sum']
		return context


