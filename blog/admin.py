from django.contrib import admin
from .models import UserDetails


# Register your models here.
class UserDetailsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name','course', 'email', 'mobile', 'age', 'images')

admin.site.register(UserDetails, UserDetailsAdmin)


