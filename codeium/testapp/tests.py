from django.test import TestCase, Client as TestClient
from django.urls import reverse

from .models import Client


class AddClientTestCase(TestCase):
    def setUp(self):
        self.client = TestClient()

    def test_add_client(self):
        # Create a POST request with a name parameter
        response = self.client.post(reverse('add_client'), {'name': 'Test Client'})

        # Assert that the response is a redirect to the client_list page
        self.assertRedirects(response, reverse('client_list'))

        # Assert that a new Client object was created with the correct name
        self.assertTrue(Client.objects.filter(name='Test Client').exists())


class ClientListViewTestCase(TestCase):
    def setUp(self):
        self.client = TestClient()
        self.client1 = Client.objects.create(name='Client 1')
        self.client2 = Client.objects.create(name='Client 2')

    def test_client_list(self):
        # Send a GET request to the client_list URL
        response = self.client.get(reverse('client_list'))

        # Assert that the response is a 200 OK
        self.assertEqual(response.status_code, 200)

        # Assert that the response contains the names of the Client objects
        self.assertContains(response, self.client1.name)
        self.assertContains(response, self.client2.name)