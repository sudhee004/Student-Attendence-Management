from django.db import models

# Create your models here.
class Department(models.Model):
  BranchName= models.CharField(max_length=255)

def __str__(self) :
        return self.BranchName

class Subject(models.Model):
  SubjectName= models.CharField(max_length=255)

def __str__(self) :
        return self.SubjectName



def __str__(self) :
        return self.Name

class Semester(models.Model):
  Semester= models.CharField(max_length=255)

def __str__(self) :
        return self.Semester