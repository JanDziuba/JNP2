from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Message

@api_view(['GET'])
def get_messages(request):
    messages = Message.objects.all().values()
    return Response({'data': messages}, status=status.HTTP_200_OK)
