from  django.urls import re_path, include, path
from profiller.api.views import ProfilViewSet,ProfilFotoUpdateView
from profiller.api.views import OkulViewSet,DenemeSonucuViewSet, DersViewSet, KonuViewSet
from profiller.api.views import YayinEviViewSet, TestViewSet, GTTViewSet, DenemeViewSet, TestSonucuViewSet
from profiller.api.views import GTTSonucuViewSet, SoruViewSet, YazarViewSet, KitapViewSet, OkumaViewSet

from .views import MyTokenObtainPairView
from rest_framework_simplejwt.views import TokenRefreshView

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'profiller', ProfilViewSet)
router.register(r'okullar', OkulViewSet)
router.register(r'dersler', DersViewSet)
router.register(r'konular', KonuViewSet, basename= 'konular')    
router.register(r'yayinevleri', YayinEviViewSet)
router.register(r'testler', TestViewSet)
router.register(r'geneltestler', GTTViewSet)
router.register(r'denemeler', DenemeViewSet)
router.register(r'denemesonuclari', DenemeSonucuViewSet,basename= 'denemesonuclari')
router.register(r'testsonuclari', TestSonucuViewSet, basename= 'testsonuclari')
router.register(r'gttsonuclari', GTTSonucuViewSet, basename= 'gttsonuclari')
router.register(r'sorular', SoruViewSet,basename= 'sorular')
router.register(r'yazarlar', YazarViewSet)
router.register(r'kitaplar', KitapViewSet)
router.register(r'okumalar', OkumaViewSet,basename= 'okumalar')
 
urlpatterns = [
    path('', include(router.urls)),
    re_path(r'profil_foto/',ProfilFotoUpdateView.as_view(),name='profil-foto'),
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]