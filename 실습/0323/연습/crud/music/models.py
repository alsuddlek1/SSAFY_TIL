from django.db import models

# Create your models here.
class Music(models.Model):
    singer = models.CharField(max_length=10)
    title = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # def __str__(self):
        # return f'{self.id} 노래제목 : {self.title}'