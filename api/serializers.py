
from rest_framework import serializers
from account.models import User

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id','full_name', 'email', 'National_number','phone_number','password']

    def create(self, validated_data):
        user = User.objects.create(**validated_data)
        # User.objects.create(user=user)
        return user
    def update(self, instance, validated_data):
        """
        Update and return an existing `User` instance, given the validated data.
        """
        instance.full_name = validated_data.get('full_name', instance.full_name)
        instance.email = validated_data.get('email', instance.email)
        instance.National_number = validated_data.get('National_number', instance.National_number)
        instance.phone_number = validated_data.get('phone_number', instance.phone_number)
        instance.password = validated_data.get('password', instance.password)
        instance.save()
        return instance