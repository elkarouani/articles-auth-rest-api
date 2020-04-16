from django.db import models


class Article(models.Model):
    user = models.ForeignKey('authentication.CustomUser', on_delete=models.CASCADE)
    title = models.CharField(verbose_name="Article title", max_length=100)
    description = models.TextField(verbose_name="Article description")

    def __str__(self):
        return self.title