from django.db import models

class lugat(models.Model):
    MAHSULOT = (
        ('Kartoshka','Kartoshka'),
        ('Sabzi','Sabzi'),
        ('Piyoz','Piyoz'),
        ('Sarimsoq','Sarimsoq'),
        ('Karam','Karam'),
        ('Pomidor','Pomidor'),
        ('Bodring','Bodring'),
        ('Mosh','Mosh'),
        ('Loviya','Loviya'),
        ('Qovun','Qovun'),
        ('Tarvuz','Tarvuz'),
        ('Oshqovoq','Oshqovoq'),
        ('Olma','Olma'),
        ('O`rik','O`rik'),
        ('Xurmo','Xurmo'),
        ('Gilos','Gilos'),
        ('Anor','Anor'),
        ('Limon','Limon'),
        ('Nok','Nok'),
        ('Uzum','Uzum'),
      )
    MASLAHAT = (
         ('In-Vitro, Tomorqa xizmati, Rubikon water','In-Vitro, Tomorqa xizmati, Rubikon water'),
      )
    sotix = models.CharField('Sotix',max_length=128)
    maslahat = models.CharField('Maslahat', max_length=128, choices = MASLAHAT)
    mahsulot_turi = models.CharField('Mahsulot turi', max_length=128, choices = MAHSULOT)
    xarajat = models.IntegerField()
    hosildorlik = models.CharField('Hosildorlik', max_length=15)
    daromad = models.IntegerField()
    list_display = ['sotix','mahsulot_turi','xarajat','hosildorlik','daromad','sof_foyda','rentabellik']

    def sof_foyda(self):
      sof_foyda=self.daromad-self.xarajat
      return sof_foyda
    def rentabellik(self):
      rentabellik=round((self.daromad/self.xarajat)*100)
      return rentabellik
 



    
    