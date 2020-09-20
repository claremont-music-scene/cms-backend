from django.db import models
from django.utils.timezone import now


class Post(models.Model):
    title = models.CharField(max_length=150)
    slug = models.SlugField()
    teaser = models.TextField(blank=True, null=True)
    body = models.TextField()
    image = models.ImageField(upload_to="news/%Y/%m/%d")
    author = models.ForeignKey(
        "auth.User", null=True, blank=True, on_delete=models.SET_NULL
    )
    date_created = models.DateTimeField(auto_created=True)
    date_modified = models.DateTimeField(auto_now=True)
    is_draft = models.BooleanField(default=True)
    date_published = models.DateTimeField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.is_draft and not self.date_published:
            self.date_published = now()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title