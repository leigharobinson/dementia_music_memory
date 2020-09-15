from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
# STATUS USER FOR DESTROY/UPDATE METHODS
from rest_framework import status
from musicmemoryapi.models import Patient, Caretaker
from django.contrib.auth.models import User

# Making sure the caretaker objects are avalible
# caretaker_test = Caretaker.objects.all()
# print(caretaker_test)


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
        fields = ('id', 'caretaker', 'first_name', 'last_name',
                  'diagnosis', 'year_of_birth', 'caretaker_id')
        depth = 2


class PatientView(ViewSet):

    """Patient for MusicMemory API"""

    def create(self, request):
        """Handle POST operations

        Returns:
            Response -- JSON serialized patient instance
        """
        user = User.objects.get(pk=request.user.id)
        caretaker = Caretaker.objects.get(pk=user.caretaker.id)

        newpatient = Patient()
        newpatient.first_name = request.data["first_name"]
        newpatient.last_name = request.data["last_name"]
        newpatient.diagnosis = request.data["diagnosis"]
        newpatient.year_of_birth = request.data["year_of_birth"]
        newpatient.caretaker = caretaker

        newpatient.save()

        serializer = PatientSerializer(
            newpatient, context={'request': request})

        return Response(serializer.data)

    def list(self, request):
        """Handle GET requests to park areas resource

        Returns:
            Response -- JSON serialized list of park areas
        """
        user = User.objects.get(pk=request.user.id)
        caretaker = Caretaker.objects.get(pk=user.caretaker.id)
        # This is my query to the database
        patients = Patient.objects.filter(caretaker_id=caretaker.id)
        serializer = PatientSerializer(
            patients, many=True, context={'request': request})
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        """Handle GET requests for single park area

        Returns:
            Response -- JSON serialized park area instance
        """
        try:
            patient = Patient.objects.get(pk=pk)
            serializer = PatientSerializer(
                patient, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def destroy(self, request, pk=None):
        """Handle DELETE requests for a single park area
        Returns:
            Response -- 200, 404, or 500 status code
        """
        try:
            patient = Patient.objects.get(pk=pk)
            patient.delete()

            return Response({}, status=status.HTTP_204_NO_CONTENT)

        except Patient.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def update(self, request, pk=None):
        '''
        Handling a PUT request for a customer/user
        Returns -- Empty body with 204 status code
        '''

        # This is my query to the database
        patient = Patient.objects.get(pk=pk)
        patient.first_name = request.data['first_name']
        patient.last_name = request.data['last_name']
        patient.diagnosis = request.data['diagnosis']
        patient.year_of_birth = request.data['year_of_birth']
        patient.save()
        # serializer = PatientSerializer(patient, context={'request': request})

        return Response({}, status=status.HTTP_204_NO_CONTENT)
