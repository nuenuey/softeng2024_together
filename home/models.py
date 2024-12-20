from django.db import models


# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()

    head_image = models.ImageField(upload_to='blog/images/%Y/%m/%d/', blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f'[{self.pk}] {self.title}'

    def get_absolute_url(self):
        return f'/{self.pk}/'

class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()
    operating_hours = models.TextField()
    main_menu = models.TextField()
    description = models.TextField()

    def __str__(self):
        return self.name
