from django.db import models


class Pins(models.Model):

    name = models.CharField(max_length=20)
    number = models.IntegerField()


class Server(models.Model):

    name = models.CharField(max_length=20)
    ip = models.CharField(max_length=20)


class Status(models.Model):

    type = models.CharField(max_length=10)
    amount = models.IntegerField()

