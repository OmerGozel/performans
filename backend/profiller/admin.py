from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from profiller.models import Okul, Profil, Test
from profiller.models import Deneme, YayinEvi, Ders, DenemeSonucu
from profiller.models import Konu, Test, TestCozum, GenelTaramaTest, GTTCozum, Soru, Yazar, Kitap, Okuma
# Register your models here.

admin.site.register(Okul)
admin.site.register(Profil)
admin.site.register(YayinEvi)
admin.site.register(Ders)
admin.site.register(DenemeSonucu)
admin.site.register(Test)
admin.site.register(TestCozum)
admin.site.register(GenelTaramaTest)
admin.site.register(GTTCozum)
admin.site.register(Soru)
admin.site.register(Yazar)
admin.site.register(Kitap)
admin.site.register(Okuma)

# Define an inline admin descriptor for Employee model
# which acts a bit like a singleton
class ProfilInline(admin.StackedInline):
    model = Profil
    can_delete = False
    verbose_name_plural = "Profiller"


# Define a new User admin
class UserAdmin(BaseUserAdmin):
    inlines = [ProfilInline]


# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)

class DenemeAdmin(admin.ModelAdmin):
  list_display = ("adi", "yayin", "sinifi",)
  
admin.site.register(Deneme, DenemeAdmin)

class KonuAdmin(admin.ModelAdmin):
  list_display = ("adi", "ders", "parent","sinifi")
  
admin.site.register(Konu, KonuAdmin)




