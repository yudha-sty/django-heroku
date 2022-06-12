from django.db import models

# Create your models here.

class nasdaq(models.Model):
    simbol = models.CharField(max_length=255)
    perusahaan = models.TextField()

    def __str__(self):
        return self.simbol