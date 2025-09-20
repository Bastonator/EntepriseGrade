from rest_framework import serializers
from .models import Files, Users


class UserSerilazer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = (
            "id",
            "email",
            "phone_number"
        )


class FilesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Files
        fields = "__all__"

