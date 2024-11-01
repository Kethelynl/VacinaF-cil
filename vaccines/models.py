from django.db import models
from django.contrib.auth.models import User


class Vaccines(models.Model):
    name_vacinne = models.CharField(max_length=100)
    description = models.TextField()
    age_group = models.CharField(max_length=50)
    doses = models.IntegerField()
    
    
    def __str__(self):
        return self.name_vacinne

class MarcVaccine(models.Model):
    vaccines = models.ForeignKey(Vaccines, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    last_date =  models.DateField()
    next_dose = models.DateField(null=True, blank=True)
    
    def __str__(self):
        return f"{self.user} - {self.vaccines}"