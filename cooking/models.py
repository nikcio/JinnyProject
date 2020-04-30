from django.db import models
from django.db.models.signals import post_delete
from django.dispatch import receiver
from django.urls import reverse
from django.utils.text import slugify
from django.contrib.auth.models import User
import re


# class Author(models.Model):
#     name = models.CharField(max_length=255, null=True)
#     active = models.BooleanField(null=True)
#     date = models.DateField(auto_now=True, null=True)
#
#     def __str__(self):
#         return self.name


def get_recipe_image(instance, filename):
    return 'media/jinny_cooking/img/recipes/{0}/{1}'.format(instance.title, filename)


class Recipe(models.Model):
    title = models.CharField(max_length=255, null=True, verbose_name="Title", unique=True)
    date = models.DateField(auto_now=True, null=True, verbose_name="Date")
    author = models.ForeignKey(User, verbose_name="Author", on_delete=models.SET_NULL, null=True, blank=True)
    video = models.URLField(verbose_name="Video(optional)", max_length=1084, null=True, blank=True)
    description = models.TextField(verbose_name="Description", null=True)
    image = models.ImageField(upload_to=get_recipe_image, verbose_name="Cover image", null=True)
    slug = models.SlugField(null=True, blank=True)
    published = models.BooleanField(null=True, default=False)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Recipe, self).save(*args, **kwargs)
    
    def get_absolute_url(self):
        return reverse('recipe-detail', kwargs={'slug': self.slug})

    def get_keywords(self):
        o = re.sub(r'[^A-Za-z0-9]+', ', ', self.title)
        return re.sub(r'[^A-Za-z0-9]+$', '', o)


@receiver(post_delete, sender=Recipe)
def delete_recipe_image(sender, instance, **kwargs):
    instance.image.delete(False)


class About(models.Model):
    title = models.CharField(max_length=255, null=True)
    description = models.TextField(null=True)

    def __str__(self):
        return "About"


class Frontpage(models.Model):
    title = models.CharField(max_length=255, null=True)
    subtitle = models.CharField(max_length=255, null=True)
    recipe_title = models.CharField(max_length=255, null=True)
    button_title = models.CharField(max_length=255, null=True)

    def __str__(self):
        return "Frontpage"


class ViewAll(models.Model):
    title = models.CharField(max_length=255, null=True)

    def __str__(self):
        return "Recipes"


class NavItem(models.Model):
    title = models.CharField(max_length=255, null=True)
    link = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.title


class Social(models.Model):
    SOCIALS = [
        ('linkedin', "LinkedIn"),
        ('youtube', "Youtube"),
        ('instagram', "Instagram"),
        ('discord', "Discord"),
        ('twitch', "Twitch"),
        ('twitter', "Twitter"),
        ('facebook', "Facebook"),
    ]

    type = models.CharField(max_length=255, null=True, unique=True, choices=SOCIALS)
    link = models.URLField(max_length=1084, null=True)

    def __str__(self):
        return self.type.capitalize()


class Navigation(models.Model):
    items = models.ManyToManyField(NavItem)

    def __str__(self):
        return "Navigation"
