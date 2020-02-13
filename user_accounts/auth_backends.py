from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.hashers import check_password

from .models import FairyUser

class FairyAuthBackend(BaseBackend):

    def authenticate(self, request, username=None, password=None):
        pass

    def get_user(self, user_id):
        try:
            return FairyUser.objects.get(pk=user_id)
        except FairyUser.DoesNotExist:
            return None

