from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.test import TestCase

from api.models import Envelope, Fill, Transaction


class TransactionTestCase(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="testuser", password="12345"
        )
        self.envelope = Envelope.objects.create(
            name="Test Envelope", total=100.00, user=self.user
        )

    def test_transaction_amount_cannot_be_negative(self):
        object = Transaction.objects.create(
            date="2022-01-01",
            amount="-100.00",
            name="Test Fill",
            envelope=self.envelope,
            notes="Test Notes",
        )
        TestCase.assertRaises(self, ValidationError, object.full_clean)


class FillTestCase(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="testuser", password="12345"
        )
        self.envelope = Envelope.objects.create(
            name="Test Envelope", total=100.00, user=self.user
        )

    def test_fill_amount_cannot_be_negative(self):
        object = Fill.objects.create(
            date="2022-01-01",
            amount="-100.00",
            name="Test Fill",
            envelope=self.envelope,
            notes="Test Notes",
        )
        TestCase.assertRaises(self, ValidationError, object.full_clean)
