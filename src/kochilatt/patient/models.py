from django.db import models

class Patient(models.Model):

    name = models.CharField(max_length=50)

    class Meta:
        verbose_name = ("patient")
        verbose_name_plural = ("patients")

    def __str__(self):
        return self.name
    
