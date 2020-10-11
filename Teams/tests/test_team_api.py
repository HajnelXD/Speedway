from django.test import TestCase
from Teams.models import Team
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from Teams.serializers import TeamSerializer
from django.db import IntegrityError

TEAMS_URL = reverse('teams')


class ModelYearsTests(TestCase):
    """Test Year model"""
    def test_team_str(self):
        """Test year string representation"""
        sample_team = Team.objects.create(
            team_name="Testowa nazwa"
        )
        self.assertEqual(str(sample_team), sample_team.team_name)


def sample_team(team_name='Testowa nazwa'):
    """Create sample team"""
    return Team.objects.create(team_name=team_name)


class TeamAPITests(TestCase):
    """Test Team API"""

    def setUp(self):
        self.client = APIClient()

    def test_retrieve_team(self):
        """Test retrieving a list of teams"""
        sample_team()
        res = self.client.get(TEAMS_URL)
        teams = Team.objects.all().order_by('-id')
        serializer = TeamSerializer(teams, many=True)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)

    def test_create_team(self):
        """Test creating team"""
        payload = {'team_name': 'Testowa drużyna'}
        res = self.client.post(TEAMS_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        team = Team.objects.get(team_name=res.data['team_name'])
        for key in payload.keys():
            self.assertEqual(payload[key], getattr(team, key))

    def test_add_exist_team(self):
        """Test of adding an existing team"""
        sample_team()
        payload = {'team_name': 'Testowa nazwa'}
        res = self.client.post(TEAMS_URL, payload)
        self.assertRaises(IntegrityError)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(res.data[0], "Ta drużyna już jest w bazie")
