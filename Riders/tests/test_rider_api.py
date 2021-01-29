from django.db import IntegrityError
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from Riders.models import Rider
from Riders.seralizers import RiderSerializer

RIDERS_URL = reverse('riders')


def sample_rider():
    """Create sample rider"""
    return Rider.objects.create(
        last_name="Kowalski",
        first_name="Andrzej",
        nationality="Poland",
        birthday="2000-12-12",
        rider_photo='t',
    )


class ModelRiderTests(TestCase):
    """Test rider model"""
    def test_team_str(self):
        """Test rider string representation"""
        sample_rider = Rider.objects.create(
            last_name='Kowalski',
            first_name='Andrzej',
            nationality='Poland',
            birthday='2000-12-12',
            rider_photo='t',
        )
        self.assertEqual(
            str(sample_rider),
            sample_rider.first_name + ' ' + sample_rider.last_name
        )


class RidersAPITests(TestCase):
    """Test Rider API"""
    def setUp(self):
        self.client = APIClient()

    def test_retrieve_rider(self):
        """Test retrieving a list of teams"""
        sample_rider()
        res = self.client.get(RIDERS_URL)
        riders = Rider.objects.all().order_by("-id")
        serializer = RiderSerializer(riders, many=True)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)

    def test_create_rider(self):
        """Test creating rider"""
        payload = {
            'last_name': 'Kasperczak',
            'first_name': 'Henryk',
            'birthday': '2000-12-12',
            'nationality': 'Poland',
            'rider_photo': 't',
        }
        res = self.client.post(RIDERS_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        rider = Rider.objects.get(last_name=res.data['last_name'])
        for key in payload.keys():
            self.assertEqual(payload[key], str(getattr(rider, key)))

    def test_exist_rider(self):
        """Test of adding an existing rider"""
        sample_rider()
        payload = {
            'last_name': 'Kowalski',
            'first_name': 'Andrzej',
            'birthday': '2000-12-12',
            'nationality': 'Poland',
            'rider_photo': 't',
        }
        res = self.client.post(RIDERS_URL, payload)
        self.assertRaises(IntegrityError)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(res.data[0], "Ten zawodnik już jest w bazie")
