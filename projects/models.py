from django.db import models


# Create your models here.


class NewModel(models.Model):
    text = models.CharField(max_length=255, null=False)

# makemigrations = model변경을 감지하고 변경사항을 반영할 파일 생성
