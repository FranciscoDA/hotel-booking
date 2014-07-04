from django.db.models import *

# Model, CharField, TextField,\
# PositiveSmallIntegerField, EmailField, BooleanField, DateField,\
# DateTimeField, IntegerField, ForeignKey


class Guest(Model):
    def __str__(self):
        return self.name
    name = CharField('Nombre', max_length=50)
    dni = IntegerField('DNI', unique=True, blank=True, null=True)
    email = EmailField('e-mail', blank=True, null=True)
    phone = IntegerField('Tel', blank=True, null=True)
    def book(self):
        return '<a href="../booking/add?guest=%d">Reservar</a>' % self.id
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
    checkin = DateField('Check-in', blank=True, null=True)
    checkout = DateField('Check-out', blank=True, null=True)
    pax = PositiveSmallIntegerField(default=1)
    obs = TextField('Obs', blank=True, null=True)
    # clickon = BooleanField('clickOn', default=False)
    # price = IntegerField('Precio')
    # car = BooleanField('Coche', default=False)

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
    type = CharField('Tipo', max_length=50, default='Matrimonial')
    obs = TextField('Obs', blank=True, null=True)

