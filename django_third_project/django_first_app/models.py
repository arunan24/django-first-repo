from django.db import models
from django.urls import reverse

# Create your models here.
class School(models.Model):
    nameofSchool = models.CharField(max_length=256)
    nameofPrincipal=models.CharField(max_length=256)
    locationofSchool = models.CharField(max_length=256)

    def __str__(self):
        return self.nameofSchool

    def get_absolute_url(self):
        return reverse('student',kwargs={'pk': self.pk})


class studentDetails(models.Model):
    nameofStudent = models.CharField(max_length=256)
    ageofStuden = models.PositiveIntegerField()
    nameofSchool= models.ForeignKey(School,related_name='student',on_delete=models.CASCADE)

    def __str__(self):
        return  self.nameofStudent
