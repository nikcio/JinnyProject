from django.contrib import admin
from cooking import models

admin.site.register(models.Author)
admin.site.register(models.Recipe)
