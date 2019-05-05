from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from Riders.models import Rider
from Riders.seralizers import RiederSerializer


class RiderListView(APIView):

    def get(self, request, format=None):
        riders = Rider.objects.all()
        serializer = RiederSerializer(riders, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = RiederSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
