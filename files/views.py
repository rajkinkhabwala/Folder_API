from rest_framework import viewsets, parsers, permissions
from rest_framework.response import Response
from .models import Upload
from .serializers import FileSerializer

class FileViewSet(viewsets.ModelViewSet):
    permission_classes  = [permissions.IsAuthenticated]
    serializer_class = FileSerializer
    parser_classes = [parsers.MultiPartParser, parsers.FormParser]

    def get_queryset(self):
            user = self.request.user
            return Upload.objects.filter(user=user)




