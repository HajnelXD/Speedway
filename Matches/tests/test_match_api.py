from django.db import IntegrityError
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from Matches.models import Match
from Teams.models import Team


def sample_team(team_name):
    """Create sample team"""
    return Team.objects.create(team_name=team_name)


class ModelMatchTest(TestCase):
    """Test Match model"""
    def test_match_str(self):
        """Test rmatch string representation"""
        team1 = sample_team('Team1')
        team2 = sample_team('Team2')
        sample_match = Match.objects.create(
            home_team=team1,
            home_team_points=55,
            guest_team=team2,
            guest_team_points=35,
            date='2009-10-03',
        )
        print(sample_match)
        self.assertEqual(str(sample_match), str(sample_match.date) + " "
                         + sample_match.home_team.team_name + " " +
                         str(sample_match.home_team_points) + " " +
                         str(sample_match.guest_team_points) + " " +
                         sample_match.guest_team.team_name)
