from django.db import models

class Pers(models.Model):
    CHOICES = (
        ('tg', 'Targon'),
        ('io', 'Ionia'),
        ('nx', 'Noxus'),
        ('dm', 'Demacia'),
        ('pz', 'Piltover & Zaun'),
        ('fj', 'Freljord'),
        ('si', 'Shadow Isles'),
        ('bw', 'Bilgewater')
    )
    photo = models.ImageField(null=True, default=None, upload_to='avatars')
    lor = models.TextField()
    fraction = models.CharField(max_length=100, choices=CHOICES)
    name = models.CharField(max_length=30, default='Unknow')
    character = models.ForeignKey('Сharacteristics', on_delete=models.SET_NULL, null=True, blank=True)
    def __str__(self) -> str:
        return self.name
    
class Сharacteristics(models.Model):
    WP = (
        ('gun', 'Gun'),
        ('axe', 'Axe'),
        ('sword', 'Sword'),
        ('magic', 'Magic')
    )
    CL = (
        ('mage', 'Mage'),
        ('war', 'War'),
        ('rogue', 'Roque'),
        ('archer', 'Archer')
    )
    power = models.IntegerField()
    mana = models.IntegerField()
    weapon = models.CharField(max_length=100, choices=WP)
    who = models.CharField(max_length=40, choices=CL)
    hp = models.IntegerField()
    
    def __str__(self) -> str:
        return self.who