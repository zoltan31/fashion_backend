from django.db import models

class User(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.TextField(default='user')
    #TODO: typo
    class Meta:
        ordering = ['created']

class Cloth(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    date_of_purchase = models.DateTimeField()
    style = models.TextField()
    type = models.TextField()
    class Meta:
        ordering = ['created']
