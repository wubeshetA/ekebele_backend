from rest_framework import serializers
from .models import BirthCertificate


class BirthCertificateSerializer(serializers.ModelSerializer):
    application_number = serializers.ReadOnlyField()
    user = serializers.PrimaryKeyRelatedField(
        read_only=True)  # Make user read-only

    # exclude picture field from the serializer
    class Meta:
        model = BirthCertificate
        exclude = ('picture',)

    def get_fields(self):
        fields = super().get_fields()
        request = self.context.get('request')

        # Make 'status' field read-only for non-staff users
        if request and not request.user.is_staff:
            fields['status'].read_only = True
            # Non-staff users cannot write to 'comment'
            fields['comment'].read_only = True

        return fields

    def create(self, validated_data):
        # Set the user to the currently authenticated user
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)
