from django.test import TestCase
from Teams.models import Year, Team, TeamInfo
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from Teams.serializers import TeamInfoSerializer
from django.db import IntegrityError

TEAMS_INFO_URL = reverse('teamsinfo')


class TeamsInfoModelsTests(TestCase):
    """Test Team Info model"""
    def test_team_info_str(self):
        """Test year string representation"""
        sample_team = Team.objects.create(
            team_name='testowa drużyna',
        )
        sample_year = Year.objects.create(
            year=2009
        )
        sample_year2 = Year.objects.create(
            year=2010
        )
        team_info = TeamInfo(team_name=sample_team)
        team_info.save()
        team_info.years_in_ekstraliga.add(sample_year)
        team_info.years_in_ekstraliga.add(sample_year2)
        team_info.save()
        self.assertEqual(str(team_info), str(sample_team))


def sample_team_info(team, year):
    sample_team = Team.objects.create(
        team_name=team
    )
    sample_year = Year.objects.create(
        year=year
    )
    team_info = TeamInfo(id=1, team_name=sample_team)
    team_info.years_in_ekstraliga.add(sample_year)
    team_info.save()


class TeamsInfoAPITests(TestCase):
    """Test team information model"""

    def setUp(self):
        self.client = APIClient()

    def test_retrieve_teaminfo(self):
        """Test retrieving a list of riders info"""
        sample_team_info('Testowa dtużyna', 2009)
        res = self.client.get(TEAMS_INFO_URL)
        team_info = TeamInfo.objects.all().order_by('id')
        serializer = TeamInfoSerializer(team_info, many=True)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)

    def test_create_teaminfo(self):
        """Test create riders info"""
        payload = {
            "team_name": {
                "team_name": "Testowa dtużyna"
            },
            "years_in_ekstraliga": [
                {
                    "year": 2010
                },
            ]
        }
        res = self.client.post(TEAMS_INFO_URL, payload, format='json')
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)

    def test_add_exist_teaminfo(self):
        """Test of adiing an existing team"""
        sample_team_info('Testowa dtużyna', 2009)
        payload = {
            "team_name": {
                "team_name": "Testowa dtużyna"
            },
            "years_in_ekstraliga": [
                {
                    "year": 2009
                },
            ]
        }
        res = self.client.post(TEAMS_INFO_URL, payload, format='json')
        self.assertRaises(IntegrityError)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(res.data[0], "Ten klub jest już w bazie")
