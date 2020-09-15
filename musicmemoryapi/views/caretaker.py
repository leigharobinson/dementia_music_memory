from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
# STATUS USER FOR DESTROY/UPDATE METHODS
from rest_framework import status
from musicmemoryapi.models import Caretaker
from .user import UserSerializer
from django.contrib.auth.models import User


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
    def update(self, request, pk=None):
        '''
        Handling a PUT request for a customer/user
        Returns -- Empty body with 204 status code
        '''
        caretaker = Caretaker.objects.get(pk=pk)
        caretaker.title = request.data['title']
        caretaker.save()

        user = User.objects.get(pk=caretaker.user.id)
        user.first_name = request.data['first_name']
        user.last_name = request.data['last_name']
        user.username = request.data['username']
        user.save()

        return Response({}, status=status.HTTP_204_NO_CONTENT)

    def retrieve(self, request, pk=None):
        try:
            caretaker = Caretaker.objects.get(pk=pk)
            serializer = CaretakerSerializer(
                caretaker, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def list(self, request):

        caretakers = Caretaker.objects.filter(user=request.auth.user)
        serializer = CaretakerSerializer(
            caretakers, many=True, context={'request': request})
        return Response(serializer.data)
