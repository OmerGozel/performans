from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from PIL import Image

# Create your models here.
class Okul (models.Model):
   adi = models.CharField(max_length=250)
 
   def __str__(self):
     return f'{self.adi}'
   
   class Meta:
      verbose_name_plural = "Okullar"

class Profil (models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name= 'profil' ) 
    first_name = models.CharField (max_length=150)
    last_name = models.CharField (max_length=150)
    tel  = models.IntegerField(null=True, blank=True)
    email = models.EmailField()
    okulu = models.ForeignKey(Okul, on_delete= models.SET_NULL, null= True, blank= True)    
    sinifi = models.IntegerField(null=True, blank=True)
    foto = models.ImageField(null=True, blank= True, upload_to='profilPhoto/')

    def __str__(self):
      grup = ''

      if self.user.groups.all().values().count() > 0:
         grup = self.user.groups.all()[0].name

      return f'{self.first_name} {self.last_name} ({grup})'
    
    class Meta:
        verbose_name_plural = "Profiller"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.foto:
            img= Image.open(self.foto.path)
            if img.height > 600 or img.width > 600:
                output_size = (600, 600)
                img.thumbnail(output_size)
                img.save(self.foto.path)

class Ders (models.Model):
   adi = models.CharField (max_length=150)
   sinifi = models.IntegerField(default=8)

   def __str__(self):
      return self.adi
   
   class Meta:
        verbose_name_plural = "Dersler"


class Konu (models.Model):
   adi = models.CharField (max_length=150)
   ders = models.ForeignKey(Ders, on_delete= models.CASCADE)
   parent = models.ForeignKey('self',on_delete= models.CASCADE, null=True, blank= True)
   sinifi = models.IntegerField(default=8)

   def __str__(self):
      return self.adi
   
   class Meta:
        verbose_name_plural = "Konular"
   
class YayinEvi (models.Model):
   adi = models.CharField(max_length=150)

   def __str__(self):
         return self.adi
   
   class Meta:
        verbose_name_plural = "Yayin Evleri"

#Konu testleri
class Test (models.Model): 
   adi  = models.CharField (max_length=150)
   konu = models.ForeignKey(Konu,on_delete=models.CASCADE)
   ders = models.ForeignKey(Ders,on_delete=models.CASCADE)
   sinifi = models.IntegerField(default=8)
   yayin = models.ForeignKey(YayinEvi,on_delete=models.CASCADE)
   soru_sayisi = models.IntegerField(default=0)

   def __str__(self):
      return f'{self.adi}({self.konu}-{self.yayin})'
   
   class Meta:
        verbose_name_plural = "Testler"
   
class GenelTaramaTest (models.Model):
   adi  = models.CharField (max_length=150)
   ders = models.ForeignKey(Ders,on_delete=models.CASCADE)
   sinifi = models.IntegerField(default=8)
   yayin = models.ForeignKey(YayinEvi,on_delete=models.CASCADE)
   soru_sayisi = models.IntegerField(default=0)

   def __str__(self):
      return self.adi
   
   class Meta:
        verbose_name_plural = "Genel Tarama Testleri"

class Deneme (models.Model):
   adi  = models.CharField (max_length=150)
   yayin = models.ForeignKey(YayinEvi,on_delete=models.CASCADE)
   soru_sayisi = models.IntegerField(default=0)
   sinifi = models.IntegerField(default=8)
   
   def __str__(self):
      return self.adi
      
   class Meta:
        verbose_name_plural = "Denemeler"


class DenemeSonucu(models.Model):
   deneme = models.ForeignKey(Deneme,on_delete=models.CASCADE, null = True)
   user = models.ForeignKey(User,on_delete=models.CASCADE, null = True, related_name = 'user_DenemeSonucu')
   tarih = models.DateField()
   ders  = models.ForeignKey(Ders,on_delete= models.CASCADE)
   dogru = models.IntegerField(default=0)
   yanlis = models.IntegerField(default=0)
   bos = models.IntegerField(default=0)

   def __str__(self):
      return f'{self.tarih}...{self.deneme} : {self.user.get_full_name()} ({self.ders})'
   
   class Meta:
        verbose_name_plural = "Deneme Sonuçları"
   
class TestCozum(models.Model):
   test  = models.ForeignKey(Test,on_delete=models.CASCADE)
   user  = models.ForeignKey(User,on_delete=models.CASCADE)
   tarih = models.DateField()
   dogru = models.IntegerField(default=0)
   yanlis = models.IntegerField(default=0)
   bos = models.IntegerField(default=0)
   
   def __str__(self):
      return f'{self.tarih}...{self.test} : {self.user.get_full_name()} ({self.dogru}-{self.yanlis}-{self.bos})'
   
   class Meta:
        verbose_name_plural = "Test Çözümleri"

class GTTCozum(models.Model):
   test= models.ForeignKey(GenelTaramaTest,on_delete=models.CASCADE)
   user = models.ForeignKey(User,on_delete=models.CASCADE)
   tarih = models.DateField()
   dogru = models.IntegerField(default=0)
   yanlis = models.IntegerField(default=0)
   bos = models.IntegerField(default=0)

   def __str__(self):
      return f'{self.tarih}...{self.test.ders}...{self.test.adi} : {self.user.get_full_name()} ({self.dogru}-{self.yanlis}-{self.bos}))'
   
   class Meta:
        verbose_name_plural = "Genel Tarama Test Sonuçları"

#Boş bırakılan veya yanlış yapılan sorular
class Soru (models.Model):
   user = models.ForeignKey(User, on_delete=models.CASCADE, null=True,related_name= 'soru_user')
   konu = models.ForeignKey(Konu,on_delete=models.CASCADE, null= True)
   ders = models.ForeignKey(Ders,on_delete=models.CASCADE, null=True)
   soru  = models.ImageField(null=True)
   cozum = models.ImageField(null=True)
   yanlis = models.BooleanField(default=True) #True yanlis False Bos
   goster= models.BooleanField(default=True) # goster yada gosterme

   class Meta:
        verbose_name_plural = "Sorular"
   
   def __str__(self):
      return f'{self.konu} - {self.id}'
   
   def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.img:
            img1= Image.open(self.soru.path)
            if img1.height > 600 or img1.width > 600:
                output_size = (600, 600)
                img1.thumbnail(output_size)
                img1.save(self.soru.path)
        if self.cozum:
            img2= Image.open(self.cozum.path)
            if img2.height > 600 or img2.width > 600:
                output_size = (600, 600)
                img2.thumbnail(output_size)
                img2.save(self.cozum.path)
   

class Yazar (models.Model):
   adi  = models.CharField (max_length=150)
   
   def __str__(self):
      return self.__all__
   
   class Meta:
        verbose_name_plural = "Yazarlar"

class Kitap (models.Model):
   adi  = models.CharField (max_length=150)
   yayin = models.ForeignKey(YayinEvi,on_delete=models.CASCADE, null=True)
   yazar = models.ForeignKey(Yazar, on_delete=models.CASCADE, null= True)
   sayfa_sayisi= models.IntegerField(default=0)

   def __str__(self):
      return self.__all__
   
   class Meta:
        verbose_name_plural = "Kitaplar"
# Ogrencilerin okuma takibi
class Okuma (models.Model):
   kitap = models.ForeignKey(Kitap,on_delete=models.CASCADE)
   user  = models.ForeignKey(User, on_delete= models.CASCADE)
   tarih = models.DateField()
   sayfa = models.IntegerField(default=0)

   def __str__(self):
      return self.__all__
   
   class Meta:
        verbose_name_plural = "Okumalar"