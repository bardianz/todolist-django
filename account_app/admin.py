from django.contrib import admin
from account_app.models import Profile
from django.contrib.auth.admin import UserAdmin

# Register your models here.


# class ProfileAdmin(UserAdmin):
#         list_display = (
#         'username', 'email', 'firstname', 'lastname', 'is_staff',
#         )

# admin.site.register(Profile, ProfileAdmin)
admin.site.register(Profile)