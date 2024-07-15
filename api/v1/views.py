from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User


@api_view(["GET"])
def index(request):
    response = {
        "message": "Hello World",
    }
    return Response(response, status=status.HTTP_200_OK)
