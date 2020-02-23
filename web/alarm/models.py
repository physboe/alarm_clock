from django.db import models


class Alarm(models.Model):
    WEEKDAY_CHOICES = (
        ("Mon", "Montag"),
        ("Tue", "Dienstag"),
        ("Wed", "Mittwoch"),
        ("Thu", "Donnerstag"),
        ("Fri", "Freitag"),
        ("Sat", "Samstag"),
        ("Sun", "Sonntag"),
    )

    name = models.CharField(max_length=200)
    isOn = models.BooleanField()
    time = models.CharField(max_length=25)
    repeat = models.BooleanField()
    weekdays = models.CharField(max_length=27)
