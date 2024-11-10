from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import UserProfile

class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = 'Perfiles de Usuario'

class CustomUserAdmin(BaseUserAdmin):
    inlines = (UserProfileInline,)
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'get_user_type')
    list_select_related = ('userprofile',)

    def get_user_type(self, instance):
        return instance.userprofile.get_user_type_display()
    get_user_type.short_description = 'Tipo de Usuario'

    def save_model(self, request, obj, form, change):
        # Primero, guarda el usuario
        super().save_model(request, obj, form, change)
        if change:
            # Si estamos cambiando un usuario existente, asegurarse de que el perfil se guarde
            try:
                profile = UserProfile.objects.get(user=obj)
                profile.save()
            except UserProfile.DoesNotExist:
                UserProfile.objects.create(user=obj)
        else:
            # Crear un nuevo perfil solo si no existe
            UserProfile.objects.get_or_create(user=obj)

    def delete_model(self, request, obj):
        # Asegurarse de que se elimine el perfil del usuario cuando el usuario se elimina
        try:
            profile = UserProfile.objects.get(user=obj)
            profile.delete()
        except UserProfile.DoesNotExist:
            pass
        super().delete_model(request, obj)

admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
admin.site.register(UserProfile)
