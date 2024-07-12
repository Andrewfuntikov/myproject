from django.db import models

from django.urls import reverse


# Create your models here.
class Articles(models.Model):
    title = models.CharField(max_length=120)
    post = models.TextField()
    date = models.DateTimeField()
    image = models.ImageField(upload_to='img_dir/', blank=True, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('article_detail', args=[str(self.id)])
