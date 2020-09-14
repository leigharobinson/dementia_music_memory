from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
# STATUS USER FOR DESTROY/UPDATE METHODS
from rest_framework import status
from musicmemoryapi.models import Song
from musicmemoryapi.models import Patient


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
        print("somestring ")
        patient_id = request.query_params.get(
            'patient_id', None)

        print("patient id", patient_id)

        year = request.query_params.get("birth_year", None)

        songlist = []

        if patient_id is not None:
            patient = Patient.objects.get(pk=patient_id)
            print("patient id", patient_id)
            yob = int(patient.year_of_birth)
            start_year = (yob + 10)
            last_year = (yob + 21)

            for i in range(start_year, last_year):

                stringify = str(i)
                songs = Song.objects.filter(year=i)
                for song in songs:
                    songlist.append(song)

        if year is not None:
            yob = int(year)
            start_year = (yob + 10)
            last_year = (yob + 21)

            for i in range(start_year, last_year):
                stringify = str(i)
                songs = Song.objects.filter(year=i)
                for song in songs:
                    songlist.append(song)

        # This is my query to the database
        serializer = SongSerializer(
            songlist, many=True, context={'request': request})
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
