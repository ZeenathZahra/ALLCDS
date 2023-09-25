from django.db import models

# Create your models here.


class Record(models.Model):
    # ID-7.5
    # time
    created_At=models.DateTimeField(auto_now_add=True)

    # Personal Information
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)

    address=models.CharField(max_length=100)
    city=models.CharField(max_length=50)
    state=models.CharField(max_length=50)
    zipcode=models.CharField(max_length=10)

    email=models.CharField(max_length=50)
    phone=models.CharField(max_length=15)

    # cell images
    image = models.ImageField(upload_to='images/',blank=True, null=True)  # Use ImageField to store images



    # Medical History
    medical_history= models.FileField(blank=True, null=True,upload_to='medical_history/')


    # Genatic Information
    genatic_information= models.FileField(blank=True, null=True,upload_to='genatic_information/')

    # Lab Results
    lab_results= models.FileField(upload_to='lab_results/',blank=True, null=True)

    # Radiology and imaging Results

    radiology_results= models.FileField(upload_to='radiology_results/',blank=True, null=True)

    # Other pertinant clinical Results

    clinical_results= models.FileField(upload_to='clinical_results/',blank=True, null=True)

    def __str__(self):
        return (f"{self.first_name} {self.last_name}")



