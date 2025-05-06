from django.db import models
from django.core.validators import MinLengthValidator
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.core.validators import MinValueValidator, MaxValueValidator

from decimal import Decimal

# Create your models here.


class SearchFilter(models.Model):
    caption = models.CharField(max_length=20)

    def __str__(self):
        return self.caption


class Recipe(models.Model):
    title = models.CharField(max_length=150)
    excerpt = models.CharField(max_length=200)
    image = models.ImageField(upload_to="recipes", null=True)
    date = models.DateField(auto_now=True)
    slug = models.SlugField(unique=True, db_index=True)
    procedure = models.TextField(validators=[MinLengthValidator(10)])
    no_of_ingredients = models.IntegerField(default=0, editable=False)
    search_filter = models.ManyToManyField(SearchFilter)


    def __str__(self):
        return self.title
    
class Ingredients(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name="ingredients")
    name = models.CharField(max_length=50)
    amount = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name} - {self.amount}"

@receiver(post_save, sender=Ingredients)
def update_no_of_ingredients_on_save(sender, instance, **kwargs):
    recipe = instance.recipe
    recipe.no_of_ingredients = recipe.ingredients.count()
    recipe.save()

@receiver(post_delete, sender=Ingredients)
def update_no_of_ingredients_on_delete(sender, instance, **kwargs):
    recipe = instance.recipe
    recipe.no_of_ingredients = recipe.ingredients.count()
    recipe.save()


class Comment(models.Model):
    username = models.CharField(max_length=120)
    rating = models.DecimalField(
        max_digits=2, 
        decimal_places=1, 
        validators=[
            MinValueValidator(Decimal('0.0')), 
            MaxValueValidator(Decimal('5.0'))
        ]
    )
    text = models.TextField(max_length=400)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name="comments")