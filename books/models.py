from django.db import models


class Book(models.Model):
    """Book"""
    title = models.CharField("Title", max_length=250)
    author = models.CharField("Author", max_length=250)
    description = models.TextField("Description", max_length=455, )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Book"
        verbose_name_plural = "Books"
