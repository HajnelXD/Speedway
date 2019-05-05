import datetime
from django.test import TestCase
from rest_framework.exceptions import ValidationError
from Teams.models import Year, Team, TeamInfo
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from Teams.serializers import YearSerializer, TeamSerializer
from django.db import IntegrityError

TEAMS_INFO_URL = reverse('teamsinfo')


class TeamsInfoAPITests(TestCase):
    """Test Team Info model"""
    def test_team_info_str(self):
        """Test year string representation"""
        sample_team = Team.objects.create(
            team_name='testowa drużyna'
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

# class TeamsInfoAPITests(TestCase):
#     """Test team information model"""
#     def test_create_team_info(self):
#         """Test year string representation"""
#         payload = {'team_name': {'team_name': 'Motor Lublin'}, 'years_in_ekstraliga': [{'year': 2010}, {'year': 2007}]}
#
#         res = self.client.post(TEAMS_INFO_URL, payload)
#         self.assertEqual(res.status_code, status.HTTP_201_CREATED)
#         teams_info = TeamInfo.objects.get(id=res.data['id'])
#         years = teams_info.years_in_ekstraliga.all()
#         self.assertEqual(years.count(), 2)


