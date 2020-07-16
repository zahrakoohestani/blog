from django.urls import path
from .views import home, detail

app_name = "Blog"
urlpatterns = [
    path('', home, name="home"),
    path('article/<slug:slug>', detail, name="detail"),
]
