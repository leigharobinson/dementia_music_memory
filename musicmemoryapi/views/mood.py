from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
# STATUS USER FOR DESTROY/UPDATE METHODS
from rest_framework import status
from musicmemoryapi.models import Mood


class MoodSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Mood
        url = serializers.HyperlinkedIdentityField(
            view_name='Moods',
            lookup_field='id'
        )
        fields = ('id', 'description')


class MoodView(ViewSet):

    """Moods for MusicMemory API"""

    def list(self, request):
        """Handle GET requests to mood resource

        Returns:
            Response -- JSON serialized list of mood
        """
        moods = Mood.objects.all()  # This is my query to the database
        serializer = MoodSerializer(
            moods, many=True, context={'request': request})
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        """Handle GET requests for single mood

        Returns:
            Response -- JSON serialized mood instance
        """
        try:
            mood = Mood.objects.get(pk=pk)
            serializer = MoodSerializer(
                mood, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def update(self, request, pk=None):
        """Handle PUT requests for Mood

        Returns:
            Response -- Empty body with 204 status code
        """
        mood = Mood.objects.get(pk=pk)
        mood.description = request.data["description"]
        mood.save()

        return Response({}, status=status.HTTP_204_NO_CONTENT)
