from django.shortcuts import render
from .models import Expense


def home_page(request):
	return render(request, 'bestoon/home.html', {'objs': Expense.objects.all })

