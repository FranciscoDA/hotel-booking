from django.utils.translation import ugettext_lazy as _
from django.utils.encoding import python_2_unicode_compatible
from django.db.models import *

# Model, CharField, TextField,\
# PositiveSmallIntegerField, EmailField, BooleanField, DateField,\
# DateTimeField, IntegerField, ForeignKey

# Translators: observations (obs) field. Used in several models.
obs_verbose = _('observations')


@python_2_unicode_compatible
class Guest(Model):
    first_name = CharField(_('first name'), max_length=50)
    last_name = CharField(_('last name'), max_length=50)
    # Translators: use your national identification number.
    nid = IntegerField(_('ID'), help_text=_('national identification number'),
                       unique=True, blank=True, null=True)
    # Translators: title based on marital or professional status, etc.
    # title = CharField(choices=())
    email = EmailField(_('e-mail'), blank=True, null=True,
                       help_text=_('telephone number'))
    tel = IntegerField(_('tel.'), blank=True, null=True)
    # address = ForeignKey('Address')
    obs = TextField(obs_verbose, blank=True, null=True)

    class Meta:
        verbose_name = _('guest')
        verbose_name_plural = _('guests')

    def __str__(self):
        return self.first_name + ' ' + self.last_name

    def book(self):
        return '<a href="../booking/add?guest=%d">%s</a>' % (self.id, _('new booking'))

    def booking_history(self):
        return '<a href="../booking?guest=%d">%s</a>' % (self.id, _('booking history'))
    book.allow_tags = True
    booking_history.allow_tags = True


# class CreditCard(Model):
#     guest = ForeignKey('Guest')
#     number = IntegerField()


@python_2_unicode_compatible
class Booking(Model):
    # self.id in base 32 could be a nice booking ID (also returned as __str__)
    def __str__(self):
        return 'r' + str(self.id)
    guest = ForeignKey('Guest', verbose_name=_('guest'))
    added = DateTimeField(_('added'), auto_now_add=True)
    last_mod = DateTimeField(_('last mod.'), auto_now=True)
    check_in = DateField(_('check-in'), blank=True, null=True)
    check_out = DateField(_('check-out'), blank=True, null=True)
    pax = PositiveSmallIntegerField(_('pax'), default=1)
    obs = TextField(obs_verbose, blank=True, null=True)
    # Price should be calculated automatically according to room type, pax,
    # special offers and discounts, etc.
    price = IntegerField(_('price'), default=0)
    has_car = BooleanField('has car', default=False)


@python_2_unicode_compatible
class Occupancy(Model):
    booking = ForeignKey('Booking')
    date = DateField()
    room = ForeignKey('Room')
    obs = CharField(obs_verbose, max_length=200, blank=True, null=True)

    class Meta:
        unique_together = ('date', 'room')
        verbose_name = _('occupancy')
        verbose_name_plural = _('occupancies')

    def __str__(self):
        return self.date.isoformat()


@python_2_unicode_compatible
class Room(Model):
    number = PositiveSmallIntegerField(_('number'), primary_key=True)
    type = CharField(_('type'), max_length=50, default='Matrimonial')
    obs = TextField(_('observations'), blank=True, null=True)

    def __str__(self):
        return str(self.number)
