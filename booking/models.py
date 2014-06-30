from django.db.models import *

# Model, CharField, TextField,\
# PositiveSmallIntegerField, EmailField, BooleanField, DateField,\
# DateTimeField, IntegerField, ForeignKey


class Guest(Model):
    def __str__(self):
        return self.name
    name = CharField('Nombre', max_length=50)
    dni = IntegerField('DNI', unique=True, blank=True, null=True)
    email = EmailField('e-mail')
    phone = IntegerField('Tel', blank=True, null=True)
    def book(self):
        return '<a href="../booking/add">Reservar</a>'
    def details(self):
        return '<a href="#">Ver detalles</a>'
    book.allow_tags = True
    details.allow_tags = True


class Booking(Model):
    # Por el momento, Localizador = id. Ideal: base 32.
    def __str__(self):
        return 'r' + str(self.id)
    guest = ForeignKey('Guest', verbose_name='Huésped')
    booked = DateTimeField('Efectuada', auto_now_add=True)
    last_mod = DateTimeField('Últ. mod.', auto_now=True)
    # room = ForeignKey('Room', verbose_name='Habitación')
    # checkin = DateField('Check-in')
    # checkout = DateField('Check-out')
    # pax = PositiveSmallIntegerField(default=1)
    # clickon = BooleanField('clickOn', default=False)
    # price = IntegerField('Precio')
    # car = BooleanField('Coche', default=False)
    # obs = TextField('Obs')

class Night(Model):
    def __str__(self):
        return self.date.isoformat()
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

