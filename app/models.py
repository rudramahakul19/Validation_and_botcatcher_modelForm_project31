from django.db import models

# Create your models here.
from django import forms
from django.core import validators

def check_for_a(value):
    if value.lower()[0]=='a':
        raise forms.ValidationError('Invalid')

class Student(models.Model):
    sname=models.CharField(max_length=100,primary_key=True,validators=[check_for_a])
    sage=models.IntegerField()
    smobile=models.CharField(max_length=10,validators=[validators.RegexValidator('[6-9]\d{9}')])

    def __str__(self):
        return self.sname

    