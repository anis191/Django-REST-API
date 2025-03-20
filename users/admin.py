from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from users.models import User

#Here we register the 'users' model in django admin panel,but we do it with our needed customization
class CustomUserAdmin(UserAdmin):
    model = User
    # Define the fields to be displayed in the admin panel
    list_display = ('email', 'first_name', 'last_name', 'is_active')
    # We need to add list_filter():
    list_filter = ('is_staff','is_active')
    # We need to add fieldsets():
    fieldsets = (
        (None, {'fields':('email','password')}),
        ('Personal Info', {'fields':('first_name','last_name','address','phone_number')}),
        ('Permissions', {'fields':('is_staff','is_active','is_superuser','groups','user_permissions')}),
        ('Important Dates', {'fields':('last_login','date_joined')})
    )
    add_fieldsets=(
        (None, {
            'classes':('wide',),
            'fields':('email','password1','password2','is_staff','is_active')
        }),
    )
    search_fields = ('email',)
    ordering = ('email',)

#Now register the model:
admin.site.register(User, CustomUserAdmin)