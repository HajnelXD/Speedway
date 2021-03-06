from django.db import IntegrityError
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from Riders.models import Rider, RiderInfo
from Riders.seralizers import RiderInfoSerializer
from Teams.models import Year, Team

RIDERSINFO_URL = reverse('ridersinfo')


class ModelRiderInfoTest(TestCase):
    """Test Rider Info model"""
    def test_rider_info_str(self):
        sample_team = Team.objects.create(
            team_name='testowa drużyna',
            stadium='Testowy',
            team_photo='t',
        )
        sample_year = Year.objects.create(
            year=2009
        )
        sample_rider = Rider.objects.create(
            last_name='Kowalski',
            first_name='Jan',
            birthday='2020-12-12',
            nationality='Poland',
            rider_photo='t'
        )
        rider_info = RiderInfo(
            id=None,
            team=sample_team,
            rider=sample_rider,
            year=sample_year,
            junior='N'
        )
        rider_info.save()
        self.assertEqual(
            str(rider_info), str(sample_rider) + " " + str(sample_year) +
            " " + str(sample_team)
        )


def sample_rider_info(team_name, year, last_name, first_name, birthday,
                      nationality, rider_photo, stadium, team_photo):
    sample_team = Team.objects.create(
        team_name=team_name,
        stadium=stadium,
        team_photo=team_photo,
    )
    sample_year = Year.objects.create(
        year=year
    )
    sample_rider = Rider.objects.create(
        last_name=last_name,
        first_name=first_name,
        birthday=birthday,
        nationality=nationality,
        rider_photo=rider_photo,
    )
    rider_info = RiderInfo(
        id=None,
        team=sample_team,
        rider=sample_rider,
        year=sample_year,
        junior='N'
    )
    rider_info.save()


class RiderInfoAPITest(TestCase):
    """Test RidersInfo API"""

    def setUp(self):
        self.client = APIClient()

    def test_retrieve_ridersinfo(self):
        """Test retrieving a list of riders info"""
        sample_rider_info(
            'AKS',
            2008,
            'Smith',
            'Agent',
            '2000-12-12',
            'Poland',
            't',
            'Testowy',
            't'
        )
        res = self.client.get(RIDERSINFO_URL)
        rider_info = RiderInfo.objects.all().order_by('id')
        serializer = RiderInfoSerializer(rider_info, many=True)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)

    def test_create_riderinfo(self):
        """Test create riders info"""
        payload = {
            "rider":
                {
                    "last_name": "Drabik",
                    "first_name": "Maksym",
                    "birthday": "2000-12-12",
                    "nationality": "Poland",
                    "rider_photo": "t"
                },
            "team": {
                "team_name": "Sparta Wrocław",
                "stadium": "Testowy",
                "team_photo": "t"
                },
            "year": {
                "year": 2019
                },
            "junior": 'N'
        }
        res = self.client.post(RIDERSINFO_URL, payload, format='json')
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)

    def test_add_exist_rider_info(self):
        """Test of adding an existing team"""
        sample_rider_info(
            'AKS',
            2008,
            'Smith',
            'Agent',
            '2000-12-12',
            'Poland',
            't',
            'Testowy',
            't',
        )
        payload = {
            "rider": {
                "last_name": "Smith",
                "first_name": "Agent",
                "birthday": "2000-12-12",
                "nationality": "Poland",
                "rider_photo": "t"
            },
            "team": {
                "team_name": "AKS",
                "stadium": "Testowy",
                "team_photo": 't',
            },
            "year": {
                "year": 2008
            },
            "junior": "N"
        }
        res = self.client.post(RIDERSINFO_URL, payload, format='json')
        self.assertRaises(IntegrityError)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(res.data[0], "Takie dane już są w bazie")
