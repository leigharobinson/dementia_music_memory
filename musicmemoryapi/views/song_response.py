from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
# STATUS USER FOR DESTROY/UPDATE METHODS
from rest_framework import status
from musicmemoryapi.models import SongResponse
from musicmemoryapi.models import Patient
from musicmemoryapi.models import Song, Caretaker
from .eye_contact import EyeContact
from .talkativeness import Talkativeness
from .mood import Mood
from .movement import Movement
from .vocalization import Vocalization
from .liked_song import LikedSong
from django.contrib.auth.models import User


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
        fields = ('id', 'caretaker_id', 'song', 'song_id', 'patient', 'patient_id', 'eye_contact_id', 'eye_contact',
                  'talkativeness_id', 'talkativeness', 'mood_id', 'mood', 'movement_id', 'movement',
                  'vocalization_id', 'notes', 'vocalization', 'liked_song_id', 'liked_song')
        depth = 3


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
        caretaker = Caretaker.objects.get(pk=request.data["caretaker_id"])

        newsongresponse = SongResponse()
        newsongresponse.patient = patient
        newsongresponse.song = song
        newsongresponse.eye_contact = eye_contact
        newsongresponse.talkativeness = talkativeness
        newsongresponse.mood = mood
        newsongresponse.movement = movement
        newsongresponse.vocalization = vocalization
        newsongresponse.liked_song = liked_song
        newsongresponse.caretaker = caretaker
        newsongresponse.notes = request.data["notes"]

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
        patient_id = self.request.query_params.get('patient_id', None)

        user = User.objects.get(pk=request.user.id)
        caretaker = Caretaker.objects.get(pk=user.caretaker.id)
        # 8000/songresponses
        song_responses = SongResponse.objects.filter(caretaker_id=caretaker.id)
        # song_responses = SongResponse.objects.all()
        # 8000/songresonponses?patient_id=5
        if patient_id is not None:
            song_responses = SongResponse.objects.filter(caretaker_id=caretaker.id,
                                                         patient_id=int(patient_id))

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

    def update(self, request, pk=None):
        """Handle PUT requests for Movement

        Returns:
            Response -- Empty body with 204 status code
        """
        SongResponse = SongResponse.objects.get(pk=pk)
        SongResponse.eye_contact = request.data["eye_contact"]
        SongResponse.talkativeness = request.data["talkativeness"]
        SongResponse.vocalization = request.data["vocalization"]
        SongResponse.mood = request.data["mood"]
        SongResponse.movement = request.data["movement"]
        SongResponse.liked_song = request.data["liked_song"]
        SongResponse.notes = request.data["notes"]
        SongResponse.save()

        return Response({}, status=status.HTTP_204_NO_CONTENT)
