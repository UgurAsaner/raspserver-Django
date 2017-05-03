from django.db import models


class Pin(models.Model):

    name = models.CharField(max_length=20)
    number = models.IntegerField()


class Server(models.Model):

    name = models.CharField(max_length=20)
    ip = models.CharField(max_length=20)


class Status(models.Model):

    type = models.CharField(max_length=10)
    amount = models.IntegerField()


class Value(models.Model):

    name = models.CharField(max_length=20)
    value = models.IntegerField()


class Path(models.Model):

    name = models.CharField(max_length=10)
    path = models.CharField(max_length=100)
