from django.db import models

class Post(models.Model):
    title = models.CharField(max_length = 70)
    description = models.TextField()
    slug = models.SlugField(max_length = 40)

    def __str__(self):
        return self.slug