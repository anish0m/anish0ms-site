from django.db import models

# Create your models here.

class Project(models.Model):
    CATEGORY_CHOICES = [
        ('web-dev', 'Development'),
        ('web-des', 'Research'),
        ('dig-mar', 'Machine Learning'),
    ]

    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=300)
    description = models.TextField()
    image = models.ImageField(upload_to='projects/')
    github_link = models.URLField()
    filter_tag = models.CharField(max_length=20, choices=CATEGORY_CHOICES)

    def __str__(self):
        return self.title
