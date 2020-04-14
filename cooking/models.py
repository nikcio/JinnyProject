from django.db import models
from django.db.models.signals import post_delete
from django.dispatch import receiver
from django.urls import reverse
from autoslug import AutoSlugField


class Author(models.Model):
    name = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.name


def get_recipe_image(instance, filename):
    return 'static/jinny_cooking/img/recipes/{0}/{1}'.format(instance.title, filename)


class Recipe(models.Model):
    title = models.CharField(max_length=255, null=True, verbose_name="Title", unique=True)
    date = models.DateField(auto_now=True, null=True, verbose_name="Date")
    author = models.ForeignKey(Author, verbose_name="Author", on_delete=models.CASCADE, null=True)
    video = models.URLField(verbose_name="Video", max_length=1084, null=True, blank=True)
    description = models.TextField(verbose_name="Description", null=True)
    image = models.ImageField(upload_to=get_recipe_image, verbose_name="Image", null=True)
    slug = AutoSlugField(populate_from=title, unique=True, null=True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('recipe-detail', kwargs={'slug': self.slug})


@receiver(post_delete, sender=Recipe)
def delete_recipe_image(sender, instance, **kwargs):
    instance.image.delete(False)
