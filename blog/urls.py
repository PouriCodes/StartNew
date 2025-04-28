from django.urls import path
from blog.views import *
# from django.urls import path

app_name = "blog"

# from .views import index_view, about_view, contact_view  # Import your views here
urlpatterns = [
    path("", blog_view, name="index"),  # Add this line to include the test view
    path("<int:pid>", blog_single, name="single"),  # Add this line to include the test view
    path("category/<str:cat_name>", blog_view, name="category"),  # Add # Add this line to include the test view
    path("author/<str:author_username>", blog_view, name="author"),  # Add this line to include the test view
    path('test',test,name='test'),
]
