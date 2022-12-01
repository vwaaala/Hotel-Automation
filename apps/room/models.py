from django.db import models

import apps.users.models as users_models
from apps import users

'''
Initiate models here to avoid circular import error
'''
# Guest = users_models.Guest()


class Room(models.Model):
    class Meta:
        verbose_name_plural = 'Room'
        db_table = 'room'

    ROOM_TYPES = (('Forest Face', 'FF'), ('River Face', 'RF'))
    number = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    capacity = models.SmallIntegerField()
    numberOfBeds = models.SmallIntegerField()
    roomType = models.CharField(max_length=20, choices=ROOM_TYPES)
    price = models.FloatField()
    statusStartDate = models.DateTimeField(null=True)
    statusEndDate = models.DateTimeField(null=True)

    def __str__(self):
        return str(self.number)


class Booking(models.Model):
    class Meta:
        verbose_name_plural = 'Booking'
        db_table = 'booking'

    roomNumber = models.ForeignKey(Room, null=True, on_delete=models.SET_NULL)
    guest = models.ForeignKey('users.Guest', null=True, on_delete=models.SET_NULL)
