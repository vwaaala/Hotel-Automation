from django.utils import timezone
from django.db import models

'''
Initiate models here to avoid circular import error
'''


# Guest = users_models.Guest()


class Room(models.Model):
    class Meta:
        verbose_name_plural = 'Room'
        db_table = 'room'

    ROOM_TYPES = (('FF', 'Forest Face'), ('RF', 'River Face'))
    number = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    capacity = models.SmallIntegerField()
    number_of_beds = models.SmallIntegerField()
    room_type = models.CharField(max_length=20, choices=ROOM_TYPES)
    price = models.FloatField()
    status_start_date = models.DateTimeField(null=True)
    status_end_date = models.DateTimeField(null=True)

    def __str__(self):
        return str(self.number)


class Booking(models.Model):
    class Meta:
        verbose_name_plural = 'Booking'
        db_table = 'booking'

    roomNumber = models.ForeignKey(Room, null=True, on_delete=models.SET_NULL)
    guest = models.ForeignKey('users.Guest', null=True, on_delete=models.SET_NULL)
    reservation_date = models.DateField(default=timezone.now)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f"{self.guest.user.first_name} {self.guest.user.last_name}"
