from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
# STATUS USER FOR DESTROY/UPDATE METHODS
from rest_framework import status
from musicmemoryapi.models import Facility


class FacilitySerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Facility
        url = serializers.HyperlinkedIdentityField(
            view_name='facilities',
            lookup_field='id'
        )
        fields = ('id', 'facility_name', 'address')


class FacilityView(ViewSet):

    """Facility for MusicMemory API"""

    def create(self, request):
        """Handle POST operations

        Returns:
            Response -- JSON serialized facility instance
        """
        newfacility = Facility()
        newfacility.facility_name = request.data["facility_name"]
        newfacility.address = request.data["address"]
        newfacility.save()

        serializer = FacilitySerializer(
            newfacility, context={'request': request})

        return Response(serializer.data)

    def list(self, request):
        """Handle GET requests to park areas resource

        Returns:
            Response -- JSON serialized list of park areas
        """
        facilities = Facility.objects.all()  # This is my query to the database
        serializer = FacilitySerializer(
            facilities, many=True, context={'request': request})
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        """Handle GET requests for single park area

        Returns:
            Response -- JSON serialized park area instance
        """
        try:
            facility = Facility.objects.get(pk=pk)
            serializer = FacilitySerializer(
                facility, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)
