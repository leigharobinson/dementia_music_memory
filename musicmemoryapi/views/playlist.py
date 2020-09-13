from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
# STATUS USER FOR DESTROY/UPDATE METHODS
from rest_framework import status
from musicmemoryapi.models import CaretakerPatient
from musicmemoryapi.models import Song
from musicmemoryapi.models import Playlist


class PlaylistSerializer(serializers.HyperlinkedModelSerializer):
    """JSON serializer for Patient and Caretaker

    Arguments:
        serializers.HyperlinkedModelSerializer
    """

    class Meta:
        model = Playlist
        url = serializers.HyperlinkedIdentityField(
            view_name='playlists',
            lookup_field='id'
        )
        fields = ('id', 'caretaker_patient',
                  'caretaker_patient_id', 'song', 'song_id')
        depth = 2


class PlaylistView(ViewSet):

    """Playlists for MusicMemory API"""

    def create(self, request):
        """Handle POST operations

        Returns:
            Response -- JSON serialized patients and caretakers instance
        """
        song = Song.objects.get(pk=request.data["song_id"])
        caretaker_patient = CaretakerPatient.objects.get(
            pk=request.data["caretaker_patient_id"])

        newplaylist = Playlist()
        newplaylist.song = song
        newplaylist.caretaker_patient = caretaker_patient

        newplaylist.save()

        serializer = PlaylistSerializer(
            newplaylist, context={'request': request})

        return Response(serializer.data)

    def list(self, request):
        """Handle GET requests to park areas resource

        Returns:
            Response -- JSON serialized list of park areas
        """
        playlists = Playlist.objects.all(
        )  # This is my query to the database
        serializer = PlaylistSerializer(
            playlists, many=True, context={'request': request})
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        """Handle GET requests for single park area

        Returns:
            Response -- JSON serialized park area instance
        """
        try:
            playlist = Playlist.objects.get(pk=pk)
            serializer = PlaylistSerializer(
                playlist, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def destroy(self, request, pk=None):
        """Handle DELETE requests for a single product

        Returns:
            Response -- 200, 404, or 500 status code
        """
        try:
            playlist = Playlist.objects.get(pk=pk)
            playlist.delete()

            return Response({}, status=status.HTTP_204_NO_CONTENT)

        except Playlist.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def update(self, request, pk=None):
        """Handle PUT requests for product quantity

        Returns:
            Response -- Empty body with 204 status code
        """
        playlist = Playlist.objects.get(pk=pk)
        playlist.song = request.data["song"]
        playlist.save()

        return Response({}, status=status.HTTP_204_NO_CONTENT)
