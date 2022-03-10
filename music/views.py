from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import SongsSerializer
from .models import Songs







@api_view(['GET'])
def songs_list(request):

  # Creating variable and setting it to our imported class then adding all objects to it
  songs = Songs.objects.all()  


  # Converting into python dictionary (then into Json) using the class SongsSerializer we created in serializers.py
  serializer = SongsSerializer(songs, many=True) 

  # returning the response as the data collected and converted in the serializer
  return Response(serializer.data)

