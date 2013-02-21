from django.db import models
from django.forms import ModelForm, PasswordInput
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms.extras.widgets import SelectDateWidget

import account.forms


class SignupForm(account.forms.SignupForm):

    birthdate = forms.DateField(widget=SelectDateWidget(years=range(1910, 1991)))

class Person(models.Model):
    user = models.OneToOneField(User)
    university = models.CharField(max_length=100)
    email = models.CharField(max_length=50)

class PersonForm(forms.Form):
    username = forms.CharField(max_length=30)
    password = forms.CharField(widget=PasswordInput())
    university = forms.CharField(max_length=100)
    email = forms.EmailField()
    
    
class UserCreateForm(UserCreationForm):
    email = forms.EmailField(required=True)
    
    class Meta:
        model = User
        fields = ("username","email","password1","password2")
        
    def save(self,commit=True):
        user = super(UserCreateForm,self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user
    
class Review(models.Model):
    ACADEMIC = 'ACADEMIC'
    SUMMER = 'SUMMER'
    PAID = 'PAID'
    UNPAID = 'UNPAID'
    
    TYPE_CHOICES = (
                    (ACADEMIC,'Academic Year'),
                    (SUMMER,'Summer'),
    )
    PAY_CHOICES = (
                   (PAID,'Paid'),
                   (UNPAID,'Unpaid'),
    )
    
    person = models.ForeignKey('Person')
    employer = models.CharField(max_length=100)
    type = models.CharField(max_length=10,
                            choices = TYPE_CHOICES,
                            default = SUMMER)
    pay = models.CharField(max_length=10,
                           choices = PAY_CHOICES,
                           default = PAID)
    comment = models.CharField(max_length=1000)

class ReviewForm(ModelForm):
    class Meta:
        model = Review


