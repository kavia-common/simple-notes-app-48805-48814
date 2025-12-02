from rest_framework.test import APITestCase
from django.urls import reverse


class HealthTests(APITestCase):
    def test_health(self):
        url = reverse('Health')  # Make sure the URL is named
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, {"message": "Server is up!"})


class NotesCrudTests(APITestCase):
    def setUp(self):
        self.list_url = reverse("notes-list-create")

    def test_crud_flow(self):
        # Create
        create_payload = {"title": "Test Note", "content": "Hello world"}
        create_resp = self.client.post(self.list_url, data=create_payload, format="json")
        self.assertEqual(create_resp.status_code, 201)
        note_id = create_resp.data["id"]

        # List
        list_resp = self.client.get(self.list_url)
        self.assertEqual(list_resp.status_code, 200)
        self.assertTrue(any(n["id"] == note_id for n in list_resp.data))

        # Retrieve
        detail_url = reverse("notes-detail", kwargs={"id": note_id})
        get_resp = self.client.get(detail_url)
        self.assertEqual(get_resp.status_code, 200)
        self.assertEqual(get_resp.data["title"], "Test Note")

        # Update (PUT)
        put_payload = {"title": "Updated Title", "content": "Updated"}
        put_resp = self.client.put(detail_url, data=put_payload, format="json")
        self.assertEqual(put_resp.status_code, 200)
        self.assertEqual(put_resp.data["title"], "Updated Title")

        # Partial Update (PATCH)
        patch_payload = {"content": "Patched content"}
        patch_resp = self.client.patch(detail_url, data=patch_payload, format="json")
        self.assertEqual(patch_resp.status_code, 200)
        self.assertEqual(patch_resp.data["content"], "Patched content")

        # Delete
        del_resp = self.client.delete(detail_url)
        self.assertEqual(del_resp.status_code, 204)

        # Ensure gone
        gone_resp = self.client.get(detail_url)
        self.assertEqual(gone_resp.status_code, 404)
