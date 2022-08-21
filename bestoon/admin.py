from django.contrib import admin
from .models import Income, Expense



class IncomeAdmin(admin.ModelAdmin):
	search_fields = ('title', )
	list_display = ('title', 'amount', 'jdate', 'user')
	list_filter = ('amount', 'date')
	ordering = ['-amount']


admin.site.register(Income, IncomeAdmin)


class ExpenseAdmin(admin.ModelAdmin):
	search_fields = ('title', )
	list_display = ('title', 'amount', 'jdate', 'user')
	list_filter = ('amount', 'date')
	ordering = ['-amount']
	

admin.site.register(Expense, ExpenseAdmin)
