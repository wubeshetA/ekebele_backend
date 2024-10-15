from django.shortcuts import render


from rest_framework.permissions import AllowAny


from rest_framework.views import APIView


from rest_framework.response import Response


from rest_framework import status


from .models import BirthCertificate

from .serializers import BirthCertificateSerializer


class BirthCertificateView(APIView):

    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):

        events = BirthCertificate.objects.all()

        serializer = BirthCertificateSerializer(events, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):

        serializer = BirthCertificateSerializer(data=request.data)

        if serializer.is_valid():

            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, *args, **kwargs):

        try:

            event = BirthCertificate.objects.get(pk=kwargs.get('pk'))

        except BirthCertificate.DoesNotExist:

            return Response({'error': 'Not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = BirthCertificateSerializer(event, data=request.data)

        if serializer.is_valid():

            serializer.save()

            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
