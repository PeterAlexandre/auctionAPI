from django.contrib.auth.hashers import make_password
from rest_framework import serializers

from .models import User, Address


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = [
            "url",
            "id",
            "street",
            "house_number",
            "city",
            "state",
            "postal_code",
            "country",
        ]


class PublicAddressField(serializers.RelatedField):
    def to_representation(self, value):
        return (f"{value.city} / {value.state} - {value.country}")


class UserSerializer(serializers.ModelSerializer):
    # address = PublicAddressField(read_only=True)
    address = AddressSerializer(read_only=True)

    class Meta:
        model = User
        fields = [
            "url",
            "id",
            "username",
            "password",
            "email",
            "first_name",
            "last_name",
            "phone_number",
            "cpf",
            "birth_date",
            "address",
            "is_staff",
            "is_active",
        ]
        extra_kwargs = {
            "password": {"write_only": True, "min_length": 8, "required": False},
            "email": {"required": True},
        }
        read_only_fields = (
            "id",
            "is_staff",
            "is_active",
            "address"
        )

    def create(self, validated_data):
        validated_data["password"] = make_password(validated_data.get("password"))
        return super().create(validated_data)

    def update(self, instance, validated_data):
        validated_data.pop("password", None)
        return super().update(instance, validated_data)


class ChangePasswordSerializer(serializers.ModelSerializer):
    current_password = serializers.CharField(required=True, write_only=True)
    new_password = serializers.CharField(required=True, write_only=True, min_length=8)

    class Meta:
        model = User
        fields = ["current_password", "new_password"]

    def validate_current_password(self, value):
        instance = self.instance
        if not instance.check_password(value):
            raise serializers.ValidationError("The current password does not match")

        return value
