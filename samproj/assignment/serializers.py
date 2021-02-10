from django.contrib.auth.models import User, Group
from assignment.models import *
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
import copy

class UserSerializer(serializers.HyperlinkedModelSerializer):
    username = models.CharField(unique=True)
    email = serializers.EmailField(validators=[UniqueValidator(queryset=User.objects.all())])
    first_name = serializers.CharField(required=True, allow_blank=False, allow_null=False)
    user_type = serializers.ChoiceField(source='userprofile.user_type', choices=['Admin', 'Client'])
    password = serializers.CharField(
        write_only=True,
        required=True,
        style={'input_type': 'password', 'placeholder': 'Password'}
    )


    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'first_name', 'last_name', 'email', 'user_type']

    def create(self, validated_data):
        val_data = copy.deepcopy(validated_data)
        profile_data = val_data['userprofile']
        del val_data['userprofile']
        instance = User.objects.create(**val_data)
        userprofile,is_created = UserProfile.objects.get_or_create(user_id=instance.id)
        userprofile.user_type = profile_data['user_type']
        userprofile.save()
        return instance

    def update(self, instance, validated_data):
        val_data = copy.deepcopy(validated_data)
        profile_data = val_data['userprofile']
        del val_data['userprofile']
        userprofile,is_created = UserProfile.objects.get_or_create(user_id=instance.id)
        userprofile.user_type = profile_data['user_type']
        userprofile.save()
        for key, value in val_data.items():
            setattr(instance, key, value)
        instance.save()
        return instance


class UserMappingSerializer(serializers.HyperlinkedModelSerializer):
    admin_user = serializers.PrimaryKeyRelatedField(queryset=User.objects.filter(is_superuser=0,userprofile__user_type='Admin'))
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.filter(usermapping__isnull=True, userprofile__user_type='Client'), required=True)

    class Meta:
        model = UserMapping
        fields = ['admin_user', 'user']

class LoginRequestSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)
    name = serializers.CharField(required=True, allow_blank=False, allow_null=False)
    company = serializers.CharField(required=True, allow_blank=False, allow_null=False)

    class Meta:
        model = LoginRequest
        fields = ['id', 'email', 'name', 'company', 'status']

    def create(self, validated_data):
        user, is_created = User.objects.get_or_create(email=validated_data['email'], defaults={'first_name': validated_data['name']})
        validated_data['user_id'] = user.id
        instance = LoginRequest.objects.create(**validated_data)
        return instance
