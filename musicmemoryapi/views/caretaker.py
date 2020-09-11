from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
# STATUS USER FOR DESTROY/UPDATE METHODS
from rest_framework import status
from musicmemoryapi.models import Caretaker
from .user import UserSerializer


class CaretakerSerializer(serializers.HyperlinkedModelSerializer):

    user = UserSerializer()

    class Meta:
        model = Caretaker
        url = serializers.HyperlinkedIdentityField(
            view_name='caretaker',
            lookup_field='id'
        )
        fields = ('id', 'url', 'user', 'title')
        depth = 2


class CaretakerView(ViewSet):

    def retrieve(self, request, pk=None):
        try:
            caretaker = Caretaker.objects.get(pk=pk)
            serializer = CaretakerSerializer(
                caretaker, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def list(self, request):

        caretakers = Caretaker.objects.all()
        serializer = CaretakerSerializer(
            caretakers, many=True, context={'request': request})
        return Response(serializer.data)
