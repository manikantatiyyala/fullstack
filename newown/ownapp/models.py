from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Papers(models.Model):
    Creator = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    PaperId = models.AutoField(primary_key=True)
    PaperName = models.CharField(max_length=500)
    DateOfCreating = models.DateField()
    saved_file = models.FileField()

    def __str__(self):
        return f"{self.PaperName} {self.DateOfCreating} {self.saved_file}"
