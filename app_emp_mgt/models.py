from django.db import models


class Employee(models.Model):
    CH_GENDER = (
        ('Male', 'Male'), ('Female', 'Female')
    )
    name = models.CharField(max_length=50, null=False, blank=False)
    gender = models.CharField(max_length=10, choices=CH_GENDER)
    cont_no = models.CharField(max_length=10, null=False, blank=False)
    email = models.EmailField(max_length=255, unique=True, null=False, blank=False)

    def __str__(self):
        return '{}'.format(self.name)
