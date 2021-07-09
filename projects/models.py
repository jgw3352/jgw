from django.db import models

# Create your models here.



class NewModel(models.Model):
    Text = models.CharField(max_length=255, null=False)

