from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
# STATUS USER FOR DESTROY/UPDATE METHODS
from rest_framework import status
from musicmemoryapi.models import SongResponse
from musicmemoryapi.models import Patient
from musicmemoryapi.models import Song
from .eye_contact import EyeContact
from .talkativeness import Talkativeness
from .mood import Mood
from .movement import Movement
from .vocalization import Vocalization
from .liked_song import LikedSong


class SongResponseSerializer(serializers.HyperlinkedModelSerializer):
    """JSON serializer for Patient and Song

    Arguments:
        serializers.HyperlinkedModelSerializer
    """

    class Meta:
        model = SongResponse
        url = serializers.HyperlinkedIdentityField(
            view_name='song_response',
            lookup_field='id'
        )
        fields = ('id', 'song', 'song_id', 'patient', 'patient_id', 'eye_contact_id', 'eye_contact',
                  'talkativeness_id', 'talkativeness', 'mood_id', 'mood', 'movement_id', 'movement',
                  'vocalization_id', 'vocalization', 'liked_song_id', 'liked_song')
        depth = 2


class SongResponseView(ViewSet):

    """Patients and Songss for MusicMemory API"""

    def create(self, request):

        print("EYE CONTACT ID", request.data["eye_contact_id"])

        """Handle POST operations

        Returns:
            Response -- JSON serialized patients and songs instance
        """
        patient = Patient.objects.get(pk=request.data["patient_id"])
        song = Song.objects.get(pk=request.data["song_id"])
        eye_contact = EyeContact.objects.get(pk=request.data["eye_contact_id"])
        talkativeness = Talkativeness.objects.get(
            pk=request.data["talkativeness_id"])
        mood = Mood.objects.get(pk=request.data["mood_id"])
        movement = Movement.objects.get(pk=request.data["movement_id"])
        vocalization = Vocalization.objects.get(
            pk=request.data["vocalization_id"])
        liked_song = LikedSong.objects.get(pk=request.data["liked_song_id"])

        newsongresponse = SongResponse()
        newsongresponse.patient = patient
        newsongresponse.song = song
        newsongresponse.eye_contact = eye_contact
        newsongresponse.talkativeness = talkativeness
        newsongresponse.mood = mood
        newsongresponse.movement = movement
        newsongresponse.vocalization = vocalization
        newsongresponse.liked_song = liked_song

        newsongresponse.save()

        serializer = SongResponseSerializer(
            newsongresponse, context={'request': request})

        return Response(serializer.data)

    def list(self, request):
        """Handle GET requests to park areas resource
        Returns:
            Response -- JSON serialized list of park areas
        """
        # direction = self.request.query_params.get('direction', None)
        patient = Patient.objects.filter(
            patient_id=request.query_params["patient_id"])
        song_responses = SongResponse.objects.filter(patient_id=patient.id)
        # This is my query to the database
        serializer = SongResponseSerializer(
            song_responses, many=True, context={'request': request})
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        """Handle GET requests for single park area

        Returns:
            Response -- JSON serialized park area instance
        """
        try:
            song_response = SongResponse.objects.get(pk=pk)
            serializer = SongResponseSerializer(
                song_response, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)
