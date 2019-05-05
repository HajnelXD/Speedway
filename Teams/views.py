from Teams.models import Year, Team, TeamInfo
from Teams.serializers import YearSerializer, TeamSerializer, TeamInfoSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class YearsList(APIView):
    """List all availabe years"""

    def get(self, request, format=None):
        years = Year.objects.all()
        serializer = YearSerializer(years, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = YearSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TeamsList(APIView):
    """List all teams"""

    def get(self, request, format=None):
        teams = Team.objects.all()
        serializer = TeamSerializer(teams, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = TeamSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TeamsInfoList(APIView):
    """List teams with information"""

    def get(self, request, format=None):
        teams_info = TeamInfo.objects.all()
        serializer = TeamInfoSerializer(teams_info, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = TeamInfoSerializer(data=request.data, many=False)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)