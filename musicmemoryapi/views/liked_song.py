from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
# STATUS USER FOR DESTROY/UPDATE METHODS
from rest_framework import status
from musicmemoryapi.models import LikedSong


class LikedSongSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = LikedSong
        url = serializers.HyperlinkedIdentityField(
            view_name='LikedSongs',
            lookup_field='id'
        )
        fields = ('id', 'description')


class LikedSongView(ViewSet):

    """Liked Song Scale for MusicMemory API"""

    def list(self, request):
        """Handle GET requests to Liked Songs Scale resource

        Returns:
            Response -- JSON serialized list of liked songs
        """
        liked_songs = LikedSong.objects.all()  # This is my query to the database
        serializer = LikedSongSerializer(
            liked_songs, many=True, context={'request': request})
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        """Handle GET requests for single liked song rating

        Returns:
            Response -- JSON serialized liked song instance
        """
        try:
            liked_song = LikedSong.objects.get(pk=pk)
            serializer = MovementSerializer(
                liked_song, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def update(self, request, pk=None):
        """Handle PUT requests for liked song

        Returns:
            Response -- Empty body with 204 status code
        """
        liked_song = LikedSong.objects.get(pk=pk)
        liked_song.description = request.data["description"]
        liked_song.save()

        return Response({}, status=status.HTTP_204_NO_CONTENT)
