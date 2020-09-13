from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
# STATUS USER FOR DESTROY/UPDATE METHODS
from rest_framework import status
from musicmemoryapi.models import CaretakerPatient
from musicmemoryapi.models import Patient
from musicmemoryapi.models import Caretaker


class CaretakerPatientSerializer(serializers.HyperlinkedModelSerializer):
    """JSON serializer for Patient and Caretaker

    Arguments:
        serializers.HyperlinkedModelSerializer
    """

    class Meta:
        model = CaretakerPatient
        url = serializers.HyperlinkedIdentityField(
            view_name='caretakers_patients',
            lookup_field='id'
        )
        fields = ('id', 'caretaker', 'caretaker_id', 'patient', 'patient_id')
        depth = 2


class CaretakerPatientView(ViewSet):

    """Patients and Caretakers for MusicMemory API"""

    def create(self, request):
        """Handle POST operations

        Returns:
            Response -- JSON serialized patients and caretakers instance
        """
        patient = Patient.objects.get(pk=request.data["patient_id"])
        caretaker = Caretaker.objects.get(pk=request.data["caretaker_id"])

        newcaretakerpatient = CaretakerPatient()
        newcaretakerpatient.patient = patient
        newcaretakerpatient.caretaker = caretaker

        newcaretakerpatient.save()

        serializer = CaretakerPatientSerializer(
            newcaretakerpatient, context={'request': request})

        return Response(serializer.data)

    def list(self, request):
        """Handle GET requests to park areas resource

        Returns:
            Response -- JSON serialized list of park areas
        """
        caretakers_patients = CaretakerPatient.objects.all(
        )  # This is my query to the database
        serializer = CaretakerPatientSerializer(
            caretakers_patients, many=True, context={'request': request})
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        """Handle GET requests for single park area

        Returns:
            Response -- JSON serialized park area instance
        """
        try:
            caretaker_patient = CaretakerPatient.objects.get(pk=pk)
            serializer = CaretakerPatientSerializer(
                caretaker_patient, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)
