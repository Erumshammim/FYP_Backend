from rest_framework import generics, permissions
from rest_framework import serializers
from django.contrib.auth.models import User

# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')


# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    is_admin = serializers.BooleanField(required=False)
    is_data_entry = serializers.BooleanField(required=False)
    confirm_password = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'confirm_password',
                    'is_admin', 'is_data_entry')
        extra_kwargs = {'password': {'write_only': True, 'style': {'input_type': 'password'}}}

    def create(self, validated_data):
        password = validated_data['password']
        confirm_password = validated_data['confirm_password']

        if password != confirm_password:
            raise serializers.ValidationError({'password': 'Password must match.'})
        
        user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])
        
        if validated_data['is_admin'] == True:
            user.is_superuser = True
        if validated_data['is_data_entry'] == True:
            user.is_staff = True
        user.save()

        return user

# User Serializer
class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ('id', 'username', 'email', 'is_superuser', 'is_staff')

# Change Password
from rest_framework import serializers
from django.contrib.auth.models import User

class ChangePasswordSerializer(serializers.Serializer):
    model = User

    """
    Serializer for password change endpoint.
    """
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)