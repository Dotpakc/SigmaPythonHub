from django.contrib import admin

from .models import Post

# Register your models here.
admin.site.register(Post) # Це потрібно для відображення моделі в адмінці

