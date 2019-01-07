from django.db import models
from django.utils import timezone
from django.core.validators import RegexValidator


class Client(models.Model):
    name = models.CharField(max_length=50)
    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$', \
        message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone = models.CharField(validators=[phone_regex], max_length=17, blank=False)
    created_date = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ('created_date',)
