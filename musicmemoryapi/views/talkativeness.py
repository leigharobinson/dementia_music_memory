from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
# STATUS USER FOR DESTROY/UPDATE METHODS
from rest_framework import status
from musicmemoryapi.models import Talkativeness


class TalkativenessSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Talkativeness
        url = serializers.HyperlinkedIdentityField(
            view_name='Talkativeness',
            lookup_field='id'
        )
        fields = ('id', 'description')


class TalkativenessView(ViewSet):

    """Movement for MusicMemory API"""

    def list(self, request):
        """Handle GET requests to movement resource

        Returns:
            Response -- JSON serialized list of movement
        """
        talkativeness = Talkativeness.objects.all()  # This is my query to the database
        serializer = TalkativenessSerializer(
            talkativeness, many=True, context={'request': request})
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        """Handle GET requests for single movement rating

        Returns:
            Response -- JSON serialized movement instance
        """
        try:
            talkativeness = Talkativeness.objects.get(pk=pk)
            serializer = TalkativenessSerializer(
                talkativeness, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def update(self, request, pk=None):
        """Handle PUT requests for Movement

        Returns:
            Response -- Empty body with 204 status code
        """
        talkativeness = Talkativeness.objects.get(pk=pk)
        talkativeness.description = request.data["description"]
        talkativeness.save()

        return Response({}, status=status.HTTP_204_NO_CONTENT)
