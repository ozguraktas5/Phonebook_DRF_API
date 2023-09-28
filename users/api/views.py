from django.contrib.auth.models import User
from ..models import Profile
from .serializers import ProfileSerializer, PasswordSerializer, UserSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .permissions import IsRequestUserPermissions

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    @action(detail=False, methods=["get"])
    def get_user_count(self, request):
        user_count = User.objects.all().count()
        return Response({"Kullanici sayisi":user_count})
    
    @action(detail=True, 
            methods=["post"], 
            serializer_class=PasswordSerializer, 
            permission_classes = [IsAuthenticated, IsRequestUserPermissions])
    def set_password(self, request, pk=None):
        instance = self.get_object()
        serializer = self.serializer_class(instance, data=request.data)
        if serializer.is_valid():
            new_password = serializer.validated_data['password']
            instance.set_password(new_password)
            instance.save()
            return Response({"status": "set_password"})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer