from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import get_user_model

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from rest_framework.permissions import AllowAny
from .serializers import VerifyEmailSerializer

User = get_user_model()


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def check_is_staff(request):
    # Check if the authenticated user has is_staff set to True
    is_staff = request.user.is_staff
    return Response({'is_staff': is_staff})


class VerifyEmailView(APIView):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        # Parse incoming data
        email = request.data.get('email')
        code = request.data.get('verification_code')

        if not email or not code:
            return Response({"error": "Both email and verification code are required."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            # Check if the user exists
            user = User.objects.get(email=email)

            if user.verification_code == code:
                user.is_active = True  # Activate the account
                user.verification_code = None  # Clear the code
                user.save()
                return Response({"message": "Email verified successfully. Account activated."}, status=status.HTTP_200_OK)

            return Response({"error": "Invalid verification code."}, status=status.HTTP_400_BAD_REQUEST)

        except User.DoesNotExist:
            return Response({"error": "User with this email does not exist."}, status=status.HTTP_404_NOT_FOUND)
