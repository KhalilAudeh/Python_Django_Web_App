from django.contrib import admin
from .models import Post

# Register your models here.
# adding this will let us view on localhost/admin the vacations list
admin.site.register(Post)
