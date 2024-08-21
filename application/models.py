from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class AppPerInfo(models.Model):
    username = models.ForeignKey(User, on_delete=models.SET_DEFAULT, default=None)
    fullName = models.CharField(max_length=50)
    dob = models.DateField()
    gender=models.CharField(max_length=10)
    category=models.CharField(max_length=10)
    caste_certi_no = models.CharField(max_length=15)
    aadhar=models.CharField(max_length=12)
    father=models.CharField(max_length=50)
    phone= models.IntegerField()
    email=models.EmailField()
    income=models.IntegerField()
    address=models.CharField(max_length=200)
    pincode = models.CharField(max_length=7)
    pass

class AppEduInfo(models.Model):
    username = models.ForeignKey(User, on_delete=models.SET_DEFAULT, default=None)
    eduLevel= models.CharField(max_length=20)
    InstName=models.CharField(max_length=80)
    address=models.CharField(max_length=200)
    enrollment=models.CharField(max_length=15)
    program=models.CharField(max_length=20)
    year = models.IntegerField()
    percent = models.DecimalField(decimal_places=2,max_digits=3)
    passingYear=models.IntegerField()
    marksheet = models.FileField(upload_to="marksheet/", max_length=500,null=True,default=None)

class AppBanInfo(models.Model):
    username = models.ForeignKey(User, on_delete=models.SET_DEFAULT, default=None)
    accHolderName = models.CharField(max_length=50)
    accNumber= models.CharField(max_length=30)
    bankName = models.CharField(max_length=50)
    branchName= models.CharField(max_length=50)
    ifsc = models.CharField(max_length=12)

class AppDocInfo(models.Model):
    username = models.ForeignKey(User, on_delete=models.SET_DEFAULT, default=None)
    casteCerti=models.FileField(upload_to="Caste_Certificate/", max_length=500,null=True,default=None)
    incomeCerti=models.FileField(upload_to="Income_Certificate/", max_length=500,null=True,default=None)
    aadhaar=models.FileField(upload_to="Aadhaar/", max_length=500,null=True,default=None)
    photo=models.FileField(upload_to="Photographs/", max_length=500,null=True,default=None)
    sign=models.FileField(upload_to="Signature/", max_length=500,null=True,default=None)
    addmissionLetter=models.FileField(upload_to="Admission_Letter/", max_length=500,null=True,default=None)

class FormStatus(models.Model):
    status_CHOICES = [
        ('Requested', 'Pending'),
        ('Accepted', 'Accepted'),
        ('Rejected', 'Rejected'),
    ]
    username = models.ForeignKey(User, on_delete=models.SET_DEFAULT, default="Requested")
    status= models.CharField(max_length=10,choices=status_CHOICES)
    message = models.CharField(max_length=100,default=None)

class HodApprove(models.Model):
    username = models.ForeignKey(User, on_delete=models.SET_DEFAULT, default=None)

class HodReject(models.Model):
    username = models.ForeignKey(User, on_delete=models.SET_DEFAULT, default=None)
    rejectMessage = models.CharField(max_length=400)

class PrincipalApprove(models.Model):
    username = models.ForeignKey(User, on_delete=models.SET_DEFAULT, default=None)

class PrincipalReject(models.Model):
    username = models.ForeignKey(User, on_delete=models.SET_DEFAULT, default=None)
    rejectMessage = models.CharField(max_length=400)


