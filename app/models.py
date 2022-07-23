from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.


class Item(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    category = models.CharField(max_length=50, null=True)
    save_date = models.DateTimeField(blank=True, null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)

    def saveItem(self):
        self.save_date = timezone.now()
        self.save()

    def __str__(self):
        return self.name
