from django.shortcuts import render
from djoser.views import UserViewSet
from .serializers import CustomUserSerializer

# Create your views here.


from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def check_is_staff(request):
    # Check if the authenticated user has is_staff set to True
    is_staff = request.user.is_staff
    return Response({'is_staff': is_staff})
