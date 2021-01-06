from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from Riders.models import Rider, RiderInfo
from Riders.seralizers import RiderSerializer, RiderInfoSerializer


class RiderListView(APIView):

    def get(self, request, format=None):
        riders = Rider.objects.all()
        serializer = RiderSerializer(riders, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = RiderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RiderInfoView(APIView):

    def get(self, request, format=None):
        riders_info = RiderInfo.objects.all()
        serializer = RiderInfoSerializer(riders_info, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = RiderInfoSerializer(data=request.data, many=False)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TeamRidersList(APIView):

    def get(self, request, year, team_id, format=None):
        riders_list = RiderInfo.objects.filter(
            year__year=year,
            team_id=team_id,
        )
        serializer = RiderInfoSerializer(riders_list, many=True)
        return Response(serializer.data)


class RiderView(APIView):

    def get(self, request, rider_id, format=None):
        rider = Rider.objects.filter(
            id=rider_id
        )
        serializer = RiderSerializer(rider, many=True)
        return Response(serializer.data)
