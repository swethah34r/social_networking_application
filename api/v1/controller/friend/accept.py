from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status, serializers
from v1.models import Friend
from v1.controller.common import user_check


@api_view(["POST"])
def accept(request):
    res = dict()
    try:
        try:
            user = user_check(request)
        except Exception:
            return Response(status=status.HTTP_403_FORBIDDEN)

        data = request.data
        data_validator = UserInputValidator(data=data)
        friend = data.get("friend_id")

        if data_validator.is_valid():
            user = Friend.objects.get(friend_id=friend, user_id=user.id)
            user.validated = True
            user.save()
            res["status"] = "accept success"
            return Response(res, status=status.HTTP_200_OK)
        else:
            return Response(data_validator.errors, status=status.HTTP_400_BAD_REQUEST)

    except Exception as e:
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class UserInputValidator(serializers.Serializer):
    friend_id = serializers.IntegerField()


class FriendSerializer(serializers.ModelSerializer):
    class Meta:
        model = Friend
        fields = "__all__"
