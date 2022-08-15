from django.urls import path
from .views import home_page


app_name = 'bestoon'
urlpatterns = [
	
	path('', home_page, name='home'),
]

