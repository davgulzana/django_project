from django.db import models

class Biography(models.Model):
    description = models.TextField(max_length=500)

    class Meta:
        verbose_name = 'Biography'
        verbose_name_plural = 'Biographies'

class Author(models.Model):
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_birth = models.DateField()
    biography = models.OneToOneField(Biography, on_delete=models.CASCADE, primary_key=True)

class Genre(models.Model):
    title = models.CharField(max_length=50)


class Book(models.Model):
    title = models.CharField(max_length=100)
    pub_date = models.DateField()
    pages = models.PositiveIntegerField()
    description = models.CharField(max_length=255)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='authors')
    genre = models.ManyToManyField(Genre)
