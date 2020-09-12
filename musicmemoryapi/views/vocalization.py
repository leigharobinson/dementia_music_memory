from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
# STATUS USER FOR DESTROY/UPDATE METHODS
from rest_framework import status
from musicmemoryapi.models import Vocalization


class VocalizationSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Vocalization
        url = serializers.HyperlinkedIdentityField(
            view_name='Vocalizations',
            lookup_field='id'
        )
        fields = ('id', 'description')


class VocalizationView(ViewSet):

    """Movement for MusicMemory API"""

    def list(self, request):
        """Handle GET requests to movement resource

        Returns:
            Response -- JSON serialized list of movement
        """
        vocalizations = Vocalization.objects.all()  # This is my query to the database
        serializer = VocalizationSerializer(
            vocalizations, many=True, context={'request': request})
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        """Handle GET requests for single movement rating

        Returns:
            Response -- JSON serialized movement instance
        """
        try:
            vocalization = Vocalization.objects.get(pk=pk)
            serializer = VocalizationSerializer(
                vocalization, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def update(self, request, pk=None):
        """Handle PUT requests for Movement

        Returns:
            Response -- Empty body with 204 status code
        """
        vocalization = Vocalization.objects.get(pk=pk)
        vocalization.description = request.data["description"]
        vocalization.save()

        return Response({}, status=status.HTTP_204_NO_CONTENT)
