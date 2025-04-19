from django.urls import path
from website.views import *
# from django.urls import path

app_name = 'website'

# from .views import index_view, about_view, contact_view  # Import your views here
urlpatterns = [
    path('', index_view,name='index'),  # Add this line to include the test view
    path('about/', about_view,name='about'),  # Add this line to include the test view
    path('contact/', contact_view,name='contact'),
    
]
