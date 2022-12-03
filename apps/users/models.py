from django.db import models

from apps.room.models import Booking


class Guest(models.Model):
    class Meta:
        verbose_name_plural = 'Guest'
        db_table = 'guest'

    user = models.OneToOneField('auth.User', null=True, on_delete=models.SET_NULL)
    phone_number = models.CharField(max_length=13)

    def __str__(self):
        return f"{self.user}"

    def num_of_booking(self):
        return Booking.objects.filter(guest=self).count()

    def num_of_total_booking_days(self):
        total = 0
        bookings = Booking.objects.filter(guest=self)
        for b in bookings:
            day = b.end_date - b.start_date
            total += int(day.days)
        return total

    # TODO num_of_last_booking_days
    def num_of_last_booking_days(self):
        pass

    def current_room(self):
        booking = Booking.objects.filter(guest=self).last()
        return booking.roomNumber


class Employee(models.Model):
    class Meta:
        db_table = 'employee'
        verbose_name_plural = 'Employee'

    user = models.OneToOneField('auth.User', null=True, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=13)
    salary = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.user}"
