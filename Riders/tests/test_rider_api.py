from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from Riders.models import Rider
from Riders.seralizers import RiederSerializer

RIDERS_URL = reverse('riders')


class ModelRiderTests(TestCase):
    """Test rider model"""
    def test_team_str(self):
        """Test rider string representation"""
        sample_rider = Rider.objects.create(
            last_name="Kowalski",
            first_name="Andrzej"
        )
        self.assertEqual(str(sample_rider), sample_rider.first_name+" "+sample_rider.last_name)


class RidersAPITests(TestCase):
    """Test Rider API"""
    def setUp(self):
        self.client = APIClient()

    def test_retrieve_rider(self):
        """Test retrieving a list of teams"""
        res = self.client.get(RIDERS_URL)
        riders = Rider.objects.all().order_by("-id")
        serializer = RiederSerializer(riders, many=True)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)

    def test_create_team(self):
        """Test creating rider"""
        payload = {'last_name': 'Kasperczak', 'first_name': 'Henryk'}
        res = self.client.post(RIDERS_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        rider = Rider.objects.get(last_name=res.data['last_name'])
        for key in payload.keys():
            self.assertEqual(payload[key], getattr(rider, key))