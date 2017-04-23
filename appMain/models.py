from django.db import models

# Create your models here.

class Student(models.Model):

    Name = models.CharField(max_length=200, default="NAME_MISSING")
    Form = models.IntegerField(default=0)
    Gender = models.IntegerField(default=0) #1 = male; 2 = female; not sexist, just self-centered
    StudentID = models.IntegerField(default=0)

    def __str__():
        return (str(self.StudentID) + " " + str(self.Name))
