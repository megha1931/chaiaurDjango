from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Recipe(models.Model):
    #user = models.ForeignKey(User, on_delete=models.)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    recipe_name = models.CharField(max_length=100)
    recipe_description = models.TextField()
    recipe_img = models.ImageField(upload_to="recipe")
    recipe_view_count = models.IntegerField(default=1)
    def __str__(self):
        return self.recipe_name
