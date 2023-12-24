from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin
from rest_framework import generics
from profiller.api.serializers import ProfilSerializer, VeliSerializer
from profiller.models import Profil, Veli
# Create your views here.
