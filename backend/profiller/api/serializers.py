from profiller.models import Profil
from rest_framework import serializers

from ..models import User, Okul, Ders, Konu, YayinEvi, GTTCozum
from ..models import Test, GenelTaramaTest, Deneme, DenemeSonucu, TestCozum, Soru, Yazar, Kitap, Okuma

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class ProfilSerializer (serializers.ModelSerializer):
    #user = UserSerializer(many= False,read_only=True)
    user = serializers.StringRelatedField(read_only=True)
    foto = serializers.ImageField(read_only=True)
    grup = serializers.StringRelatedField(read_only=True)
    
    class Meta:
        model = Profil
        fields = '__all__'
    

class ProfilFotoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profil
        fields = ['foto']

class OkulSerializer(serializers.ModelSerializer):
    class Meta:
        model=Okul
        fields = '__all__'
        read_only_fields = ['id']


class DersSerializer (serializers.ModelSerializer):

    class Meta:
        model= Ders
        fields = '__all__'
        read_only_fields = ['id']

class KonuSerializer (serializers.ModelSerializer):

    class Meta:
        model= Konu
        fields = '__all__'
        read_only_fields = ['id']

class YayinEviSerializer(serializers.ModelSerializer):
    
    class Meta:
        model= YayinEvi
        fields = '__all__'
        read_only_fields = ['id']

class TestSerializer(serializers.ModelSerializer):
    #konu = serializers.StringRelatedField()
    #ders = serializers.StringRelatedField()
    class Meta:
        model= Test
        fields = '__all__'
        read_only_fields = ['id']

class GTTSerializer(serializers.ModelSerializer):
    
    class Meta:
        model= GenelTaramaTest
        fields = '__all__'
        read_only_fields = ['id']

class DenemeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model= Deneme
        fields = '__all__'
        read_only_fields = ['id']


class DenemeSonucuSerializer(serializers.ModelSerializer):
    # user = serializers.StringRelatedField(read_only=True)
    # deneme = serializers.StringRelatedField(read_only=True)
    # ders = serializers.StringRelatedField(read_only=True)

    class Meta:
        model= DenemeSonucu
        fields = '__all__'
        read_only_fields = ['id']

class TestSonucuSerializer(serializers.ModelSerializer):
    #user = serializers.StringRelatedField(read_only=True)
    #test = TestSerializer()
    class Meta:
        model= TestCozum
        fields = '__all__'
        read_only_fields = ['id']

class GTTSonucuSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    class Meta:
        model= GTTCozum
        fields = '__all__'
        read_only_fields = ['id']

class SoruSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    img = serializers.ImageField(read_only=True)
    cozum = serializers.ImageField(read_only=True)
    
    class Meta:
        model= Soru
        fields = '__all__'
        read_only_fields = ['id']

class YazarSerializer(serializers.ModelSerializer):
    
    class Meta:
        model= Yazar
        fields = '__all__'
        read_only_fields = ['id']

class KitapSerializer(serializers.ModelSerializer):
    
    class Meta:
        model= Kitap
        fields = '__all__'
        read_only_fields = ['id']

class OkumaSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    kitap = serializers.ImageField(read_only=True)
    
    class Meta:
        model= Okuma
        fields = '__all__'
        read_only_fields = ['id']

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['username'] = user.username
        return token
    
