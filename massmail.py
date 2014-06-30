# A mass mail test.
# Not quite sure of wtf was I trying to accomplish here...


from booking.models import Guest

mails = [guest.email for guest in Guest.objects.all()]

rec = ['example@gmail.com',
       'example2@hotmail.com',]

subject = 'Envío masivo'
msg = 'Ahora sí. Un mail por cada destinatario.'

print(mails)