from django.db import models
from account.models import User
from extensions.utils import jalali_converter
from django.utils import timezone
from django.urls import reverse



class Income(models.Model):
	title = models.CharField(max_length=150, verbose_name='عنوان')
	amount = models.BigIntegerField(verbose_name='درامد')
	date = models.DateTimeField(auto_now_add=True)
	user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)


	def get_absolute_url(self):
		return reverse('account:home')


	def jdate(self):
		return jalali_converter(self.date)


	def __str__(self):
		return '{}-{}-{}'.format(self.title, self.amount, self.date)


	class Meta:
		verbose_name='درامد'
		verbose_name_plural='درامدها'


class Expense(models.Model):
	title = models.CharField(max_length=150, verbose_name='عنوان')
	amount = models.BigIntegerField(verbose_name='خرج')
	date = models.DateTimeField(auto_now_add=True)
	user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

	def jdate(self):
		return jalali_converter(self.date)

	def __str__(self):
		return '{}-{}-{}'.format(self.title, self.amount, self.date)



	def get_absolute_url(self):
		return reverse('account:home')	


	class Meta:
		verbose_name='خرج'
		verbose_name_plural='خرج ها'


