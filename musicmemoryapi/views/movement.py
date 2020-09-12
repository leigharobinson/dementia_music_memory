from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
# STATUS USER FOR DESTROY/UPDATE METHODS
from rest_framework import status
from musicmemoryapi.models import Movement


class MovementSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Movement
        url = serializers.HyperlinkedIdentityField(
            view_name='Movements',
            lookup_field='id'
        )
        fields = ('id', 'description')


class MovementView(ViewSet):

    """Movement for MusicMemory API"""

    def list(self, request):
        """Handle GET requests to movement resource

        Returns:
            Response -- JSON serialized list of movement
        """
        movements = Movement.objects.all()  # This is my query to the database
        serializer = MovementSerializer(
            movements, many=True, context={'request': request})
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        """Handle GET requests for single movement rating

        Returns:
            Response -- JSON serialized movement instance
        """
        try:
            movement = Movement.objects.get(pk=pk)
            serializer = MovementSerializer(
                movement, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def update(self, request, pk=None):
        """Handle PUT requests for Movement

        Returns:
            Response -- Empty body with 204 status code
        """
        movement = Movement.objects.get(pk=pk)
        movement.description = request.data["description"]
        movement.save()

        return Response({}, status=status.HTTP_204_NO_CONTENT)
