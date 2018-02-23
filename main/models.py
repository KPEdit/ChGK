from django.db import models


class Article(models.Model):
    heading = models.CharField(max_length=100)
    description = models.TextField()
    time = models.DateTimeField(auto_created=True)
    picture = models.ImageField(upload_to='articles/')

    def __str__(self):
        return '%s' % self.heading
