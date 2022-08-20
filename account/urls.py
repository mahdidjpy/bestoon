from django.urls import path 
from .views import ( 
Profile, Home, Login, IncumSubmit,
 ExpenseSubmit, UpdateIncome, UpdateExpense,
 DeleteExpense, DeleteIncome, Registration,
 activate, ChangePassword 
  )
from django.contrib.auth.views import LogoutView, PasswordChangeDoneView


app_name = 'account'
urlpatterns= [
	path('',Home.as_view(), name='home'),
	path('create/income/', IncumSubmit.as_view(), name='create_income'),
	path('create/expense/', ExpenseSubmit.as_view(), name='create_expense'),
	path('profile/', Profile.as_view(), name='profile'),
	path('income/update/<int:pk>', UpdateIncome.as_view(), name='update_income'),
	path('expense/update/<int:pk>', UpdateExpense.as_view(), name='update_expense'),
	path('delete/income/<int:pk>', DeleteIncome.as_view(), name='delete_income'),
	path('delete/expense/<int:pk>', DeleteExpense.as_view(), name='delete_expense'),
	path('login/', Login.as_view(), name='login'),
	path('logout/', LogoutView.as_view(), name='logout'),
	path('signup/', Registration.as_view(), name='signup'),
	path('activate/<str:uidb64>/<str:token>',activate, name='activate'),
	path('password_change/',ChangePassword.as_view(), name='password_change'),
	path('password_change/done/',PasswordChangeDoneView.as_view(), name='password_change_done')
	

]



