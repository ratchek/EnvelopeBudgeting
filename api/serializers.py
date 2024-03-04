from rest_framework import serializers

from .models import Envelope, Fill, Transaction


class EnvelopeSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source="user.username")

    class Meta:
        model = Envelope
        fields = "__all__"


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = "__all__"


class FillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fill
        fields = "__all__"
