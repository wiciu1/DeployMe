from rest_framework import generics
from rest_framework.permissions import AllowAny

from ..serializers.register_serializer import RegisterSerializer
from ..models import CustomUser


class RegisterView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    permission_classes = [AllowAny]
    serializer_class = RegisterSerializer