from django.http import response
from django.shortcuts import render
from .models import Song
from .serializers import SongSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer

# Create your views here.
class SongList(APIView):
    
    def get(self, request):
        song = Song.objects.all()
        serializer = SongSerializer(song, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = SongSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    @api_view(('GET',))
    def get_single(self, id):
        song = Song.objects.get(id=id)
        serializer = SongSerializer(song, many=False)
        return Response(serializer.data)
