from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
# STATUS USER FOR DESTROY/UPDATE METHODS
from rest_framework import status
from musicmemoryapi.models import EyeContact


class EyeContactSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = EyeContact
        url = serializers.HyperlinkedIdentityField(
            view_name='EyeContacts',
            lookup_field='id'
        )
        fields = ('id', 'description')


class EyeContactView(ViewSet):

    """EyeContacts for MusicMemory API"""

    def list(self, request):
        """Handle GET requests to EyeContact resource

        Returns:
            Response -- JSON serialized list of EyeContact
        """
        eye_contacts = EyeContact.objects.all()  # This is my query to the database
        serializer = EyeContactSerializer(
            eye_contacts, many=True, context={'request': request})
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        """Handle GET requests for single eye contact

        Returns:
            Response -- JSON serialized eye contact instance
        """
        try:
            eye_contact = EyeContact.objects.get(pk=pk)
            serializer = EyeContactSerializer(
                eye_contact, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def update(self, request, pk=None):
        """Handle PUT requests for Mood

        Returns:
            Response -- Empty body with 204 status code
        """
        eye_contact = EyeContact.objects.get(pk=pk)
        eye_contact.description = request.data["description"]
        eye_contact.save()

        return Response({}, status=status.HTTP_204_NO_CONTENT)
