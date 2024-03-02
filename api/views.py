from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

from .models import Envelope, Fill, Transaction
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
    def get_queryset(self):
        return Envelope.objects.filter(user=self.request.user)

    serializer_class = EnvelopeSerializer


class EnvelopeDetail(generics.RetrieveUpdateDestroyAPIView):
    def get_queryset(self):
        return Envelope.objects.filter(user=self.request.user)

    serializer_class = EnvelopeSerializer


class TransactionList(generics.ListCreateAPIView):
    def get_queryset(self):
        return Transaction.objects.filter(envelope__user=self.request.user)

    serializer_class = TransactionSerializer


class TransactionDetail(generics.RetrieveUpdateDestroyAPIView):
    def get_queryset(self):
        return Transaction.objects.filter(envelope__user=self.request.user)

    serializer_class = TransactionSerializer


class FillList(generics.ListCreateAPIView):
    def get_queryset(self):
        return Fill.objects.filter(envelope__user=self.request.user)

    serializer_class = FillSerializer


class FillDetail(generics.RetrieveUpdateDestroyAPIView):
    def get_queryset(self):
        return Fill.objects.filter(envelope__user=self.request.user)

    serializer_class = FillSerializer
