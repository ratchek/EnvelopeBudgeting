from django.contrib.auth import get_user_model
from django.test import Client, TestCase

from api.models import Envelope, Fill, Transaction


class EnvelopePermissionsTestCase(TestCase):
    def setUp(self):
        self.user1 = get_user_model().objects.create_user(
            username="testuser1", password="12345"
        )
        self.user2 = get_user_model().objects.create_user(
            username="testuser2", password="12345"
        )
        self.envelope = Envelope.objects.create(
            name="test", total=100.00, user=self.user1
        )
        self.client = Client()

    def test_unauthenticated_user_cannot_view_envelopes_list(self):
        response = self.client.get("/envelopes/")
        self.assertEqual(response.status_code, 403)

    def test_unauthenticated_user_cannot_view_envelopes(self):
        response = self.client.get(f"/envelopes/{self.envelope.id}/")
        self.assertEqual(response.status_code, 403)

    def test_user_cannot_view_other_users_envelopes_list(self):
        self.client.login(username="testuser2", password="12345")
        response = self.client.get("/envelopes/")
        self.assertEqual(response.content, b"[]")

    def test_user_cannot_view_other_users_envelopes(self):
        self.client.login(username="testuser2", password="12345")
        response = self.client.get(f"/envelopes/{self.envelope.id}/")
        self.assertEqual(response.status_code, 404)


class TransactionPermissionsTestCase(TestCase):
    def setUp(self):
        self.user1 = get_user_model().objects.create_user(
            username="testuser1", password="12345"
        )
        self.user2 = get_user_model().objects.create_user(
            username="testuser2", password="12345"
        )
        self.envelope = Envelope.objects.create(
            name="test", total=100.00, user=self.user1
        )
        self.transaction = Transaction.objects.create(
            date="2020-01-01",
            amount=50.00,
            name="test",
            envelope=self.envelope,
            notes="test",
        )
        self.client = Client()

    def test_unauthenticated_user_cannot_view_transactions_list(self):
        response = self.client.get("/transactions/")
        self.assertEqual(response.status_code, 403)

    def test_unauthenticated_user_cannot_view_transactions(self):
        response = self.client.get(f"/transactions/{self.transaction.id}/")
        self.assertEqual(response.status_code, 403)

    def test_user_cannot_view_other_users_transactions_list(self):
        self.client.login(username="testuser2", password="12345")
        response = self.client.get("/transactions/")
        self.assertEqual(response.content, b"[]")

    def test_user_cannot_view_other_users_transactions(self):
        self.client.login(username="testuser2", password="12345")
        response = self.client.get(f"/transactions/{self.transaction.id}/")
        self.assertEqual(response.status_code, 404)


class FillPermissionsTestCase(TestCase):
    def setUp(self):
        self.user1 = get_user_model().objects.create_user(
            username="testuser1", password="12345"
        )
        self.user2 = get_user_model().objects.create_user(
            username="testuser2", password="12345"
        )
        self.envelope = Envelope.objects.create(
            name="test", total=100.00, user=self.user1
        )
        self.fill = Fill.objects.create(
            date="2020-01-01",
            amount=50.00,
            name="test",
            envelope=self.envelope,
            notes="test",
        )
        self.client = Client()

    def test_unauthenticated_user_cannot_view_fills_list(self):
        response = self.client.get("/fills/")
        self.assertEqual(response.status_code, 403)

    def test_unauthenticated_user_cannot_view_fills(self):
        response = self.client.get(f"/fills/{self.fill.id}/")
        self.assertEqual(response.status_code, 403)

    def test_user_cannot_view_other_users_fills_list(self):
        self.client.login(username="testuser2", password="12345")
        response = self.client.get("/fills/")
        self.assertEqual(response.content, b"[]")

    def test_user_cannot_view_other_users_fills(self):
        self.client.login(username="testuser2", password="12345")
        response = self.client.get(f"/fills/{self.fill.id}/")
        self.assertEqual(response.status_code, 404)
