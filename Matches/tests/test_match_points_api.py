from django.db import IntegrityError
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from Matches.models import MatchPoints, Match
from Riders.models import Rider
from Teams.models import Team


def sample_rider():
    """Create sample rider"""
    return Rider.objects.create(last_name="Kowalski", first_name="Andrzej")


def sample_team(team_name, stadium):
    """Create sample team"""
    return Team.objects.create(team_name=team_name, stadium=stadium)


def sample_match():
    team1 = sample_team('Team1', 'stadium1')
    team2 = sample_team('Team2', 'stadium2')
    return Match.objects.create(
        home_team=team1,
        home_team_points=55,
        guest_team=team2,
        guest_team_points=35,
        date='2009-10-03',
        isFinished=True,
        queue=1,
        playoff=True,
    )


class ModelMatchPointsTest(TestCase):
    """Test Match Points model"""
    def test_sample_match_points(self):
        """Create sample match"""

        match = sample_match()
        rider = sample_rider()
        match_points = MatchPoints.objects.create(
            rider=rider,
            match=match,
            first_run='0',
            second_run='1',
            third_run='2',
            fourth_run='3',
            fifth_run='2',
            sixth_run='-',
            seventh_run='-',
            joker_rider=0,
            runs=[1, 2, 3, 4, 5]
        )
        self.assertEqual(str(match_points), str(match_points.match.date)
                         + ' ' + str(match_points.rider.last_name))