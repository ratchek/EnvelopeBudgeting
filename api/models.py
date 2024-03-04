from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator
from django.db import models


class CustomUser(AbstractUser):
    pass
    # add additional fields in here

    def __str__(self):
        return self.username


# An envelope is a budget category. It has a name and a total amount of money in it.
class Envelope(models.Model):
    name = models.CharField(max_length=50)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name="envelopes", on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name


# A transaction is a record of money being spent from an envelope. It has a date, an amount, a name, notes, and a reference to the envelope it came from.
class Transaction(models.Model):
    date = models.DateField()
    amount = models.DecimalField(
        max_digits=10, decimal_places=2, validators=[MinValueValidator(0)]
    )
    name = models.CharField(max_length=100)
    notes = models.TextField(blank=True)
    envelope = models.ForeignKey(Envelope, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} - {self.envelope.user} - {self.date}"


# A fill is a record of money being added to an envelope. It has a date, an amount, a name, notes, and a reference to the envelope it came from.
class Fill(models.Model):
    date = models.DateField()
    amount = models.DecimalField(
        max_digits=10, decimal_places=2, validators=[MinValueValidator(0)]
    )
    name = models.CharField(max_length=100)
    notes = models.TextField(blank=True)
    envelope = models.ForeignKey(Envelope, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} - {self.envelope.user} - {self.date}"
