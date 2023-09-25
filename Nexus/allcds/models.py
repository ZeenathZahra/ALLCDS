from django.db import models

# Create your models here.


class Record(models.Model):
    created_At=models.DateTimeField(auto_now_add=True)
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)

    address=models.CharField(max_length=100)
    city=models.CharField(max_length=50)
    state=models.CharField(max_length=50)
    zipcode=models.CharField(max_length=10)

    email=models.CharField(max_length=50)
    phone=models.CharField(max_length=15)

    def __str__(self):
        return (f"{self.first_name} {self.last_name}")



