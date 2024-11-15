from django.db import models
import string
import random

class URL(models.Model):
    original_url = models.URLField()
    short_code = models.CharField(max_length=10, unique=True, blank=True)
    tfug_url = models.URLField(blank=True)

    def save(self, *args, **kwargs):
        if not self.short_code:
            s_c = str(random.randint(10000,99999))
            self.short_code = s_c
            self.tfug_url = 'https://tfug-ghaziabad.tech/link/'+s_c
        super().save(*args, **kwargs)

    def __str__(self):
        return self.original_url