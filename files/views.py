from rest_framework import viewsets, parsers
from .models import Upload
from .serializers import FileSerializer

class FileViewSet(viewsets.ModelViewSet):
    queryset = Upload.objects.all()
    serializer_class = FileSerializer
    parser_classes = [parsers.MultiPartParser, parsers.FormParser]