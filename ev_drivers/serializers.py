from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from rest_framework.serializers import ModelSerializer
from .constants import STAFF, STANDARD_USER, PREMIUM_USER
from django.contrib.auth.models import Group
from payments.models import Rate


class LoginTokenObtainSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super(LoginTokenObtainSerializer, cls).get_token(user)
        return token


class UserSerializer(ModelSerializer):
    rate = serializers.SerializerMethodField()

    def get_rate(self, obj):
        group = Group.objects.filter(user=obj).order_by('id').last()  # get the most privileges
        user_rate = Rate.objects.get(group=group)
        return user_rate.rate

    class Meta:
        model = User
        fields = (
            'email', 'username', 'groups', 'rate'
        )


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )

    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'password2', 'email', 'first_name', 'last_name', 'is_staff')
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True}
        }

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )

        user.set_password(validated_data['password'])
        if validated_data.get('is_staff', None):
            user.is_staff = True
            user.groups.add(STAFF)
        else:
            user.groups.add(STANDARD_USER)
        user.save()

        return user
