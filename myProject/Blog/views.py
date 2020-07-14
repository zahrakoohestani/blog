from django.shortcuts import render
from .models import article

def home(request):
    context = {
        'articles' : article.objects.filter(status='p')
    }
    return render(request, "Blog/home.html", context)

