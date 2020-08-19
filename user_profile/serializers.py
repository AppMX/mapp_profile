from rest_framework import serializers
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=100)
    email = serializers.EmailField(max_length=100)
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['email', 'username', 'password']

    def validate(self, user_list):
        if User.objects.filter(username=user_list['username']):
            raise serializers.ValidationError({'username', 'Username already in use'})

        if User.objects.filter(email=user_list['email']):
            raise serializers.ValidationError({'email', 'Email already in use'})

        return super().validate(user_list)

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
