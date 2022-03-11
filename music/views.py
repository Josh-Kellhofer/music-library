from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import SongsSerializer
from .models import Songs


@api_view(['GET', 'POST'])
def songs_list(request):

  # Separating GET from POST Method within the same function
  if request.method == 'GET':

  # Creating variable and setting it to our imported class then adding all objects to it
    songs = Songs.objects.all()  


  # Converting into python dictionary (then into Json) using the class SongsSerializer we created in serializers.py
    serializer = SongsSerializer(songs, many=True) 

  # returning the response as the data collected and converted in the serializer
    return Response(serializer.data)

  # Separating GET from POST Method within the same function
  elif request.method == 'POST':
    serializer = SongsSerializer(data=request.data)
    # Validating data to make sure all data attempting to be added is valid (ex: Someone adding a model parameter vs. using existing ones)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)
   
    
@api_view(['GET', 'PUT', 'DELETE'])
# pk (primary key) goes to views, path with int to ensure it is an integer since this is the id and id's are always integers. 
def song_detail(request, pk):
  # Querying songs table to get specific song utilizing the imported shortcut (line 1 above)
    song = get_object_or_404(Songs, pk=pk)
    # Separating GET and PUT requests.
    if request.method == 'GET':
      serializer = SongsSerializer(song);
      return Response(serializer.data)
    elif request.method == 'PUT':
      # song is current version of the object; data=request.data compares it to current version
      serializer = SongsSerializer(song, data=request.data)
      # Validation
      serializer.is_valid(raise_exception=True)
      # If valid, telling it to save the PUT data
      serializer.save()
      return Response(serializer.data)
    # Separating DELETE from GET & PUT requests
    elif request.method == 'DELETE':
      song.delete()
      return Response(status=status.HTTP_204_NO_CONTENT)
      
 

 


