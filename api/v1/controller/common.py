import jwt
from api.settings import SECRET_KEY
from django.contrib.auth.models import User


def user_check(request):
    jwt_token = request.META.get("HTTP_AUTHORIZATION").split(" ")[1]
    jwt_decoded = jwt.decode(
        jwt_token, SECRET_KEY, algorithms=["HS256"], options={"verify_aud": False}
    )
    user_id = jwt_decoded.get("user_id")
    return User.objects.get(id=user_id)
