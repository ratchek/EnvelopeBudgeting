from django.contrib.auth import get_user_model
from django.test import Client, TestCase

from api.models import Envelope, Fill, Transaction


class EnvelopeGETPermissionsTestCase(TestCase):
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

    def test_user_can_view_own_envelopes_list(self):
        self.client.login(username="testuser1", password="12345")
        response = self.client.get("/envelopes/")
        self.assertEqual(response.status_code, 200)

    def test_unauthenticated_user_cannot_view_envelopes_list(self):
        response = self.client.get("/envelopes/")
        self.assertEqual(response.status_code, 403)

    def test_other_user_cannot_view_envelopes_list(self):
        self.client.login(username="testuser2", password="12345")
        response = self.client.get("/envelopes/")
        self.assertEqual(response.content, b"[]")

    def test_user_can_view_own_envelopes(self):
        self.client.login(username="testuser1", password="12345")
        response = self.client.get(f"/envelopes/{self.envelope.id}/")
        self.assertEqual(response.status_code, 200)

    def test_unauthenticated_user_cannot_view_envelopes(self):
        response = self.client.get(f"/envelopes/{self.envelope.id}/")
        self.assertEqual(response.status_code, 403)

    def test_other_user_cannot_view_envelopes(self):
        self.client.login(username="testuser2", password="12345")
        response = self.client.get(f"/envelopes/{self.envelope.id}/")
        self.assertEqual(response.status_code, 404)


class EnvelopePOSTPermissionsTestCase(TestCase):
    def setUp(self):
        self.user1 = get_user_model().objects.create_user(
            username="testuser1", password="12345"
        )
        self.user2 = get_user_model().objects.create_user(
            username="testuser2", password="12345"
        )
        self.client = Client()

    def test_user_can_create_envelope(self):
        self.client.login(username="testuser1", password="12345")
        response = self.client.post("/envelopes/", {"name": "test", "total": 100.00})
        self.assertEqual(response.status_code, 201)

    def test_unauthenticated_user_cannot_create_envelope(self):
        response = self.client.post("/envelopes/", {"name": "test", "total": 100.00})
        self.assertEqual(response.status_code, 403)

    def test_other_user_cannot_create_envelope_1(self):
        self.client.login(username="testuser2", password="12345")
        _ = self.client.post(
            "/envelopes/", {"name": "test", "total": 100.00, "user": self.user1.id}
        )
        self.assertEqual(self.user1.envelopes.count(), 0)


class EnvelopePUTPermissionsTestCase(TestCase):
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

    def test_user_can_update_own_envelope(self):
        self.client.login(username="testuser1", password="12345")
        response = self.client.put(
            f"/envelopes/{self.envelope.id}/",
            {"name": "test", "total": "200.00"},
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 200)
        self.envelope.refresh_from_db()
        self.assertEqual(self.envelope.total, 200.00)

    def test_unauthenticated_user_cannot_update_envelope(self):
        response = self.client.put(
            f"/envelopes/{self.envelope.id}/",
            {"name": "test", "total": "200.00"},
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 403)

    def test_other_user_cannot_update_envelope(self):
        self.client.login(username="testuser2", password="12345")
        response = self.client.put(
            f"/envelopes/{self.envelope.id}/",
            {"name": "test", "total": "200.00"},
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 404)


class EnvelopeDELETEPermissionsTestCase(TestCase):
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

    def test_user_can_delete_own_envelope(self):
        self.client.login(username="testuser1", password="12345")
        response = self.client.delete(f"/envelopes/{self.envelope.id}/")
        self.assertEqual(response.status_code, 204)
        self.assertEqual(Envelope.objects.count(), 0)

    def test_user_can_delete_own_envelope_2(self):
        self.client.login(username="testuser1", password="12345")
        response = self.client.delete(f"/envelopes/{self.envelope.id}/")
        self.assertEqual(response.status_code, 204)

    def test_unauthenticated_user_cannot_delete_envelope(self):
        response = self.client.delete(f"/envelopes/{self.envelope.id}/")
        self.assertEqual(response.status_code, 403)

    def test_other_user_cannot_delete_envelope(self):
        self.client.login(username="testuser2", password="12345")
        response = self.client.delete(f"/envelopes/{self.envelope.id}/")
        self.assertEqual(response.status_code, 404)


class TransactionGETPermissionsTestCase(TestCase):
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

    def test_user_can_view_own_transactions_list(self):
        self.client.login(username="testuser1", password="12345")
        response = self.client.get("/transactions/")
        self.assertEqual(response.status_code, 200)

    def test_unauthenticated_user_cannot_view_transactions_list(self):
        response = self.client.get("/transactions/")
        self.assertEqual(response.status_code, 403)

    def test_other_user_cannot_view_transactions_list(self):
        self.client.login(username="testuser2", password="12345")
        response = self.client.get("/transactions/")
        self.assertEqual(response.content, b"[]")

    def test_user_can_view_own_transactions(self):
        self.client.login(username="testuser1", password="12345")
        response = self.client.get(f"/transactions/{self.transaction.id}/")
        self.assertEqual(response.status_code, 200)

    def test_unauthenticated_user_cannot_view_transactions(self):
        response = self.client.get(f"/transactions/{self.transaction.id}/")
        self.assertEqual(response.status_code, 403)

    def test_other_user_cannot_view_transactions(self):
        self.client.login(username="testuser2", password="12345")
        response = self.client.get(f"/transactions/{self.transaction.id}/")
        self.assertEqual(response.status_code, 404)


class FillGETPermissionsTestCase(TestCase):
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

    def test_user_can_view_own_fills_list(self):
        self.client.login(username="testuser1", password="12345")
        response = self.client.get("/fills/")
        self.assertEqual(response.status_code, 200)

    def test_unauthenticated_user_cannot_view_fills_list(self):
        response = self.client.get("/fills/")
        self.assertEqual(response.status_code, 403)

    def test_user_cannot_view_other_users_fills_list(self):
        self.client.login(username="testuser2", password="12345")
        response = self.client.get("/fills/")
        self.assertEqual(response.content, b"[]")

    def test_user_can_view_own_fills(self):
        self.client.login(username="testuser1", password="12345")
        response = self.client.get(f"/fills/{self.fill.id}/")
        self.assertEqual(response.status_code, 200)

    def test_unauthenticated_user_cannot_view_fills(self):
        response = self.client.get(f"/fills/{self.fill.id}/")
        self.assertEqual(response.status_code, 403)

    def test_user_cannot_view_other_users_fills(self):
        self.client.login(username="testuser2", password="12345")
        response = self.client.get(f"/fills/{self.fill.id}/")
        self.assertEqual(response.status_code, 404)
