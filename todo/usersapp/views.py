from rest_framework.renderers import JSONOpenAPIRenderer
from rest_framework.viewsets import ModelViewSet

from .models import User
from .serializers import UserModelSerializer

class UserModelViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserModelSerializer