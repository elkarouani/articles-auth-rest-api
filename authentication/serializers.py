from rest_framework import serializers

from allauth.account.adapter import get_adapter
from allauth.account.utils import setup_user_email

from rest_auth.registration.serializers import RegisterSerializer


class CustomRegisterSerializer(RegisterSerializer):
    is_provider = serializers.BooleanField(required=False)

    def get_cleaned_data(self):
        data_dict = super().get_cleaned_data()
        data_dict['is_provider'] = self.validated_data.get('is_provider', '')
        return data_dict