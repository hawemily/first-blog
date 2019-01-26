from django.db import models
from django.conf import settings
from django.utils import timezone

#create a blog post model
class Post(models.Model):
    #link for another model
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    #define text with limited no of char
    title = models.CharField(max_length=200)
    #define long text without a limit
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


