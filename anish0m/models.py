from django.db import models

# Create your models here.


class Contents(models.Model):
    name = models.CharField(max_length=100)  # Name of the app
    description = models.TextField()  # Short description of the app
    icon = models.ImageField(upload_to="contents/icons/")  # Icon for the app
    url_name = models.CharField(max_length=100)  # URL name for the app's starting page

    def __str__(self):
        return self.name