from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status, serializers, pagination
from v1.models import Friend
from django.contrib.auth.models import User
from v1.controller.common import user_check


@api_view(["GET"])
def list_all(request):
    res = dict()
    try:
        try:
            user = user_check(request)
        except Exception:
            return Response(status=status.HTTP_403_FORBIDDEN)

        user = User.objects.all()

        res = UserWihtoutAccept(
            instance=CustomPagination().paginate_queryset(
                queryset=user, request=request
            ),
            many=True,
        ).data

        return Response(res, status=status.HTTP_200_OK)

    except Exception:
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class CustomPagination(pagination.LimitOffsetPagination):
    default_limit = 100
    limit_query_param = "limit"
    offset_query_param = "offset"
    max_limit = 500

    def paginate_queryset(self, queryset, request):
        return super().paginate_queryset(queryset, request)


class FriendSerializer(serializers.ModelSerializer):
    class Meta:
        model = Friend
        fields = "__all__"


class UserWihtoutAccept(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "first_name"]


class UserWihAccept(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "first_name", "email"]
