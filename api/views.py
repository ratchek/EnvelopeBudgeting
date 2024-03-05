from rest_framework import generics, permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

from .models import Envelope, Fill, Transaction
from .permissions import IsEnvelopeOwner
from .serializers import EnvelopeSerializer, FillSerializer, TransactionSerializer


@api_view(["GET"])
def api_root(request, format=None):
    return Response(
        {
            "envelopes": reverse("envelope-list", request=request, format=format),
            "transactions": reverse("transaction-list", request=request, format=format),
            "fills": reverse("fill-list", request=request, format=format),
        }
    )


class EnvelopeList(generics.ListCreateAPIView):
    serializer_class = EnvelopeSerializer

    def get_queryset(self):
        return Envelope.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class EnvelopeDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = EnvelopeSerializer
    permission_classes = [permissions.IsAuthenticated, IsEnvelopeOwner]

    def get_queryset(self):
        return Envelope.objects.filter(user=self.request.user)


class TransactionList(generics.ListCreateAPIView):
    serializer_class = TransactionSerializer

    def get_queryset(self):
        return Transaction.objects.filter(envelope__user=self.request.user)


class TransactionDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TransactionSerializer

    def get_queryset(self):
        return Transaction.objects.filter(envelope__user=self.request.user)


class FillList(generics.ListCreateAPIView):
    serializer_class = FillSerializer

    def get_queryset(self):
        return Fill.objects.filter(envelope__user=self.request.user)


class FillDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = FillSerializer

    def get_queryset(self):
        return Fill.objects.filter(envelope__user=self.request.user)
