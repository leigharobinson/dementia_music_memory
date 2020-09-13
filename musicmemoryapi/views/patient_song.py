from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
# STATUS USER FOR DESTROY/UPDATE METHODS
from rest_framework import status
from musicmemoryapi.models import PatientSong
from musicmemoryapi.models import Patient
from musicmemoryapi.models import Song


class PatientSongSerializer(serializers.HyperlinkedModelSerializer):
    """JSON serializer for Patient and Song

    Arguments:
        serializers.HyperlinkedModelSerializer
    """

    class Meta:
        model = PatientSong
        url = serializers.HyperlinkedIdentityField(
            view_name='patients_songs',
            lookup_field='id'
        )
        fields = ('id', 'song', 'song_id', 'patient', 'patient_id')
        depth = 2


class PatientSongView(ViewSet):

    """Patients and Songss for MusicMemory API"""

    def create(self, request):
        """Handle POST operations

        Returns:
            Response -- JSON serialized patients and songs instance
        """
        patient = Patient.objects.get(pk=request.data["patient_id"])
        song = Song.objects.get(pk=request.data["song_id"])

        newpatientsong = PatientSong()
        newpatientsong.patient = patient
        newpatientsong.song = song

        newpatientsong.save()

        serializer = PatientSongSerializer(
            newpatientsong, context={'request': request})

        return Response(serializer.data)

    def list(self, request):
        """Handle GET requests to park areas resource

        Returns:
            Response -- JSON serialized list of park areas
        """
        patients_songs = PatientSong.objects.all(
        )  # This is my query to the database
        serializer = PatientSongSerializer(
            patients_songs, many=True, context={'request': request})
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        """Handle GET requests for single park area

        Returns:
            Response -- JSON serialized park area instance
        """
        try:
            patient_song = PatientSong.objects.get(pk=pk)
            serializer = PatientSongSerializer(
                patient_song, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)
