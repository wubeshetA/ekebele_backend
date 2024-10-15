from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from .models import BirthCertificate
from .serializers import BirthCertificateSerializer


class BirthCertificateView(generics.ListCreateAPIView):
    queryset = BirthCertificate.objects.all()
    serializer_class = BirthCertificateSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            # Return the serialized data along with the application_number
            return Response({
                "application_number": serializer.data["application_number"],
                "details": serializer.data
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
