from django.db import models

TYPE = (
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

FSTATUS = (
    ('U', 'Ufakturert'),
    ('F', 'Fakturert'),
    ('B', 'Betalt'),
)

ATYPE = (
    ('R', 'Rigg'),
    ('L', 'Lystekniker'),
    ('S', 'Lydtekniker'),
    ('A', 'Annet'),
)

ASTATUS = (
    ('A', 'Aktiv'),
    ('H', 'Halvaktiv'),
    ('I', 'Innaktiv'),
) 

BSTATUS = (
    ('I', 'Ikke registrert'),
    ('R', 'Registrert i SPF'),
    ('M', 'Mangler SPF'),
    ('U', 'Utbetalt'),
)

class Utstyr(models.Model):
    navn = models.CharField(max_length=100)
    uType = models.CharField(max_length=1, choices=TYPE)
    plasering = models.CharField(max_length=1, choices=PLASSERING)
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
    email = models.CharField(max_length=100)
    fakturaddr = models.CharField(max_length=200)
    beskrivelse = models.CharField(max_length=100)

    def __unicode__(self):
        return self.navn 

class Booking(models.Model):
    beskrivelse = models.CharField(max_length=100)
    utDato = models.DateField()
    innDato = models.DateField()
    kunde = models.ForeignKey(Kunde)
    utstyr = models.ManyToManyField(Utstyr)
    pris = models.IntegerField()
    fakturaStatus = models.CharField(max_length=1, choices=FSTATUS)
    fakturaNr = models.CharField(max_length=10)

    def __unicode__(self):
        return self.beskrivelse
    

class Person(models.Model):
    navn = models.CharField(max_length=50)
    epost = models.CharField(max_length=50)
    tlf = models.CharField(max_length=15)
    aktivStatus = models.CharField(max_length=1, choices=ASTATUS)
    beskrivelse = models.CharField(max_length=500)
    regiInntreden = models.IntegerField()

    def __unicode__(self):
        return self.navn

class Arbeid(models.Model):
    booking = models.ForeignKey(Booking)
    person = models.ForeignKey(Person)
    sats = models.IntegerField()
    arbeidsType = models.CharField(max_length=1, choices=ATYPE)
    betalStatus = models.CharField(max_length=1, choices=BSTATUS)
        
    def __unicode__(self):
        return self.navn
