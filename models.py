from django.db import models
from django.contrib.auth.models import User

UTSTYRSTYPE = (
    ('S', 'Lys'),
    ('D', 'Lyd'),
    ('A', 'Annet'),
)

PLASSERING = (
    ('G', 'Garderoben'),
    ('K', 'Kjelleren'),
)

STATUS = (
    ('O', 'Ok'),
    ('S', 'Til service'),
    ('R', 'Maa repareres'),
    ('K', 'Kassert'),
)

FAKTURASTATUS = (
    ('U', 'Ufakturert'),
    ('F', 'Fakturert'),
    ('B', 'Betalt'),
)

ARBEIDSTYPE = (
    ('R', 'Rigg'),
    ('L', 'Lystekniker'),
    ('S', 'Lydtekniker'),
    ('A', 'Annet'),
)

AKTIVSTATUS = (
    ('A', 'Aktiv'),
    ('H', 'Halvaktiv'),
    ('I', 'Inaktiv'),
) 

BETALINGSSTATUS = (
    ('I', 'Ikke registrert'),
    ('R', 'Registrert i SPF'),
    ('M', 'Mangler SPF'),
    ('U', 'Utbetalt'),
)

class Utstyr(models.Model):
    navn = models.CharField(max_length=100)
    utstyrstype = models.CharField(max_length=1, choices=UTSTYRSTYPE)
    plassering = models.CharField(max_length=1, choices=PLASSERING)
    status = models.CharField(max_length=1, choices=STATUS)
    effekt = models.IntegerField()
    innkjopsdato = models.DateField()
    innkjopspris = models.IntegerField()
    utleiepris = models.IntegerField()
    saldo = models.IntegerField()

    def __unicode__(self):
        return self.navn

class Kunde(models.Model):
    navn = models.CharField(max_length=100)
    tlfNr = models.CharField(max_length=15)
    epost = models.EmailField(max_length=100)
    fakturaddr = models.TextField()
    beskrivelse = models.TextField()

    def __unicode__(self):
        return self.navn 

class Booking(models.Model):
    beskrivelse = models.TextField()
    utDato = models.DateField()
    innDato = models.DateField()
    kunde = models.ForeignKey(Kunde)
    utstyr = models.ManyToManyField(Utstyr)
    pris = models.DecimalField(max_digits=2) 
    fakturastatus = models.CharField(max_length=1, choices=FAKTURASTATUS)
    fakturasato = models.DateField()
    fakturanr = models.CharField(max_length=10)

    def __unicode__(self):
        return self.beskrivelse
    

class Person(models.Model):
    user = models.OneToOneField(User)
    tlf = models.CharField(max_length=15)
    aktivstatus = models.CharField(max_length=1, choices=AKTIVSTATUS)
    beskrivelse = models.TextField
    regiInntreden = models.IntegerField()

    def __unicode__(self):
        return self.user.first_name + " " + self.user.last_name

class Arbeid(models.Model):
    booking = models.ForeignKey(Booking)
    person = models.ForeignKey(Person)
    sats = models.DecimalField(max_digits=2)
    arbeidstype = models.CharField(max_length=1, choices=ARBEIDSTYPE)
    betalstatus = models.CharField(max_length=1, choices=BETALINGSSTATUS)
        
    def __unicode__(self):
        return self.navn
