from django.contrib import admin
from .models import Post

# this allows us to see Post in admin page -tian
admin.site.register(Post)
