from django.db import models

# Create your models here.
class News_post(models.Model):
  title = models.CharField(max_length=150)
  author = models.CharField(max_length=30, default='Anonim')
  text = models.TextField()

  def __str__(self):
    return self.title