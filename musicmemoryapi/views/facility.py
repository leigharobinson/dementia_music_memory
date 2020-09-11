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
            view_name='facility',
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
