from django.db import models
from django.shortcuts import reverse

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    author = models.CharField(max_length=50)
    summary = models.TextField()
    cover_image = models.ImageField(upload_to="appbooks/images/", blank=True, null=True)
    category = models.ManyToManyField(Category, related_name="books")
    pdf = models.FileField(upload_to="appbooks/pdf/", blank=True, null=True)
    recommended_books = models.BooleanField(default=False)
    ficition_books = models.BooleanField(default=False)
    business_books = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    @property
    def cover_image_url(self):
        return f"/media/{self.cover_image}"

    @property
    def show_url(self):
        url = reverse("appbooks.show_book", args=[self.slug])
        return url

    @property
    def view_pdf_url(self):
        return f"/media/{self.pdf}"
