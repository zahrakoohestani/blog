from django.contrib import admin
from .models import article

class article_admin(admin.ModelAdmin):
    list_display = (
        'title',
        'slug',
        'published_date',
        'status',            
    )

    list_filter = (
        'published_date',
        'status', 
    )

    search_fields = (
        'title',
        'description',
    )

    prepopulated_fields = {
        'slug' : ('title',)
    }

    ordering = [
        '-status',
        '-published_date',
        ]

admin.site.register(article, article_admin)