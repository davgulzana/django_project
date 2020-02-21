from django.db import models

class Biography(models.Model):
    description = models.TextField(max_length=500)

    class Meta:
        verbose_name = 'Biography'
        verbose_name_plural = 'Biographies'

    def __str__(self):
        return self.description

class Author(models.Model):
    name = models.CharField(max_length=50, verbose_name='First name')
    last_name = models.CharField(max_length=50)
    date_birth = models.DateField(verbose_name='Date of birth')
    biography = models.OneToOneField(Biography, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return self.name + ' ' + self.last_name

class Genre(models.Model):
    title = models.CharField(max_length=50, verbose_name='Name of genre')

    def __str__(self):
        return self.title


class Book(models.Model):
    title = models.CharField(max_length=100)
    pub_date = models.DateField(verbose_name='Published date', null=True, blank=True)
    pages = models.PositiveIntegerField(null=True, blank=True)
    description = models.CharField(max_length=255)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
    genre = models.ManyToManyField(Genre)

    def __str__(self):
        return self.title
