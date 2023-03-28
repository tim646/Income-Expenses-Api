from rest_framework import serializers
from authentication.models import User


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=68, min_length=8, write_only=True)
    email = serializers.EmailField(max_length=255, min_length=4)

    class Meta:
        model = User
        fields = ['email', 'username', 'password']

    def validate(self, attrs):
        email = attrs.get('email', '')
        username = attrs.get('username', '')
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError({'email': 'Email is already in use'})

        if not username.isalnum():
            raise serializers.ValidationError({'username': 'Username should only contain alphanumeric characters'})
        return attrs

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
