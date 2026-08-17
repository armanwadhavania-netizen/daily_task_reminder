from django.contrib import admin
from .models import Task,Reminder


admin.site.register(Task)
admin.site.register(Reminder)