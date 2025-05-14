from django.db import models

# Create your models here.

class Technology(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name


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
    modal_image = models.ImageField(upload_to='projects/modal/', null=True, blank=True)
    github_link = models.URLField()
    filter_tag = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    technologies = models.ManyToManyField(Technology)

    def save(self, *args, **kwargs):
        if not self.modal_image:
            self.modal_image = self.image
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
