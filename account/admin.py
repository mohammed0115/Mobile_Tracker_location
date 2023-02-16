from django.contrib import admin

# Register your models here.
from django.contrib import admin

# Register your models here.from django.contrib import admin
from import_export.admin import ImportExportActionModelAdmin
# Register your models here.
# Register your models here.
from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = User
        fields = ('email','password','phone_number','full_name')


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = User
        fields = ('email','password','phone_number','full_name')

class CustomUserAdmin(UserAdmin):
    
    
    fieldsets = (
        (None, {'fields': ('email', 'password','phone_number','full_name','National_number',
                    'address','date_of_birth','gender','user_type','Business_name')}),
       ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser',
                                   'groups','user_permissions'
                                      )}),
      
    )
    filter_horizontal=('groups','user_permissions',)
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)
    
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User
    list_display = ('email', 'is_staff', 'is_active','phone_number','full_name','National_number',
                    'address','date_of_birth','gender','user_type','Business_name')
    list_filter = ('email', 'is_staff', 'is_active','user_type')
    def get_fieldsets(self, request, obj=None):
        if obj:
            return self.fieldsets
        else:
            return self.add_fieldsets


admin.site.register(User, CustomUserAdmin)