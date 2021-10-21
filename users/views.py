from rest_framework import status, viewsets, parsers
from django.contrib.auth.models import User
from rest_framework.response import Response
import json
from .serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self, request, format='json'):

        serializer = UserSerializer(data=request.data, context={'request':request})
        print(request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                js = serializer.data
                return Response(js, status=status.HTTP_201_CREATED)
        #print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)