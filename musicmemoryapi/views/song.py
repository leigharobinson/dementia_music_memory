from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
# STATUS USER FOR DESTROY/UPDATE METHODS
from rest_framework import status
from musicmemoryapi.models import Song


class SongSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Song
        url = serializers.HyperlinkedIdentityField(
            view_name='Songs',
            lookup_field='id'
        )
        fields = ('id', 'position', 'artist', 'song_title', 'year')


class SongView(ViewSet):

    """Songs for MusicMemory API"""

    def list(self, request):
        """Handle GET requests to park areas resource

        Returns:
            Response -- JSON serialized list of park areas
        """
        # THis is where i need to get the patient by id and then find their YOB and calculate the
        # correct  song range to give back
        songs = Song.objects.all()  # This is my query to the database
        serializer = SongSerializer(
            songs, many=True, context={'request': request})
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        """Handle GET requests for single park area

        Returns:
            Response -- JSON serialized park area instance
        """
        try:
            song = Song.objects.get(pk=pk)
            serializer = SongSerializer(
                song, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)
