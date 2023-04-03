from django.conf import settings
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from manager.models import Task, Tag, User

admin.site.register(Tag)
admin.site.register(Task)


@admin.register(User)
class UserAdmin(UserAdmin):
    pass
