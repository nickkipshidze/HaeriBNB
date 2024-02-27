from rest_framework import serializers
from . import models

class UserSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = models.User
        fields = [
            "id", "username", "profile_picture", "first_name", "last_name", "password", "email", "birthday", "country_code", "phone_number", "goverment_id", "address", "emergency_contact"
        ]
