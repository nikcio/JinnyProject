from django.contrib import admin
from cooking import models


class RecipeAdmin(admin.ModelAdmin):
    list_display = ('title', 'published', 'date')


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'active', 'date')


admin.site.register(models.Author, AuthorAdmin)
admin.site.register(models.Recipe, RecipeAdmin)
admin.site.register(models.About)
admin.site.register(models.Frontpage)
admin.site.register(models.NavItem)
admin.site.register(models.Navigation)
admin.site.register(models.ViewAll)
admin.site.register(models.Social)