from django.urls import path
from .views import HomePage


app_name = 'bestoon'
urlpatterns = [
	
	path('', HomePage.as_view(), name='home'),
	
]

