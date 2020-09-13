from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
# STATUS USER FOR DESTROY/UPDATE METHODS
from rest_framework import status
from musicmemoryapi.models import Facility, Patient

facility_test = Facility.objects.all()
print(facility_test)


class PatientSerializer(serializers.HyperlinkedModelSerializer):
    """JSON serializer for product

    Arguments:
        serializers.HyperlinkedModelSerializer
    """

    class Meta:
        model = Patient
        url = serializers.HyperlinkedIdentityField(
            view_name='patients',
            lookup_field='id'
        )
        fields = ('id', 'facility', 'facility', 'first_name', 'last_name',
                  'diagnosis', 'year_of_birth', 'facility_name', 'facility_id')
        depth = 2


class PatientView(ViewSet):

    """Patient for MusicMemory API"""

    def create(self, request):
        """Handle POST operations

        Returns:
            Response -- JSON serialized facility instance
        """
        facility = Facility.objects.get(pk=request.data["facility_id"])

        newpatient = Patient()
        newpatient.first_name = request.data["first_name"]
        newpatient.last_name = request.data["last_name"]
        newpatient.diagnosis = request.data["diagnosis"]
        newpatient.year_of_birth = request.data["year_of_birth"]
        newpatient.facility = facility

        newpatient.save()

        serializer = PatientSerializer(
            newpatient, context={'request': request})

        return Response(serializer.data)

    def list(self, request):
        """Handle GET requests to park areas resource

        Returns:
            Response -- JSON serialized list of park areas
        """
        patients = Patient.objects.all()  # This is my query to the database
        serializer = PatientSerializer(
            patients, many=True, context={'request': request})
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        """Handle GET requests for single park area

        Returns:
            Response -- JSON serialized park area instance
        """
        try:
            patient = patient.objects.get(pk=pk)
            serializer = PatientSerializer(
                patient, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)
