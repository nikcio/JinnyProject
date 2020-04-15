from django.forms import ModelForm
from cooking import models


class RecipeFormSet(ModelForm):
    def __init__(self, *args, **kwargs):
        super(RecipeFormSet, self).__init__(*args, **kwargs)
        self.fields['author'].queryset = models.Author.objects.filter(active=True)

    class Meta:
        model = models.Recipe
        fields = ['title', 'author', 'video', 'description', 'image']


class AuthorFormSet(ModelForm):
    class Meta:
        model = models.Author
        fields = ['name']
