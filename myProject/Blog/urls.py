from django.urls import path
from .views import home

app_name = "Blog"
urlpatterns = [
    path('', home, name="home"),
]
