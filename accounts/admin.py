from django.contrib import admin
from .models import User
from .forms import CustomUserCreationForm
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
# Register your models here.
class UserModelAdmin(admin.ModelAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserCreationForm
    model = User
    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserModelAdmin
    # that reference specific fields on auth.User.
    list_display = ['id', 'username', 'email', 'tc', 'is_admin', 'is_superuser']
    list_filter = ['is_staff', 'is_superuser'] 
    fieldsets = [
        ('User Credentials', {"fields": ["email", "password"]}),
        ("Personal info", {"fields": ['username', 'tc']}),
        ("Permissions", {"fields": ["is_admin"]}),
    ]
    # add_fieldsets is not a standard ModelAdmin attribute. UserModelAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = [
        (
            None,
            {
                "classes": ["wide"],
                "fields": ["email", "username", "tc", "password1", "password2"],
            },
        ),
    ]
    search_fields = ["email", 'username']
    ordering = ["email",]
    filter_horizontal = []


    def tc(self, obj):
        return obj.tc

    def is_admin(self, obj):
        return obj.is_admin
    
admin.site.register(User,UserModelAdmin)
