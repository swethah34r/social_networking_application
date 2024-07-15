from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status, serializers
from v1.models import Friend
from django.contrib.auth.models import User
from v1.controller.common import user_check


@api_view(["POST"])
def invite(request):
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
            friend = User.objects.get(id=friend)
            try:
                friend_check = Friend.objects.filter(
                    friend_id=friend.id, user_id=user.id
                )
                if friend_check:
                    res["status"] = "already invited"
                    return Response(res, status=status.HTTP_400_BAD_REQUEST)

                Friend.objects.create(friend_id=friend.id, user_id=user.id)
                res["status"] = "invite success"
                return Response(res, status=status.HTTP_200_OK)
            except Exception:
                res["status"] = "already invited"
                return Response(res, status=status.HTTP_400_BAD_REQUEST)
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
