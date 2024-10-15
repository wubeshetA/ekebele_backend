from rest_framework import serializers


from .models import BirthCertificate


class BirthCertificateSerializer(serializers.ModelSerializer):


    class Meta:


        model = BirthCertificate


        fields = '__all__'

