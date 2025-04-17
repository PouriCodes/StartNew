from django.urls import path
from website.views import *
# from django.urls import path

urlpatterns = [
    path('', index_view),  # Add this line to include the test view
    path('about/', about_view),  # Add this line to include the test view
    path('contact/', contact_view)
]
