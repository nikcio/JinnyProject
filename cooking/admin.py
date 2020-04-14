from django.contrib import admin
from cooking import models

admin.site.register(models.Author)
admin.site.register(models.Recipe)
admin.site.register(models.About)
admin.site.register(models.Frontpage)
admin.site.register(models.NavItem)
admin.site.register(models.Navigation)
admin.site.register(models.ViewAll)
admin.site.register(models.Social)