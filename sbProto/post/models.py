from django.db import migrations, models
from django.contrib.auth.models import User
# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    TimePublished = models.DateTimeField()
    image = models.ImageField(upload_to='files/images', default='default.png')

    def __str__(self):
        return self.title + " / " + str(self.author) + " / " + str(self.TimePublished)
