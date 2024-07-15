from django.urls import path
from v1.views import index
from v1.controller.auth.signin import signin
from v1.controller.auth.signup import signup
from v1.controller.auth.list_all import list_all
from v1.controller.friend.invite import invite
from v1.controller.friend.list import list
from v1.controller.friend.accept import accept

urlpatterns = [
    path("v1/", index),
    path("v1/login", signin),
    path("v1/signup", signup),
    path("v1/users", list_all),
    path("v1/friend/invite", invite),
    path("v1/friend/list", list),
    path("v1/friend/accept", accept),
]
