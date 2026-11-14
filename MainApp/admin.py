from django.contrib import admin

# Register your models here.
from .models import Topic

admin.site.register(Topic)

# importing entry
from .models import Entry
admin.site.register(Entry)