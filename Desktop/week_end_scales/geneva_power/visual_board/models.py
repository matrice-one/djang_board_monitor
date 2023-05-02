from django.db import models

# Create your models here.
from django.db import models

class BoardMember(models.Model):
    name_and_surname = models.CharField(max_length=512, null=True)
    signature_mode = models.CharField(max_length=512, null=True)
    status = models.CharField(max_length=512, null=True)

    def __str__(self):
        return self.name_and_surname

class Company(models.Model):
    name = models.CharField(max_length=512, null=True)
    board_members = models.ManyToManyField(BoardMember, through='BoardMembership')

    def __str__(self):
        return self.name

class BoardMembership(models.Model):
    board_member = models.ForeignKey(BoardMember, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
