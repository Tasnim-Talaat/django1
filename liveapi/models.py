from django.db import models


# Create your models here.


class Course(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.name+' '+str(self.id)


class Trainee(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    nid = models.DecimalField(max_digits=14, decimal_places=0)
    courses = models.ForeignKey(Course, on_delete=models.CASCADE, default=2)
    def __str__(self):
        return self.name+' '+str(self.id)