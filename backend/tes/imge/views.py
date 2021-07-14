from imge.serializers import ImageSerializer
from django.shortcuts import render
from .models import Image
from rest_framework import viewsets
from .serializers import ImageSerializer

# Create your views here.

class ImageViewSet(viewsets.ModelViewSet):
    """
    """
    serializer_class = ImageSerializer
    queryset = Image.objects.all()