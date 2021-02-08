from django.db import models
from django.contrib.auth.models import AbstractUser


class Address(models.Model):
    street = models.CharField(max_length=160)
    house_number = models.CharField(max_length=16)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    postal_code = models.CharField(max_length=16)
    country = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.street}, {self.house_number} - {self.city} / {self.state}"


class User(AbstractUser):
    phone_number = models.CharField(max_length=16)
    cpf = models.CharField(max_length=11, unique=True)
    birth_date = models.DateField()
    address = models.OneToOneField(Address, on_delete=models.CASCADE)

    class Meta:
        ordering = ["pk"]

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
