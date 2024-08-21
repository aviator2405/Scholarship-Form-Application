from .models import *
from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
class AppPerInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppPerInfo
        fields = "__all__"

class AppEduInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppEduInfo
        fields = "__all__"

class AppBanInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppBanInfo
        fields = '__all__'

class AppDocInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppDocInfo
        fields = ["username"]

class AppDocInfoSerializer2(serializers.ModelSerializer):
    class Meta:
        model = AppDocInfo
        fields="__all__"

class HodApproveSerializer(serializers.ModelSerializer):
    class Meta:
        model = HodApprove
        fields = "__all__"

class HodRejectSerializer(serializers.ModelSerializer):
    class Meta:
        model = HodReject
        fields = "__all__"
 
class PrincipalApproveSerializer(serializers.ModelSerializer):
    class Meta:
        model = PrincipalApprove
        fields = "__all__"
 
class PrincipalRejectSerializer(serializers.ModelSerializer):
    class Meta:
        model = PrincipalReject
        fields = "__all__"
 