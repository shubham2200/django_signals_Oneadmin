from django.contrib import admin
from .models import *
from django.contrib.auth.models import User

# Register your models here.


# class authenticate_Admin(admin.ModelAdmin):
#     list_display = ('user_name', 'date_time', 'recordstype')
# admin.site.register(authenticate_history , authenticate_Admin)
admin.site.unregister(User)
class auth_admin(admin.TabularInline):
    model = authenticate_history

class AuthorAdmin(admin.ModelAdmin):
    inlines = [
        auth_admin,
    ]
admin.site.register(User , AuthorAdmin)
