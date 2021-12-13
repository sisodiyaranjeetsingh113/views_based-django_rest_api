from django.db import models
# Create your models here.
from Status_Service.models import Status
from Task_Service.models import Task
class Tile(models.Model):
    launch_date=models.DateField(blank=True,null=True)
    status=models.OneToOneField(Status,on_delete=models.CASCADE)
    task=models.ManyToManyField(Task)
    

