from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions

from profiller.models import Profil, Okul, Ders, Konu, YayinEvi,Test, DenemeSonucu
from profiller.models import GenelTaramaTest, Deneme, TestCozum, GTTCozum, Soru, Yazar, Kitap, Okuma

from profiller.api.serializers import ProfilSerializer,ProfilFotoSerializer
from profiller.api.serializers import OkulSerializer,DenemeSonucuSerializer
from profiller.api.serializers import DersSerializer, KonuSerializer, YayinEviSerializer, TestSerializer
from profiller.api.serializers import GTTSerializer, DenemeSerializer, TestSonucuSerializer
from profiller.api.serializers import GTTSonucuSerializer, SoruSerializer, YazarSerializer, KitapSerializer
from profiller.api.serializers import OkumaSerializer

from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.viewsets import ModelViewSet
from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins
from profiller.api.permissions import KendiProfiliYadaReadOnly

from django_filters.rest_framework import DjangoFilterBackend

from .serializers import MyTokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

class ProfilViewSet (
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    GenericViewSet
):
    queryset = Profil.objects.all()
    serializer_class = ProfilSerializer
    permission_classes = [IsAuthenticated,KendiProfiliYadaReadOnly]

class ProfilFotoUpdateView(generics.UpdateAPIView):
    serializer_class = ProfilFotoSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        profil_nesnesi = self.request.user.profil_user
        return profil_nesnesi

class OkulViewSet (ModelViewSet):
    queryset = Okul.objects.all()
    serializer_class = OkulSerializer
    permission_classes = [DjangoModelPermissions]

class DersViewSet (ModelViewSet):
    queryset = Ders.objects.all()
    serializer_class = DersSerializer
    permission_classes = [DjangoModelPermissions]

class KonuViewSet (ModelViewSet):
    queryset = Konu.objects.all()
    serializer_class = KonuSerializer
    permission_classes = [DjangoModelPermissions]

class YayinEviViewSet (ModelViewSet):
    queryset = YayinEvi.objects.all()
    serializer_class = YayinEviSerializer
    permission_classes = [DjangoModelPermissions]

class TestViewSet (ModelViewSet):
    queryset = Test.objects.all()
    serializer_class = TestSerializer
    permission_classes = [DjangoModelPermissions]

class GTTViewSet (ModelViewSet):
    queryset = GenelTaramaTest.objects.all()
    serializer_class = GTTSerializer
    permission_classes = [DjangoModelPermissions]

class DenemeViewSet (ModelViewSet):
    queryset = Deneme.objects.all()
    serializer_class = DenemeSerializer
    permission_classes = [DjangoModelPermissions]

class DenemeSonucuViewSet (ModelViewSet):
    #queryset = DenemeSonucu.objects.all()
    serializer_class = DenemeSonucuSerializer
    permission_classes = [DjangoModelPermissions]

    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['user', 'deneme']
    
    def get_queryset(self):
        queryset = DenemeSonucu.objects.all()
        username = self.request.query_params.get('username',None)

        if username is not None:
            queryset= queryset.filter(user__username=username)
        return queryset

class TestSonucuViewSet (ModelViewSet):
    queryset = TestCozum.objects.all()
    serializer_class = TestSonucuSerializer
    permission_classes = [DjangoModelPermissions]

class GTTSonucuViewSet (ModelViewSet):
    queryset = GTTCozum.objects.all()
    serializer_class = GTTSonucuSerializer
    permission_classes = [DjangoModelPermissions]

class SoruViewSet (ModelViewSet):
    queryset = Soru.objects.all()
    serializer_class = SoruSerializer
    permission_classes = [DjangoModelPermissions]

class YazarViewSet (ModelViewSet):
    queryset = Yazar.objects.all()
    serializer_class = YazarSerializer
    permission_classes = [DjangoModelPermissions]

class KitapViewSet (ModelViewSet):
    queryset = Kitap.objects.all()
    serializer_class = KitapSerializer
    permission_classes = [DjangoModelPermissions]

class OkumaViewSet (ModelViewSet):
    queryset = Okuma.objects.all()
    serializer_class = OkumaSerializer
    permission_classes = [DjangoModelPermissions]

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

