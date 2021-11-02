from django.http import response
from django.shortcuts import render
from .models import Song
from .serializers import SongSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


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
    
class SongDetail(APIView):
    
    # def get_single(self, id):
    #     song = Song.objects.get_object(id)
    #     serializer = SongSerializer(song)
    #     return Response(serializer.data)        
    def get_object(self, id):
        try:
            return Song.objects.get(id=id)
        except: Song.DoesNotExist 
        raise Http404
    
    def get(self, request, id):
        song = self.get_object(id)
        serializer = SongSerializer(song)
        return Response(serializer.data)
    
    def put(self, request, id):
        song = self.get_object(id)
        serializer = SongSerializer(song, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        song = self.get_object(id)
        serializer = SongSerializer(song)
        song.delete()
        return Response(serializer.data, status=status.HTTP_200_OK)