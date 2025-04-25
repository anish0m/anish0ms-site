from django.db import models
from django.core.validators import MinLengthValidator
from django.core.exceptions import ValidationError
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

# Create your models here.


class Tag(models.Model):
    caption = models.CharField(max_length=20)

    def __str__(self):
        return self.caption


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.full_name()
    
class Book(models.Model):
    title = models.CharField(max_length=150)
    excerpt = models.CharField(max_length=200)
    image = models.ImageField(upload_to="books", null=True)
    date = models.DateField(auto_now=True)
    slug = models.SlugField(unique=True, db_index=True)
    content = models.TextField(validators=[MinLengthValidator(10)])
    author = models.ForeignKey(
        Author, null=True, on_delete=models.SET_NULL, related_name="books")
    no_of_books = models.IntegerField(default=0, editable=False)
    starter_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    complete_price = models.DecimalField(max_digits=10, decimal_places=2)
    ultimate_price = models.DecimalField(max_digits=10, decimal_places=2)
    tags = models.ManyToManyField(Tag)


    def __str__(self):
        return self.title
    
class SubBook(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="sub_books")
    title = models.CharField(max_length=150)
    description = models.TextField(validators=[MinLengthValidator(10)], null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.description and self.book:
            self.description = self.book.content
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

@receiver(post_save, sender=SubBook)
def update_no_of_books_on_save(sender, instance, **kwargs):
    book = instance.book
    book.no_of_books = book.sub_books.count()
    book.save()

@receiver(post_delete, sender=SubBook)
def update_no_of_books_on_delete(sender, instance, **kwargs):
    book = instance.book
    book.no_of_books = book.sub_books.count()
    book.save()