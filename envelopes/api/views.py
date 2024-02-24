from rest_framework import generics

from .models import Envelope, Fill, Transaction
from .serializers import EnvelopeSerializer, FillSerializer, TransactionSerializer


class EnvelopeList(generics.ListCreateAPIView):
    queryset = Envelope.objects.all()
    serializer_class = EnvelopeSerializer


class EnvelopeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Envelope.objects.all()
    serializer_class = EnvelopeSerializer


class TransactionList(generics.ListCreateAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer


class TransactionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer


class FillList(generics.ListCreateAPIView):
    queryset = Fill.objects.all()
    serializer_class = FillSerializer


class FillDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Fill.objects.all()
    serializer_class = FillSerializer
