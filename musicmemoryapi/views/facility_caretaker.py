from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
# STATUS USER FOR DESTROY/UPDATE METHODS
from rest_framework import status
from musicmemoryapi.models import FacilityCaretaker
from musicmemoryapi.models import Facility
from musicmemoryapi.models import Caretaker


class FacilityCaretakerSerializer(serializers.HyperlinkedModelSerializer):
    """JSON serializer for Facility and Caretaker

    Arguments:
        serializers.HyperlinkedModelSerializer
    """

    class Meta:
        model = FacilityCaretaker
        url = serializers.HyperlinkedIdentityField(
            view_name='facilities_caretakers',
            lookup_field='id'
        )
        fields = ('id', 'caretaker', 'caretaker_id', 'facility', 'facility_id')
        depth = 2


class FacilityCaretakerView(ViewSet):

    """Facilities and Caretakers for MusicMemory API"""

    def create(self, request):
        """Handle POST operations

        Returns:
            Response -- JSON serialized facility instance
        """
        facility = Facility.objects.get(pk=request.data["facility_id"])
        caretaker = Caretaker.objects.get(pk=request.data["caretaker_id"])

        newfacilitycaretaker = FacilityCaretaker()
        newfacilitycaretaker.facility = facility
        newfacilitycaretaker.caretaker = caretaker

        newfacilitycaretaker.save()

        serializer = FacilityCaretakerSerializer(
            newfacilitycaretaker, context={'request': request})

        return Response(serializer.data)

    def list(self, request):
        """Handle GET requests to park areas resource

        Returns:
            Response -- JSON serialized list of park areas
        """
        facilities_caretakers = FacilityCaretaker.objects.all(
        )  # This is my query to the database
        serializer = FacilityCaretakerSerializer(
            facilities_caretakers, many=True, context={'request': request})
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        """Handle GET requests for single park area

        Returns:
            Response -- JSON serialized park area instance
        """
        try:
            facility_caretaker = FacilityCaretaker.objects.get(pk=pk)
            serializer = FacilityCaretakerSerializer(
                facility_caretaker, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)
