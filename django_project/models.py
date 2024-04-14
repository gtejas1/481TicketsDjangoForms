from django.db import models

class Region(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Ticket(models.Model):
    time = models.DateTimeField()
    day = models.CharField(max_length=10)  # Store the day of the week as a string
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    street_address = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.street_address} - {self.time} - {self.day}"
