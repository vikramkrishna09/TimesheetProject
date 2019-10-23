from django.db import models

# Create your models here.

class UserTimeCard(models.Model):
    Sitecode = models.CharField(max_length=50)
    nameofcontracter = models.TextField()


class UserTimeCardLabor(models.Model):
    Sitecode = models.ForeignKey(UserTimeCard,on_delete=models.CASCADE)
    JobCode = models.ForeignKey('Administer.Job',on_delete=models.CASCADE)
    Totalhrs = models.CharField(max_length=50)
    Totalamount = models.CharField(max_length=50)

class UserTimeCardMachine(models.Model):
    Sitecode = models.ForeignKey(UserTimeCard, on_delete=models.CASCADE)
    MachineCode = models.ForeignKey('Administer.Machine', on_delete=models.CASCADE)
    Totalhrs = models.CharField(max_length=50)
    Totalamount = models.CharField(max_length=50)

