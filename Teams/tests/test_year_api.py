import datetime

from django.test import TestCase
from rest_framework.exceptions import ValidationError

from Teams.models import Year
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from Teams.serializers import YearSerializer
from django.db import IntegrityError

YEARS_URL = reverse('years')


class ModelYearsTests(TestCase):
    """Test Year model"""
    def test_year_str(self):
        """Test year string representation"""
        sample_year = Year.objects.create(
            year=2015
        )
        self.assertEqual(str(sample_year), str(sample_year.year))


def sample_year(year):
    """Create sample year"""
    return Year.objects.create(year=year)


class YearAPITests(TestCase):
    """Test year API"""

    def setUp(self):
        self.client = APIClient()

    def test_retrieve_year(self):
        """Test retrieving a list of years"""
        sample_year(year=2007)
        res = self.client.get(YEARS_URL)
        years = Year.objects.all().order_by('-id')
        serializer = YearSerializer(years, many=True)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)

    def test_create_year(self):
        """Test creating year"""
        payload = {'year': 2008}
        res = self.client.post(YEARS_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        year = Year.objects.get(year=res.data['year'])
        for key in payload.keys():
            self.assertEqual(payload[key], getattr(year, key))

    def test_add_exist_year(self):
        """test of adding an existing year"""
        sample_year(2007)
        payload = {'year': 2007}
        res = self.client.post(YEARS_URL, payload)
        self.assertRaises(IntegrityError)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(res.data[0], "Ten rok już jest w bazie")

    def test_add_later_year(self):
        """test of adding later than the maximum"""
        payload = {'year': int(datetime.datetime.now().year+1)}
        res = self.client.post(YEARS_URL, payload)
        self.assertRaises(ValidationError)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(
            res.data['non_field_errors'][0],
            "Rok nie może być późniejszy niż niż bieżący"
        )

    def test_add_earlier_year(self):
        """test of adding an earlier year than the minimum"""
        payload = {'year': 2006}
        res = self.client.post(YEARS_URL, payload)
        self.assertRaises(ValidationError)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(
            res.data['non_field_errors'][0],
            "Rok nie może być wczęsniejszy niż 2007"
        )
