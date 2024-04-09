from django.contrib import admin
from django.contrib.auth.models import Group, User

from .models import TgUser


admin.site.unregister(Group)
admin.site.unregister(User)


@admin.register(TgUser)
class TgUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'nickname', 'first_name', 'last_name', )
    list_display_links = ('id', 'nickname')
    empty_value_display = 'empty'


