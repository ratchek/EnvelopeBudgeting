from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserChangeForm, CustomUserCreationForm
from .models import CustomUser, Envelope, Fill, Transaction


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = [
        "username",
        "email",
        "id",
    ]


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Envelope)
admin.site.register(Transaction)
admin.site.register(Fill)
