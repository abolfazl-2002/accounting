from django.db import models
from django.urls import reverse

# Create your models here.

# accountry table
class AccountryTable(models.Model):

    # choisec
    CHOICE = [
        ('+','income'),
        ('-','expenditrue')
    ]

    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.FloatField()
    group = models.CharField(default='+',max_length=1,choices=CHOICE)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.title)

    def get_absolute_url(self):
        return reverse("", kwargs={"pk": self.pk})
    
