from django.db import models
from django.forms import ModelForm

class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    university = models.CharField(max_length=100)
    email = models.CharField(max_length=50)
    def __unicode__(self):
        return self.first_name

class PersonForm(ModelForm):
    class Meta:
        model = Person
