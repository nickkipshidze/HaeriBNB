from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm
from . import models

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = models.User
        fields = [
            "id", "username", "profile_picture", "first_name", "last_name", "password", "email", "birthday", "country_code", "phone_number", "goverment_id", "address", "emergency_contact"
        ]

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm

    list_display = (
        "id", "username", "first_name", "last_name", "email", "phone_number"
    )

    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (None, {"fields": ("profile_picture", "first_name", "last_name", "email", "birthday", "country_code", "phone_number", "goverment_id", "address", "emergency_contact")}),
        (
            None,
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (None, {"fields": ("last_login", "date_joined")}),
    )

    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "username", "first_name", "last_name", "profile_picture", "password1", "password2", "email", "birthday", "country_code", "phone_number", "goverment_id", "address", "emergency_contact"
                ),
            },
        ),
    )

admin.site.register(models.User, CustomUserAdmin)