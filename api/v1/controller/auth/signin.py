from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status, serializers
from django.contrib.auth.models import User
from datetime import datetime
from api.settings import SECRET_KEY
import jwt


@api_view(["POST"])
def signin(request):
    res = dict()
    try:
        data = request.data
        data_validator = UserInputValidator(data=data)
        if data_validator.is_valid():
            user = User.objects.filter(email=data["email"], password=data["password"])
            if not user:
                return Response(status=status.HTTP_401_UNAUTHORIZED)
            user = user[0]
            expire_time = int(datetime.now().timestamp()) + 60 * 60 * 24
            token = jwt.encode(
                {
                    "email": data["email"],
                    "user_id": user.id,
                    "exp": expire_time,
                },
                SECRET_KEY,
                algorithm="HS256",
            )
            res["token"] = str(token)
            res["expire_time"] = expire_time
            return Response(res, status=status.HTTP_200_OK)
        else:
            return Response(data_validator.errors, status=status.HTTP_400_BAD_REQUEST)

    except Exception as e:
        return Response(e, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class UserInputValidator(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()
