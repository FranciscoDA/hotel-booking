from django.db.models import *

# Model, CharField, TextField,\
# PositiveSmallIntegerField, EmailField, BooleanField, DateField,\
# DateTimeField, IntegerField, ForeignKey


class Client(Model):
    def __str__(self):
        return self.name
    name = CharField('Nombre', max_length=50)
    # dni = IntegerField('DNI', unique=True)
    # email = EmailField('e-mail')
    # phone = IntegerField('Tel')


class Booking(Model):
    # Por el momento, Localizador = id. Ideal: base 32.
    def __str__(self):
        return 'r' + str(self.id)
    client = ForeignKey('Client', verbose_name='Cliente')
    booked = DateTimeField('Efectuada', auto_now=True)
    # room = ForeignKey('Room', verbose_name='Habitación')
    # checkin = DateField('Check-in')
    # checkout = DateField('Check-out')
    # pax = PositiveSmallIntegerField(default=1)
    # clickon = BooleanField('clickOn', default=False)
    # price = IntegerField('Precio')
    # car = BooleanField('Coche', default=False)
    # obs = TextField('Obs')

class Night(Model):
    booking = ForeignKey('Booking')
    date = DateField()
    room = ForeignKey('Room')
    class Meta:
        unique_together = ('date', 'room')


class Room(Model):
    def __str__(self):
        return str(self.number)
    number = PositiveSmallIntegerField('Núm.', primary_key=True)
    # type = CharField('Tipo', max_length=50)
    # obs = CharField('Obs')

