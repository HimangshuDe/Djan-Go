from django.db import models
from django.urls import reverse
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=50)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    author = models.CharField(null=True, max_length=100)
    is_bestselling = models.BooleanField(default=False)

    def get_absolute_url(self):
        """
        This will not work properly if any field is not defined in the Book Model Class.
        """
        return reverse("book-detail", args=[str(self.id)])

    def __str__(self):
        return f"{self.title} ({self.rating})"
