from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import User
from .serializers import UserSerializer


@api_view(['POST'])
def login(request):
    try:
        user_object = User.objects.get(username=request.data['username'])
    except User.DoesNotExist:
        return Response({'error': "wrong username"}, status=status.HTTP_404_NOT_FOUND)

    if user_object.password != request.data['password']:
        return Response({'error': "wrong password"}, status=status.HTTP_404_NOT_FOUND)

    return Response(UserSerializer(user_object).data, status=status.HTTP_200_OK)


@api_view(['POST'])
def register(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

