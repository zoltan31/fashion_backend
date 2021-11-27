from django.db import models

class User(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.TextField(default='user')
    #TODO: typo
    class Meta:
        ordering = ['created']

class Cloth(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.TextField()
    #TODO: Set up the correct PATH
    image = models.ImageField(upload_to='media/images/')
    date_of_purchase = models.DateTimeField()
    style = models.TextField()
    type = models.TextField()
    class Meta:
        ordering = ['created']

class Season(models.Model):
  name = models.TextField()
  start_date = models.DateTimeField()
  active = models.BooleanField()