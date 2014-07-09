from django.utils.translation import ugettext_lazy as _
from django.utils.encoding import python_2_unicode_compatible
from django.db.models import *

# Model, CharField, TextField,\
# PositiveSmallIntegerField, EmailField, BooleanField, DateField,\
# DateTimeField, IntegerField, ForeignKey


@python_2_unicode_compatible
class Guest(Model):
    first_name = CharField('Nombre', max_length=50)
    last_name = CharField('Apellido', max_length=50)
    nid = IntegerField('DNI', unique=True, blank=True, null=True) #nid sounds more generic
    # gender = CharField(choices=())
    email = EmailField('e-mail', blank=True, null=True)
    phone = IntegerField('Tel', blank=True, null=True)

    def __str__(self):
        return self.first_name + ' ' + self.last_name

    def book(self):
        return '<a href="../booking/add?guest=%d">Reservar</a>' % self.id

    def booking_history(self):
        return '<a href="../booking?guest=%d">Historial de reservas</a>' % self.id
    book.allow_tags = True
    booking_history.allow_tags = True


# class CreditCard(Model):
#     guest = ForeignKey('Guest')
#     number = IntegerField()


@python_2_unicode_compatible
class Booking(Model):
    # Por el momento, Localizador = id. Ideal: base 32.
    def __str__(self):
        return 'r' + str(self.id)
    guest = ForeignKey('Guest', verbose_name=_('guest'))
    booked = DateTimeField('Efectuada', auto_now_add=True)
    last_mod = DateTimeField('Últ. mod.', auto_now=True)
    checkin = DateField('Check-in', blank=True, null=True)
    checkout = DateField('Check-out', blank=True, null=True)
    pax = PositiveSmallIntegerField(default=1)
    obs = TextField('Obs', blank=True, null=True)
    price = IntegerField('Precio', default=0)
    car = BooleanField('Coche', default=False)


@python_2_unicode_compatible
class Occupancy(Model):
    booking = ForeignKey('Booking')
    date = DateField()
    room = ForeignKey('Room')
    obs = CharField('Observaciones', max_length=200, blank=True, null=True)

    class Meta:
        unique_together = ('date', 'room')
        verbose_name = _('occupancy')
        verbose_name_plural = _('occupancies')

    def __str__(self):
        return self.date.isoformat()


@python_2_unicode_compatible
class Room(Model):
    number = PositiveSmallIntegerField('Núm.', primary_key=True)
    type = CharField('Tipo', max_length=50, default='Matrimonial')
    obs = TextField('Obs', blank=True, null=True)

    def __str__(self):
        return str(self.number)
