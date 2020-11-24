from rest_framework.views import APIView
from rest_framework.response import Response

from Summary.models import SummaryTable
from Summary.serializer import SummaryTableSerializer


class SummaryList(APIView):
    """Table with summary results for all years"""

    def get(self, request, format=None):
        summary = SummaryTable.objects.all()
        serializer = SummaryTableSerializer(summary, many=True)
        return Response(serializer.data)


class SummaryDetails(APIView):
    """Table with summary results for one year"""

    def get(self, request, year, format=None):
        summary = SummaryTable.objects.filter(year__year=year)
        serializer = SummaryTableSerializer(summary, many=True)
        return Response(serializer.data)
