from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status, serializers
from django.contrib.auth.models import User


@api_view(["POST"])
def signup(request):
    res = dict()
    try:
        data = request.data

        data_validator = UserInputValidator(data=data)
        if data_validator.is_valid():
            user = User(
                first_name=data.get("first_name"),
                username=data.get("email"),
                email=data.get("email"),
                password=data.get("password"),
            )
            user.save()
            res["status"] = "signup success"
            return Response(data=res, status=status.HTTP_200_OK)
        else:
            return Response(data_validator.errors, status=status.HTTP_400_BAD_REQUEST)

    except Exception as e:
        return Response(e, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class UserInputValidator(serializers.Serializer):
    first_name = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField()
