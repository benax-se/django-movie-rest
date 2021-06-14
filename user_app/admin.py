from django.contrib import admin
from .models import UserProfile, UserPosition


class UsersAtPositionInline(admin.TabularInline):
    model = UserProfile


@admin.register(UserPosition)
class UserPositionAdmin(admin.ModelAdmin):
    """Должности"""
    list_display = ("name",)
    inlines = [UsersAtPositionInline]

    def get_position(self, obj):
        return obj.position.name

    def get_user(self, obj):
        return obj.user.email

    get_position.short_description = "Должность"
    get_user.short_description = "Пользователь"


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    """Профиль пользователя"""
    list_display = ("get_user", "first_name", "last_name", "get_position")
    list_display_links = ("first_name",)

    fieldsets = (
        (None, {
            "fields": (("user",),)
        }),
        (None, {
            "fields": (("first_name", "last_name"),)
        }),
        (None, {
            "fields": (("position", ),)
        }),
    )

    def get_position(self, obj):
        return obj.position.name

    def get_user(self, obj):
        return obj.user.email

    get_position.short_description = "Должность"
    get_user.short_description = "Пользователь"
# Register your models here.
